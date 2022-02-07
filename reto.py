#Wilson David Gil-Karen Johana Farfan Castro
import random
import json
base=(" ","1","2","3","4","5","6","7","8","9")
tablero=[" ","1","2","3","4","5","6","7","8","9"]
primer_player="x"
segundo_player="O"
listado=[]










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
        
