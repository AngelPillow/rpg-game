from random import *
from time import sleep
import copy

def d(n,faces):
    dsum=0
    for i in range(1,n+1):
        dsum += randint(1,faces)
    return dsum

class Player:
    global pclass , weapons , hitpoints , armourclass , damagestr , mindmg , maxdmg , focus
    weapons = {'fighter': 'sword' , 'wizard': 'firebolt' , 'monk': 'fists'}
    damagestr ={'fighter': 'd(3,6)' , 'wizard': 'd(2,12)' , 'monk': 'd(5,4)'}
    armourclass = {'fighter': 8 , 'wizard': 6 , 'monk': 7}
    hitpoints = {'fighter': 120 , 'wizard': 100 , 'monk': 110}
    mindmg = {'fighter': 3 , 'wizard': 2 , 'monk': 5}
    maxdmg = {'fighter': 18 , 'wizard': 24 , 'monk': 20}
    focus = 0

    def __init__(self, pclass):
        self.pclass = pclass
        self.hp = hitpoints[self.pclass]
        self.weapon = weapons[self.pclass]
        self.ac = armourclass[self.pclass]
        self.mindmg = mindmg[self.pclass]
        self.maxdmg = maxdmg[self.pclass]
        self.damagestr = damagestr[self.pclass]

    def damage(self):
        if self.pclass == 'fighter':
            return d(3,6)
        elif self.pclass == 'wizard':
            return d(2,12)
        elif self.pclass == 'monk':
            return d(5,4)
        else:
            return d(int(vol),int(face))

    def custom(self):
        global vol , face
        self.pclass = input('\nSelect your custom class : ')
        self.hp = input('\nSelect your HitPoint total ( 0 < Integer <= 1000) : ')
        while True:
            try:
                int(self.hp)
                if 0 >= int(self.hp) or int(self.hp) > 1000:
                    print('Enter a valid number ')
                    self.hp = input('\nSelect your HitPoint total (Integer) : ')
                else:
                    break
            except:
                print('Enter a valid number ')
                self.hp = input('\nSelect your HitPoint total (Integer) : ')
        self.hp = int(self.hp)
        self.weapon = input('\nSelect your weapon : ')
        while True:
            self.ac = input('\nSelect your ArmourClass total , min = 0 , max = 15 (can be float) : ')
            try:
                float(self.ac)
                if 15 >= float(self.ac) >= 0:
                    self.ac = float(self.ac)
                    break
                else:
                    print('Invalid input , try again. ')
            except:
                print('Invalid input , try again.')
        self.damage = input('\nSelect your damage type: [1].3d6 [2].2d12 [3].4d4 [i].info [c].Custom : ')
        while True:
            if self.damage.lower() == 'i':
                print('XdY in tabletop rpg games means X dice with Y faces\n')
                sleep(2)
                print('For example , 3d6 means that you roll 3 (three) 6-sided dice\n')
                sleep(1)
                self.damage = input('Select your damage type: [1].3d6 [2].2d12 [3].4d4 [i].info [c].Custom : ')
            elif self.damage == '1':
                self.mindmg = mindmg['fighter']
                self.maxdmg = maxdmg['fighter']
                self.damagestr = damagestr['fighter']
                break
            elif self.damage == '2':
                self.mindmg = mindmg['wizard']
                self.maxdmg = maxdmg['wizard']
                self.damagestr = damagestr['wizard']
                break
            elif self.damage == '3':
                self.mindmg = mindmg['monk']
                self.maxdmg = maxdmg['monk']
                self.damagestr = damagestr['monk']
                break
            elif self.damage.lower() == 'c':
                vol = input('\nHow many dice (min = 1 / max = 100) : ')
                face = input('How many sides (Choose between 4 ,6 ,8 ,10 ,12 ,20) : ')
                try:
                    int(vol)
                    int(face)
                    if ( 1 <= int(vol) <= 100 ) and (int(face) in [4, 6, 8, 10 ,12 ,20]):
                        self.mindmg = int(vol)
                        self.maxdmg = int(face)
                        self.damagestr = f'd({int(vol)}, {int(face)})'
                        break
                    else:
                        print('Invalid input , try again. ')
                except:
                    print('Invalid input , try again. ')
            else:
                print('Enter a valid choice ')
                self.damage = input('\nSelect your damage type: [1].3d6 [2].2d12 [3].4d4 [i].Info [c].Custom : ')

    def getstats(self):
        self.stats = [self.pclass, self.hp, self.weapon,  self.ac, self.damagestr]
        return self.stats

    def move(self):
        self.pmove = input('\nChoose your move! [1].Attack [2].Prepare [3].Focus:')
        while True:
            try:
                int(self.pmove)
            except:
                print('Enter a valid move.\n')
                self.pmove = input('\nChoose your move! [1].Attack [2].Defend [3].Focus: ')
            if int(self.pmove) == 1:
                print(f'\nYou attack with your {self.weapon}!')
                return 1
            elif int(self.pmove) == 2:
                print(f"\nYou try to absorb your opponent's incoming attacks!")
                return 2
            elif int(self.pmove) == 3:
                print(f'\nYou attempt to focus on your next attacks!')
                return 3
            else:
                print('Enter a valid move.\n')
                self.pmove = input('\nChoose your move! [1].Attack [2].Defend [3].Focus: ')

    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Enemy:
    global eclass , eweapons , ehitpoints , earmourclass , edamagestr , emindmg , emaxdmg , ename ,lichname , zombname , skelname , gobname , orcname , efocus
    eweapons = {'skeleton': 'dusty sword' , 'lich': 'witch bolt' , 'zombie': 'teeth and nails' , 'goblin': 'scimitar' , 'orc': 'greataxe' , 'imp': 'sting'}
    edamagestr = {'skeleton': 'd(3,8)' , 'lich': 'd(2,12)' , 'zombie': 'd(4,6)}' , 'goblin':'d(3,10)' , 'orc': 'd(3,12)', 'imp': 'd(7,4)'}
    earmourclass = {'skeleton': 10 , 'lich': 8 , 'zombie': 9 , 'goblin': 7 , 'orc': 10, 'imp':8}
    ehitpoints = {'skeleton': 120 , 'lich': 110 , 'zombie': 115 , 'goblin':100 , 'orc':140 , 'imp':105}
    emindmg =  {'skeleton': 4 , 'lich': 3 , 'zombie': 5 , 'goblin':3 ,'orc':3 ,'imp':7}
    emaxdmg = {'skeleton': 32 , 'lich': 36 , 'zombie': 30, 'goblin':30, 'orc':36 ,'imp':28}
    zombname = ['Dancer', 'Gnawer', 'Frenzied', 'Blabber','Riper','Clacker','Slumper','Mutant','Grower','Primer']
    lichname = ["Cram'ghaic","Mhud'ghe","Chozgee","Kradredh","Vhoktag","Thoq'gac","Nanzagradh","Shum'zoudas","Dykragnuk","Thek'vagnudh"]
    skelname = ["Naeryndam Herfir", "Thalanil Miranan", "Hagwin Balrieth", "Onas Virrel", "Aolis Enren","Braumseild", "Tyegnedrorr", "Lul"]
    gobname = ['Ung','Slierx','Woild','Jyk','Brerx','Stiabniark','Slelikx','Crikir','Blegneng','Udyr']
    orcname = ['Jukkhag','Omaghed','Urghat','Hugagug','Khargol','Xago','Xug','Knorgh','Snugug','Bugak']
    ename = zombname + lichname + skelname + orcname + gobname
    efocus = 0

    def __init__(self, eclass):
        self.eclass = eclass
        self.ehp = ehitpoints[self.eclass]
        self.eweapon = eweapons[self.eclass]
        self.eac = earmourclass[self.eclass]
        self.emindmg = emindmg[self.eclass]
        self.emaxdmg = emaxdmg[self.eclass]
        self.edamagestr = edamagestr[self.eclass]
        if eclass == 'zombie':
            self.ename = zombname[randint(0,len(zombname)-1)]
        elif eclass == 'skeleton':
            self.ename = skelname[randint(0,len(skelname)-1)]
        elif eclass == 'lich':
            self.ename = lichname[randint(0,len(lichname)-1)]
        elif eclass == 'goblin':
            self.ename = gobname[randint(0,len(gobname)-1)]
        elif eclass == 'orc':
            self.ename = orcname[randint(0,len(orcname)-1)]
        elif eclass == 'imp':
            self.ename = '???'

    def edamage(self):
        if self.eclass == 'skeleton':
            return d(4,8)
        elif self.eclass == 'lich':
            return d(3,12)
        elif self.eclass == 'zombie':
            return d(5,6)
        elif self.eclass == 'goblin':
            return d(3,10)
        elif self.eclass == 'orc':
            return d(3,12)
        elif self.eclass == 'imp':
            return d(7,4)
        else:
            return d(int(vol),int(face))

    def ecustom(self):
        global vol ,face
        self.eclass = input("\nSelect your opponent's custom class : ")
        while True:
            self.ename = input("\nSelect your opponent's name , type [r] for random : ")
            if self.ename.lower().strip() == 'r':
                self.ename = ename[randint(0,len(ename)-1)]
                break
            else:
                break
        self.ehp = input(f"\nSelect {self.ename}'s HitPoint total ( 0 < Integer <= 1000) : ")
        while True:
            try:
                int(self.ehp)
                if 0 >= int(self.ehp) or int(self.ehp) > 1000:
                    print('Enter a valid number ')
                    self.ehp = input(f"\nSelect {self.ename}'s HitPoint total (Integer) : ")
                else:
                    break
            except:
                print('Enter a valid number ')
                self.ehp = input(f"\nSelect {self.ename}'s HitPoint total (Integer) : ")
        self.ehp = int(self.ehp)
        self.eweapon = input(f"\nSelect  {self.ename}'s weapon : ")
        while True:
            self.eac = input(f"\nSelect {self.ename}'s ArmourClass total , min = 0 , max = 15 (can be float) : ")
            try:
                float(self.eac)
                if 15 >= float(self.eac) >= 0:
                    self.eac = float(self.eac)
                    break
                else:
                    print('Invalid input , try again. ')
            except:
                print('Invalid input , try again.')
        self.edamage = input(f"\nSelect  {self.ename}'s damage type: [1].4d8 [2].3d12 [3].5d6 [4].3d10 [5].7d4 [i].info [c].Custom : ")
        while True:
            if self.edamage.lower() == 'i':
                print('XdY in tabletop rpg games means X dice with Y faces')
                sleep(2)
                print('For example , 3d6 means that you roll 3 (three) 6-sided dice')
                sleep(1)
                self.edamage = input(f"\nSelect  {self.ename}'s damage type: [1].4d8 [2].3d12 [3].5d6 [4].3d10 [5].7d4 [i].info [c].Custom : ")
            elif self.edamage == '1':
                self.eclass = 'skeleton'
                self.emindmg = emindmg['skeleton']
                self.emaxdmg = emaxdmg['skeleton']
                self.edamagestr = edamagestr['skeleton']
                break
            elif self.edamage == '2':
                self.eclass = 'lich'
                self.emindmg = emindmg['lich']
                self.emaxdmg = emaxdmg['lich']
                self.edamagestr = edamagestr['lich']
                break
            elif self.edamage == '3':
                self.eclass = 'zombie'
                self.emindmg = emindmg['zombie']
                self.emaxdmg = emaxdmg['zombie']
                self.edamagestr = edamagestr['zombie']
                break
            elif self.edamage == '4':
                self.eclass = 'goblin'
                self.emindmg = emindmg['goblin']
                self.emaxdmg = emaxdmg['goblin']
                self.edamagestr = edamagestr['goblin']
                break
            elif self.edamage == '5':
                self.eclass = 'imp'
                self.emindmg = emindmg['imp']
                self.emaxdmg = emaxdmg['imp']
                self.edamagestr = edamagestr['imp']
                break
            elif self.edamage.lower() == 'c':
                vol = input('\nHow many dice (min = 1 / max = 100) : ')
                face = input('How many sides ( Choose between 4 ,6 ,8 ,10 ,12 ,20 ) : ')
                try:
                    int(vol)
                    int(face)
                    if (1 <= int(vol) <= 100) and (int(face) in [4, 6, 8, 10, 12, 20]):
                        self.emindmg = int(vol)
                        self.emaxdmg = int(face)
                        self.edamagestr = f'd({int(vol)}, {int(face)})'
                        break
                    else:
                        print('Invalid input , try again. ')
                except:
                    print('Invalid input , try again. ')
            else:
                print('Enter a valid choice \n')
                self.edamage = input(f"Select {self.ename}'s damage type: [1].4d8 [2].3d12 [3].5d6 [4].3d10 [5].7d4 [i].Info [c].Custom")

    def egetstats(self):
        self.estats = [self.eclass, self.ehp, self.eweapon,  self.eac, self.edamagestr]
        return self.estats

    def move(self):
        if self.eac < 15:
            if c[0] >= c[1] and c[0] >= c[2]:
                self.emove = 1
            elif c[1] >= c[2] and c[1] >= c[0]:
                self.emove = 3
            elif c[2] >= c[0] and c[2] >= c[1]:
                self.emove = 2
        else:
            if c[0] >= c[2]:
                self.emove = 1
            else:
                self.emove = 3
        if self.emove == 1:
            print(f'The enemy {self.eclass} attacks you with their {self.eweapon}!')
            return 1
        elif self.emove == 2:
            print(f"The enemy {self.eclass} tries to deflect your next attacks!")
            return 2
        elif self.emove == 3:
            print(f'The enemy {self.eclass} attempts to focus on their next attack!')
            return 3

    def ealive(self):
        if self.ehp > 0:
            return True
        else:
            return False


