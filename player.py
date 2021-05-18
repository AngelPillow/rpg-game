from random import *
from time import sleep

def d(n,faces):
    dsum=0
    for i in range(1,n+1):
        dsum += randint(1,faces)
    return dsum

class Player:
    global pclass , weapons , hitpoints , armourclass , damage , damagestr , mindmg , maxdmg
    weapons = {'fighter': 'sword' , 'wizard': 'firebolt' , 'monk': 'fists'}
    damagestr ={'fighter': 'd(3,6)' , 'wizard': 'd(2,12)' , 'monk': 'd(4,4)'}
    damage = {'fighter': d(3,6) , 'wizard': d(2,12) , 'monk': d(4,4)}
    armourclass = {'fighter': 8 , 'wizard': 6 , 'monk': 7}
    hitpoints = {'fighter': 120 , 'wizard': 100 , 'monk': 110}
    mindmg = {'fighter': 3 , 'wizard': 2 , 'monk': 4}
    maxdmg = {'fighter': 18 , 'wizard': 24 , 'monk': 16}

    def __init__(self, pclass):
        self.pclass = pclass
        self.hp = hitpoints[self.pclass]
        self.weapon = weapons[self.pclass]
        self.ac = armourclass[self.pclass]
        self.damage = damage[self.pclass]
        self.mindmg = mindmg[self.pclass]
        self.maxdmg = maxdmg[self.pclass]
        self.damagestr = damagestr[self.pclass]

    def custom(self):
        self.pclass = input('Select your custom class ')
        self.hp = input('Select your HitPoint total (Integer)')
        while True:
            try:
                int(self.hp)
                break
            except:
                print('Enter a valid number ')
                self.hp = input('Select your HitPoint total (Integer)')
        self.hp = int(self.hp)
        self.weapon = input('Select your weapon ')
        while True:
            self.ac = input('Select your ArmourClass total , min = 0 , max = 17.5')
            try:
                float(self.ac)
                if 17.5 >= float(self.ac) >= 0:
                    self.ac = float(self.ac)
                    break
                else:
                    print('Invalid input , try again. ')
            except:
                print('Invalid input , try again.')
        while True:
            self.damage = input('Select your damage type: [1].3d6 [2].2d12 [3].4d4 [i].info [c].Custom')
            if self.damage.lower() == 'i':
                print('XdY in tabletop rpg games means X dice with Y faces')
                sleep(2)
                print('For example , 3d6 means that you roll 3 (three) 6-sided dice')
                sleep(1)
            if self.damage == '1':
                self.damage = damage['fighter']
                self.mindmg = mindmg['fighter']
                self.maxdmg = maxdmg['fighter']
                self.damagestr = damagestr['fighter']
                break
            elif self.damage == '2':
                self.damage = damage['wizard']
                self.mindmg = mindmg['wizard']
                self.maxdmg = maxdmg['wizard']
                self.damagestr = damagestr['wizard']
                break
            elif self.damage == '3':
                self.damage = damage['monk']
                self.mindmg = mindmg['monk']
                self.maxdmg = maxdmg['monk']
                self.damagestr = damagestr['monk']
                break
            elif self.damage == 'c':
                vol = input('How many dice ')
                face = input('How many sides ')
                try:
                    int(vol)
                    int(face)
                    self.damage = d(int(vol), int(face))
                    self.mindmg = int(vol)
                    self.maxdmg = int(face)
                    self.damagestr = f'd({int(vol)}, {int(face)})'
                    break
                except:
                    print('Invalid input , try again. ')

            else:
                print('Enter a valid choice \n')
                self.damage = input('Select your damage type: [1].3d6 [2].2d12 [3].4d4 [i].Info [c].Custom')

    def getstats(self):
        self.stats = [self.pclass, self.hp, self.weapon,  self.ac, self.damagestr]
        return self.stats

    def move(self):
        self.pmove = input('Choose your move! [1].Attack [2].Prepare [3].Focus \n')
        while True:
            try:
                int(self.pmove)
            except:
                print('Enter a valid move.\n')
                self.pmove = input('Choose your move! [1].Attack [2].Defend [3].Focus \n')
            if int(self.pmove) == 1:
                print(f'You attack with your {weapons[self.pclass]}!')
                return 1
            elif int(self.pmove) == 2:
                print(f"You try to absorb the enemy's incoming attacks!")
                return 2
            elif int(self.pmove) == 3:
                print(f'You attempt to focus on your next attack!')
                return 3
            else:
                print('Enter a valid move.\n')
                self.pmove = input('Choose your move! [1].Attack [2].Defend [3].Focus \n')

    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Enemy:
    global eclass , eweapons , ehitpoints , earmourclass , edamage , edamagestr , emindmg , emaxdmg , ename ,lichname , zombname , skelname
    eweapons = {'skeleton': 'dusty sword' , 'lich': 'witch bolt' , 'zombie': 'teeth and nails'}
    edamage = {'skeleton': d(3,8) , 'lich': d(2,12) , 'zombie': d(4,6)}
    edamagestr = {'skeleton': 'd(3,8)' , 'lich': 'd(2,12)' , 'zombie': 'd(4,6)}'}
    earmourclass = {'skeleton': 10 , 'lich': 8 , 'zombie': 9}
    ehitpoints = {'skeleton': 160 , 'lich': 140 , 'zombie': 150}
    emindmg =  {'skeleton': 3 , 'lich': 2 , 'zombie': 4}
    emaxdmg = {'skeleton': 24 , 'lich': 24 , 'zombie': 24}
    zombname = ['Dancer', 'Gnawer', 'Frenzied', 'Blubber Zombie','Ripe Zombie','Clacker','Slumper','Mutant','Grower','Primer']
    lichname = ["Cram'ghaic","Mhud'ghe","Chozgee","Kradredh","Vhoktag","Thoq'gac","Nanzagradh","Shum'zoudas","Dykragnuk","Thek'vagnudh"]
    skelname = ["Naeryndam Herfir", "Thalanil Miranan", "Hagwin Balrieth", "Onas Virrel", "Aolis Enren","Braumseild", "Tyegnedrorr", "Lul"]
    ename = zombname + lichname + skelname

    def __init__(self, eclass):
        self.eclass = eclass
        self.ehp = ehitpoints[self.eclass]
        self.eweapon = eweapons[self.eclass]
        self.eac = earmourclass[self.eclass]
        self.edamage = edamage[self.eclass]
        self.emindmg = emindmg[self.eclass]
        self.emaxdmg = emaxdmg[self.eclass]
        self.edamagestr = edamagestr[self.eclass]
        if eclass == 'zombie':
            self.ename = zombname[randint(0,len(zombname)-1)]
        elif eclass == 'skeleton':
            self.ename = skelname[randint(0,len(skelname)-1)]
        elif eclass == 'lich':
            self.ename = lichname[randint(0,len(lichname)-1)]

    def ecustom(self):
        self.eclass = input("Select your opponent's custom class ")
        while True:
            self.ename = input("Select your opponent's name , type [r] for random")
            if self.ename.lower().strip() == 'r':
                self.ename = ename[randint(0,len(ename)-1)]
                break
        self.ehp = input(f"Select  {self.ename}'s HitPoint total (Integer)")
        while True:
            try:
                int(self.ehp)
                break
            except:
                print('Enter a valid number ')
                self.ehp = input(f"Select  {self.ename}'s HitPoint total (Integer)")
        self.ehp = int(self.ehp)
        self.eweapon = input(f"Select  {self.ename}'s weapon ")
        while True:
            self.eac = input(f"Select {self.ename}'s ArmourClass total , min = 0 , max = 17.5 (can be float)")
            try:
                float(self.eac)
                if 17.5 >= float(self.eac) >= 0:
                    self.eac = float(self.eac)
                    break
                else:
                    print('Invalid input , try again. ')
            except:
                print('Invalid input , try again.')
        while True:
            self.edamage = input(f"Select  {self.ename}'s damage type: [1].3d6 [2].2d12 [3].4d4 [i].info [c].Custom")
            if self.edamage.lower() == 'i':
                print('XdY in tabletop rpg games means X dice with Y faces')
                sleep(2)
                print('For example , 3d6 means that you roll 3 (three) 6-sided dice')
                sleep(1)
            if self.edamage == '1':
                self.edamage = edamage['skeleton']
                self.emindmg = emindmg['skeleton']
                self.emaxdmg = emaxdmg['skeleton']
                self.edamagestr = edamagestr['skeleton']
                break
            elif self.edamage == '2':
                self.edamage = edamage['lich']
                self.emindmg = emindmg['lich']
                self.emaxdmg = emaxdmg['lich']
                self.edamagestr = edamagestr['lich']
                break
            elif self.edamage == '3':
                self.edamage = edamage['zombie']
                self.emindmg = emindmg['zombie']
                self.emaxdmg = emaxdmg['zombie']
                self.edamagestr = edamagestr['zombie']
                break
            elif self.edamage == 'c':
                vol = input('How many dice ')
                face = input('How many sides ')
                try:
                    int(vol)
                    int(face)
                    self.edamage = d(int(vol), int(face))
                    self.emindmg = int(vol)
                    self.emaxdmg = int(face)
                    self.edamagestr = f'd({int(vol)}, {int(face)})'
                    break
                except:
                    print('Invalid input , try again. ')
            else:
                print('Enter a valid choice \n')
                self.edamage = input("Select  {self.ename}'s damage type: [1].3d6 [2].2d12 [3].4d4 [i].Info [c].Custom")

    def egetstats(self):
        self.estats = [self.eclass, self.ehp, self.eweapon,  self.eac, self.edamage]
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
            print(f'The enemy {self.eclass} attacks you with their {eweapons[self.eclass]}!')
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
    intro()
    name = input('Enter your name : ')
    menu()

