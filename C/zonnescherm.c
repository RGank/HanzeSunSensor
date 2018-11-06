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

uint8_t debug;
uint16_t rotation;
uint16_t temperature;
uint16_t light;


/*
	Print the system output like a JSON formatted array so that Python can easily use it.
	The JSON_settings array contains the settings which the Python client can have control over.
	TODO: Implement variables such as rotation_max, light_threshold, temperature_threshold
*/
unsigned char get_JSON_settings(void)
{
	printf("{'type': 'settings', 'debug': %d, 'rotation': %d}\r\n", debug, rotation);
	return 0;
}

/*
	Print the system output like a JSON formatted array so that Python can easily use it.
	The JSON_data array contains the data obtained by the sensors.
	TODO: Also send older data and average numbers of the variables
*/
unsigned char get_JSON_data(void)
{
	
	//Debugger
	if(debug){
		update_temperature();
		update_light();	
	}
	
	printf("{'type': 'current_data', 'rotation': %d, 'temperature': %d, 'light_intensity': %d}\r\n", rotation, temperature, light);
	return 0;
}

//Updaters
void update_temperature( void )
{
	temperature = adc_read(TEMP_PIN);
}

void update_light( void )
{
	light = adc_read(LIGHT_PIN);
}


//Setup things
void setup( void )
{
	
	DDRB = 0xFF;			//Set DDRB as output
	
	adc_init();				//Init Analog to Digital Converter
	uart_init();			//Init Serial
	SCH_Init_T1();			//Init Scheduler
	stdout = &mystdout;		//Init printf()
	
	update_light();
	update_temperature();
	
}

/************************************************************************/
/* Input handler														*/
/************************************************************************/
void input_handler()
{

	//Return if there is nothing incoming on RX
	if(!message_incomming()){
		return 0;
	}
	
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

void main(void)
{
	
	light = 0;
	rotation = 0;
	temperature = 0;
	debug = 1;	//If debugger is true (1), all the sensors will be updated when JSON formatted data is requested
	
	setup();
	
	connection_lost();		//Wait for a connection to be made
	
	SCH_Add_Task(input_handler, 0, 1);
	
	if(!debug){
		SCH_Add_Task(update_temperature, 0, 4000);
		SCH_Add_Task(update_light, 0, 3000);
		SCH_Add_Task(get_JSON_data, 0, 6000);
	}	
	
	SCH_Start();
	
	while(1){
		SCH_Dispatch_Tasks();
	}		
	
	return 0;
		
}