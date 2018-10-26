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

Voorbeeld:
```
[s] > Waiting for a connection..
[s] > Waiting for a connection..
[c] > a
[s] > Connected!
[c] > d
[s] > Disconnected!
[s] > Waiting for a connection..
```
[s] = Systeem
[c] = Client

Op het moment is er nog geen sprake van een goede handshake protocol. Dat zal later nog toegevoegd worden.