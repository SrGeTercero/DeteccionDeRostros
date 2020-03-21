import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHFaceRecognizer()
#path='E:/imagenesbase/'
path='imagenes_2019/'

def getimagenesconid(path):
	imagenpaths=[os.path.join(path,f) for f in os.listdir(path)]
	#print imagenpath
	caras=[]
	ids=[]
	for imagenpath in imagenpaths:
		caraImg=Image.open(imagenpath).convert('L')
		caraNp=np.array(caraImg,'uint8')
		ID=int(os.path.split(imagenpath)[-1].split('.')[1])
		caras.append(caraNp)
		print(ID)
		ids.append(ID)
		cv2.imshow("Entrenamiento",caraNp)
		cv2.waitKey(10)
	return ids, caras

ids,caras=getimagenesconid(path)
recognizer.train(caras,np.array(ids))
recognizer.save('archivos/Entrenamiento.yml')
cv2.destroyAllWindows()



#getimagenesconid(path)