import analizador
import sys



archivoTexto = open(sys.argv[1],'r')
archivoAnalizador = open(sys.argv[2],'r+')
cantDeTransiciones = int(sys.argv[3])

analizador.analizar_archivo_de_texto(archivoAnalizador, archivoTexto, cantDeTransiciones)



archivoAnalizador.close()

print("termino")