def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c

# => decorador = funcion_a(suma)
@funcion_a
def suma(a, b):
    return a + b

#    decorador(10, 20) 
print(suma(10, 20))

# Resultado:
# Antes de la ejecución de la función a decorar
# Entra en la función suma
# Después de la ejecución de la función a decorar
# 30
