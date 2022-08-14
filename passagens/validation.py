def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino sao iguais"""
    if origem == destino:
            lista_de_erros['destino'] = 'Origem e destino nao podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numerico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Nao inclua numeros nesse campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se data de ida e maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta nao pode ser menor que data de ida'

def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se a data de ida e menor que data de hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida nao pode ser menor do que a data de hoje'
