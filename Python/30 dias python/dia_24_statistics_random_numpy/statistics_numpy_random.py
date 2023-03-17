# Statistics

'''
La estadística es la disciplina que estudia la recopilación, organización, visualización, análisis, interpretación y presentación de datos. La estadística es una rama de las matemáticas que se recomienda como requisito previo para la ciencia de datos y el aprendizaje automático.

Data --> Los datos son cualquier conjunto de caracteres que se recopilan y traducen para algún propósito, generalmente análisis. Puede ser cualquier carácter, incluidos texto y números, imágenes, sonido o video. Si los datos no se ponen en un contexto, no tienen ningún sentido

Statistics Module --> El módulo de estadísticas de Python proporciona funciones para calcular estadísticas matemáticas de datos numéricos. (Está dirigido al nivel de graficadores y calculadoras científicas.)

NumPy --> para instalarlo pip3 install numpy

          NumPy es la biblioteca central para computación científica en Python. Proporciona un objeto de matriz multidimensional de alto rendimiento y herramientas para trabajar con matrices.

          para importarlo --> import numpy as np
'''

# numpy
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Creating numpy array using

# forma clasica
lst = [1, 5, 9, 6, 3]
print(type(lst))
print(lst)
array_dos_dimensiones = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print()

# con numpy
# por defecto es el tipo del array es int
numpy_array = np.array(lst)
print(type(numpy_array))
print(numpy_array)
print()

# array float
numpy_array_float = np.array(lst, dtype=float)
print(type(numpy_array_float))
print(numpy_array_float)

# arry bool
numpy_array_bool = np.array([0, 1, 0, -1], dtype=bool)
print(type(numpy_array_bool))
print(numpy_array_bool)
print()

# arry multidimencional
numpy_array_multidimencional = np.array(array_dos_dimensiones)
print(type(numpy_array_multidimencional))
print(numpy_array_multidimencional)
print()

# tolist() --> convertir numpy array a lista
np_to_lst = numpy_array.tolist()
print(type(np_to_lst))
print(np_to_lst)
print()

# shape --> El método de forma proporciona la forma de la matriz como una tupla. La primera es la fila y la segunda es la columna. Si la matriz es solo unidimensional, devuelve el tamaño de la matriz.
nums = np.array([1, 2, 3, 4, 5, 6])
print(nums)
print("shape : ", nums.shape)
print(numpy_array_multidimencional)
print("shape : ", numpy_array_multidimencional.shape)

array_tres_por_cuatro = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [7, 8, 9, 10]])
print(array_tres_por_cuatro)
print("shape : ", array_tres_por_cuatro.shape)
print()

# size --> nos da el la cantidad de elementos del array
array_size = np.array([1, 5, 8, 9, 6, 3])
print("size:", array_size.size)
print()
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
print('The size:', two_dimensional_list.size)
print()


# operaciones matematicas usando numpy
'''
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)
'''
# +
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
plus_ten = numpy_array_from_list + 10
print(plus_ten)
print()
# -
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)
print()
# *
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
print()
# /
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
print()
# %
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
print()
# //
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
print()
# **
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)
print()

# dtype --> nos permite ver el tipo de los array
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
print()


# convertir un tipo a otro
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
numpy_int_arr

numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
numpy_int_arr

np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print()

# Multi-dimensional Arrays
numpy_array_multidimencional = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(numpy_array_multidimencional))
print(numpy_array_multidimencional.size)
print(numpy_array_multidimencional.shape)
print(numpy_array_multidimencional.dtype)
print()


# obtener elementos del array
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
print()

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
print()


# slice
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# el primero acota las filas, el segundo las columnas
first_two_rows_and_columns = two_dimension_array[0:3, 0:1]
print(first_two_rows_and_columns)
print()

# Reverse the row and column positions
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array[::-1, ::-1])
print()

# modificar elementos
print(two_dimension_array)
# primer elem fila y segundo columna (osea coordenada x y)
two_dimension_array[0, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)
print()

# poner todos los elementos en 0
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)
print()

# poner todos los elementos en 1
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)
print()

# para n
twoes = numpy_ones * 2
print(twoes)
print()

# reshape y faltten
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)  # acota el array
print(reshaped)
print()
flattened = reshaped.flatten()
print(flattened)  # aplana el array
print()


# concatenar
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
print()

# Random
# casi todo se puede hacer tambien con el modulo random
# num random
random_float = np.random.random()
print(random_float)
print()

# array de numeros float
random_nums = np.random.random(5)
print(random_nums)
print()

# int random nums
random_num_int = np.random.randint(0, 11)
print(random_num_int)
print()

# generar nums int random y meterlos en un arrya
# size te indica la cantidad de elementos
array_nums = np.random.randint(0, 11, size=4)
print(array_nums)
print()

# array multidimencional de nums random
random_nums_array_mult = np.random.randint(2, 11, size=(3, 3))
print(random_nums_array_mult)
print()

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
print()

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2, 3])
print(r)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2, 2)
rand

rand2 = np.random.randn(2, 2)
rand2

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5, 3])
rand_int


#Numpy and Statistics
sns.set()
plt.hist(normal_array, color="grey", bins=50)
print()

# matices con numpy
four_x_four_matrix = np.matrix(np.ones((4, 4), dtype=int))
print(four_x_four_matrix)
print()

np.asarray(four_x_four_matrix)[2] = 2
print(four_x_four_matrix)


# numpy arange() --> A veces, desea crear valores que estén espaciados uniformemente dentro de un intervalo definido. Por ejemplo, desea crear valores del 1 al 10; puedes usar la función numpy.arange()

# con range
lst = range(0, 11, 2)
for i in lst:
    print(i)

# arange()
whole_nums = np.arange(0, 20, 1)
print(whole_nums)
print()
whole_nums2 = np.arange(1, 20, 1)
print(whole_nums2)
print()
whole_nums3 = np.arange(1, 20, 2)
print(whole_nums3)
print()

# mínimo, máximo, media, mediana, percentil, desviación estándar y varianza, etc.
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print()

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ==')
# el axis te marca si mira la matris desde el eje x o y
# si el axis es = 1 entonces las filas ahora son las columnas
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))
print()

# crear una secuencia repetida
a = [1, 2, 3]
# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))


# mean, standard deviation, number of samples
# np_normal_dis = np.random.normal(5, 0.5, 1000)
# np_normal_dis
# ## min, max, mean, median, sd
# print('min: ', np.min(np_normal_dis))
# print('max: ', np.max(np_normal_dis))
# print('mean: ', np.mean(np_normal_dis))
# print('median: ', np.median(np_normal_dis))
# print('mode: ', stats.mode(np_normal_dis))
# print('sd: ', np.std(np_normal_dis))


# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()
print()

# Dot Product
# Linear algebra
# Dot product: product of two arrays
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
print()

# multiplicacion de matrices
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(np.matmul(a, b))
print()

# determinarnte
print(np.linalg.det(a))
print()

# matrices con listas comprendidas
new_list = [x + 2 for x in range(0, 11)]
print(new_list)
print()

# We use linear equation for quantities which have linear relationship. Let's see the example below:
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)


plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()


# To draw the Gaussian normal distribution
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()
