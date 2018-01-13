#ANALIZADOR

#ANALIZAR TEXTOS

#abrir texto
#abrir archivo de analizador
#leer palabras una por una
#leer letras una por una
#guardar la relacion con la cantidad de veces que aparece
#y si no existe crearla
#cerrar archivo

import sys
import time

cantDeCeros=10
g_diccionarioTransiciones={} #diccionario

def sumar_transicion(seekUbicacion, archivoAnalizador):
   #devuelve la linea donde esta la transicion
   archivoAnalizador.seek(seekUbicacion)
   transicion = archivoAnalizador.readline()
   archivoAnalizador.seek(seekUbicacion)
   archivoAnalizador.write(transicion.split()[0] + " " + str(int(transicion.split()[1])+1).zfill(20) + "\n")

def agregar_combinacion(combinacionBuscar):
   #busca si esta la transicion en la lista y le suma 1,
   #si no esta lo agrega


   #se fija si la transicion esta en el archivo(diccionario)
   if (g_diccionarioTransiciones.has_key(combinacionBuscar)):   
      #si esta la transicion, consige el valor y le suma 1
      g_diccionarioTransiciones[combinacionBuscar] += 1
   else:
      #si no esta la transicion, lo agrega
      g_diccionarioTransiciones[combinacionBuscar] = 1

def dividir_linea_en_transiciones(linea, cantLetrasTransicion):
   listaTransiciones=[]
   indexlinea = 0
   lengthLinea = len(linea)
   while indexlinea<lengthLinea:     
      combinacion = ""
      for indexCombinacion in range(cantLetrasTransicion+1):
         try:
            combinacion += linea[indexCombinacion + indexlinea]           
         except:
            break
         if(len(combinacion) != 1):
            listaTransiciones.append(combinacion)
      indexlinea += 1
   return listaTransiciones

def analizar_archivo_de_texto(archivoAnalizador,archivoTexto, cantLetrasTransicion):
   g_diccionarioTransiciones = crear_diccionario_del_archivo_analizador(archivoAnalizador)
   linea = archivoTexto.readline()
   lineasAnalizadas = 0
   while linea:
      lineasAnalizadas += 1
      analizar_linea(linea, cantLetrasTransicion)
      print(str(lineasAnalizadas) + " lineas analizadas.")
      linea = archivoTexto.readline()
   escribirEnArchivo(archivoAnalizador);


def analizar_linea(linea, cantLetrasTransicion):
   listaTransiciones = dividir_linea_en_transiciones(linea,cantLetrasTransicion)
   for transicion in listaTransiciones:
      if(transicion.isalpha()):
         agregar_combinacion(transicion)
         


def crear_diccionario_del_archivo_analizador(archivoAnalizador):
   linea = archivoAnalizador.readline() 
   while linea != "":
      transicion = linea.split(" ")
      g_diccionarioTransiciones[transicion[0]] = int(transicion[1])
      linea = archivoAnalizador.readline()


def escribirEnArchivo(archivoAnalizador):
   archivoAnalizador.seek(0)
   for item in g_diccionarioTransiciones.items():
      archivoAnalizador.write(str(item[0]) + " " +  str(item[1]) + "\n")
    
    


