def silneheslo():
    heslo = input("napiste heslo,ktere ma alespon 6 znaku a ktere obsahuje mala a velka pismena a cisla, nebo napiste 'vygenerovat nove heslo' pro vygenerovani noveho hesla: ")
    '''if heslo == "vygenerovat heslo" '''
    pocet(heslo)
    maCisla
    if not maCisla(heslo):
        
        silneheslo()
    else: maMalaPismena
    if not maMalaPismena(heslo):
        silneheslo()
    else: maVelkaPismena
    if not maVelkaPismena(heslo):
        silneheslo()
    else: print("vase heslo je silne", heslo)
    
    
    
        
            


def pocet(heslo):
    if len(heslo) < 6:
        print ("heslo musi obsahovat alespon 6 znaku, napiste nove heslo")
        silneheslo()

def maCisla(heslo):
    for znak in heslo:
        if ord(znak) in range(48,58):
            return True
    print("heslo musi obsahovat alespon jednu cislici")
    return False

def maMalaPismena(heslo):
    for znak in heslo:
        if ord(znak) in range(97,122):
            return True
    print("heslo musi obsahovat i mala pismena")
    return False

def maVelkaPismena(heslo):
    for znak in heslo:
        if ord(znak) in range(65,90):
            return True
    print("heslo musi obsahovat i velka pismena")
    return False

def generator():
    import random
    znaky = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    delka = int(8)
    heslo =''
    for p in range(delka):
        heslo += random.choice(znaky)
    print("Tohle je tve nahodne vygenerovane heslo: ", heslo)







    



    
