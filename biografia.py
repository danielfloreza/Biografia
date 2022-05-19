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
    
    year_r=year()
    month_r=month()
    day_r=day()
    
    complet_date=[day_r,month_r,year_r]
    
    #email_r=email()
    
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