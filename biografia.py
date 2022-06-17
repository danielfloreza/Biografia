def show(complet_information):
    print("Has quedado registrado. Esta es tu informaciom:\n")
    print("\nNombre completo: "+str(" ".join(complet_information[0])))
    print("-------------------------------")
    print("Tu fecha de nacimiento: Dia: "+str((complet_information[1])[0])+ " Mes: "+ str((complet_information[1])[1])+ " Anio: "+str((complet_information[1])[2]))
    print("-------------------------------")
    print("Tu correo: "+str(complet_information[2]))
    print("-------------------------------")
    print("Tu meta: "+str(complet_information[3]))
    print("-------------------------------\n")
    run()

def goal():
    goal_r=input("Escribe tus metas más grandes:\n")
    goal_r=goal_r.strip()
    print("Si así quieres almacenar tu meta la he guardado.\n")
    return goal_r


def check_email(email_r):
    email_final=email_r
    if ((not email_r[0].isdigit()) and (not email_r[0].isalpha())) or ((not email_r[len(email_r)-1].isalpha()) and (not email_r[len(email_r)-1].isdigit())):
        email_r=False
        email_final=False
        
    if email_r != False:
        for i in range(0,len(email_r)):
            if (str(email_r[i])==".") or (email_r[i]=="-") or (email_r[i]=="_") or (email_r[i]=="_@"):
                if email_r[i+1]== "." or email_r[i+1]== "-" or email_r[i+1]== "_" or email_r[i+1]== "@":
                    email_final=False
    return email_final


def play_email():
    email_r=input("Correo: ")
    email_r=email_r.strip()
    email_r=email_r.replace(" ","")
    counter_arroba=0
    counter_punto=0
    for character in email_r:
        if (not character.isalpha()) and (not character.isdigit()):
            if character != "." and character != "_" and character != "-":
                if character =="@":
                    counter_arroba+=1
                else:
                    print("""\nError!!
Solo se admiten letras(A-z), numeros,puntos,guiones y @\n""")
                    play_email()
            else:
                if character ==".":
                    counter_punto+=1
    if counter_arroba!=1:
        print("Debes escribir al menos y no más de una @\n")
        play_email()
    elif counter_punto==0:
        print("Debes escribir al menos un punto(.)\n")
        play_email()
        
    else:
        email_r=check_email(email_r)
    
    if email_r is not False:
        return email_r
    else:
        print("Tu correo solo puede terminar con un numero o una letra y no pueden estar dos puntos o guiones seguidos o seguido o antecedido por una @.\n")
        play_email()
        
        
def email():
    email_r=play_email()
    return email_r


def check_number(received,number_cycles):
    received_r=False
    for i in number_cycles:
        if i==int(received):
            received_r=received
    return received_r


def play_number(received,number_cycles):
    try:
        number=int(input(received+": "))
        status=check_number(number,number_cycles)
        if status is False:
            print(""""               ¡¡Error!!
Escoge un """+str(received)+" que este en entre "+str((list(number_cycles))[0])+" y "+str((list(number_cycles))[len(number_cycles)-1]))
            play_number(received,number_cycles)
        else:
            return status
    except ValueError:
        print("\nEscribe un numero. sin espacios ni guiones, ni letras.\n")
        play_number(received,number_cycles)


def check(verified):
    verified= verified.strip()
    if verified.isalpha():
        verified=verified.lower()
        verified=verified.capitalize()
        if len(verified)>1:
            return(verified)
        else:
            return False
    else:
        return(False)


def play(received):
    name= input(str(received)+": ")
    
    status=check(str(name))
    if status is False:
        print("Escribe un "+str(received)+""" correcto. Debe ser de al menos 2 letras y No debe incluir:
              
              -Numeros
              -caracteres especiales
              -mas de un nombre
              
              """)
        play(received)
    else:
        return(status)


def start():
    name_r=play("Nombre")
    name2_r=play("Segundo Nombre")
    last_name_r=play("Apellido")
    last_name2_r=play("Segundo Apellido")
            
    complet_name=[name_r, name2_r,last_name_r,last_name2_r]
    
    print("\nHas completado tu nombre. Vamos a registrar tu fecha nacimiento.\n")
    year_r=play_number("Anio de nacimiento",range(1900,2023))
    month_r=play_number("Mes de nacimiento",range(1,13))
    day_r=play_number("Día de nacimiento",range(1,31))
    
    complet_date=[day_r,month_r,year_r]
    
    email_r=email()
 
    goal_r=goal()
    
    complet_information=[complet_name,complet_date,email_r,goal_r]
    
    show(complet_information)
    
def run():
    try:
        answer=int(input("""Quieres continuar?
                 
1- Si
2- No
                 
"""))   
        if answer !=1 and answer!=2:
            print("Escoge una de las opción válida")
            run()
        else:
            if answer ==1:
                print("\n")
                start()
            else:
                print("Hasta la proxima!!\n")
    except ValueError:
        print("Debes escribir un número.\n")
        run()


if __name__ == '__main__':
    run()
