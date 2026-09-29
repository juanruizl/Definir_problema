def normalizar(texto):
    texto = texto.lower()

    con_tilde = "áéíóúü"
    sin_tilde = "aeiouu"

    limpio = ""
    for caracter in texto:
        if caracter in con_tilde:
            posicion = con_tilde.index(caracter)
            caracter = sin_tilde[posicion]

        if caracter.isalnum():
            limpio += caracter

    return limpio

    def es_palindromo(texto):
        limpio = normalizar(texto)

        invertido = ""
        for i in range(len(limpio) - 1, -1, -1):
            invertido += limpio[i]

        return limpio == invertido


if __name__ == '__main__':
    texto = input('Introduce una palabra o frase: ')

    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo.')
    else:
        print(f'"{texto}" no es un palíndromo.')