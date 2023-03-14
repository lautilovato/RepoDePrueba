import sys

from paquete.funciones_mats import sumar, restar, multiplicar, dividir, potencia
"""
otras forma de importar:
import funciones_matematicas as fm
from funciones_matematicas import *
"""

if len(sys.argv) == 3:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    print(f"La suma entre {n1} y {n2} da: {sumar(n1, n2)}")
    print(f"La resta entre {n1} y {n2} da: {restar(n1, n2)}")
    print(f"La multiplicación entre {n1} y {n2} da: {multiplicar(n1, n2)}")
    print(f"La división entre {n1} y {n2} da: {dividir(n1, n2)}")
    print(f"La potencia entre {n1} y {n2} da: {potencia(n1, n2)}")
else:
    print("Cantidad de argumentos incorrectos(Ingrese dos números)")