def menu():
    print('             ~~~|         Main menu        |~~~\n')
    print('             ~~~|  [1]    Game Info        |~~~')
    print('             ~~~|  [2]     Battle          |~~~')
    print('             ~~~|  [3]      Quit           |~~~\n')
    print('### Since this is a alpha version of the game , it may have inconsistencies ###\n')
    enter = input('Type number to select')
    if enter == '1':
        info()
    elif enter == '2':
        print('             ~~~|           Battle Modes        |~~~\n')
        print('             ~~~|   [1]    Classic Battle       |~~~')
        print('             ~~~|   [2]     Custom Battle       |~~~')
        print('             ~~~|   [3]         Back            |~~~\n')
        print('### Please note that this game is not essentially balanced , since it has not been playtested ###\n')
        reenter = input('Type number to select')
        if reenter == '1':
            defaultbattle()
        elif reenter == '2':
            custombattle()
        elif reenter == '3':
            print('You are now heading back to the main menu\n')
            menu()
        else:
            print('Invalid choice.\n')
            print('You are now heading back to the main menu\n')
            menu()
    else:
        print('You are now exiting the game.\n')

def info():
    print('This is an info guide on the battle mechanisms of "The Game" (Pending title).')
    sleep(1)
    print("Be sure to read this if you haven't played the game yet!")
    sleep(1)
    print('In this game the Player (you!) fights an opponent in a classic text-based rpg style.')
    sleep(1)
    print('The key traits of your character are: Class , HitPoints , Damage and Armour Class')
    sleep(1)
    while True:
        know = input('For which asset do you want to know about? [class] / [hp] / [dmg] / [ac] / [modes] / [quit]\n')
        if know.lower().strip() == 'class':
            print('''            Character Class is the path your character has chosen in their life.
            In this pre Alpha version , in non-custom battles , your character can be
            either a fighter , a wizard or a monk. In similar fashion , your ready-to-fight
            opponents have a limited variety of classes.\n  ''' )
            print()
            print('Note: Your class determines your damage input as well as your HitPoint total and ArmourClass!\n')
        elif know.lower().strip() == 'hp':
            print('''            Your HitPoint total represents your ability to survive damage in battle.
            The more HitPoints you have , the harder it is for you to be dealt lethal
            damage from a hit and die.\n  ''')
            print()
            print('Note: Your HitPoint total varies for different character classes!\n')
        elif know.lower().strip() == 'dmg':
            print('''            The term damage represents the lethality of your hits versus your opponent's 
            HitPoint total. You can deal damage to your opponent by selecting the [Attack]
            action in-battle and vise-versa. The [Focus] action makes your future attacks 
            deal more damage. \n  ''')
            print()
            print('Note: Your damage varies for different character classes!\n')
        elif know.lower().strip() == 'ac':
            print('''            Your ArmourClass score represents your ability to not be hit or affected by
            an attack. When attacking or being attacked , a 20-sided dice is rolled and if that roll is 
            equal or greater than your AC , the attack hits! In the special case of a 20 ,
            the attack hits and deals two times the damage it would normally deal.
            Your (and your enemy's) AC can be amplified by the [Prepare] action in-battle
            to make it harder for your opponent to hit you (and vise-versa).\n  ''')
            print()
            print('Note: Your AC varies for different classes!\n')
        elif know.lower().strip() == 'modes':
            print('''            The modes in this pre Alpha version are: Classic & Custom.
            In Classic , you may choose to be a character with pre determined stats
            that fights a similarly determined opponent.
            In Custom you may choose to be a character made completely out of your imagination
            (some restrictions are applied) and battle either a pre-determined opponent or create
            one of your own. For the time being , you cannot save your own characters or opponents.\n  ''')
            print()
            print('Note: This took way longer than expected...\n')
        elif know.lower().strip() == 'quit':
            print('You have now exited the info menu.\n')
            menu()
            break
        else:
            print("That asset doesn't exist / Invalid choice.")
            print('You are heading back to the main menu\n')
            menu()

