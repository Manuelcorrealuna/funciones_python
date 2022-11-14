# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# Objetivo:
# Reutilizar código escrito en desafios anteriores

# --------------------------------
# Alumno:
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados():
    lista_invitados = []
    print("Función Generar Invitados")
    
    for i in range(3):
        print("Ingrese un nombre:", i)
        nombre = str(input())
        lista_invitados.append(nombre)
        
    return lista_invitados
# --------------------------------

# --------------------------------
# Alumno:
# Aquí copiar la función "ordenar"
# ya elaborada

def ordenar(numeros):
    print("Función Ordenar")
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: 
    # Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bloque "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el retorno en "lista_invitados"

    # lista_invitados = generar_invitados()
lista_invitados = generar_invitados()


    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada
    #    --> Almacenar el retorno en "lista_invidatos_ordenada"

    # lista_invidatos_ordenada = ordenar(lista_invitados)
lista_invitados_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":
print("La lista ordenada es:", lista_invitados_ordenada)

print("terminamos")