def main():
    global p1 , e1 , name
    print('     ____________     ')
    print(' ---| Welcome to |--- ')
    print(' ---| "The Game" |--- ')
    print('     ------------     ')
    name = input('\nEnter your name : ')
    show = input('\nShow intro ? [Y] / [N] : ')
    if show.lower().strip() == 'y':
        intro()
    tut = input('\nPlay the Tutorial? (Strongly suggested for those that have not played the game yet) [Y] / [N] : ')
    if tut.lower().strip() == 'y':
        tutorial()
    print('\n')
    menu()

def menu():
    print('             ~~~|          Main menu         |~~~\n')
    print('             ~~~|  [1]     Game Info         |~~~')
    print('             ~~~|  [2]      Battle           |~~~')
    print('             ~~~|  [?]   {Stay tuned}        |~~~')
    print('             ~~~|  [3]       Quit            |~~~\n')
    print('### Since this is a alpha version of the game , it may have inconsistencies ###\n')
    enter = input('Type number to select : ')
    if enter == '1':
        info()
    elif enter == '2':
        print('             ~~~|         Battle Modes        |~~~\n')
        print('             ~~~|  [1]   Classic Battle       |~~~')
        print('             ~~~|  [2]    Custom Battle       |~~~')
        print('             ~~~|  [3]        Back            |~~~\n')
        print('### Please note that this game is not essentially balanced , since it has not been playtested ###\n')
        reenter = input('Type number to select : ')
        if reenter == '1':
            defaultbattle()
        elif reenter == '2':
            custombattle()
        elif reenter == '3':
            print('You are now heading back to the main menu\n')
            menu()
        else:
            print('Invalid choice.\n')
            sleep(1)
            print('You are now heading back to the main menu\n')
            menu()
    else:
        print('You are now exiting the game.\n')

