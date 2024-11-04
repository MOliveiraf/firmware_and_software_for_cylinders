import serial
import serial.tools.list_ports
import time
import logging

class SerialManager:
    def __init__(self):
        self.ser = None
        self.log = []
        self.received_data = ""

        # Configuração do logger para capturar mais detalhes
        logging.basicConfig(
            filename='app.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def listar_portas(self):
        """Retorna uma lista das portas seriais disponíveis."""
        try:
            ports = serial.tools.list_ports.comports()
            return [port.device for port in ports]
        except Exception as e:
            self.log.append(f"Erro ao listar portas seriais: {e}")
            logging.error(f"Erro ao listar portas seriais: {e}")
            return []

    def conectar(self, port, baudrate):
        """Conecta à porta serial especificada com o baudrate."""
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)

            # Verifica se a porta foi aberta com sucesso
            if self.ser.is_open:
                self.log.append(f"Conectado à porta {port} com baud rate {baudrate}.")
                logging.info(f"Conectado à porta {port} com baud rate {baudrate}.")
                self.verificar_estado_conexao()  # Verifica o estado após a conexão
            else:
                self.log.append(f"Falha ao abrir a porta {port}.")
                logging.warning(f"Falha ao abrir a porta {port}.")
                self.ser = None

        except serial.SerialException as e:
            self.log.append(f"Erro ao conectar à porta {port}: {e}")
            logging.error(f"Erro ao conectar à porta {port}: {e}")
            self.ser = None
        except Exception as e:
            self.log.append(f"Erro inesperado ao tentar conectar: {e}")
            logging.error(f"Erro inesperado ao tentar conectar: {e}")
            self.ser = None

    def verificar_estado_conexao(self):
        """Verifica e registra o estado atual da conexão serial."""
        if self.ser and self.ser.is_open:
            self.log.append(f"Porta {self.ser.port} está aberta e ativa.")
            logging.info(f"Porta {self.ser.port} está aberta e ativa.")
        else:
            self.log.append("Porta serial está fechada ou inativa.")
            logging.warning("Porta serial está fechada ou inativa.")

    def desconectar(self):
        """Desconecta da porta serial, se estiver conectada."""
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
                self.log.append("Desconectado da porta serial.")
                logging.info("Desconectado da porta serial.")
                self.ser = None
            else:
                self.log.append("Tentativa de desconexão sem conexão ativa.")
                logging.warning("Tentativa de desconexão sem conexão ativa.")
        except Exception as e:
            self.log.append(f"Erro ao desconectar: {e}")
            logging.error(f"Erro ao desconectar: {e}")

    def enviar_comando(self, comando):
        """Envia um comando via serial e lê a resposta."""
        # Verifica se a conexão está ativa antes de enviar o comando
        logging.debug("Verificando se a conexão está ativa antes de enviar o comando.")
        if not self.ser or not self.ser.is_open:
            self.log.append("Não está conectado a nenhuma porta serial.")
            logging.warning("Tentativa de enviar comando sem conexão serial.")
            return

        try:
            logging.debug("Conexão ativa antes do envio do comando.")
            self.ser.write(comando.encode('utf-8'))
            self.log.append(f"Enviado: {comando}")
            logging.info(f"Enviado: {comando}")
            time.sleep(0.5)

            resposta_total = []
            while self.ser.in_waiting > 0:
                try:
                    resposta = self.ser.readline().decode('utf-8').strip()
                    if resposta:
                        resposta_total.append(resposta)
                        self.received_data += f"{resposta}\n"
                        self.log.append(f"Recebido: {resposta}")
                        logging.info(f"Recebido: {resposta}")
                except UnicodeDecodeError as e:
                    self.log.append(f"Erro ao decodificar resposta: {e}")
                    logging.error(f"Erro ao decodificar resposta: {e}")

            if not resposta_total:
                self.log.append("Nenhuma resposta recebida do dispositivo.")
                logging.warning("Nenhuma resposta recebida do dispositivo.")

            logging.debug("Envio de comando e leitura de resposta concluídos.")

        except serial.SerialTimeoutException as e:
            self.log.append(f"Erro de timeout ao enviar comando: {e}")
            logging.error(f"Erro de timeout ao enviar comando: {e}")
        except Exception as e:
            self.log.append(f"Erro ao enviar comando: {e}")
            logging.error(f"Erro ao enviar comando: {e}")

    def limpar_logs(self):
        """Limpa os logs de atividades."""
        self.log = []
        logging.info("Logs de atividades limpos.")

    def limpar_recebido(self):
        """Limpa os dados recebidos."""
        self.received_data = ""
        logging.info("Dados recebidos limpos.")
