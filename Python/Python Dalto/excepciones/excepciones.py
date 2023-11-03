def sumar():

    while True:
        a = input("num1: ")
        b = input("num2: ")

        # try --> intenta hacer esto
        try:
            res = int(a) + int(b)

        # caso de q try tire una excepcion
        # tambien podemos acceder a la excepcion
        # Exception es el padre de todas las excepciones (osea la clase padre)
        except Exception as e:
            print("tenes q pasarme numeros")
            print(f"Error: {e}")
            # nombre de la excepcion
            print(f"Error: {type(e).__name__}")
        # al igual q el else en for pero aca si se ejecuta el except no se ejecuta el else y vicebersa
        # osea else se ejecuta solo si try no tiro una excepcion

        else:
            break
        # el finally se ejecuta sin importar lo q pase
        finally:
            print("soy una finally q se ejecuta siempre")

    return res


print(sumar())
