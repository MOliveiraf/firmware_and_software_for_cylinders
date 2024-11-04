#include "dispositivos.h"
#include "comandos.h"

void setup() {
  iniciarDispositivos();
  iniciarComunicacao();
}

void loop() {
  verificarComandos();
}
