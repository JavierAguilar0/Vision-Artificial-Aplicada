import numpy as np
import cv2
from matplotlib import pyplot as plt

imagen=cv2.imread('db.jpg')
mascara=np.zeros(imagen.shape[:2],np.uint8)

Modelo_fondo=np.zeros((1,65),np.float64)
Modelo_frontal=np.zeros((1,65),np.float64)

rectangulo=(100,100,300,300)
cv2.grabCut(imagen,mascara,rectangulo,Modelo_fondo,Modelo_frontal,5,cv2.GC_INIT_WITH_RECT)
mascara2=np.where((mascara==2)|(mascara==0),0,1).astype('uint8')
imagen=imagen*mascara2[:,:,np.newaxis]

plt.imshow(imagen)
plt.colorbar()
plt.show()