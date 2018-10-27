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
#include "adc.h"

uint16_t rotation;
uint16_t temperature;
uint16_t light;

/*
	Attempt to make a JSON parser which Python can process
*/
unsigned char get_JSON_settings(void)
{
	printf("{type: settings, rotation: %d}\r\n", rotation);
	return 0;
}

unsigned char get_JSON_data(void)
{
	temperature = adc_read(TEMP_PIN);
	light = adc_read(LIGHT_PIN);
	printf("{type: current_data, rotation: %d, temperature: %d, light_intensity: %d}\r\n", rotation, temperature, light);
	return 0;
}

void main(void)
{
	
	//Init variables
	rotation = 0;	//TODO: Get previous rotation from SRAM
	temperature = 0;
	light = 0;
	
	//Set DDRB as output
	DDRB = 0xFF;
	
	adc_init();				//Init ADC
	uart_init();			//Init UART
	stdout = &mystdout;		//Init printf()
	
	connection_lost();
	
	while(1){
	
		char input = receive();
		
		//Expected input: X, x
		//Action: Disconnect
		if(input==0x58||input==0x78){
			printf("Disconnected!\r\n");
			connection_lost();
		}
		
		//Expected input: D, d
		//Action: Give the current data in JSON format
		if(input==0x64||input==0x44){
			get_JSON_data();
		}			
		
		//Expected input: S, s
		//Action: Give the current settings in a JSON format
		else if(input==0x53||input==0x73){
			get_JSON_settings();
		}
	
	}
		
}