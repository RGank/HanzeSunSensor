/*
 * distance.c
 *
 * Measure distance
 *
 * Created: 05-11-2018 13:45:23
 * Author: Rein Gankema
 * HC-SR04
 */
 
#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#define F_CPU 16E6
#include "distance.h"
#include "serial.h"
#define TRIGpin 0

static volatile int gv_echo = 0; // a 16 bit flag
static volatile int gv_count = 0;
uint8_t distance = 0;
int working;


void init_ports(void)
{
	DDRD = 0b11111011;			//Set TRIG pin on output (PIN 0) and set ECHO pin on input (PIN 2)
	_delay_ms(50);

}

void Initialize_external_interrupt(void)
{
	EIMSK |= (1 << INT0);	// enable INT0
	EICRA |= (1 << ISC10);	// set INT0 to trigger while rising edge = HIGH
}

void init_timer()
// prescaling : max time = 2^16/16E6 = 4.1 ms, 4.1 >> 2.3, so no prescaling required
// normal mode, no prescale, stop timer
{
	cli();				//Clear interrupts
	TCCR1B = 0;			//Set timer to 0
	
}

uint16_t Pulse()
{

		//Restart HC-SR04 by setting TRIG pin back to LOW
		_delay_ms(100);
		PORTD &= ~(1 <<TRIGpin);
		//Send a pulse
		_delay_us(1);
		PORTD |=(1<<TRIGpin);	//Set PIN 0 HIGH
		_delay_us(15);
		PORTD &= ~(1<<TRIGpin); //Set PIN 0 LOW
			
}	

uint16_t calc_cm()
{
	distance = gv_echo;		//Convert the distance in us to cm
}


int main(void)
{
	init_ports();						//Init ports
	init_timer();						//Init timer
	Initialize_external_interrupt();	//Init interrupts
	uart_init();						//Init UART
	stdout = &mystdout;
	sei();								//enable interrupts
	
	while (1)
	{
		Pulse();
		calc_cm();
		printf("distance %d \r\n: ", distance);
	}
}

ISR (INT0_vect)
{
	if (gv_count==1)//when logic from HIGH to LOW
	{
		
		TCCR1B = 0;					//disabling counter
		gv_echo = TCNT1;			//count memory is updated to integer
		TCNT1 = 0;					//resetting the counter memory
		gv_count = 0;				//Set count to 0
			
	}

	if (gv_count==0)				//when logic change from LOW to HIGH
	{
		TCCR1B |= _BV(CS10);		//enabling counter (TCNT1) without any prescaling
		gv_count=1;					//Set count to 1
	}
}
