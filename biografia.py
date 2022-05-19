def show(name_r,name2_r,last_name_r,last_name2_r):
    print("Has completado tus nombre.\n")
    print(str(name_r)+" "+str(name2_r)+" "+str(last_name_r)+" "+str(last_name2_r))
    


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
    answer=input("""Quieres empezar a registrar tus datos?
                 
1- Si
2- No
                 
""")
    answer=answer.strip()
    if answer != str(1) and answer != str(2):
        print("\nEscribe una opcion valida.\n")
        start()
    else:
        if answer == str(1):
            print("\n")
            name_r=name()
            name2_r=name2()
            last_name_r=last_name()
            last_name2_r=last_name2()
            
            show(name_r, name2_r,last_name_r,last_name2_r)
        
        else:
            print("Hasta la proxima!!\n")

def run():
    print("Bienvenido al registro de tu biografia.\n")
    start()


if __name__ == '__main__':
    run()