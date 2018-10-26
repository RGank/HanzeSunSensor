/*
 * zonnescherm.c
 *
 * Created: 26-10-2018 12:38:35
 *  Author: Arnold
 */ 

#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#define UBBRVAL 51

#include "serial.h"

/*
	Connection has been lost, wait for a new connection to be made.
	TODO: The program should preform a handshake with the client in order for a connection to be set.
*/
void connection_lost( void )
{
	PORTB = 0x00;
	while(!(UCSR0A & (1<<RXC0))){
		writeln("Waiting for a connection..\r\n");
		_delay_ms(500);
	}
	connected();
	 
}

void connected( void )
{
	PORTB = 0x01;
	writeln("Connected!\r\n");	
}

/*
	Print an array of characters
*/
void writeln(char str[]){
	
	for(int i=0;i<strlen(str);i++){
		transmit(str[i]);
	}		
					
}


void main(void)
{
	
	DDRB = 0xFF;
	
	uart_init();
	connection_lost();
	
	while(1){
	
		char input = receive();
		
		//Als de client 'd' of 'D' verstuurd, dan word de verbinding verbroken.
		if(input==0x64||input==0x44){
			writeln("Disconnected!\r\n");
			connection_lost();
		}
	
	}
		
}