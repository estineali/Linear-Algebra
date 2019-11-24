import matplotlib.pyplot as plt 
import numpy as np

x = [i for i in np.arange(-10, 10, 0.1)]

def basis_1(x):
	return x**2 - 49
def basis_2(x):
	return x - 7

b1 = [basis_1(i) for i in x]
b2 = [basis_2(i) for i in x]

fig = plt.figure()
basis = fig.add_subplot(111)
basis.set_xlabel('x')
basis.set_title("basis for p(7) = 0")

basis.plot(x, b1, label=f'x\N{SUPERSCRIPT TWO} - 49')
basis.plot(x, b2, label='x - 7')
basis.plot(x, [-49 for i in x], linestyle='--', label='y = -49')
basis.set_title('Basis Functions for p(7) = 0')

basis.grid(linestyle='-')
legend = basis.legend()
plt.show()