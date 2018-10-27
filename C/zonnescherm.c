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

#include "serial.h"
#include "connection.h"
#include "adc.h"

uint16_t rotation;
uint16_t temperature;
uint16_t light;


/*
	Print the system output like a JSON formatted array so that Python can easly use it.
	The JSON_settings array contains the settings which the Python client can have control over.
	TODO: Implement variables such as rotation_max, light_threshold, temperature_threshold
*/
unsigned char get_JSON_settings(void)
{
	printf("{type: settings, rotation: %d}\r\n", rotation);
	return 0;
}

/*
	Print the system output like a JSON formatted array so that Python can easly use it.
	The JSON_data array contains the data obtained by the sensors.
	TODO: Also send older data and average numbers of the variables
*/
unsigned char get_JSON_data(void)
{
	temperature = adc_read(TEMP_PIN);
	light = adc_read(LIGHT_PIN);
	printf("{type: current_data, rotation: %d, temperature: %d, light_intensity: %d}\r\n", rotation, temperature, light);
	return 0;
}

void main(void)
{
	
	light = 0;
	rotation = 0;			//TODO: Get previous rotation from SRAM
	temperature = 0;
	
	DDRB = 0xFF;			//Set DDRB as output
	
	adc_init();				//Init ADC
	uart_init();			//Init UART
	stdout = &mystdout;		//Init printf()
	
	connection_lost();		//Wait for a connection to be made
	
	while(1){
	
		//Wait for input by the client
		//TODO: Can input be used as a interrupt so that the while loop would continue until there's input?
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