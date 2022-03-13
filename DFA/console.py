import lexer

# We open the file and print the result

archivo = lexer.openFile("ejercicio.txt")
mensaje = 'Token' + ' ' * 55 + 'Tipo'
print(mensaje)
for x in range(len(archivo)):
    result = lexer.lexerAritmetico(archivo[x])
    for y in range(len(result)):
        print(result[y], end = "\n")

