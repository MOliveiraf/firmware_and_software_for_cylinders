# Firmware de Controle de Dispositivos via Comunicação Serial

Este projeto é um firmware desenvolvido para microcontroladores, como a ESP32, projetado para receber comandos via comunicação serial e controlar dispositivos conectados a diferentes pinos. O firmware é configurado para aceitar comandos específicos que acionam ou desligam dispositivos e inclui funcionalidades como avançar e recuar cilindros simulados (ou outros dispositivos controlados).

## Funcionalidades

- **Comandos Seriais**:
  - **X/x**: Avança/retorna o dispositivo S1Y1.
  - **Y/y**: Avança/retorna o dispositivo S2Y1.
  - **Z/z**: Avança/retorna o dispositivo S3Y1.
  - **H**: Comando para posição inicial (home position), configurando os dispositivos para um estado específico.
- **Configuração de Pinos**: O firmware é facilmente adaptável para diferentes pinos GPIO de microcontroladores.
- **Feedback via Serial**: Mensagens informativas são enviadas de volta ao monitor serial para auxiliar na depuração.

## Estrutura do Projeto

- **`main.ino`**: Arquivo principal que inicializa a comunicação e o loop principal.
- **`dispositivos.h` e `dispositivos.cpp`**: Contêm funções para inicializar, ligar e desligar dispositivos.
- **`comandos.h` e `comandos.cpp`**: Implementam a lógica de processamento de comandos recebidos via serial.
- **`firmware`**: Diretório contendo todo o código fonte necessário para o microcontrolador.

## Pré-requisitos

1. **Plataforma de desenvolvimento**:
   - **Arduino IDE** ou **Visual Studio Code** com a extensão **PlatformIO**.
2. **Microcontrolador**:
   - ESP32, ESP8266, ou outro compatível.
3. **Componentes físicos**:
   - LEDs e resistores (para simulação) ou dispositivos controlados (como relés, atuadores, etc.).
4. **Bibliotecas**:
   - `Arduino.h` (padrão no ambiente de desenvolvimento Arduino).

## Como Instalar e Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/MOliveiraf/firmware_and_software_for_cylinders.git
   cd seu_repositorio_firmware/firmware
