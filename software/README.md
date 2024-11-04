# Interface de Controle Serial com Streamlit

Este projeto fornece uma interface gráfica baseada em web, usando Streamlit, para interagir com dispositivos controlados via comunicação serial. A aplicação permite ao usuário configurar a porta serial, enviar comandos específicos para o dispositivo e visualizar o histórico de atividades e respostas recebidas.

## Funcionalidades

- **Conexão com Porta Serial**: Configuração da porta e baud rate para estabelecer uma comunicação serial com o dispositivo.
- **Envio de Comandos**: Envio de sequências de comandos através da interface.
- **Recepção de Respostas**: Exibe respostas recebidas do dispositivo em tempo real.
- **Logs de Atividades**: Histórico de comandos enviados e respostas recebidas, com opções para limpar o histórico.
- **Controle de Conexão**: Conectar e desconectar dinamicamente da porta serial diretamente pela interface.
- **Compatibilidade com Streamlit**: Visualização direta no navegador, com execução de sessões e estado mantidos.

## Pré-requisitos

1. **Python 3.7+** instalado.
2. **Bibliotecas necessárias** listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
3. **Dispositivo Serial** conectado (ex.: Arduino ou ESP com código de firmware configurado).

## Estrutura do Projeto

- **`app.py`**: Arquivo principal com o código Streamlit para rodar a interface de controle serial.
- **`serial_manager.py`**: Arquivo com a classe responsável pelo gerenciamento da conexão serial.
- **`ui_components.py`**: Arquivo contendo funções auxiliares para a interface do Streamlit.
- **`utils.py`**: Funções utilitárias gerais.
- **`app.log`**: Arquivo de log para registrar informações e erros.
- **`requirements.txt`**: Lista de dependências para instalar as bibliotecas necessárias.
- **`README.md`**: Documentação do projeto.
- **`logs`** (Opcional): Diretório para armazenar logs de conexão ou arquivos relacionados.

## Configuração

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio

## Como Executar o Projeto

Para iniciar a interface Streamlit, use o seguinte comando no terminal:
bash
streamlit run app.py
 ```bash
   streamlit run app.py