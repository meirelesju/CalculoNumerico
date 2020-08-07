import numpy as np
import matplotlib.pyplot as plt

h = 0.5
x0 = 0
y0 = 0
t = 5
n = t/h #5 segundos com intervalos de 0.5, ou seja, 10 intervalos

array = []
array1 =[]

def f(x, y):
    function = (2000 - (2*y)) / (200-x)
    return function

def metodoHeun (h, n):
    xi = x0
    yi = y0
    print("\n","-----------Método Heun------------------","\n")
    for i in range (int(n+1)):
        
        k1 = f(xi, yi) 
        k2 = f(xi+h, yi + (h * k1))
        k = (k1+k2)/2
        
        y_i_mais_1 = yi + h * k
        
        #Se estiver na última iteração
        if i == n:
            #armazena o yi para colocar na tabela e dispensa o que não é necessário
            armazenar = [i, xi, yi, '-' , '-', '-'] 
            array.append(armazenar) 
            print("v(5) =", yi)
            return yi                      
        else:
            #Se não estiver na última iteração, calcula normalmente e armazena os valores
            armazenar = [i, xi, yi, k1, k2, y_i_mais_1]
            print("Iteração:", i,"\n", "x%d:" % (i), xi ,"y%d:" % (i), yi,"\n", "k1:", k1, "k2:", k2, "\n", "y%d:"  % (i+1),y_i_mais_1,"\n")        
            array.append(armazenar)
       
        xi += h 
        yi =  y_i_mais_1
    

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
        
        #Se estiver na última iteração
        if i == n:
            #armazena o yi para colocar na tabela e dispensa o que não é necessário
            armazenar = [i, xn, yn, '-' , '-', '-', '-', '-']
            array1.append(armazenar)
            print("v(5) =", yn)
            return yn                      
        else:
             #Se não estiver na última iteração, calcula normalmente e armazena os valores
            armazenar = [i, xn, yn, k1, k2, k3, k4, y_n_mais_1]
            print("Iteração:", i,"\n", "x%d:" % (i), xn ,"y%d:" % (i), yn,"\n", "k1:", k1, "k2:", k2, "k3:", k3, "k4:", k4, "\n", "y%d:"  % (i+1),y_n_mais_1,"\n")
            array1.append(armazenar)
       
        xn += h 
        yn =  y_n_mais_1


def solucaoExata(t):
    function = 10*t - (t**2/40)
    return function

valorAproximadoHeun = metodoHeun(h, n)
print(valorAproximadoHeun)
valorAproximadoRunge = metodoRungeKutta(h, n)
valorExato = solucaoExata(t)

print("Solução exata: ",valorExato)

ErroAbsoluto1 = abs(valorExato-valorAproximadoHeun)
ErroAbsoluto2 = abs(valorExato-valorAproximadoRunge)
print ("Erro absoluto Heun: ", ErroAbsoluto1, "Erro absoluto Hunge: ", ErroAbsoluto2)


#------------------- Construção das tabelas ----------------------#

#Janela 1
fig, ax = plt.subplots()
nomes = ['i', 'xi', 'yi = f(xi)', 'k1', 'k2', 'y i+1']
nomes1 = ['i', 'xi', 'yi = f(xi)', 'k1', 'k2', 'k3', 'k4', 'y i+1']

colors = [[(0.98, 0.98, 0.98) for c in range(6)] for r in range(11)]
colors1 = [[(0.98, 0.98, 0.98) for c in range(8)] for r in range(11)]

plt.text(0, 1.02, 'Tabela da questão 3 a) - Heun:', fontweight ="bold", size = 10)
table1 = plt.table(cellText=array,
                  cellLoc = 'center',
                  colLabels=nomes,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors,
                  loc = 8,
                  bbox=[0, 0.5, 1, 0.5]
                  )
                  
table1.auto_set_font_size(False)
table1.set_fontsize(10)


plt.text(0, 0.430, 'Tabela da questão 3 b) - Runge Kutta:', fontweight ="bold", size = 10)
table2 = plt.table(cellText=array1,
                  colLabels=nomes1,
                  colColours =["#c4def2"]*10, 
                  cellColours = colors1,
                  cellLoc = 'center',
                  loc='lower center',
                  bbox=[0, -0.09, 1, 0.5])
table2.auto_set_font_size(False)
table2.set_fontsize(10)

cellDict=table2.get_celld()
for i in range (int(n+2)):cellDict[(i,0)].set_width(0.05)
for i in range (int(n+2)):cellDict[(i,1)].set_width(0.05)

table1.auto_set_font_size(False)
table1.set_fontsize(10)
ax.set_axis_off() 

#Janela 2
fig1, ax1 = plt.subplots()
desc1 = 'a) Valor aproximado Heun: v(5) =' + str(valorAproximadoHeun) + '\n\nb) Valor aproximado RungeKutta: v(5) =' + str(valorAproximadoRunge)+ '\n\nc) Solução exata da integral: '+ str(valorExato) +'\n\n             Erro absoluto Heun: '+ str(ErroAbsoluto1)+'\n\n             Erro absoluto Hunge: '+ str(ErroAbsoluto2)
ax1.text(0.2, 0.5, desc1,fontweight ="bold",
        bbox ={'facecolor':'lightgreen', 
               'alpha':0.6, 'pad':20}) 
ax1.set_axis_off() 

plt.show()
