
def suma(n1, n2):
	try:
		suma = n1 + n2
	except TypeError:

		print('Error: Tipo de dato no válido')
		print('#############################')
		return f"No es posible sumar '{n1}' y '{n2}'ya que son tipos de datos distintos"

	return suma

def resta(n1, n2):
	try:
		resta = n1 - n2
	except TypeError:

		print('Error: Tipo de dato no válido')
		print('#############################')
		return f"No es posible restar '{n1}' y '{n2}' ya que son tipos de datos distintos"

	return resta


def producto(n1, n2):
	try:
		mul = n1 * n2
	except TypeError:

		print('Error: Tipo de dato no válido')
		print('#############################')
		return f"No es posible multiplicar '{n1}' y '{n2}' ya que son tipos de datos distintos"

	return mul


def division(n1, n2):
	try:
		div = n1 / n2

	except TypeError:

		print('Error: Tipo de dato no válido')
		print('#############################')
		return f"No es posible dividir '{n1}' y '{n2}' ya que son tipos de datos distintos"

	except ZeroDivisionError:
		print('Error: no es posible dividir por cero')
		print('#############################')
		return f"No es posible dividir '{n1}' y '{n2}' ya que la divison por '{n2}' no es posible"



	return div



########################### Funcion Unica con argumento operacion y aprendizaje ###########################################
sumar = ["sumar", "+"]
restar = [ "restar", "-"]
dividir = ["dividir", "/"]
multiplicar = ["multiplicar", "*" ]


def calculadora(n1, n2, operacion):


	try:     #Funciones matematicas basicas
		if operacion.lower() in sumar:
		    return n1 + n2
		elif operacion.lower() in restar:
		    return n1 - n2
		elif operacion.lower() in dividir:
		    return n1 / n2
		elif operacion.lower() in multiplicar:
		    return n1 * n2 
		else:
		    print(f"""No he entendido la operacion que quieres hacer,porfavor indicame que querias hacer:

[1] - sumar {n1} + {n2}
[2] - restar {n1} - {n2}
[3] - dividir {n1} / {n2}
[4] - multiplicar {n1} * {n2}
""")   
		    res = int(input("Indica el numero de la operacion que querias realizar: "))

		    if res == 1:
		    	sumar.append(operacion)
		    elif res == 2:
		    	restar.append(operacion)
		    elif res == 3:
		    	dividir.append(operacion)
		    elif res == 4:
		        multiplicar.append(operacion)
		    else:
		        print("Has escrito un numero fuera de rango no puedo ayudarte")    
		    return calculadora(n1, n2, operacion)	

	except TypeError: 

		print('Error: Tipo de dato no válido')
		print('#############################')
		return f"No es posible dividir '{n1}' y '{n2}' ya que son tipos de datos distintos"

	except ZeroDivisionError:
		print('Error: no es posible dividir por cero')
		print('#############################')
		return f"No es posible dividir '{n1}' y '{n2}' ya que la divison por '{n2}' no es posible"

	                        	