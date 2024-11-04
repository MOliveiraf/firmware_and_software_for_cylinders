#include "comandos.h"
#include "dispositivos.h"
#include <Arduino.h>

void iniciarComunicacao() {
  Serial.begin(9600);
  Serial.println("Sistema iniciado. Aguardando comandos...");
}

void verificarComandos() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == '\n' || comando == '\r') return;

    Serial.print("Comando recebido: ");
    Serial.println(comando);

    switch (comando) {
      case 'X':
        Serial.println("Desligando S1Y1");
        desligarDispositivo(PIN_S1Y1);
        delay(3000);
        break;
        
      case 'x':
        Serial.println("Ligando S1Y1");
        ligarDispositivo(PIN_S1Y1);
        delay(3000);
        break;

      case 'Y':
        Serial.println("Desligar S2Y1 e Ligar S2Y2");
        desligarDispositivo(PIN_S2Y1);
        ligarDispositivo(PIN_S2Y2);
        delay(3000);
        ligarDispositivo(PIN_S2Y1);
        break;

      case 'y':
        Serial.println("Ligar S2Y1 e Desligar S2Y2");
        ligarDispositivo(PIN_S2Y1);
        desligarDispositivo(PIN_S2Y2);
        delay(3000);
        ligarDispositivo(PIN_S2Y2);
        break;

      case 'Z':
        Serial.println("Desligar S3Y1");
        desligarDispositivo(PIN_S3Y1);
        delay(3000);
        break;

      case 'z':
        Serial.println("Ligar S3Y1");
        ligarDispositivo(PIN_S3Y1);
        delay(3000);
        break;

      case 'H':
        Serial.println("Home Position");
        ligarDispositivo(PIN_S1Y1);
        ligarDispositivo(PIN_S2Y1);
        desligarDispositivo(PIN_S2Y2);
        ligarDispositivo(PIN_S3Y1);
        delay(3000);
        ligarDispositivo(PIN_S2Y2);
        break;

      default:
        Serial.println("Comando inválido.");
        break;
    }
  }
}
