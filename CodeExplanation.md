# The Game
Alpha version of a text-based rpg battle simulator , made in Python

Here I will briefly try to explain how the code works , and how the different classes and functions connect to make the whole thing come to life.
Most of the in-game mechanics' info can be accessed via the game itself , in the info() function.

General functions:
-------------------
d(num,faces) ----------> this represents the sum of the prices of the dice 'thrown' for in-game purposes



1.[Classes]

The classes in this game are the one of the player ( Player() ) and of the CPU playing the opponent ( Enemy() ).

~ Class characteristics:

* Player Class
----------------
1) class  (in-game character) , i.e. fighter
2) weapon , i.e. sword
3) hitpoints (the so called HP) , i.e. 120 HP
4) armourclass (AC) , i.e. 12
5) damage (points of damage) , i.e. 12 damage
6) damagestr   -------> for in-game display purposes
7) mindmg  -------> Displays the minimum damage output you can deal
8) maxdmg  -------> Displays the maximum damage output you can deal

~Functions
-----------
1)Custom ------> Create a custom character with their own statblock
2)getstats --------> I don't know why it is still here , testing purposes
3)move ---------> Select your move
4)alive ----------> if your character is above 0 HP




* Enemy Class
---------------
(Same characteristics as above , but to call them I have added the e- in front of the original , i.e. eweapon / edamage)
9)skelname , lichname , zombname ----------> lists of possible names for opposing skeletons , liches , zombies 
10)ename ----------> all of the above as a united list , used for custom enemies

~Functions
-----------
(Same as the players' , same as before , with the e- in front of the original except move)




---Game Functions---
____________________

- main() -----------> The heart of the game

- menu() -----------> Main Menu

- info() -----------> in-game mechanisms info

- intro() -----------> self-explanatory

- custombattle() ------------> initiates a custom battle

- defaultbattle() -----------> initiates a classic battle

- select() ------------> character selection

- challenger() -------------> enemy selection

- moveoutcome(player,enemy) ------------> outcome of the moves the player selects

- emoveoutcome(player,enemy) ------------> outcome of the moves the enemy 'selects'

- showdown(player,enemy) ------------> the battle mechanism
