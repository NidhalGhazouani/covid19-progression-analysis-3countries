#le 02-04-2021---->1-05-2021
from scipy.signal import *
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
Y = [703,710,709,767,778,783,789,794,801,812,818,823,831,837,841,845,850,852,855,861,872,884,912,953,991,1003,1011,1003,1021,1032]
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
z= [43,39,40,47,43,37,33,39,43,40,42,39,44,41,42,41,44,40,42,46,48,45,39,51,58,61,51,59,61,63]
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