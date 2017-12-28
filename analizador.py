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


def esta_en_archivo(combinacion, archivoAnalizador):
   #devuelve la posicion del archivo donde esta la combinacion y si no devuelve -1
   archivoAnalizador.seek(0)
   seekAnterior = 0
   linea = archivoAnalizador.readline()
   while linea != '':
      if(linea.split(" ")[0]==combinacion):
         return seekAnterior
      seekAnterior = archivoAnalizador.tell()
      linea = archivoAnalizador.readline()
   return -1

def sumar_transicion(seekUbicacion, archivoAnalizador):
   #devuelve la linea donde esta la transicion
   archivoAnalizador.seek(seekUbicacion)
   transicion = archivoAnalizador.readline()
   archivoAnalizador.seek(seekUbicacion)
   archivoAnalizador.write(transicion.split()[0] + " " + str(int(transicion.split()[1])+1).zfill(20) + "\n")

def agregar_combinacion(combinacion, archivoAnalizador):
   #busca si esta la transicion en la lista y le suma 1,
   #si no esta lo agrega
   
   #se fija si la transicion esta en el archivo
   seekUbicacion = esta_en_archivo(combinacion, archivoAnalizador)
   if (seekUbicacion != -1 ):   
      #esta la transicion, consige el valor y le suma 1
      sumar_transicion(seekUbicacion, archivoAnalizador)

   else:
      #no esta la transicion, va al final del archivo y lo agrega
      archivoAnalizador.seek(0, 2)
      archivoAnalizador.write(combinacion + " " + str(1).zfill(20) + "\n")


def dividir_en_transiciones(palabra, cantLetrasTransicion):
   listaTransiciones=[]
   indexPalabra = 0
   longPalabra = len(palabra)
   while longPalabra > indexPalabra:
      combinacion = ""
      for indexCombinacion in range(cantLetrasTransicion+1):
         try:
            combinacion += palabra[indexCombinacion + indexPalabra]           
         except:
            break
         if(len(combinacion) != 1):
            listaTransiciones.append(combinacion)
      indexPalabra += 1
   return listaTransiciones

def analizar_palabra(archivoAnalizador, palabra, cantLetrasTransicion):
   #creo una lista de transiciones
   listaTransiciones = dividir_en_transiciones(palabra,cantLetrasTransicion)
   #agrego cada transicion al archivo
   for transicion in listaTransiciones:
      if(transicion.isalpha()):
         agregar_combinacion(transicion,archivoAnalizador)




    
    


