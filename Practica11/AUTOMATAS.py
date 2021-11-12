import math

def normal_round(n, decimals=0):          #USE ESTA FUNCION PARA REDONDEAR CORRECTAMENTE LAS CANTIDADES
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals


alfabeto=[0.05,0.10,0.25]
menu = 1
m=0
while m == 0:
    print("---MAQUINA EXPENDEDORA---")
    if menu == 1:
        precio = 0.25
        print("TE ENCUENTRAS EN q0 ESTADO INICIAL")
        print("el costo del refresco es de $0.25 CENTAVOS")
        print("INGRESE SUS MONEDAS(ALFABETO) PARA COMENZAR SU PAGO:")
          
        tipoMoneda= 0
        pagocompleto =(precio - tipoMoneda)
        suma = 0
        while pagocompleto > 0:
            

            tipoMoneda= str(input("MONEDAS VALIDAS\n  N)◉0.05 \n  D)◉0.10\n  Q)◉0.25\n:"))

            if tipoMoneda == "N":
                tipoMoneda= 0.05
            elif tipoMoneda == "D":
                tipoMoneda= 0.10
            else:
                tipoMoneda= 0.25
            tipoMoneda= (tipoMoneda) 
            
            
    
            round(tipoMoneda, 2)
            print("HA INTROUDCIDO $", tipoMoneda,) 
            for nominacion in alfabeto:
                if tipoMoneda in alfabeto:
                    if tipoMoneda==nominacion:
                        pagocompleto = pagocompleto-tipoMoneda
                        float(pagocompleto)
                        pagocompleto = normal_round(pagocompleto,2)
                        while pagocompleto > 0:
                            suma= suma+tipoMoneda
                            suma = normal_round(suma,2)
                            
                            if suma == 0.05:
                                estado = "q1"
                            elif suma == 0.1:
                                estado =  "q2"
                            elif suma == 0.15:
                                estado = "q3"
                            elif suma == 0.2:
                                estado = "q4"
                            elif suma == 0.25:
                                estado = "q5"
                            elif suma == 0.3:
                                estado = "q6"
                            elif suma == 0.35:
                                estado = "q7"
                            elif suma == 0.4:
                                estado = "q8"
                            else:
                                estado = "q9"
                                
                            print ("TE ENCUENTRAS EN EL ESTADO: ", estado,)
                            print("""para llegar a un estado de aceptacion te falta por pagar""",pagocompleto)
                            print("INGRESE MAS MONEDAS PARA COMPLETAR EL PAGO DE: ",pagocompleto)
                             
                            break
                else:
                    print("billete o moneda no valida, ingrese una opcion valida")


    
        
        cambio = pagocompleto*-1
        cambio = normal_round(cambio ,2)
        if cambio == 0: 
            aceptacion= "q5"
        elif cambio == 0.5:
            aceptacion= "q6"
        elif cambio == 0.10:
            aceptacion = "q7"
        elif cambio == 0.15:
            aceptacion = "q8"
        
        float(cambio)
        round(cambio, 2)
        print("!!!!¡PAGO COMPLETO/ESTADO DE ACEPTACION", aceptacion, "!!!!\ntu cambio es $",cambio)
        if cambio !=0:
            print("RETIRA TU CAMBIO")
        for i in alfabeto:
            if cambio >=  i:
                queda =(cambio // i)
                print( queda ,'monedas de:', i)
                cambio = cambio % i
        m =int(input("PRESIONE ""SELECT = 0"" PARA VOLVER AL ESTADO INICIAL q0: "))
        
    


        
      
