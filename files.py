def salvar_produto(produto):
    with open('C:/Users/andre/PycharmProjects/Flaske/banco/cerveja.txt', 'a') as arquivo:
        arquivo.write(
            f'{produto["cerveja"]};{produto["teor"]};{produto["tipo"]};{produto["valor"]}\n')


def ler_produto():
    lista = []

    with open('C:/Users/andre/PycharmProjects/Flaske/banco/cerveja.txt', 'r') as arquivo:
        for linha in arquivo:
            produtoLista = linha.strip().split(';')
            produto = {'cerveja': produtoLista[0], 'teor': produtoLista[1],
                       'tipo': produtoLista[2], 'valor': produtoLista[3]}
            lista.append(produto)

    return lista
