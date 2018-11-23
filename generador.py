import random, math


def leer_numero(ini, fin, mensaje):

    while True:
    	try:
    		num = int(input(f"{mensaje} "))
    		if num >= ini and num <= fin:
    			break
    		else:
    			print("PorFavor introduce un valor dentro del rango")
    			continue
    	except:
    		print("PorFavor introduce un valor numerico")
    return num	

def generador():

	numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]:")
	modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

	lst=[random.uniform(0, 101) for num in range(numeros)]

	if modo == 1:

		for i, num in enumerate(lst):

			print(f"El {num} ha sido redondeado al {math.ceil(num)} que es el entero mas cercano al alza")
			
			lst[i] = math.ceil(num)

		return lst

	if modo == 2:
		for i, num in enumerate(lst):
			print(f"El {num} ha sido redondeado al {math.floor(num)} que es el entero mas cercano ala baja")
			lst[i] = math.floor(num)
		return lst
	if modo == 3:
		for i, num in enumerate(lst):
			print(f"El {num} ha sido redondeado al {round(num)} que es el entero mas cercano al decimal")
			lst[i] = round(num)
		return lst		

print(generador())	