def info():
    print('\nThis is an info guide on the battle mechanisms of "The Game" (Pending title).\n')
    sleep(3)
    print("Be sure to read this if you haven't played the game yet!\n")
    sleep(2)
    print('In this game the Player (you!) fights an opponent in a classic text-based rpg style.\n')
    sleep(2)
    print('The key traits of your character are: Class , HitPoints , Damage and Armour Class\n')
    sleep(2)
    know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
    while True:
        if know.lower().strip() == 'class':
            print('''            Character Class is the path your character has chosen in their life.
            In this pre Alpha version , in non-custom battles , your character can be
            either a fighter , a wizard or a monk. In similar fashion , your ready-to-fight
            opponents have a limited variety of classes.\n  ''' )
            print()
            print('Note: Your class determines your damage input as well as your HitPoint total and ArmourClass!\n')
            know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        elif know.lower().strip() == 'hp':
            print('''            Your HitPoint total represents your ability to survive damage in battle.
            The more HitPoints you have , the harder it is for you to be dealt lethal
            damage from a hit and die.\n  ''')
            print()
            print('Note: Your HitPoint total varies for different character classes!\n')
            know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        elif know.lower().strip() == 'dmg':
            print('''            The term damage represents the lethality of your hits versus your opponent's 
            HitPoint total. You can deal damage to your opponent by selecting the [Attack]
            action in-battle and vise-versa. The [Focus] action makes your future attacks 
            deal more damage. \n  ''')
            print()
            print('Note: Your damage varies for different character classes!\n')
            know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        elif know.lower().strip() == 'ac':
            print('''            Your ArmourClass score represents your ability to not be hit or affected by
            an attack. When attacking or being attacked , a 20-sided dice is rolled and if that roll is 
            equal or greater than your AC , the attack hits! In the special case of a 20 ,
            the attack hits and deals two times the damage it would normally deal.
            Your (and your enemy's) AC can be amplified by the [Prepare] action in-battle
            to make it harder for your opponent to hit you (and vise-versa).\n  ''')
            print()
            print('Note: Your AC varies for different classes!\n')
            know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        elif know.lower().strip() == 'modes':
            print('''            The modes in this pre Alpha version are: Classic & Custom.
            In Classic , you may choose to be a character with pre determined stats
            that fights a similarly determined opponent.
            In Custom you may choose to be a character made completely out of your imagination
            (some restrictions are applied) and battle either a pre-determined opponent or create
            one of your own. For the time being , you cannot save your own characters or opponents.\n  ''')
            print()
            print('Note: This took way longer than expected...\n')
            know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        elif know.lower().strip() == 'quit':
            print('You are now exiting the info menu.\n')
            menu()
            break
        else:
            print("That asset doesn't exist / Invalid choice.")
            print('You are heading back to the main menu\n')
            menu()
            break

