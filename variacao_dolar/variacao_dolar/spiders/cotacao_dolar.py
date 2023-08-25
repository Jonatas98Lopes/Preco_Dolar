


arquivo_crendenciais_acesso = 'C:\\Users\\jonat\\Documents\\GitHub\\' \
  'Preco-Do_Dolar\\variacao_dolar\\variacao_dolar\\spiders\\utils\\' \
  'credenciais_acesso.txt'
with open(arquivo_crendenciais_acesso, 'r') as arquivo:
     EMAIL_USER, EMAIL_PASSWORD = arquivo.read().split('\n')


arquivo_contatos = 'C:\\Users\\jonat\\Documents\\GitHub\\' \
    'Preco-Do_Dolar\\variacao_dolar\\variacao_dolar\\spiders\\utils\\' \
    'contatos.txt'
with open(arquivo_contatos, 'r') as arquivo:
    contatos = arquivo.readlines()