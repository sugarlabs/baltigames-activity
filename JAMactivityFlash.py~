#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   JAMactivityFlash.py por:
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

from sugar.activity import activity

import gtk
import pygtk
pygtk.require("2.0")

import os
import time
import string
import sys

from Archivos_y_Directorios import Archivos_y_Directorios

#ICONOS = os.getcwd() + "/Iconos/"

COLOR1 = gtk.gdk.Color(0,0,0,1)

DIRECTORIO_DATOS = os.path.join(activity.get_activity_root(), 'data/')
DIRECTORIO_JUEGOS = os.getcwd()+"/Juegos/"
JUEGOS = os.listdir(DIRECTORIO_JUEGOS)

class JAMactivityFlash(activity.Activity):

	def __init__(self, handle):

		activity.Activity.__init__(self, handle, False)

		self.manejo_de_archivos = Archivos_y_Directorios()
		self.manejo_de_archivos.Crear_Directorio(DIRECTORIO_DATOS)
		#self.manejo_de_archivos.Crear_Directorio(DIRECTORIO_JUEGOS)

		# Toolbar
		barra_de_herramientas = Mibarra()
		barra_de_herramientas.set_Mibarra(JUEGOS, self.abrir_juego)

		barra_de_herramientas.show()
		self.set_toolbox(barra_de_herramientas)

		# Canvas
		self.caja = gtk.HBox()
		self.set_canvas(self.caja)

		archivo = DIRECTORIO_JUEGOS + "Ajedrez.swf"
		from swf_player_xo import Navegador
		self.navegador = Navegador(DIRECTORIO_DATOS)	
		self.navegador.set_web_por_defecto(archivo)

		self.caja.pack_start(self.navegador.get_Navegador(),True,True,0)

        	self.connect("destroy", self.destroy)

		self.show_all()

	def destroy(self, widget=None):
	# Cuando cierran la actividad desde el panel.
		sys.exit(0)

	def abrir_juego(self, widget, direccion_de_ejecucion):
	# Abre un archivo swf
		print "*** Abrir Juego ***", direccion_de_ejecucion
		self.navegador.navegador.load_uri(direccion_de_ejecucion)

class Mibarra(gtk.Toolbar):
# Barra de Herramientas gtk # http://library.gnome.org/devel/pygtk/stable/class-gtktoolbar.html
	
	def __init__(self):

		gtk.Toolbar.__init__(self)
		self.show_all()

	def set_Mibarra(self, juegos, callback):
	# agrega los juegos a la barra de herramientas.
	# tambien se puede: self.append_item(text, tooltip_text, tooltip_private_text, icon, callback, user_data=None)

		for juego in juegos:
			nombre_del_juego = juego.split(".")[0]
			direccion_de_ejecucion = DIRECTORIO_JUEGOS + juego
			#callback = None

			item = gtk.ToolItem()
			boton = gtk.Button(juego.split(".")[0])
			boton.modify_bg(gtk.STATE_NORMAL, COLOR1)
			item.add(boton)
			boton.show()
			item.show()
			boton.connect("clicked", callback, direccion_de_ejecucion)
			self.insert(item,-1)

		# salir
		item = gtk.ToolItem()
		salir = gtk.Button("Salir")
		salir.modify_bg(gtk.STATE_NORMAL, COLOR1)
		item.add(salir)
		salir.show()
		item.show()
		salir.connect("clicked", self.destroy)

		self.insert(item,-1)

	def destroy(self, widget=None):
	# Cuando cierran la actividad desde el panel.
		sys.exit(0)
