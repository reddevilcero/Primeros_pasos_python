from io import open

texto = "Una linea con texto\nOtra linea con texto"
#abrir un fichero en modo escritura borra todo el contenido
fichero = open("fichero.txt", 'w')

fichero.write(texto)
#Importante cerrar el fichero para guardar cambios y 
fichero.close()

fichero = open('fichero.txt', 'r')

texto = fichero.read()

fichero.close()

print(texto)

