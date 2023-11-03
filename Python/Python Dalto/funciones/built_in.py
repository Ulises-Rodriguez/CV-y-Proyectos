nums = [1, 8, 6, 7, 5]

res = max(nums)
print(res)


# con la funcion round podes trabajar los numeros con , de mejor manera podemos elegir cuantos numeros decumales queresmo dejar
numero = round(12.587955469, 2)
print(numero)

# funcion bool --> devuelve false si : 0, dato vacio, false , nunguno / true si: true, algo q no sea 0, cadena, datos no vacios

res = bool()
print(res)


# all --> retorna true si todo lo valores son verdaderos
res_all = all([2569, "true", [5, 6]])
print(res_all)

res_all = all([None, "true", [5, 6]])
print(res_all)

# sum --> suma todos los valores
res_sum = sum([2, 5, 9, 3])
print(res_sum)