def intro():
    print('\nWelcome to the pre Alpha version of "The Game" (Pending title).\n')
    sleep(2)
    print('This is a simulator for text-based rpg battles\n')
    sleep(2)
    print('Three different classes await you... Three different ways to play the game.\n')
    sleep(2)
    print('Fighter')
    sleep(1)
    print('           Wizard')
    sleep(1)
    print('                      Monk\n')
    sleep(1)
    print('The fighter uses their sword and bulky defence to outlast their opponent.\n')
    sleep(2)
    print('The wizard specializes in destructive spells , while being relatively easy to be taken down.\n')
    sleep(2)
    print('Last but not least , the monk uses their own hands to knock out their opponent.\n')
    sleep(2)
    print('What kind of opponents are you ready to face? Because they are lurking . . .\n')

def custombattle():
    p1 = Player('wizard')
    e1 = Enemy('lich')
    p1.custom()
    e1.ecustom()
    showdown(p1,e1)

def defaultbattle():
    ch = select()
    p1 = Player(ch)
    op = challenger()
    e1 = Enemy(op)
    showdown(p1,e1)

def select():
    char = input('Type the name of your desired class : [Fighter] / [Wizard] / [Monk] \n')
    while True:
        if char.lower().strip() == 'fighter' or char.lower().strip() == 'wizard' or char.lower().strip() == 'monk':
            char = char.lower().strip()
            sleep(1)
            print(f'\nSo you are {name} the {char}! Well then!\n')
            break
        else:
            print('Enter a valid class')
            char = input('Type the name of your desired class\n')
    return char

