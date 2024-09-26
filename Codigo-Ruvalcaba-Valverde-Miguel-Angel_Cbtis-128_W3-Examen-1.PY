#primero hise hare unas variables, de lista y una sola
na = ("Miguel","Angel","Ruvalcaba","Valverde")
extra0 = ("Nombre:")
extra1 = ("3","W","Grupo:")
extra2 = ("23308051281212","Numero de control:")
#al prinsipio no entendi pero por si acaso dejare lo de ariba
#primero hay que capturar el nombre con mayuscula preferentemente y usando input
print("--Escribe tu nombre en mayusculas--")
cn1 = input("Añadir mi apellido paterno:")#con estos input "Capturamos los numeros"
cn2 = input("Añadir mi apellido materno:")
cn3 = input("Nombre:")
#ahora que los apellidos ya estan en la mesa ahora hay que ver el resultado
print("---------")
print(extra0,cn1,cn2,cn3)#aqui se ve el resultado, y se concatena las varaibles
print("---------")
#esto se pone qui por si acaso, pero qui se ve el numero de contro, grupo y nombre.
#aqui tanmbien se concatenar
print(extra0,na[3],na[2],na[1],na[0])
print(extra1[2],extra1[0],extra1[1])
print(extra2[1],extra2[0])
