
#Randomizer

import random

#characters
character_list = [
    
    'Vander', 'Clanne', 'Framme', 'Alfred', 'Etie', 'Boucheron', 'Céline', 'Louis', 'Chloé',
    'Jean', 'Yunaka', 'Anna', 'Alcryst', 'Lapis', 'Citrinne', 'Diamant', 'Amber', 'Jade', 'Ivy',
    'Kagetsu', 'Zelkov', 'Fogado', 'Bunet', 'Pandreo', 'Timerra', 'Panette', 'Merrin', 'Hortencia', 'Sedall',
    'Rosado', 'Goldmary', 'Lindon', 'Saphir', 'Veyle', 'Mauvier'
    
]

dlc_characters = [

    'Nel', 'Nil', 'Zelestia', 'Gregory', 'Madeline'

]

#emblems
emblem1 = [
    
    'Marth', 'Sigurd','Celica','Micaiah',
    'Roy', 'Leif'
    
]
emblem2 = [
    
    'Lyn', 'Lucina', 'Ike', 'Byleth', 'Corrin', 'Erika',
    'Leif', 'Sigurd', 'Roy', 'Micaiah', 'Celica', 'Marth'
    
]

emblem_maxdlc = [
    
    'Edelgard', 'Tiki', 'Camilla', 'Sorren', 'Hector', 'Veronica', 'Chrom'
    
]

def alear(x,y,z,emblem_list1,emblem_list2,e1,e2,dlc_list):
    amount_dlc = len(dlc_list)
    reverse_dlc = amount_dlc*(-1)
    if z < 11:
        no_pop = True
        maybe = random.randrange(e1)
        if maybe == 1 or y <= x:
            alear_emblem = random.randint(reverse_dlc,y-1)
            alear_nemblem = alear_emblem
            alear_emblem = emblem_list1[alear_emblem]
            if alear_emblem in emblem_maxdlc:
                no_pop = True
            else:
                no_pop = False
            emblem_list1.pop(alear_nemblem)
        else:
            alear_emblem = False
        
    if z >= 11:
        maybe = random.randrange(e2)
        if maybe == 1 or y <= x:
            alear_emblem = random.randint(reverse_dlc,y-1)
            alear_nemblem = alear_emblem
            alear_emblem = emblem_list2[alear_emblem]
            if alear_emblem in emblem_maxdlc:
                no_pop = True
            else:
                no_pop = False
            emblem_list2.pop(alear_nemblem)
        else:
            alear_emblem = False
    return alear_emblem, no_pop

def dlc_emblems():
    x = input('Do you have any DLC emblems? ')
    x = x.lower()
    while x != 'yes' and x != 'no':
        x = input('Do you have any DLC emblems? ')
    if x == 'yes':
        y = 8
        while y > 7 and y != 'all':
            y = input('How many? ')
            y = y.lower()
            if y == 'all':
                y = 7
            else:
                y = int(y)
        add_rings = y
        if y < 7 or y == 'all':
            z = input('Which? ')
            emblem_dlc = z.split()
            while len(emblem_dlc) != y:
                z = input(f'Requires {y} names, which? ')
                emblem_dlc = z.split()
            emblem_list1 = emblem1 + emblem_dlc
            emblem_list2 = emblem2 + emblem_dlc
            dlc_list = emblem_dlc
        else:
            emblem_list1 = emblem1 + emblem_maxdlc
            emblem_list2 = emblem2 + emblem_maxdlc
            dlc_list = emblem_maxdlc
    else:
        emblem_list1 = emblem1
        emblem_list2 = emblem2
        dlc_list = []
        add_rings = 0
    return emblem_list1, emblem_list2, add_rings,dlc_list

def deaths(character_list):
    number_dead = 0
    deaths = input('Do you have any deaths? ')
    while deaths != 'yes' and deaths != 'no':
        deaths = input('Do you have any deaths? ')
    if deaths.lower() == 'no':
        return character_list, number_dead
    else:
        i = 0
        c = 0
        deaths = input('Who? ')
        deaths = deaths.split()
        while i < len(deaths):
            if deaths[i].capitalize() in character_list:
                character_list.remove(deaths[i].capitalize())
                number_dead += 1
            i += 1
    return character_list, number_dead

def dlc_char(dlc_characters,characters,character_list):
    x = input('Do you have the DLC characters? ')
    if x.lower() == 'no':
        return characters, character_list
    else:
        characters += 5
        character_list = dlc_characters + character_list
    return characters, character_list
        

