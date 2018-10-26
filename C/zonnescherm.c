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

//Output on USB = PD1 = Board pin 1
//Datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200
#define UBBRVAL 51

void uart_init()
{
	//Set baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	
	//Disable U2X mode
	UCSR0A = 0;
	
	//Enable transmitter and receiver
	UCSR0B = (1<<RXEN0)|(1<<TXEN0);
	
	//Set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

/*
	Transmit data to the client
	Reference: ATMEGA328p Datasheet 20.6.1
*/
void transmit(unsigned char data){
	/* Wait for empty transmit buffer */
	while( !(UCSR0A & (1<<UDRE0)) );
	
	/* Put data into buffer, sends the data */
	UDR0 = data;
}

/*
	Receive input from the client
	Reference: ATMEGA328p Datasheet 20.7.1
*/
unsigned char receive( void )
{
	/* Wait for data to be received */
	while ( !(UCSR0A & (1<<RXC0)) );
	/* Get and return received data from buffer */
	return UDR0;
}

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