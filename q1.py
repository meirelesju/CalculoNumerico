import numpy as np 
from scipy.integrate import quad
import matplotlib.pyplot as plt

a = -1
b = 1
n = 8
array = []

def f(x):
    function = 1/(x**4 + 1)
    return function

def simpsonComposta(a, b, n):
    h = (b-a)/n
    somatorio = 0
    print("i   |   xi   |   yi   |   ci   |   yi*ci")
    
    for i  in range(n+1):
        xi = a + i*h
        yi = f(xi)
        
        if i == 0 or i == n:
            ci = 1
        elif (i%2) == 0:
            ci = 2
        else:
            ci = 4

        yi_vezes_ci = yi*ci
        somatorio +=  yi_vezes_ci
        
        armazenar = [i, xi, yi, ci, yi_vezes_ci]
        array.append(armazenar)
        print (i, xi, yi, ci, yi_vezes_ci)

    Final = (h/3)*somatorio
    print ("Valor final: ", Final)

    return Final

#Calculando o valor da integral diretamente
def integralNormal(a, b):
    ans, err = quad(f, a, b)
    print ("Valor da integral calculada diretamente: ", ans)
    return ans


valorAproximado = simpsonComposta(a, b, n)
valorExato = integralNormal(a,b)

ErroAbsoluto = abs(valorExato-valorAproximado)
print ("Erro absoluto: ", ErroAbsoluto)
            

#------------------- Construção da tabela ----------------------#
fig, ax = plt.subplots()
nomes = ['i', 'xi', 'yi = f(xi)', 'ci', 'yi * ci']

valores=[]
for i in range (n+1):
    valores.append(array[i])

desc1 = '• Valor aproximado pelo método de Simpson: '+ str(valorAproximado)
desc2 = '• Valor exato: '+ str(valorExato)
desc3 = '• Erro absoluto: '+ str(ErroAbsoluto)

plt.text(0.2619, 0.181, desc1, fontweight ="bold")
plt.text(0.2619, 0.135, desc2, fontweight ="bold")
plt.text(0.2619, 0.089, desc3, fontweight ="bold")

colors = [[(0.98, 0.98, 0.98) for c in range(5)] for r in range(9)]

table = plt.table(cellText=valores,
                  colLabels=nomes,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors,
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
ax.set_axis_off() 
ax.set_title('Tabela da questão 1', 
             fontweight ="bold") 

plt.show()


