import matplotlib.pyplot as plt
from random import choice
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.title('Números elevados ao quadrado',fontsize=20)
plt.xlabel("Valores",fontsize=10)
plt.ylabel("Resultados da potencia",fontsize=10)

plt.scatter(2,4)
plt.scatter(1,1)
plt.scatter(3,9)
plt.scatter(4,16)
plt.scatter(5,25)

plt.plot(input_values,squares,linewidth=2)
plt.show()
'''
'''
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.axis([0, 1100, 0, 1100000]) # 4 args: valor minimo e maximo para X, valor minimo e máximo para Y

#plt.scatter(x_values,y_values,edgecolor='none',s=10,c='lightblue')

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,edgecolor='none', s=40) # usando colormap
# nome da cor começando com maiúsculo e terminando com s



#edgecolor --> para tirar o contorno preto padrão dos pontos
# s é para a grossura do ponto(por mais que no gráfico parece contínuo, vale lembrar que toda reta é um conjunto de pontos muito pŕoximos)
# outra coisa interessante: não importa a ordem dos argumentos pq são argumentos nomeados e não posicionais!!
# cor pode ser dada em RGB, só fazer uma tupla com três itens. Egg:c=(0.5,0.5,0.5) sempre entre 0 e 1

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)