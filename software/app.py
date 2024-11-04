import streamlit as st
from serial_manager import SerialManager
import ui_components  


serial_manager = SerialManager()
st.set_page_config(page_title="Controle Serial", layout="wide")

# Cria a seção de configuração do sidebar
ui_components.configurar_serial_sidebar(serial_manager)

# Cria a seção de envio de comandos
ui_components.enviar_comandos_section(serial_manager)

# Exibe os logs de atividades
ui_components.exibir_logs(serial_manager)

# Exibe os dados recebidos do dispositivo
ui_components.exibir_dados_recebidos(serial_manager)








