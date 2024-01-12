#31-03-2021--->29-04-2021
from scipy.signal import *
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
Y = [67029,79034,69822,62974,34932,77794,61958,75038,79878,82698,66535,46380,70230,77878,75375,74289,79991,52373,42018,67933,61273,62857,62257,62399,53363,32065,47691,50856,55125,58199]
X=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
plt.subplot(3,1,1)
figure(1)
plt.title("Nombre d'infectées par jour")
plt.plot(X,Y,marker = '.',c = 'red',label="f(x)")
plt.legend()
plt.ylabel("nombre des infectés")
yprime=diff(Y)
plt.subplot(3,1,2)
plt.plot(X[0:len(X)-1],yprime,marker = '.',c = 'red',label="f'(x)")
plt.legend()
plt.xlabel("jours")
plt.ylabel("nombre des infectés")
ysecond=diff(yprime)
plt.subplot(3,1,3)
plt.plot(X[0:len(X)-2],ysecond,'o:',c = 'yellow',label="f'(x)")
plt.legend()
plt.xlabel("jours")
plt.ylabel("nombre des infectés")
z= [1076,1162,933,712,283,515,921,2570,1090,872,709,283,467,897,956,887,903,680,313,477,913,842,1008,764,724,279,474,641,959,854]
figure(2)
plt.subplot(3,1,1)
plt.title("Nombre de déces par jour")
plt.plot(X,z,marker = '.',c = 'red',label="f(x)")
plt.legend()
plt.ylabel("nombre de déces")
yprimee=diff(z)
plt.subplot(3,1,2)
plt.plot(X[0:len(X)-1],yprimee,marker = '.',c = 'red',label="f'(x)")
plt.legend()
plt.xlabel("jours")
plt.ylabel("nombre de déces")
yseconde=diff(yprimee)
plt.subplot(3,1,3)
plt.plot(X[0:len(X)-2],yseconde,'o:',c = 'yellow',label="f'(x)")
plt.legend()
plt.xlabel("jours")
plt.ylabel("nombre de déces")
plt.show() 

