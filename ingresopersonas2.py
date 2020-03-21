import sys
import cv2
import sqlite3
import numpy as np

face_cascade = cv2.CascadeClassifier('archivos/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
ID=0
decision=True

def insertorupdate(ID,nombrepersona,carnet):
    conn=sqlite3.connect("Fasebase.db")
    cmd="SELECT * FROM personas WHERE id="+str(ID)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE personas SET nombre='"+str(nombrepersona)+"', carnet='"+str(carnet)+"' WHERE id="+str(ID)
    else:
        cmd="INSERT INTO personas (id, nombre, carnet) VALUES ("+str(ID)+", '"+str(nombrepersona)+"', '"+str(carnet)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()


def capturar(nombrepersona):
    tope=0
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.imshow('camara',img)
        for (x,y,w,h) in faces:
            #captura=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),1)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
            region=gray[y:y+h,x:x+w]
            cv2.imshow("captura",region)
            #cv2.imwrite("E:/imagenesbase/"+nombrepersona+"."+str(ID)+"."+str(tope)+".jpg",region)
            cv2.imwrite("imagenes_2019/"+nombrepersona+"."+str(ID)+"."+str(tope)+".jpg",region)
        #if captura.any() == True:
            tope=tope+1
            print(tope)
            cv2.imshow('camara',img)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            sys.exit()
        if tope==20:
            break
            cap.release()
            cv2.destroyAllWindows()


def guardar():
    nombrepersona=raw_input("Ingrese su nombre: ")
    carnet=raw_input("Ingrese su carnet: ")
    insertorupdate(ID,nombrepersona,carnet)
    capturar(nombrepersona)
    cv2.destroyAllWindows()
    print("Seguir registrando: [1:Si]/[0:No] : ")
    mas=int(input())
    if mas==0:
        sys.exit()
    return mas

while decision:
    mas=guardar()
    if mas==0:
        break
    else:
        ID=ID+1
        mas=guardar()