#unlocked characters in every chapter
def chapter():
    chap = 0
    characters = 0
    
    while chap < 3 or chap > 26:
        chap = int(input('Chapter: '))
    if chap == 4:
        characters = 6
        emblems = 2
    elif chap == 5:
        characters = 9
        emblems = 3
    elif chap == 6:
        characters = 10
        emblems =  3
    elif chap == 7:
        characters = 12
        emblems = 4
    elif chap == 8:
        characters = 15
        emblems = 4
    elif chap == 9:
        characters = 15
        emblems = 6
    elif chap == 10:
        characters = 18
        emblems = 6
    elif chap == 11:
        characters = 18
        emblems = 0
    elif chap == 12:
        characters = 21
        emblems = 2
    elif chap == 13:
        characters = 24
        emblems = 2
    elif chap == 14:
        characters = 27
        emblems = 3
    elif chap == 15:
        characters = 28
        emblems = 4
    elif chap == 16:
        characters = 29
        emblems = 5
    elif chap == 17:
        characters = 31
        emblems = 6
    elif chap == 18:
        characters = 31
        emblems = 8
    elif chap == 19:
        characters = 32
        emblems = 7
    elif chap == 20:
        characters = 33
        emblems = 10
    elif chap == 21:
        characters = 33
        emblems = 11
    elif chap == 22:
        characters = 35
        emblems = 0
    elif chap == 23:
        characters = 35
        emblems = 12
    elif chap == 24:
        characters = 35
        emblems = 11
    elif chap == 25:
        characters = 35
        emblems = 12
    elif chap == 26:
        characters = 35
        emblems = 12
    return characters, emblems, chap

#thinning list to number of characters avaliable in the chapter
def char_in_chap(character_list):
    x,y,z = chapter()
    x,character_list = dlc_char(dlc_characters,x,character_list)
    if x == 40:
        add = 5
    else:
        add = 0
    amount_emblems = y
    w = 1 #When alear doesn't have an emblem
    w2 = 0 #for when alear_emblem is not DLC, the list range to match is one less
        
    if z > 6:
        emblem_list1, emblem_list2, add_rings, dlc_list = dlc_emblems()
        if dlc_list == []:#no DLC
            w2 = 0
        e1 = len(emblem_list1)
        e2 = len(emblem_list2)
        if y != 0:
            y += add_rings
            #alear emblem
            alear_emblem, no_pop = alear(x,amount_emblems,z,emblem_list1,emblem_list2,e1,e2,dlc_list)
            if alear_emblem == False or no_pop == True: #Alear no emblem or a DLC emblem
                w -= 1
                w2 += 1
            elif alear_emblem != False and no_pop != True: #Alear has a non DLC emblem
                y -= 1
        else:
            if z == 22:
                alear_emblem = 'Marth'
            else:
                alear_emblem = False
    else:
        dlc_list = []
        emblem_list1 = emblem1
        emblem_list2 = emblem2
        e1 = len(emblem1)
        e2 = len(emblem2)
        #alear emblem
        alear_emblem, no_pop = alear(x,y,z,emblem_list1,emblem_list2,e1,e2, dlc_list)
        if alear_emblem == False:
            w -= 1
            w2 += 1
        elif alear_emblem != False:
            y -= 1
            w2 -= 1

    character_list, number_dead = deaths(character_list)#changing characters when they die  
    for i in range (x-number_dead,(35+add)-number_dead):
        if i < (35+add)-number_dead:
            character_list.pop(x-number_dead)
    random.shuffle(character_list)
    if z != 11 and z != 22: #chapter with no emblems
        if z < 11:
            for t in range (y,100):
                if y < len(emblem_list1)+w2:
                    emblem_list1.pop(amount_emblems-w)
            random.shuffle(emblem_list1)
        elif z >= 11:
            for t in range (y,100):
                if y < len(emblem_list2)+w2:
                    emblem_list2.pop(amount_emblems-w)
            random.shuffle(emblem_list2)
    else:
        emblem_list1 = []
        emblem_list2 = []

    
    i = 0
    char_with_emblems = y-w2 #if too many people die and more emblems than characters left
    if char_with_emblems > len(character_list):
        char_with_emblems = len(character_list)
    if z < 11: #adding in emblem rings (pre ch 11)
        for i in range(i,char_with_emblems):
            character_list[i] = character_list[i] + f' + {emblem_list1[i]}'
    else: #emblem rings after ch 11
        for i in range(i,char_with_emblems):
            character_list[i] = character_list[i] + f' + {emblem_list2[i]}'

    if add == 5:
        Nel = True
    else:
        Nel = False
    return alear_emblem,character_list,Nel
            
#function to print units per deployed spot
def randomizer(alear_emblem,character_list,dlc_characters,Nel):
    if Nel == True:
        character_list = character_list + dlc_characters
    print(character_list)
    x = (int(input('How many deloyment slots are avaliable? '))-1)
    y = 0
    if x > len(character_list): #if many characters die ends list early
        x = len(character_list)
    if alear_emblem == False:
        print(f'Characters: Alear, ',end='')
    else:
        print(f'Characters: Alear + {alear_emblem}, ',end='')
    for y in range(y,x):
        if y == (x-1):
            print(character_list[y],end='')
            print()
        else:
            print(character_list[y],end=', ')

def main():
    alear_emblem,x,Nel = char_in_chap(character_list)
    randomizer(alear_emblem,x,dlc_characters,Nel)


main()
input('Click enter to end.')


