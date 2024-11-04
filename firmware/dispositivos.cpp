#include "dispositivos.h"
#include <Arduino.h>

// Array com os pinos dos dispositivos
const int dispositivos[] = {PIN_S1Y1, PIN_S2Y1, PIN_S2Y2, PIN_S3Y1};
const int numDispositivos = sizeof(dispositivos) / sizeof(dispositivos[0]); // Quantidade de dispositivos

// Função para configurar os pinos dos dispositivos como saídas e inicializá-los
void iniciarDispositivos() {
  for (int i = 0; i < numDispositivos; i++) {
    pinMode(dispositivos[i], OUTPUT);   // Define cada pino como saída
    digitalWrite(dispositivos[i], HIGH); // Define cada dispositivo como "ligado" inicialmente
  }
}

// Função para ligar um dispositivo específico
void ligarDispositivo(int dispositivo) {
  digitalWrite(dispositivo, HIGH);
}

// Função para desligar um dispositivo específico
void desligarDispositivo(int dispositivo) {
  digitalWrite(dispositivo, LOW);
}
