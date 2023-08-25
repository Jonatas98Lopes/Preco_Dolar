

def remove_caracteres_especiais(lista, caracteres_especiais):
    for caractere_especial in caracteres_especiais:
        if caractere_especial in lista:
            lista.remove(caractere_especial)
        return lista

def remove_caracteres_em_elementos_lista(lista, caracteres_especiais):
    for caractere_especial in caracteres_especiais:
        for elemento in lista:
            if caractere_especial in elemento:
                novo_elemento = elemento.replace(caractere_especial, '')
                lista.remove(elemento)
                lista.append(novo_elemento)
    return lista


arquivo_crendenciais_acesso = 'C:\\Users\\jonat\\Documents\\GitHub\\' \
  'Preco-Do_Dolar\\variacao_dolar\\variacao_dolar\\spiders\\utils\\' \
  'credenciais_acesso.txt'
with open(arquivo_crendenciais_acesso, 'r') as arquivo:
     EMAIL_USER, EMAIL_PASSWORD = arquivo.read().split('\n')


arquivo_contatos = 'C:\\Users\\jonat\\Documents\\GitHub\\' \
    'Preco-Do_Dolar\\variacao_dolar\\variacao_dolar\\spiders\\utils\\' \
    'contatos.txt'
with open(arquivo_contatos, 'r') as arquivo:
    contatos = remove_caracteres_especiais(arquivo.readlines(), ['\n', '\r', '\t'])
    contatos = remove_caracteres_em_elementos_lista(contatos, ['\n', '\r', '\t'])


arquivo_mensagem = 'C:\\Users\\jonat\\Documents\\GitHub\\' \
     'Preco-Do_Dolar\\variacao_dolar\\variacao_dolar\\spiders\\utils\\' \
     'mensagem.html'
with open(arquivo_mensagem, 'r', encoding='utf-8') as arquivo:
    mensagem_original = arquivo.read()