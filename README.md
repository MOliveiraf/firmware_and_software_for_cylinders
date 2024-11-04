# Projeto Completo: Controle de Cilindros com Firmware e Software de Interface

Este projeto integra um firmware desenvolvido para microcontroladores, como ESP32/ESP8266, e um software de interface web usando Streamlit. O objetivo é controlar dispositivos (ex.: cilindros) por meio de comandos seriais, com monitoramento e visualização em uma interface amigável.

## Estrutura do Projeto

A pasta `firmware_and_software_for_cylinders` está organizada da seguinte forma:

- **`firmware/`**: Contém o código do firmware para microcontroladores, desenvolvido para receber comandos via comunicação serial e acionar dispositivos conectados.
- **`software/`**: Contém o software baseado em Streamlit, que fornece uma interface gráfica para enviar comandos e monitorar respostas via comunicação serial.

## Visão Geral

### Firmware

- **Propósito**: Receber comandos via serial e controlar dispositivos conectados aos pinos GPIO da ESP32/ESP8266.
- **Principais Funcionalidades**:
  - Processamento de comandos seriais como `X`, `Y`, `Z`, etc.
  - Controle de dispositivos com tempos predefinidos.
  - Mensagens de feedback para depuração via monitor serial.
- **Diretório**: [`firmware`](./firmware)

### Software

- **Propósito**: Fornecer uma interface web para o usuário interagir com o microcontrolador, enviando comandos e visualizando respostas.
- **Principais Funcionalidades**:
  - Conectar e desconectar da porta serial.
  - Enviar comandos e exibir logs de atividades.
  - Visualizar respostas recebidas em tempo real.
- **Diretório**: [`software`](./software)

## Pré-requisitos

- **Hardware**:
  - Microcontrolador (ESP32/ESP8266)
  - Componentes conectados (ex.: LEDs, relés)
- **Software**:
  - Python 3.7+ com as bibliotecas necessárias (listadas no `requirements.txt` dentro da pasta `software`)
  - IDE de desenvolvimento para o firmware (Arduino IDE ou Visual Studio Code com PlatformIO)

## Como Configurar

Para configurar o projeto completo, siga as instruções específicas para o firmware e o software:

### Firmware

- Navegue até a pasta `firmware` para acessar o código do microcontrolador. O `README.md` dentro dessa pasta contém todas as instruções detalhadas sobre como configurar e carregar o firmware no seu dispositivo.

### Software

- Vá para a pasta `software` para acessar o código da interface de controle. O `README.md` na pasta `software` inclui as instruções de instalação das dependências e como executar a interface Streamlit.
