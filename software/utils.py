def validar_comando(comando, comandos_validos):
    """Valida se todos os caracteres do comando estão na lista de comandos válidos."""
    return all(c in comandos_validos for c in comando)
