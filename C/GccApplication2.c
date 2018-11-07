/*
 * distance.c
 *
 * meausers distance betwee 2 and 70 cm
 *
 * Created: 29-6-2016 14:44:43
 *  Author: jacob
 */ 

/* 
 * HC-SR04
 * trigger to sensor : uno 0 (PD0) output
 * echo from sensor  : uno 3 (PD3 = INT1) input
 * 
 * DIO : uno 8  (PB0) data
 * CLK : uno 9  (PB1) clock
 * STB : uno 10 (PB2) strobe
 *
 */
#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#include <avr/interrupt.h>
#define F_CPU 16E6
#include <util/delay.h>
#include "distance.h"
#include "serial.h"

static volatile uint8_t gv_echo = 0; // a 16 bit flag
static volatile uint8_t gv_count = 0;

uint16_t distance;
int working = 0;


void init_ports(void)
{
	DDRD = 0b11110111;			//Set TRIG pin on output (PIN 0) and set ECHO pin on input (PIN 3)
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
    TCCR1A = 0;
	TCCR1B = 0;
}

uint16_t Pulse()
{
		_delay_ms(10);			//Restart HC-SR04
		PORTD &= ~(1 << PIND0);
		_delay_us(1);
		PORTD |=(1<<PIND0);	//Set PIN 0 HIGH
		_delay_us(10);
		PORTD &= ~(1<<PIND0); //Set PIN 0 LOW		
}	

uint16_t calc_cm()
{
	distance = gv_echo / 58;		//Convert the distance in us to cm
}


int main(void)
{
	init_timer();						//Init timer
	init_ports();						//Init ports
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
			TCCR1B=0;//disabling counter

			gv_echo=TCNT1;//count memory is updated to integer
			
			TCNT1=0;//resetting the counter memory
			
			gv_count=0;
			
		}

		if (gv_count==0)//when logic change from LOW to HIGH

		{

			TCCR1B|=(1<<CS10);//enabling counter

			gv_count=1;
			
		}
	
}
