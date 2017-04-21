#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Navegador.py por:
#   Flavio Danesse <fdanesse@gmail.com>
#   Ceibal Jam - Uruguay - Plan Ceibal

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk
import pygtk
pygtk.require("2.0")

import sys

import os
import hulahop
from sugar import env
hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))
from hulahop.webview import WebView

class Navegador():
	''' Es un Navegador web from hulahop.webview import WebView '''
	def __init__(self, DIRECTORIO_DATOS):
		self.directorio = DIRECTORIO_DATOS
		self.uri = None
		self.navegador = WebView()
	
	def get_Navegador(self):
	# Establece la dirección por defecto, y devuelve el navegador para ser incrustado en un contenedor gtk
		self.uri = self.directorio+"web.htm"
		self.navegador.load_uri(self.uri)
		return self.navegador
	
	def set_web_por_defecto(self, archivo):
	# crea una web para el archivo swf
		htm = """
		<html>
		<head>
		<title>Embedded SWF Player</title>
		</head>
		<body onLoad="resizeTo(1000, 800);">
		<embed src = %s width="822" height="554"
		   hidden=false autostart=true loop=1>
		</body>
		</html>
		""" % archivo

		# Abrir la web creada
		web = open(self.directorio+"web.htm", "w")
		web.write(htm)
		web.close()

		try:
		# solo sucede la 1º vez que ejecutas la actividad ya que solo el propietario puede modificar los permisos
			os.chmod(self.directorio+"web.htm", 0666)
		except:
			pass