def challenger():
    enemylist = ['skeleton', 'lich', 'zombie', 'goblin', 'orc']
    while True:
        enemy = input('Choose your opponent: [1].Skeleton [2].Lich [3].Zombie [4].Goblin [5].Orc [6].Imp [r].Random')
        if enemy == '1' or enemy.lower() == 'skeleton':
            return 'skeleton'
        elif enemy == '2' or enemy.lower() == 'lich':
            return 'lich'
        elif enemy == '3' or enemy.lower() == 'zombie':
            return 'zombie'
        elif enemy == '4' or enemy.lower() == 'goblin':
            return 'goblin'
        elif enemy == '5' or enemy.lower() == 'orc':
            return 'orc'
        elif enemy == '6' or enemy.lower() == 'imp':
            return 'imp'
        elif enemy.lower().strip() == 'r':
            return enemylist[randint(0, len(enemylist)-1)]
        else:
            print('Invalid choice.\n')

def moveoutcome(player,enemy):
    global c , ch , focus
    c = [0, 0, 0]
    ch = 0
    mymove = player.move()
    roll = d(1,20)
    dmg = player.damage() + focus
    if mymove == 1:
        c[0]+=1
        ch = 1
        print(f'You rolled a {roll}!')
        sleep(1)
        if roll >= enemy.eac:
            print('The attack hits!')
            sleep(1)
            if roll == 20:
                print('\n### Critical Hit ###\n')
                sleep(2)
                enemy.ehp -= 2 * dmg
                print(f'You dealt a total of {2 * dmg} points of damage to  {enemy.ename}!\n')
                return True
            else:
                sleep(2)
                enemy.ehp -= dmg
                print(f'You dealt a total of {dmg} points of damage!\n')
                return True
        else:
            print("The attack doesn't hit...\n")
            return True
    elif mymove == 2:
        sleep(1)
        if player.ac >= 15:
            print(f'You cannot make it harder for {enemy.ename} to hit you...\n')
            return True
        else:
            c[1] += 1
            ch = 2
            print('It is now harder for the opponent to hit you!\n')
            player.ac += 0.5
            return True
    elif mymove == 3:
        sleep(1)
        c[2] += 1
        ch = 3
        print('Your next attacks will be more devastating!\n')
        focus += d(1,4)
        player.mindmg += 1
        player.maxdmg += 4
        return True