def intro():
    print('Welcome to the pre Alpha version of "The Game" (Pending title).')
    sleep(2)
    print('This is a simulator for text-based rpg style battles')
    sleep(2)
    print('Three different classes await you... Three different ways to play the game.')
    sleep(2)
    print('Fighter')
    sleep(1)
    print('           Wizard')
    sleep(1)
    print('                      Monk')
    sleep(1)
    print('The fighter uses their sword and bulky defence to outlast their opponent.')
    sleep(2)
    print('The wizard specializes in destructive spells , while being relatively easy to be taken down.')
    sleep(2)
    print('Last but not least , the monk uses their own hands to knock out their opponent.')
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
    char = input('Type the name of your desired class\n')
    while True:
        if char == 'fighter' or char == 'wizard' or char == 'monk':
            print(f'So you are {name} the {char}! Well then!')
            break
        else:
            print('Enter a valid class')
            char = input('Type the name of your desired class\n')
    return char

def challenger():
    enemylist = ['skeleton', 'lich', 'zombie']
    while True:
        enemy = input('Choose your opponent: [1].skeleton [2].lich [3].zombie [r].Random')
        if enemy == '1' or enemy.lower() == 'skeleton':
            return 'skeleton'
        elif enemy == '2' or enemy.lower() == 'lich':
            return 'lich'
        elif enemy == '3'or enemy.lower() == 'zombie':
            return 'zombie'
        elif enemy.lower().strip() == 'r':
            return enemylist[randint(0, 2)]
        else:
            print('Invalid choice.\n')

