# DeteccionDeRostros
Detección de rostros con Python y OpenCV (haarcascade_frontalface_default.xml) con lectura y escritura de datos en sql lite

PREPARACION:

Descargar e instalar Python 2.7 - https://www.python.org/downloads/release/python-2710/
	Verificar que python sea variable de entorno

Descargar OpenCV 2.4.13 - https://opencv.org/releases/page/4/
	Descomprimir y guardar en C:/
		Copiar la libreria "cv2.pyd" de OpenCV 
		[Ubicada en: C:\opencv 2.4.13\build\python\2.7\x64\cv2.pyd]
		en la carpeta "site-packages" del directorio de instalacion de python 2.7
		[C:\Python27\Lib\site-packages]

Descargar easy_install.exe - file:///C:/Python27/Scripts/
	Ubicar este archivo en la carpeta "Scripts" del directorio de instalacion de python 2.7
	[C:\Python27\Scripts]

Descargar e instalar SQLliteStudio 3.1.1 - https://sqlitestudio.pl/index.rvt?act=download

Elegir un directorio "Deteccion de rostros" para alojar los ejecutables, dentro de este crear la siguiente estructura de carpetas:

C:\..\Deteccion de rostros>dir
 El volumen de la unidad C es Windows10
 El número de serie del volumen es: A6D5-BE07

 Directorio de C:\..\Deteccion de rostros

21/03/2020  13:06    <DIR>          .
21/03/2020  13:06    <DIR>          ..
21/03/2020  13:06    <DIR>          archivos
21/03/2020  13:06    <DIR>          imagenes
               0 archivos              0 bytes
               4 dirs  12.369.747.968 bytes libres

A nivel de la carpeta "Deteccion de rostros" colocar los archivos ejecutables .py y el archivo de SQLite .db

Dentro de la carpeta "archivos" colocar los archivos:
haarcascade_frontalface_default.xml
Entrenamiento.yml

Dentro de la carpeta "imagenes" se guardaran las capturas de rostros que el sistema utiliza para el proceso de entrenamiento

FUNCIONALIDAD:

Este proyecto esta enfocado al reconocimiento de rostros y busca ser implementado
como apoyo para la toma de asistencia de grupos de personas dentro de
un salon de clases, reunion y demas.

EXPLICACION:

Para esto existen cinco modulos, que deben ejecutarse en un orden establecido:

Uno: El sistema debe registrar el rostro (fotografia), nombre e identificador por persona.
Dos: El sistema debe entrenarse para el posterior reconocimiento.
Tres: Identificar el ingreso de personas, lo que seria ya el funcionamiento o la toma de asistencia. En esta parte se registra en base de datos la hora en que se capturan los rostros.
Cuatro: Identificar la salida de personas, lo que seria el funcionamiento o la validacion de las personas que estan presentes al termino de una sesion presencial.
Quinto: Generar un listado de pesonas con su respectivo horario entrada y salida, bajo el supuesto que si una persona unicamente tiene hora de ingreso esta no permanecio hasta el termino de la sesion y viceversa.

EJECUCION:

Ejecutar desde consola CMD, Power Shell o Terminal, ubicarse en el directorio donde estan los ejecutables y seguir el orden descrito anterioremente.

Windows: >python [nombre del archivo].py

1ero : ingresopersonas2.py\n
2do: entrenamiento.py\n
3ero: identificaringreso.py
4to: identificarsalida.py
5to: checklist.py
