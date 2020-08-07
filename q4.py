import numpy as np
import matplotlib.pyplot as plt

h = 0.5
x0 = 0
y0 = 1000
t = 5
n = t/h #5 dias com intervalos de 0.5, ou seja, 10 intervalos

def f(x,y):
    function = 2*10**-6 * (100000-y) *y
    return function

array = []
def metodoRungeKutta (h, n):
    xn = x0
    yn = y0

    print("\n","-----------Método Runge Kutta------------------","\n")
    for i in range (int(n+1)):
        
        k1 = f(xn, yn) 
        k2 = f(xn+(h/2), yn+(k1*(h/2)))
        k3 = f(xn+(h/2), yn+(k2*(h/2)))
        k4 = f(xn+h, yn + (k3 * h))
        k = (k1+2*k2+2*k3+k4)/6

        y_n_mais_1 = yn + h * k

        if i == n:
            armazenar = [i, xn, yn, '-' , '-', '-', '-', '-']
            array.append(armazenar)
            return yn              
        else:
            armazenar = [i, xn, yn, k1, k2, k3, k4, y_n_mais_1]
            print("Iteração:", i,"\n", "x%d:" % (i), xn ,"y%d:" % (i), yn,"\n", "k1:", k1, "k2:", k2, "k3:", k3, "k4:", k4, "\n", "y%d:"  % (i+1),y_n_mais_1,"\n")
            array.append(armazenar)
        
        xn += h 
        yn =  y_n_mais_1
        


a = metodoRungeKutta(h, n)
print ("Ao final de 5 dias, o número de infectados será de" , a, "pessoas")


#------------------- Construção da tabela ----------------------#
fig, ax = plt.subplots()
nomes = ['i', 'xi', 'yi = f(xi)', 'k1', 'k2', 'k3', 'k4', 'y i+1']

desc1 = '• Ao final de 5 dias, o número de infectados será de '+ str(a) + ' pessoas'
plt.text(-0.125, 0.1, desc1, fontweight ="bold", size = 9.5)

colors = [[(0.98, 0.98, 0.98) for c in range(8)] for r in range(11)]


table2 = plt.table(cellText=array,
                  cellLoc = 'center',
                  colLabels=nomes,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors,
                  loc='center',
                  bbox=[-0.14, 0.2, 1.25, 0.7]
                  )
#

cellDict=table2.get_celld()
for i in range (int(n+2)):cellDict[(i,0)].set_width(0.05)
for i in range (int(n+2)):cellDict[(i,1)].set_width(0.05)

table2.auto_set_font_size(False)
table2.set_fontsize(10)

plt.text(0.3, 1, 'Tabela da questão 4 - Método Runge Kutta', fontweight ="bold", size = 10)
   
ax.set_axis_off() 
plt.show()