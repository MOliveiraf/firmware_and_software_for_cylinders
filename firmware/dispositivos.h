#ifndef DISPOSITIVOS_H
#define DISPOSITIVOS_H

#include <Arduino.h>

// Definindo os pinos dos dispositivos
#define PIN_S1Y1 23
#define PIN_S2Y1 22
#define PIN_S2Y2 21
#define PIN_S3Y1 19

void iniciarDispositivos();
void ligarDispositivo(int dispositivo);
void desligarDispositivo(int dispositivo);

#endif 