def moveoutcome(player,enemy):
    global c , ch , dmg
    c = [0, 0, 0]
    mymove = player.move()
    roll = d(1,20)
    if mymove == 1:
        c[0]+=1
        ch = 1
        print(f'You rolled a {roll}!')
        if roll >= enemy.eac:
            print('The attack hits!\n')
            if roll == 20:
                print('### Critical Hit ###\n')
                dmg = 2 * player.damage
                print(f'You dealt a total of {dmg} points of damage to  {enemy.ename}!')
                enemy.ehp -= dmg
            else:
                dmg = player.damage
                print(f'You dealt a total of {dmg} damage!')
                enemy.ehp -= dmg
        else:
            print("The attack doesn't hit...\n")
    elif mymove == 2:
        if player.ac >= 15:
            print(f'You cannot make it harder for  {enemy.ename} to hit you...')
        else:
            c[1] += 1
            ch = 2
            print('It will be now harder for the opponent to hit you!\n')
            player.ac += 0.5
    elif mymove == 3:
        c[2] += 1
        ch = 3
        print('Your next attacks will be more devastating!\n')
        player.damage += d(1,4)
        player.mindmg += 1
        player.maxdmg += 4


def emoveoutcome(player,enemy):
    global edmg
    theirmove = enemy.move()
    eroll = d(1,20)
    if theirmove == 1:
        print(f'The enemy rolled a {eroll}!')
        if eroll >= player.ac:
            print('The attack hits!\n')
            if eroll == 20:
                print('### Critical Hit ###\n')
                edmg = 2 * enemy.edamage
                print(f' {enemy.ename} dealt {edmg} points of damage to you!')
                player.hp -= edmg
            else:
                edmg = enemy.edamage
                print(f' {enemy.ename} dealt {edmg} points of damage to you!')
                player.hp -= edmg
        else:
            print("The attack doesn't hit...\n")
    elif theirmove == 2:
        if enemy.eac >= 17.5:
            print(" {enemy.ename} cannot make it any harder for you to hit")
        else:
            print(f'It will be now harder to hit  {enemy.ename}!\n')
            enemy.eac += 0.5
    elif theirmove == 3:
        print(f"{enemy.ename}'s next attacks will be more devastating!\n")
        enemy.edamage += d(1,10)
        enemy.emindmg += 1
        enemy.emaxdmg += 10

def showdown(player,enemy):
    print(f'The battle between you and the opposing {enemy.ename} , the {enemy.eclass} have begun!\n')
    while True:
        if player.alive() and enemy.ealive():
            moveoutcome(player,enemy)
            emoveoutcome(player,enemy)
        elif not enemy.ealive():
            print('~~~You have won!~~~\n')
            break
        elif not player.alive():
            print('~~~You have died~~~')
            break
        print(f"~~~ Your HP : [{player.hp}] ~~~  VS  ~~~ {enemy.ename}'s HP : [{enemy.ehp}] ~~~\n")
        print(f'~~~ Chance of landing an attack : {(20-enemy.eac)*5}% ~~~  VS  ~~~ Chance of being hit by an attack : {(20-player.ac)*5}% ~~~\n')
        print(f"~~~ Expected damage from your attacks : {player.mindmg} - {player.maxdmg}~~~  VS  ~~~ Expected damage from opponent's attacks : {enemy.emindmg} - {enemy.emaxdmg}\n")
    replay = input('Replay? [Y] / [N]')
    if replay.lower().strip() == 'y':
        showdown(player,enemy)
    else:
        menu()


main()
