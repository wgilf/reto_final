#Wilson David Gil-Karen Johana Farfan Castro
import random
import json
base=(" ","1","2","3","4","5","6","7","8","9")
tablero=[" ","1","2","3","4","5","6","7","8","9"]
primer_player="x"
segundo_player="O"
listado=[]
def table(tablero,primer_player,segundo_player,PRIMER_NAME,SEGUNDO_NAME,listado):
    ii=0
   
    for ii in range(9):
        EEE=0
        if(ii%2==0):
            ppr=PRIMER_NAME
        else:
            ppr=SEGUNDO_NAME

        print("Cual posicion es deseada "+ str(ppr))
        for i in range(3):
            for j in range(3):
                p=(j)+i*3
                p+=1
                print("["+str(tablero[p])+"]", end="")
            print()
        try:
            q=int(input("="))
            if(tablero[q]==str(q)):
                ()
            else:
                ll=0
                while ll==0:
                    print("posicion full escriba otro valor "+ str(ppr))
                    q=int(input("="))
                    if(tablero[q]==str(q)):
                        ll=1
                    
           
            if(ii%2==0):
                tablero[q]=primer_player
            else:
                tablero[q]=segundo_player
            EEE=comprobar(tablero,ii,ppr,listado)
            if(EEE==1):
                exit()
        
        except:
            if(EEE==1):
                exit()
            print("pierde el turno por no saber digitar un entero xd")
  #####      
        
    return print("NADIE GANA"), exit()


def comprobar(tablero,ii,ppr,listado):
    primer_player="x"
    segundo_player="O"
    tr=""
    r=0
    if(ii%2==0):
        tr=primer_player
    else:
        tr=segundo_player
    if(tablero[1]==tr and tablero[2]==tr and tablero[3]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[4]==tr and tablero[5]==tr and tablero[6]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[7]==tr and tablero[8]==tr and tablero[9]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[1]==tr and tablero[4]==tr and tablero[7]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[2]==tr and tablero[5]==tr and tablero[8]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[3]==tr and tablero[6]==tr and tablero[9]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[1]==tr and tablero[5]==tr and tablero[9]==tr):
        print("gano = "+str(ppr))
        r=1
    elif(tablero[3]==tr and tablero[5]==tr and tablero[7]==tr):
        print("gano = "+str(ppr))
        r=1
    if(r==1):
        #listado.append(ppr)
        with open(r'bus.json', 'r') as f:
            json_data = json.load(f)
        json_data=list(json_data)
        json_data.append(ppr)
        with open("bus.json", "w") as write_file:
            json.dump(json_data, write_file)
        
        #listado=(",")
        
        for i in range(3):
            for j in range(3):
                p=(j)+i*3
                p+=1
                print("["+str(tablero[p])+"]", end="")
            print()
        print("Si decea jugar de nuevo escriba 1 de lo contrario marque cualquier cosa")
        try:
            w=input("=")
            
            if(int(w)==1):
                print("in")
                tablero=list(base)
                listado=[]
                PRIMER_NAME_in=input(Fore.BLUE +"Nombre del primer jugador = " )
                SEGUNDO_NAME_in=input(Fore.RED +"Nombre del segundo jugador = ")
                llll=[]
                llll.append(PRIMER_NAME_in)
                llll.append(SEGUNDO_NAME_in)
                q=random.choice(llll)
                print("El que inicia= "+ str(q))
                print(Fore.MAGENTA + "NOTA:El ususario tiene que ingresar valores entre 1 y 9 ")
                if(q==(llll[0])):
                    PRIMER_NAME=PRIMER_NAME_in
                    SEGUNDO_NAME=SEGUNDO_NAME_in
                else:
                    PRIMER_NAME=SEGUNDO_NAME_in
                    SEGUNDO_NAME=PRIMER_NAME_in
                print(table(tablero,primer_player,segundo_player,PRIMER_NAME,SEGUNDO_NAME,listado))
            else:
                p("ee")
                return 1
                
        except:
            return 1


    return print("-----------------------------------------------------------------------------------------")








print(Fore.GREEN + "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(Fore.GREEN + "||||||                |||           ||||   |||||      |||||   |||                |||           |||||      ||||   ||||||||||||")
print(Fore.GREEN + "||||||||||||   ||||||||||   |||||   ||||   ||||  ||||  ||||   |||||||||   ||||||||||   |||||   ||||  ||||  |||   ||||||||||||")
print(Fore.GREEN + "||||||||||||   ||||||||||   ||||   |||||   |||  ||||||  |||   |||||||||   ||||||||||   ||||   ||||  ||||||  ||   ||||||||||||")
print(Fore.GREEN + "||||||||||||   ||||||||||        |||||||   |||  |||||   |||   |||||||||   ||||||||||        ||||||  ||||||  ||   ||||||||||||")
print(Fore.GREEN + "||||||||||||   ||||||||||   |||    |||||   |||   ||||    ||   |||||||||   ||||||||||   |||    |||||  ||||  |||   ||||||||||||")
print(Fore.GREEN + "||||||||||||   ||||||||||   |||||   ||||   |||||      ||  |   |||||||||   ||||||||||   |||||   |||||      ||||         ||||||")
print(Fore.GREEN + "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(Fore.GREEN + "                                                          WELCOME")
print()
qwe=True
while (qwe==True):
    ssdf=0
    print(Fore.MAGENTA + "Para jugar introdusca el numero 1 -Para ver la lista de ganadores introdusca el numero 2")
    try:
        ppl=int(input("="))
        if(ppl==1):
            qwe=False
        elif(ppl==2):
            with open(r'bus.json', 'r') as f:
                json_data = json.load(f)
            for hh in range(len(json_data)):
                print(json_data[hh])

            
            ssdf=1
            exit()
        else:
            print(Fore.RED + "NUMERO INVALIDADO")
    except:
        if(ssdf==1):
            print(Fore.RED + "Fin")
        else:
            print("no se admiten letras")
    if(ssdf==1):
        exit()
        
PRIMER_NAME_in=input(Fore.BLUE +"Nombre del primer jugador = " )
SEGUNDO_NAME_in=input(Fore.RED +"Nombre del segundo jugador = ")
llll=[]
llll.append(PRIMER_NAME_in)
llll.append(SEGUNDO_NAME_in)
q=random.choice(llll)
print("El que inicia= "+ str(q))
print(Fore.MAGENTA + "NOTA:El ususario tiene que ingresar valores entre 1 y 9 ")
if(q==(llll[0])):
    PRIMER_NAME=PRIMER_NAME_in
    SEGUNDO_NAME=SEGUNDO_NAME_in
else:
    PRIMER_NAME=SEGUNDO_NAME_in
    SEGUNDO_NAME=PRIMER_NAME_in  
print(table(tablero,primer_player,segundo_player,PRIMER_NAME,SEGUNDO_NAME,listado))
        
