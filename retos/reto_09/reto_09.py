"""
Usaremos este script para enseñar Python a principiantes absolutos.
El script es un ejemplo de Fizz-Buzz implementado en Python.

El problema de FizzBuzz:
Para todos los enteros entre 1 y 99 (incluidos ambos):
# imprimir fizz para múltiplos de 3
# imprimir buzz para múltiplos de 5
# imprimir fizzbuzz para múltiplos de 3 y 5
"""

def fizzbuzz(max_num):
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 
    
    for i in range(1,max_num):
        if i%num1==0 and i%num2==0:
            print(i,three_mul+five_mul)
        elif i%num1==0:
            print(i,three_mul)
        elif i%num2==0:
            print(i,five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)
