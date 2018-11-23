import io,sys

#Funcion

def contador(arg = None, incr = 1):
	try:

		try:
			fichero = open('contador.txt', 'r')

		except:
			fichero = open('contador.txt', 'a+')
			fichero.write('0')

		fichero.seek(0)
		data = int(fichero.read())
		fichero.close()

		if arg == 'dec':
			data = data - int(incr)
		elif arg == 'asc':
			data = data + int(incr)
		else:
			print('Argumento no valido el contador no se ha modificado')

		print(f'El valor de contador es {data}')

		fichero = open('contador.txt', 'w')
		fichero.write(str(data))
		fichero.close()
	except:
		print('Error: Fichero corrupto')

if len(sys.argv) == 2:
	contador(sys.argv[1])
elif len(sys.argv) == 3:
	contador(sys.argv[1], sys.argv[2])	
else:
	print("Pasa los argumentos requeridos")
	contador()
