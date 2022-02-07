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
        
        
