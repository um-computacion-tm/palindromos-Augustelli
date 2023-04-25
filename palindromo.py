def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_inv = cadena[::-1].lower()
    longitud = len(cadena)
    for i in range(longitud):
        if i >= longitud // 2:
            return 'Palindromo encontrado'
        elif cadena[i] != cadena_inv[i]:
            return 'No es palindromo'