def emoveoutcome(player,enemy):
    global efocus
    theirmove = enemy.move()
    eroll = d(1,20)
    edmg = enemy.edamage() + efocus
    if theirmove == 1:
        print(f'The enemy rolled a {eroll}!')
        sleep(1)
        if eroll >= player.ac:
            print('The attack hits!')
            sleep(1)
            if eroll == 20:
                print('\n### Critical Hit ###\n')
                sleep(2)
                player.hp -= 2 * edmg
                print(f' {enemy.ename} dealt {2 * edmg} points of damage to you!\n')
            else:
                player.hp -= edmg
                sleep(2)
                print(f' {enemy.ename} dealt {edmg} points of damage to you!\n')
        else:
            print("The attack doesn't hit...\n")
    elif theirmove == 2:
        sleep(1)
        if enemy.eac >= 15:
            print(f"{enemy.ename} cannot make it any harder for you to hit them")
        else:
            print(f'It will be now harder to hit  {enemy.ename}!\n')
            enemy.eac += 0.5
    elif theirmove == 3:
        sleep(1)
        print(f"{enemy.ename}'s next attacks will be more devastating!\n")
        efocus += d(1,8)
        enemy.emindmg += 1
        enemy.emaxdmg += 8

def tutorial():
    print(f'\nWelcome to the tutorial {name} , where (I hope!) most of your possible questions about the game will be cleared out!\n')
    sleep(8)
    print('\nYou are a young wizard , taking a little stroll through a nearby forest , since you are taking a break from studying.\n')
    sleep(8)
    print('\nNature seemed to always relax you and amaze you at the same time , since you innately sensed the magic hidden in it.\n')
    sleep(8)
    print('\nThe city on the other hand might be safer to wander around , but these days it is in an uproar.\n')
    sleep(8)
    print("\nPeople from all over the city talk of an evil power rising from the depths of a cave , just a couple of miles outside of the city's borders.\n")
    sleep(8)
    print("\nThus , the whole city's brimming with soldiers and war mages , ready to attack the unknown threat.\n")
    sleep(8)
    print('\nYet , no signs of it have been sighted outside of the cave.\n')
    sleep(5)
    print("\nOr until now! As you walk through the forest trail you detect a black sphere floating in the air , just some feet in front of you.\n")
    sleep(8)
    print("\nYour curiosity is piqued and you can't help it but approach carefully the sphere.\n")
    sleep(7)
    print('\nAs you lumber towards the unexpected sight , you notice a figure pop out of the orb and stare at you.\n')
    sleep(8)
    print('\nYou feel a shiver running down your spine , as this human-like creature strides towards your position.\n')
    sleep(8)
    print('\n*** Get ready to face it ***\n')
    sleep(4)
    p1 = Player('wizard')
    p1.hp = 50
    e1 = Enemy('lich')
    e1.ehp = 30
    print(f'\nThe battle between you and the opposing lich has begun!\n')
    sleep(4)
    print('\n *** So the battle has started! Get ready , I think you get to act first ***\n')
    sleep(6)
    print('\n*** When battling , you can use your [Attack] action to try and damage your opponent ***\n')
    sleep(6)
    while True:
        epilogh = input('Choose your move! [A].Attack [?].??????? [?].?????:\n')
        if epilogh.lower().strip() == 'a':
            sleep(2)
            break
        else:
            print('Type [A] to attack!\n')
    print('\nYou attack your opponent with your firebolt! \n')
    sleep(2)
    print('\n*** After selecting to attack but before the attack deals damage , a 20-sided dice')
    sleep(5)
    print('    is rolled (or at least it is a simulation of a such throw). Then , if the roll')
    sleep(6)
    print("    is equal or higher than your opponent's ArmourClass (check out GameInfo section for more info)")
    sleep(6)
    print("    the attack hits! Otherwise , you miss. Let's see how this one goes! ***\n")
    sleep(6)
    print(f'You rolled a {randint(10,19)} !\n')
    sleep(2)
    print('The attack hits! \n')
    sleep(2)
    print('\n*** Nice! Since the attack landed , you get to deal damage to your opponent! *** \n')
    sleep(5)
    dmg = p1.damage
    print(f'You dealt a total of {dmg} points of damage!\n')
    sleep(3)
    print('\n*** Now that you attacked , prepare for what your opponent is ready to do on their turn! ***\n')
    sleep(6)
    print(" [Lich] : You dare oppose me mortal? You don't seem to understand who you are facing\n")
    sleep(7)
    print(' [Lich] : I am Norfir Wildstrider , or at least I was... Not that it matters for you! Ahahahaha!\n')
    sleep(7)
    print(' [Norfir Wildstrider(?)] : You better remember my name as you are visiting Hades for dinner tonight!\n')
    sleep(7)
    print("\n*** Talk is cheap , let's see what he's got! ***\n")
    sleep(5)
    print('Norfir Wildstrider(?) attacks you with his eldritch blast!\n')
    sleep(3)
    print(f'Norfir Wildstrider(?) rolled a {randint(10,19)} !\n')
    sleep(3)
    print('The attack hits!\n')
    sleep(2)
    edmg = e1.edamage
    print(f'Norfir Wildstrider(?) dealt a total of {edmg} points of damage to you!\n')
    p1.hp -= edmg
    sleep(4)
    print(f"\n~~~ Your HP : [{p1.hp}] VS Norfir's(?) HP [???] ~~~\n")
    sleep(6)
    print(" [Norfir Wildstrider(?)] : This is unfair! Where are your friends to help you?\n")
    sleep(4)
    while True:
        answer = input(f'''[1].I don't need anything but my spells to kill you!
[2].I have been using only the 5% of my powers all along! 
[3].Where's Hermione when I need her?... Wait, wrong game.
[4].So nobody has defeated you yet! It will be me , Dio! err {name} !I mean...\n''')
        if answer == '1':
            print(f" [{name}] : I don't need anything but my spells to kill you!\n")
            sleep(3)
            print(' [Norfir Wildstrider(?)] : So you want to go early for dinner huh? Let me give you a lift.\n')
            break
        elif answer == '2':
            print(f' [{name}] : I have been using only the 5% of my powers all along!\n')
            sleep(3)
            print(' [Norfir Wildstrider(?)] : Is that so? Then show me what you can do!\n')
            break
        elif answer == '3':
            print(f" [{name}] : Where's Hermione when I need her?... Wait, wrong game.\n")
            sleep(3)
            print(' [Norfir Wildstrider(?)] : ???\n')
            break
        elif answer == '4':
            print(f' [{name}] : So nobody has defeated you yet! It will be me , Dio! err {name} ! I mean...\n')
            sleep(3)
            print(' [Norfir Wildstrider(?)] : Is that so? Then come as close to me as you like!\n')
            break
        else:
            print(f' [{name}] : . . .\n')
            sleep(3)
            print(' [Norfir Wildstrider(?)] : The silent treatment huh?\n')
            break
    sleep(3)
    print("*** Round 2 is up champ ! Now let's try a different approach. Instead of attacking ,")
    sleep(7)
    print(" try to make it tougher for your opponent to hit you with his spells.")
    sleep(7)
    print(" You can achieve that by choosing to [Prepare] during your turn.")
    sleep(6)
    print("By preparing , you get a flat increase to your ArmourClass. That somewhat lowers the odds of you getting hit ***")
    sleep(8)
    while True:
        epilogh2 = input('Choose your move! [A].Attack [B].Prepare [?].?????:\n')
        if epilogh2.lower().strip() == 'b':
            sleep(2)
            break
        else:
            print('Type [B] to prepare!\n')
    print(f"You try to absorb Norfir's(?) incoming attacks!\n")
    sleep(2)
    p1.ac += 0.5
    print("*** Hold tight! Norfir's(?) about to unleash another barrage of spells ***\n")
    sleep(4)
    print('Norfir Wildstrider(?) attacks you with his magic missiles!\n')
    sleep(4)
    print(f'Norfir Wildstrider(?) rolled a {randint(5, 8)} !\n')
    sleep(3)
    print("The attack doesn't hit!\n")
    sleep(2)
    print(f"\n~~~ Your HP : [{p1.hp}] VS Norfir's(?) HP [???] ~~~\n")
    sleep(4)
    print(" [Norfir Wildstrider(?)] : Nonsense! How did I miss? It's ok. That was a warning shot.\n")
    sleep(5)
    print(f' [{name}] : Yeah , right...\n')
    sleep(3)
    print('*** One more helpful buzz and I will let you finish him! I guess you have already seen that')
    sleep(7)
    print(' you have one more in-battle choice. Well , that is [Focus]. By focusing on your next attacks')
    sleep(7)
    print(" you will be able to dish out more damage than normal! Why didn't I tell you about that sooner? Whoopsie! *** ")
    sleep(8)
    while True:
        epilogh3 = input('Choose your move! [A].Attack [B].Prepare [C].Focus :\n')
        if epilogh3.lower().strip() == 'c':
            sleep(2)
            break
        else:
            print('Type [C] to focus!\n')
    print('You attempt to focus on your next attacks!\n')
    sleep(3)
    print('Your next attacks will be more devastating!\n')
    sleep(3)
    p1.damage += d(1, 4)
    print(' Norfir Wildstrider(?) tries to focus on his next attacks!\n')
    sleep(3)
    e1.edamage += d(1,4)
    print("Norfir's(?) incoming attacks will be more powerful!\n")
    sleep(3)
    print("*** It's on you now to finish him. Use your new knowledge to style on him! ***\n")
    sleep(4)
    print(f"\n~~~ Your HP : [{p1.hp}] VS Norfir's(?) HP [???] ~~~\n")
    sleep(3)
    while True:
        epilogh4 = input('Choose your move! [A].Attack [B].Prepare [C].Focus:\n')
        if epilogh4.lower().strip() in 'abc':
            print("A mystical dark force rises from the orb and wraps Norfir(?). Like if it was nighttime,")
            sleep(6)
            print('everything went dark. An outlandish voice commanded you to stay still.')
            sleep(5)
            resist = input('\nDo you resist it? [Y] / [N] : ')
            if resist.lower().strip() == 'y':
                sleep(3)
                print('You try to turn around and run;') , sleep(5) , print('. . .') , sleep(5) , print('. . .\n')
                print("You can't move a muscle. Is this the end?\n")
                sleep(2)
            else:
                sleep(3)
                print('You stay still as commanded to.')
                sleep(3)
                print('You attempt to reach your pocket.')
                sleep(3)
                print("You can't move a muscle. Is this the end?")
                sleep(3)
            break
        else:
            print('Select your move!\n')
    menu()

