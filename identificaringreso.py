import cv2
import numpy as np
import sqlite3
import time

face_cascade = cv2.CascadeClassifier('archivos/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load("archivos\\Entrenamiento.yml")
#path='E:/imagenesbase/'
path='imagenes_2019/'

#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,2)

def getprofile(ID):
	conn=sqlite3.connect("Fasebase.db")
	cmd="SELECT * FROM personas WHERE id="+str(ID)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close()
	return profile

def insertorupdate(ID,carnet):
    conn=sqlite3.connect("Fasebase.db")
    cmd="SELECT * FROM asistencia WHERE id="+str(ID)
    ahora = time.strftime("%c")
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        #cmd="UPDATE asistencia SET carnet='"+str(carnet)+"' WHERE id="+str(ID)
        cmd="UPDATE asistencia SET carnet='"+str(carnet)+"', fecha='"+str(ahora)+"' WHERE id="+str(ID)
    else:
        #cmd="INSERT INTO asistencia (id, carnet) VALUES ("+str(ID)+", '"+str(carnet)+"')"
        cmd="INSERT INTO asistencia (id, carnet, fecha) VALUES ("+str(ID)+", '"+str(carnet)+"', '"+str(ahora)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

while 1:
	ret, img=cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		ID,conf=rec.predict(gray[y:y+h,x:x+w])
		profile=getprofile(ID)
		if (profile != None):
			insertorupdate(profile[0],str(profile[2]))
			cv2.cv.PutText(cv2.cv.fromarray(img),"NOMBRE: "+str(profile[1]),(x,y+h+30),font,(0,255,255))
			cv2.cv.PutText(cv2.cv.fromarray(img),"CARNET: "+str(profile[2]),(x,y+h+60),font,(0,255,255))
	cv2.imshow("EN VIVO",img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break;
cap.release()
cv2.destroyAllWindows()

