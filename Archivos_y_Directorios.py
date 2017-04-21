#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Archivos_y_Directorios.py por:
#   Flavio Danesse <fdanesse@gmail.com>
#   Ceibal Jam - Uruguay - Plan Ceibal

import os
import urllib
import string

class Archivos_y_Directorios():

	def __init__(self):
		pass
		# Directorio para crear la base de datos
		
	def Crear_Directorio(self, directorio):
	# crea los directorios y archivos necesarios

		# Si el directorio no existe, crearlo
		if not os.path.exists(directorio):
			os.mkdir(directorio)
			print "Directorio Creado Correctamente"
			os.chmod(directorio, 0666)
		else:
			print "No se crea el Directorio porque ya existía"
