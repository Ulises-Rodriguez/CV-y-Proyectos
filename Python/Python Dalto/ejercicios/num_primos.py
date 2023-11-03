# creando una funcion q nos devuelva los numeros primos entre 0 y el num q se pasa

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def nums_primos(num):

    numeros_primos = []

    for i in range(2, num+1):
        if is_prime(i) == True:
            numeros_primos.append(i)

    return numeros_primos


res = nums_primos(7)
print(res)
res = nums_primos(8)
print(res)
res = nums_primos(9)
print(res)
res = nums_primos(89)
print(res)
res = nums_primos(100)
print(res)
