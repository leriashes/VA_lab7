def F1(x):
    return pow(x[0], 2) + pow(x[1], 2) / 4 - 1

def F2(x, a, b, R):
    return pow(x[0] - a, 2) + pow(x[1] - b, 2) - pow(R, 2)

def f1x(x):
    return 2 * x

def f1y(y):
    return y / 2

def f2(x, a):
    return 2 * (x - a)

def Gauss(matrix, b):
	p = 0

	#поиск главного элемента в столбце (наибольшего по модулю)
	if (abs(matrix[1][0]) > abs(matrix[0][0])):
		(matrix[1], matrix[0]) = (matrix[0], matrix[1])
		(b[1], b[0]) = (b[0], b[1])
		p = 1

	#прямой ход
	coef = 0;

	if matrix[0][0] != 0:
	    coef = matrix[1][0] / matrix[0][0];
			
	for i in range(2):
		matrix[1][i] -= matrix[0][i] * coef

	b[1] -= b[0] * coef



	det = pow(-1, p)

	for i in range(2):
		det *= matrix[i][i]


	if det == 0:
		print("Ошибка! Матрица вырожденная!")
	else:
		x = [0, 0]

		for i in range(1, -1, -1):
			s = 0

			for j in range(1, i, -1):
				s += matrix[i][j] * x[j]

			x[i] = (b[i] - s) / matrix[i][i]

	return x;








print('a = ', end = '')
a = float(input())

print('b = ', end = '')
b = float(input())

while True:
    print('R = ', end = '')
    R = float(input())
    print('\n')

    if R > 0:
        break

p = [0, 0]

print('Начальное приближение\nx = ', end = '')
p[0] = float(input())

print('y = ', end = '')
p[1] = float(input())
print('\n')

t = 0.00000000001

delta = [0, 0]

while True:
	F = [F1(p) * (-1), F2(p, a, b, R) * (-1)]
	f = [[f1x(p[0]), f1y(p[1])], [f2(p[0], a), f2(p[1], b)]]
	delta = Gauss(f, F)

	print(p[0], ' ', p[1])
	print(delta[0], ' ', delta[1], '\n')

	for i in range(2):
		p[i] = p[i] + delta[i]

	if abs(delta[0]) < t and abs(delta[1]) < t:
		break

print('Результат x = ', p[0], '    y = ', p[1])