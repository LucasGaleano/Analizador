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

         analizador.analizar_palabra(archivoAnalizador, palabra)
         letraAnterior = ""
         for letra in palabra:   
            combinacion = letraAnterior + letra
            if(len(combinacion)==2 and letra.isalpha() and letraAnterior.isalpha() ):
                  analizador.agregar_combinacion(combinacion,archivoAnalizador)
            letraAnterior = letra
      print(str(lineasAnalizadas) + " lineas.")
      linea = texto.readline()


archivoAnalizador.close()

print("termino")