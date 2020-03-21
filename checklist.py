import cv2
import numpy as np
import sqlite3
import time



def getlista():
	#ahora = time.strftime("%c")
	conn=sqlite3.connect("Fasebase.db")
	cmd="select a.carnet, b.nombre, a.fecha, c.fecha from asistencia a left join personas b on a.id=b.id left join asistenciasalida c on a.id=c.id"
		


	cursor=conn.execute(cmd)
	archivo=open("archivos/Checklist.txt","w")
	for row in cursor:
		profile=row
		print(profile)
		archivo.write(str(profile))
		archivo.write('\n')
	archivo.close()
	conn.close()
	return profile



getlista()