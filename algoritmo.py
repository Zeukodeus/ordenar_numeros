a = int (input("ingrese el primer número: "))
b = int (input("ingrse el segundo número: "))
c = int (input("ingrse el segundo número: "))

if a>b :
    if b>c :

        rta = "el orden ascendente de los números son: " + str (c)+", " + str (b)+", " + str (a)

    else :

        rta = "el orden ascendente de los números son: " + str (b)+", " + str (c)+", " + str (a)

else :

     if b<c :

         rta = "el orden ascendente de los números son: " + str (a)+", " + str (b)+", " + str (c)
 
     else :
        

        rta = "el orden ascendente de los números son: " + str (c)+", " + str (a)+", " + str (b)

if c>a :
            
    rta = "el orden ascendente de los números son: " + str (a)+", " + str (c)+", " + str (b)
else :

     rta = "el orden ascendente de los números son: " + str (b)+", " + str (c)+", " + str (a)

print (rta)