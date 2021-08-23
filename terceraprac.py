import random
import matplotlib.pyplot as plt
#%matplotlib inline
# ||| python -m pip install -U pip  ||| y tambien este ||| python -m pip install -U matplotlib  este comando es para installar la libreria matplotlib.pyplot

#GENERAR UN NUMERO ALEATORIO DE 0 A 100 CON RANGO DE 13 EN 13; por ultimo un pip install


print(random.randrange(0,1000,13))

#REACOMODAR UNA LISTA AL AZAR

lista = [1,2,3,4,5,6,7,8,9,10]
print("lista original", lista)

random.shuffle(lista)
print("lista revolvida XD 😎", lista)


#   CAMPANA DE GAUSS

campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins = 13)
plt.show()
