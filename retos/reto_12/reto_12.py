"""
Usaremos este script para enseñar Python a principiantes absolutos.
El script es un ejemplo de Fizz-Buzz implementado en Python.

El problema de FizzBuzz:
Para todos los enteros entre 1 y 99 (incluidos ambos):
# imprimir fizz para múltiplos de 3
# imprimir buzz para múltiplos de 5
# imprimir fizzbuzz para múltiplos de 3 y 5
"""
class FizzBuzz():

    def __init__(self):
        "Initializer"
        self.num1 = 3
        self.num2 = 5
        self.three_mul = 'fizz'
        self.five_mul = 'buzz'

    
    def fizzbuzz(self,max_num):
        for i in range(1,max_num):
            if i%self.num1==0 and i%self.num2==0:
                print(i,self.three_mul+self.five_mul)
            elif i%self.num1==0:
                print(i,self.three_mul)
            elif i%self.num2==0:
                print(i,self.five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    #Testing the fizzbuzz class
    test_obj = FizzBuzz()
    test_obj.fizzbuzz(100)
