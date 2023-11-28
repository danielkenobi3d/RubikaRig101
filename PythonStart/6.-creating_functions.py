def mi_funcion(var1, var2, operacion='suma'):
    if operacion == 'suma':
        return var1 + var2
    elif operacion == 'resta':
        return var1 - var2
    elif operacion == 'mult':
        return var1 * var2
    else:
        print('operacion no reconocida')
        return None


print(mi_funcion(5, 3, operacion='rango'))
