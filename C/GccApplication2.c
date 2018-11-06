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

volatile uint8_t gv_echo = 0; // a flag
volatile uint8_t gv_count = 0;

uint16_t distance = 0;

void init_ports(void)
{
	DDRD = 0b11110111;
	
}

void init_timer(void)
// prescaling : max time = 2^16/16E6 = 4.1 ms, 4.1 >> 2.3, so no prescaling required
// normal mode, no prescale, stop timer
{
    TCCR1B = 0;
}

uint16_t Pulse()
{
	 PORTD |=(1<<PIND0);
	 _delay_us(50);
	 PORTD &=~(1<<PIND0);
	
	distance = gv_echo / 58;		// Zet afstand om van ms naar cm
	
	return distance;
}	

ISR (INT1_vect)
{
	if(gv_count == 1)
	{
		TCCR1B = 0;				//disable counter
		gv_echo = TCNT1;		//update counter to integer
		TCNT1 = 0;				//reset counter
		gv_count = 0;
		
	}
	if(gv_count == 0)
	{
		TCCR1B = _BV(CS10);		//enable counter
		gv_count = 1;
	}
}


int main(void)
{
	init_timer();
	init_ports();
	uart_init();			//Init UART
	stdout = &mystdout;
	sei();					//enable interrupssssssssssssssssssssssssssss
	
	while (1)
	{
		INT1_vect();
		Pulse();
		printf("distance %d \r\n: ", distance);
	}
}