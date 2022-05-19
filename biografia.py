def check_email(email_r):
    email_final=email_r
    print(email_r)
    if ((not email_r[0].isdigit()) and (not email_r[0].isalpha())) or ((not email_r[len(email_r)-1].isalpha()) and (not email_r[len(email_r)-1])):
        email_r=False
        
    if email_r != False:
        print(email_r)
        for i in range(0,len(email_r)):
            print(email_r)
            print(i)
            if (str(email_r[i])==".") or (email_r[i]=="-") or (email_r[i]=="_"):
                if email_r[i]==email_r[i+1]:
                    email_final=False
    return email_final


def play_email():
    email_r=input("Correo: ")
    email_r=email_r.strip()
    email_r=email_r.replace(" ","")
    counter_arroba=0
    for character in email_r:
        #print(type(character))
        if (not character.isalpha()) and (not character.isdigit()):
            if character != "." and character != "_" and character != "-":
                if character =="@":
                    counter_arroba+=1
                else:
                    print("""\nError!!
Solo se admiten letras(A-z), numeros,puntos,guiones y @\n""")
                    play_email()
    if counter_arroba!=1:
        print("Debes escribir al menos y no más de una @\n")
        play_email()
    else:
        email_r=check_email(email_r)
    
    if email_r is not False:
        return email_r
    else:
        print("Tu correo solo puede terminar con un numero o una letra y no pueden estar dos puntos o guiones seguidos.\n")
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
    number=input(str(received)+": ")
    number=number.strip()
    if number.isdigit():
        status=check_number(number,number_cycles)
        if status is False:
            print(""""               ¡¡Error!!
Escoge un """+str(received)+" que este en entre "+str((list(number_cycles))[0])+" y "+str((list(number_cycles))[len(number_cycles)-1]))
            play_number(received,number_cycles)
        else:
            return status
    else:
        print("\nEscribe un numero. sin espacios ni guiones, ni letras.\n")
        play_number(received,number_cycles)


def day():
    day_r=play_number("Dia de nacimiento",range(1,32))
    return day_r


def month():
    month_r=play_number("Mes de nacimiento",range(1,13))
    return month_r


def year():
    year_r=play_number("Anio de nacimiento",range(1900,2023))
    return year_r


def check(verified):
    verified= verified.strip()
    if verified.isalpha():
        verified=verified.lower()
        verified=verified.capitalize()
        return(verified)
    else:
        return(False)


def play(received):
    name= input(str(received)+": ")
    
    status=check(str(name))
    if status is False:
        print("Escribe un "+str(received)+""" correcto. No debe incluir:
              
              -Numeros
              -caracteres especiales
              -mas de un nombre
              
              """)
        play(received)
    else:
        return(status)


def last_name2():
    last_name2_r=play("Segundo apellido")
    return last_name2_r


def last_name():
    last_name_r=play("Apellido")
    return last_name_r


def name2():
    name2_r=play("Segundo Nombre")
    return name2_r


def name():
    name_r=play("Nombre")
    return name_r
    
    
    
def start():
    name_r=name()
    name2_r=name2()
    last_name_r=last_name()
    last_name2_r=last_name2()
            
    complet_name=[name_r, name2_r,last_name_r,last_name2_r]
    
    print("\nHas completado tu nombre. Vamos a registrar tu fecha nacimiento.\n")
    year_r=year()
    month_r=month()
    day_r=day()
    
    complet_date=[day_r,month_r,year_r]
    
    email_r=email()
    print(email_r)
    
    #goal_r=goal()
    
    #complet_information=[complet_name,complet_date,email_r,goal_r]
    
    #show(complet_information)
    
def run():
    answer=input("""Quieres empezar a registrar tus datos?
                 
1- Si
2- No
                 
""")
    answer=answer.strip()
    if answer != str(1) and answer != str(2):
        print("\nEscribe una opcion valida.\n")
        run()
    else:
        if answer == str(1):
            print("\n")
            start()
        else:
            print("Hasta la proxima!!\n")


if __name__ == '__main__':
    print("Bienvenido al registro de tu biografia.\n")
    run()