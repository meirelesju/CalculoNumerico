import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

a = 0 
b = np.pi
n = 6

array = []
array1 = []

def f(x):
    function = 2 * np.sin(2*x)
    return function

def trapezioComposta(a, b, n):
    h = (b-a)/n
    valorFinal = 0
    print("i   |   xi   |   yi   |   ci   |   yi*ci")
    
    for i  in range(n+1):
        xi = a + i*h
        yi = f(xi)

        if i == 0 or i == n:
            ci = 1
        else:
            ci = 2

        yi_vezes_ci = yi*ci
        valorFinal += yi_vezes_ci

        armazenar = [i, xi, yi, ci, yi_vezes_ci]
        array1.append(armazenar)
        print (i, xi, yi, ci, yi_vezes_ci)


    print(valorFinal)
    Final = (h/2)*valorFinal
    print ("Valor final: ", Final)
    return Final


def simpsonComposta(a, b, n):
    h = (b-a)/n
    valorFinal = 0
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
        valorFinal +=  yi_vezes_ci
        
        armazenar = [i, xi, yi, ci, yi_vezes_ci]
        array.append(armazenar)
        print (i, xi, yi, ci, yi_vezes_ci)

    Final = (h/3)*valorFinal
    print ("Valor final: ", Final)
    return Final

#Calculando o valor da integral diretamente
def integralNormal(a, b):
    ans, err = integrate.quad(f, a, b)
    print ("Valor da integral calculada diretamente: ", ans)
    return ans


valorAproximadoTrapezio = trapezioComposta(a, b, n)
valorAproximadoSimpson = simpsonComposta(a, b, n)
valorExato = integralNormal(a,b)

ErroAbsoluto1 = abs(valorExato-valorAproximadoTrapezio)
ErroAbsoluto2 = abs(valorExato-valorAproximadoSimpson)
print ("Erro absoluto Trapezio: ", ErroAbsoluto1, "Erro absoluto Simpson: ", ErroAbsoluto2)


#------------------- Construção das tabelas ----------------------#
fig, ax = plt.subplots()
nomes = ['i', 'xi', 'yi = f(xi)', 'ci', 'yi * ci']
nomes1 = ['i', 'xi', 'yi = f(xi)', 'ti', 'yi * ti']

valores=[]
for i in range (n+1):
    valores.append(array[i])
valores1=[]
for i in range (n+1):
    valores1.append(array1[i])

desc1 = '• Valor aproximado Trapézio Composto: '+ str(valorAproximadoTrapezio)
desc2 = '• Valor aproximado Simpson Composto: '+ str(valorAproximadoSimpson)
desc3 = '• Valor exato da integral: '+ str(valorExato)
desc4 = '• Erro absoluto Trapézio: '+ str(ErroAbsoluto1)
desc5 = '• Erro absoluto Simpson: '+ str(ErroAbsoluto2)

plt.text(0, 0.115, desc1, fontweight ="bold")
plt.text(0, 0.058, desc2, fontweight ="bold")
plt.text(0, 0, desc3)
plt.text(0.5560, 0.115, desc4, fontweight ="bold")
plt.text(0.5560, 0.058, desc5, fontweight ="bold")


colors = [[(0.98, 0.98, 0.98) for c in range(5)] for r in range(7)]


plt.text(0, 1, 'Tabela da questão 2 - Trapézio:', fontweight ="bold", size = 10)
table2 = plt.table(cellText=valores1,
                  cellLoc = 'center',
                  colLabels=nomes1,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors,
                  loc=8
                  )
table2.auto_set_font_size(False)
table2.set_fontsize(10)

plt.text(0, 0.566, 'Tabela da questão 2 - Simpson:', fontweight ="bold", size = 10)
table1 = plt.table(cellText=valores,
                  colLabels=nomes,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors,
                  cellLoc = 'center',
                  loc='lower center',
                  bbox=[0, 0.195, 0.9999, 0.35])
table1.auto_set_font_size(False)
table1.set_fontsize(10)

  
ax.set_axis_off() 
plt.show()
