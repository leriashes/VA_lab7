import numpy as np
import matplotlib.pyplot as plt
import math
import getch

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

def count(matrix, b):
	p = 0
	
	if (abs(matrix[1][0]) > abs(matrix[0][0])):
		(matrix[1], matrix[0]) = (matrix[0], matrix[1])
		(b[1], b[0]) = (b[0], b[1])
		p = 1
		

	coef = 0;

	if matrix[0][0] != 0:
	    coef = matrix[1][0] / matrix[0][0];
			
	for i in range(2):
		matrix[1][i] -= matrix[0][i] * coef

	b[1] -= b[0] * coef


	det = pow(-1, p)

	for i in range(2):
		det *= matrix[i][i]

	x = [0, 0]

	if det == 0:
		print("Ошибка! Матрица вырожденная!")
		exit()
	else:
		for i in range(1, -1, -1):
			s = 0

			for j in range(1, i, -1):
				s += matrix[i][j] * x[j]

			x[i] = (b[i] - s) / matrix[i][i]

	return x






while True:
	
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

	h = 0.001
	xs = np.arange(-1, 1, h)
	plt.plot(xs, 2 * np.sqrt(1 - xs * xs), 'b')
	plt.plot(xs, (-2) * np.sqrt(1 - xs * xs), 'b')
	plt.plot([xs.max(), 1, xs.max()], [2 * np.sqrt(1 - xs.max() * xs.max()), 0, -2 * np.sqrt(1 - xs.max() * xs.max())], 'b')

	g1 = a - R
	g2 = a + R

	xs = np.arange(g1, g2, h)
	plt.plot(xs, b + np.sqrt(R * R - pow(xs - a, 2)), 'r')
	plt.plot(xs, b - np.sqrt(R * R - pow(xs - a, 2)), 'r')
	plt.plot([xs.max(), g2, xs.max()], [b + np.sqrt(R * R - pow(xs.max() - a, 2)), b, b - np.sqrt(R * R - pow(xs.max() - a, 2))], 'r')

	plt.grid(True)
	plt.show()

	print('Начальное приближение\nx = ', end = '')
	p[0] = float(input())

	print('y = ', end = '')
	p[1] = float(input())
	print('\n')

	print('Точность вычислений: ', end = '')
	t = 0.00000000001
	#t = float(input())
	print('\n')

	delta = [0, 0]
	k = 0

	xs = np.arange(-1, 1, h)
	plt.plot(xs, 2 * np.sqrt(1 - xs * xs), 'b')
	plt.plot(xs, (-2) * np.sqrt(1 - xs * xs), 'b')
	plt.plot([xs.max(), 1, xs.max()], [2 * np.sqrt(1 - xs.max() * xs.max()), 0, -2 * np.sqrt(1 - xs.max() * xs.max())], 'b')

	xs = np.arange(g1, g2, h)
	plt.plot(xs, b + np.sqrt(R * R - pow(xs - a, 2)), 'r')
	plt.plot(xs, b - np.sqrt(R * R - pow(xs - a, 2)), 'r')
	plt.plot([xs.max(), g2, xs.max()], [b + np.sqrt(R * R - pow(xs.max() - a, 2)), b, b - np.sqrt(R * R - pow(xs.max() - a, 2))], 'r')


	while k < 1000:
		F = [F1(p) * (-1), F2(p, a, b, R) * (-1)]
		f = [[f1x(p[0]), f1y(p[1])], [f2(p[0], a), f2(p[1], b)]]
		delta = count(f, F)

		plt.plot(p[0], p[1], 'go')
		plt.plot([p[0], p[0] + delta[0]], [p[1], p[1] + delta[1]], 'g')

		#print(p[0], ' ', p[1])
		#print(delta[0], ' ', delta[1], '\n')

		for i in range(2):
			p[i] = p[i] + delta[i]

		if abs(delta[0]) < t and abs(delta[1]) < t:
			break

		k += 1

	if k < 1000:
		print('Результат x = ', p[0], '    y = ', p[1])

		print('\n')

		plt.grid(True)
		plt.show()

	else:
		print('Решение расходится!')
		plt.show()

	print('\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='\n')
	cont = getch.getch()
   
	if cont == '\n' or cont == b'\r':
		print('\n\n')
	else:
		break
    