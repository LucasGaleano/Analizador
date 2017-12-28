import analizador
import sys




archivoAnalizador = open(sys.argv[2],'r+')
with open(sys.argv[1],'r') as texto:
   lineasAnalizadas = 0
   linea = texto.readline()
   while linea:
      lineasAnalizadas += 1
      palabras = linea.split(" ")
      for palabra in palabras:
         analizador.analizar_palabra(archivoAnalizador, palabra, int(sys.argv[3]))

      print(str(lineasAnalizadas) + " lineas.")
      linea = texto.readline()

archivoAnalizador.close()

print("termino")