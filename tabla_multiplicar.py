# para trabajar con argumentos necesito importar la siguiente libreria:
import sys
print(sys.argv)

# tabla de x (numero ingresado por parametro)
numero = int(sys.argv[1])
for i in range(1,10):
    print(f"{numero} x {i} = {numero * i}")

print("Hola mundo!")
print("Estoy en la clase 16")

# me olvide de esto
