# Zonnescherm Project
Voor dit project van de Hanzehogeschool Groningen word er een systeem gemaakt dat automatisch of handmatig een zonnescherm kan bedienen doormiddel van een C en Python.

## Python
Voor het gebruik van de Python code moeten er wel verschillende Python packets worden geinstalleerd.

```
pip install dash
pip install dash-html-components
pip install dash-core-components
```

## C
Op het moment kan het systeem alleen nog maar een simpele verbinding maken met de client als de client een willekeurige letter verstuurd.
Zodra een verbinding tot stand is gekomen, dan is het mogelijk om doormiddel van verschillende letter combinaties data op te vragen.

Voorbeeld:
```
[s] > Waiting for a connection..
[s] > Waiting for a connection..
[c] > a
[s] > Connected!
[c] > s
[s] > {type: settings, rotation: 0}
[c] > d
[s] > {type: current_data, rotation: 0, temperature: 14, light_intensity: 96}
[c] > x
[s] > Disconnected!
[s] > Waiting for a connection..
```
[s] = Systeem
[c] = Client

Op het moment is er nog geen sprake van een goede handshake protocol. Dat zal later nog toegevoegd worden.


## Arduino aansluiting
De componenten die nodig zijn voor het systeem zijn als volgt;
- Low Voltage Temperature Sensor
- Photoconductive Cell (GL5528)
- Arduino UNO
- LED

De low voltage temperature sensor word verbonden aan analog pin 0 en de photoconductive cell word verbonden aan analog pin 1. Daarnaast is er ook een optionele LED die aangesloten kan worden aan digital pin 8 om te weergeven wanneer er een verbinding is gemaakt tussen het systeem en de client.
