def Sucesiones():

    decision=input("¿Quieres trabajar con progresiones aritméticas o greométricas? (PA) / (PG): ")

    #PROGRESIONES ARITMÉTICAS
    def PA():

        pregunta=input("Quieres usar el término general (T)\no la suma de términos(S): ")


        #---TERMINO GENERAL----------------------------------------------------------------------------------------
        def terminoGeneral():

            esquecido=input("¿Qué término te falta? (ax, an, a1, n, d): ")

            #Funciona correctamente
            if esquecido=="ax":

                a1=float(input("a1= "))
                n=float(input("n= "))
                d=float(input("d= "))

                an=a1+(n-1)*d
                print("El valor del término que ocupa el lugar ", n, " vale ", an)
  
            #Funciona correctamente
            if esquecido=="an":

                a1=float(input("a1= "))
                d=float(input("d= "))

    
    
                print("El término general de esta progresion aritmética vale ", a1, "+", "(n-1)", "*", d)

            #Funciona correctamente
            if esquecido=="n":

                #an=a1+(n-1)d //// an=a1+dn-d //// dn=a1-d-an //// n=(a1-d-an)/d

                ax=float(input("ax="))
                a1=float(input("a1= "))
                d=float(input("d= "))

                n=(-a1+d+ax)/d

                print("El término con el valor ", ax, " está en la posición ", n)

            #Funciona correctamente
            if esquecido=="a1":

                #an=a1+(n-1)*d //// -a1=-an+(n-1)*d //// -a1=-an+dn-d //// a1=an-dn+d

                an=float(input("an="))
                n=float(input("n="))
                d=float(input("d= "))

                a1=an-d*n+d
                print("El primer término de esta progresión vale ", a1)

            #Funciona correctamente
            if esquecido=="d":

                #d=(an-a1)/(n-1)

                ax=float(input("ax="))
                n=int(input("¿En qué posición está " + str(ax) + "?"))
                a1=float(input("a1="))

                d=(ax-a1)/(n-1)

                print("La diferencia entre los términos de esta sucesión es ", d)
    
        #---SUMA DE TÉRMINOS EN UNA PA
        def sumaTerminos():

            a1=float(input("a1= "))
            an=float(input("Introduce un término de la sucesión: "))
            n=float(input("¿Qué lugar de la sucesión ocupa el término ? "))

            Sn=((a1+an)/2)*n

            print("La suma de todos los términos de la sucesión hasta la posición número ", n, " es ", Sn)
        

        #---RESULTADO DE LA PREGUNTA--------------------------------------------------------------------------------
        if pregunta=="T":
            terminoGeneral()

        if pregunta=="S":
            sumaTerminos()

    #PROGRESIONES GEOMÉTRICAS
    def PG():

        pregunta=input("Quieres usar el término general (T)\no la suma de términos(S): ")

        #---TERMINO GENERAL----------------------------------------------------------------------------------------
        def terminoGeneral():

            esquecido=input("¿Qué quieres saber? (a1), (an): ")

            #Funciona correctamente
            if esquecido=="an":
            
                a1=float(input("a1="))
                r=float(input("r="))
                n=int(input("n="))

                an=a1*r**(n-1)

                print("El término de la posición número ", str(n)," es", str(an), "\nEl término general de la función es: an=", str(a1), "*", str(r), "**n-1" )

            #Funciona correctamente
            if esquecido=="a1":

                an=float(input("Introduce un término de está progresión geométrica: "))
                n=int(input("¿Qué posición ocupa este término?: "))
                r=float(input("r="))

                

                a1=an/r**(n-1)

                print("El primer término de esta sucesión geométrica vale ", a1)


        #---SUMA DE TÉRMINOS----------------------------------------------------------------------------------------

        def sumaTerminos():

            an=float(input("Introduce un término de la progresión: "))
            r=float(input("r="))
            a1=float(input("Introduce el primer término de la progresión: "))

            sn=(an*r-a1)/(r-1)

            print("La suma de los términos hasta el valor", str(an), "es ", sn)

        
        #---RESULTADO DE LA PREGUNTA--------------------------------------------------------------------------------

        if pregunta=="T":
            terminoGeneral()

        if pregunta=="S":
            sumaTerminos()

    
    if decision=="PA":
        PA()

    if decision=="PG":
        PG()


Sucesiones()