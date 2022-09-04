import cv2

imagen=cv2.imread('op.jpg',cv2.IMREAD_COLOR)
##Cambia el pixel seleccionado de color
imagen[10,10]=[255,255,255]
pixel=imagen[10,10]
print(pixel)
##Cambia un rango de pixeles de color
imagen[30:150,200:300]=[0,0,0]
print(imagen.shape)
print(imagen.size)
print(imagen.dtype)
##Trasladar un grupo de pixeles a otra parte de la imagen
luffy_face=imagen[350:450,600:700]
imagen[350:450,350:450]=luffy_face

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()