def showdown(player,enemy):
    global dummy , edummy
    dummy = copy.deepcopy(player)
    edummy = copy.deepcopy(enemy)
    print(f'\nThe battle between you and the opposing {enemy.ename} , the {enemy.eclass} has begun!\n')
    while True:
        if player.alive() and enemy.ealive():
            moveoutcome(player,enemy)
            if enemy.ealive():
                emoveoutcome(player,enemy)
            elif not enemy.ealive():
                print('\n~~~ You have won ~~~\n')
                break
        elif not player.alive():
            print('\n~~~ You have died ~~~\n')
            break
        elif not enemy.ealive():
            print('\n~~~ You have won! ~~~')
            break
        print(f"~~~ Your HP : [{player.hp}] ~~~  VS  ~~~ {enemy.ename}'s HP : [{enemy.ehp}] ~~~\n")
        sleep(0.5)
        print(f'~~~ Chance of landing an attack : {(20-enemy.eac)*5}% ~~~  VS  ~~~ Chance of being hit by an attack : {(20-player.ac)*5}% ~~~\n')
        sleep(0.5)
        print(f"~~~ Expected damage from your attacks : {player.mindmg} - {player.maxdmg}~~~  VS  ~~~ Expected damage from opponent's attacks : {enemy.emindmg} - {enemy.emaxdmg} ~~~\n")
        sleep(0.5)
    replay = input('\nReplay? [Y] / [N] : \n')
    if replay.lower().strip() == 'y':
        showdown(dummy,edummy)
    else:
        menu()

main()
