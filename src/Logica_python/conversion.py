##### FUNCIÓN DE CONVERSIÓN A MARKDOWN #####
def conversion_md(lista_filtrada, valoration):
    lista = lista_filtrada
    string = ''
    for diccionario in lista:
        for item in diccionario:
            if item == 'name':
                string += "# **Menu: " + diccionario[item] + '**' + "\n"  

            if item == 'plates':
                string += '### Platos: ' + '\n' + '- ' + \
                    diccionario[item][0] + '\n' + '- ' + diccionario[item][1] + \
                    '\n' + '- ' + diccionario[item][2] + '\n' + '\n'

            if item == 'drink':
                string += '### Bebida: ' + diccionario[item] + '\n' + '\n'

            if item == 'stock':
                string += '### Stock: ' + str(diccionario[item]) + '\n' + '\n'

            if item == 'price':
                string += '### Precio: ' + str(diccionario[item]) + '\n' + '\n'

            if item == 'discount':
                string += '### Descuento: ' + \
                    str(diccionario[item]) + ' %' + '\n' + '\n'

            if item == 'valoration':
                string += '### **Valoracion:** ' + \
                    str(diccionario[item]) + '\n' + '<br>' + '\n' + '\n'

    with open('Restaurant_Web/content/posts/pagina_' + str(valoration) + '.md', 'w', encoding='UTF-8') as f:
        f.write(string)