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