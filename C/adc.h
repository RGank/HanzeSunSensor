//Temperature analog pin
#define TEMP_PIN 0
#define LIGHT_PIN 1

void adc_init()
{

	ADMUX = (1<<REFS0);
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	//ADC Enable, prescaler 128
	
}

/*
	Read the analog input for the specified pin
*/
uint16_t adc_read(uint8_t pin) {

	ADMUX	&=	0xf0;
	ADMUX	|=	pin;										//The pin variables is which pin analog pin is being used on the board

	ADCSRA |= _BV(ADSC);									//Begin the conversion
	while ( (ADCSRA & _BV(ADSC)) );							//Wait until the conversion has finished
	return ADC;
	
}