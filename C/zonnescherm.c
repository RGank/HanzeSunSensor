/*
 * zonnescherm.c
 *
 * Created: 26-10-2018 12:38:35
 *  Author: Arnold
 */ 

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>

#define F_CPU 16E6
#include <util/delay.h>

#define UBBRVAL 51

#include "serial.h"
#include "connection.h"

int rotation;
int temperature;

/*
	Print an array of characters
*/
void writeln(char str[]){
	
	for(int i=0;i<strlen(str);i++){
		transmit(str[i]);
	}		
					
}

/*
	Attempt to make a JSON parser which Python can process
*/
unsigned char get_JSON_settings(void)
{
	printf("{type: settings, rotation: %d, temperature: %d}\r\n", rotation, temperature);
	return 0;
}

void main(void)
{
	
	//Init variables
	rotation = 0;	//TODO: Get rotation from SRAM
	temperature = 0;
	
	//Set DDRB as input
	DDRB = 0xFF;
	
	//Initialize uart
	uart_init();
	
	//Init the ouput for printf()
	stdout = &mystdout;
	
	//Start the system without a connection
	connection_lost();
	
	
	while(1){
	
		char input = receive();
		
		//Expected input: D, d
		//Action: Disconnect
		if(input==0x64||input==0x44){
			writeln("Disconnected!\r\n");
			connection_lost();
		}
		
		//Expected input: S, s
		//Action: Give the current settings in a JSON format
		else if(input==0x53||input==0x73){
			writeln(get_JSON_settings());
		}
	
	}
		
}