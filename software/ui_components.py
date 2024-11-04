import streamlit as st

def configurar_serial_sidebar(serial_manager):
    """Cria a seção de configurações serial no sidebar."""
    st.sidebar.header("Configurações Serial")
    
    portas_disponiveis = serial_manager.listar_portas()
    if portas_disponiveis:
        porta_selecionada = st.sidebar.selectbox("Selecione a porta serial", portas_disponiveis)
        baudrate = st.sidebar.number_input("Baud Rate", value=9600, step=1200, min_value=300, max_value=115200)
        
        # Botões de Conexão/Desconexão
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.sidebar.button("Conectar"):
                if serial_manager.ser is None or not serial_manager.ser.is_open:
                    serial_manager.conectar(porta_selecionada, baudrate)
                else:
                    serial_manager.log.append("Já está conectado a uma porta serial.")
        
        with col2:
            if st.sidebar.button("Desconectar"):
                serial_manager.desconectar()
    else:
        st.sidebar.warning("Nenhuma porta serial disponível. Conecte o dispositivo e atualize a página.")

def enviar_comandos_section(serial_manager):
    """Cria a seção de envio de comandos na interface principal."""
    if serial_manager.ser and serial_manager.ser.is_open:
        st.success(f"Conectado a porta {serial_manager.ser.port} com baud rate {serial_manager.ser.baudrate}.")
        
        st.subheader("Enviar Comandos")
        comando = st.text_input("Digite o comando (Ex: XYZx)")
        if st.button("Enviar Comando"):
            if comando:
                serial_manager.enviar_comando(comando)
            else:
                st.warning("Por favor, insira um comando para enviar.")
    else:
        st.warning("Não está conectado a nenhuma porta serial. Por favor, conecte-se para enviar comandos.")

def exibir_logs(serial_manager):
    """Exibe os logs de atividades."""
    st.subheader("Logs de Atividades")
    if serial_manager.log:
        for entrada in serial_manager.log:
            st.write(entrada)
    else:
        st.write("Nenhuma atividade registrada.")
    
    # Botão para limpar logs
    if st.button("Limpar Logs"):
        serial_manager.limpar_logs()

def exibir_dados_recebidos(serial_manager):
    """Exibe os dados recebidos do dispositivo."""
    st.subheader("Dados Recebidos do Dispositivo")
    st.text_area("Respostas", value=serial_manager.received_data, height=200)
    
    # Botão para limpar dados recebidos
    if st.button("Limpar Respostas"):
        serial_manager.limpar_recebido()
