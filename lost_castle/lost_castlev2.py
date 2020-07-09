###Test
## Test2
### test 3
from time import sleep

health = 5
hint = 3

print('''                       



                ____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
                \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
                 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
                  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
                   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
                    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|                                                                           
                                        .___________.  ______   
                                        |           | /  __  \  
                                        `---|  |----`|  |  |  | 
                                            |  |     |  |  |  | 
                                            |  |     |  `--'  | 
                                            |__|      \______/         
            ██       ██████  ███████ ████████      ██████  █████  ███████ ████████ ██      ███████ 
            ██      ██    ██ ██         ██        ██      ██   ██ ██         ██    ██      ██      
            ██      ██    ██ ███████    ██        ██      ███████ ███████    ██    ██      █████   
            ██      ██    ██      ██    ██        ██      ██   ██      ██    ██    ██      ██      
            ███████  ██████  ███████    ██         ██████ ██   ██ ███████    ██    ███████ ███████                                                                         

                                             -|             |-
                         -|                  [-_-_-_-_-_-_-_-]                  |-
                         [-_-_-_-_-]          |             |          [-_-_-_-_-]
                          | o   o |           [  0   0   0  ]           | o   o |
                           |     |    -|       |           |       |-    |     |
                           |     |_-___-___-___-|         |-___-___-___-_|     |
                           |  o  ]              [    0    ]              [  o  |
                           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
                _____----- |     ]              [ ||||||| ]              [     |
                           |     ]              [ ||||||| ]              [     |
                       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
                      ( (__________------------_____________-------------_________) )


          ####                                                                                       #### 
          ####     Welcome to the LOST CASTLE. Here you enter and good luck with getting out alive   #### 
          ####                                                                                       ####
------------------------------------------------------------------------------------------------------------------
''')
sleep(2)
name = input("ENTER YOUR NAME ")
print('WELCOME TO THE GAME' + "," + " " + name)



def want_to_play():
    play = None
    while play not in ("Y", "N"):
        play = input('Do you want to play? (Y/N) ').lower()
        if play == 'n':
            print('Cool, see you later')
            break
        elif play == 'y':
            print('Cool, lets begin')
            char()
        else:
            print('Sorry, didnt catch that')

def char():
    char = None
    while char not in ("1", "2"):
        char = input('''


                                   {}                           
                                  .--.                           
                                 /.--.\                           \.|.|./            
                                 |====|                            /~~~\                                     
                                 |`::`|                           (/a a\)
                             .-;`\..../`;_.-^-._                  (\_-_/)   
                      /\    /  |...::..|`   :   `|                _~' '~_
                      |:'\ |   /'' ::''|   .:.   |              /`~`"Y"`~`\   
                      |\ /\;-,/\   ::  |..:::::..|             / /(_ * _)\ \ 
                     `||\ <` >  >._::_.| ':::::' |            / /  )   (  \ \ 
                      || `""`  /   ^^  |   ':'   |            \ \_/\ _ /\_/ / 
                      ||       |       \    :    /             \/_) '*' (_\/
                      ||       |        \   :   /                |       |
                      ||       |___/\___|`-.:.-`                 |       |
                      ||        \_ || _/    `                    |       |
                      ||        <_ >< _>                         |       |
                      ||        |  ||  |                         |       |
                      ||        |  ||  |                         |       |
                      ||       _\.:||:./_                        |       |
                      \/      /____/\____\                       w*W*W*W*w


                              SIR FRANI                        PRINCESS BUBU


        CHOSE YOUR HERO
        [1] SIR FRANI
        [2] PRINCESS BUBU
        ''')
        if char == '1':
            print('''YOU CHOSE SIR FRANI

                          / \ 
                          | |
                          |.|
                          |.|
                          |:|      __
                        ,_|:|_,   /  )
                          (Oo    / _I_
                           +\ \  || __|
                              \ \||___|
                                \ /.:.\-\ 
                                 |.:. /-----\ 
                                 |___|::oOo::|
                                 /   |:<_T_>:|
                                |_____\ ::: /
                                 | |  \ \:/
                                 | |   | |
                                 \ /   | \ 
                                 /_|    \_\ 

        ######  Sir Frani is king Sheldon II's hand and a fearless knight  ######
        ######  who fought a thousand battles to defend the kingdom. The   ######
        ######  reign is now under the threat of a powerful enemy and the  ######
        ######  castle is under siege. Sir Frani was captured by the enemy ######
        ######  while defending an outpost. After long days of confinement ######
        ######  and terrible tortures, Sir Frani managed to escape thanks  ######
        ######  to his astuce and great courage. Will Sir Frani manage to  ######
        ######  go back and save the castle?                               ######             
            ''')
            sleep(8)
            first_choice_frani()
        elif char == '2':
            print('YOU CHOSE PRINCESS BUBU')

        else:
            print("SORRY, I DIDN'T GET THAT. YOU MUST ENTER 1 OR 2")






def life():
    global health
    while health >= 1:
        print('You lost 1 life')
        health -= 1
        print('Now you have', health, 'life(s)')
        first_choice_frani()
        break

def hint_():
    global hint
    while hint > 0:
        hint = hint - 1
        break

def fifth_choice():
    fifth_choice = None
    while fifth_choice not in ("hide", "fight"):
        fifth_choice = input('You made it back to your castle but the castle is under siege. What do you do? You hide '
                             'and wait for backup or you fight? (fight/hide) ')
        if fifth_choice == 'fight':
            print('Great Choice! Although your army was smaller in number, thanks to your courage and lead you '
                  'managed to defeat the enemy and take back the castle.')
            print('You won the game')
        elif fifth_choice == 'hide':
            print('You decided to hide. The backup army was to far away. You fell in an ambush trying to find a place '
                  'to hide. You got captured and tortured by the enemy')
            life()
        else:
            print('Sorry, didnt catch that')


def fourth_choice():
    fourth_choice = None
    while fourth_choice not in ("mushrooms", "berries"):
        fourth_choice = input('You are hungry now. The only things you found are very suspiciously looking berries '
                              'and mushrooms. What do you eat? (mushrooms/berries) ')
        if fourth_choice == 'mushrooms':
            print('Great Choice! The berries were Deadly nightshade also known as Devil Berries.')
            fifth_choice()
        elif fourth_choice == 'berries':
            print('Sorry, you ate the Deadly nightshade also known as Devil Berries')
            life()
        else:
            print('Sorry, didnt catch that')


def third_choice():
    third_choice = None
    while third_choice not in ("fire", "tree"):
        third_choice = input('You are in the woods and its getting dark. Do you start a fire or climb a tree and '
                             'spend the night up there? (tree/fire) ')
        if third_choice == 'tree':
            print(
                'Great Choice! Spending the night on top of the tree saved your life. The wood was plenty of dangerous wild animals.')
            fourth_choice()
        elif third_choice == 'fire':
            print('Sorry, the fire drew a pack of wolves and you got eaten')
            life()
        else:
            print('Sorry, didnt catch that')


def second_choice_frani():
    second_choice_f = None
    while second_choice_f not in ("1", "2", "3", "4", "h"):
        second_choice_f = input('''


                       []|    (______
                 []|__ /       \ 
                 ||   \________/
                 ||      ___
                 ||     /_  )__
      __|\/)     ||   _/_ \____)                       #### Sir Frani is riding fast as the wind but the enemy army ####
,----`     \     ||  />=o)                             ####  army is chasing him. He found himself at a crossroads  ####
\_____      \    ||  \]__\                             #### and he doesn't know which way to go. He found a map in  ####
      `--,_/U\  B|\__/===\                             #### the stables but it's torn apart. There is as message    ####
         |UUUU\  ||_ _|_\_ \                           #### on the back of the map                                  ####
         |UUUUU\_|[,`_|__|_)
         |UUUUUU\||__/_ __|
         |UUUUUU/-(_\_____/-------,
         /UU/    |H\__\    HHHH|   \                   #### "At the crossroads follow the path named as the naitonal ####           
         |UU/    |H\  |HHHHHHH|    |\                  ####               animal of China"                           ####        
         UU      |HH\ \HHHHHHH|    | \ 
         U       |<_\,_\HHHHHH|   /   \ 
          \ (    |HHHHHHHHHHHHH   /                             #### WHAT IS CHINA'S NATIONAL ANIMAL ####  
           \ \   |=============  /    
              \ |             | |



        [1] DRAGON
        [2] LION
        [3] EAGLE
        [4] UNICORN
        [H] Take hint

        ''').lower()
        if second_choice_f == '1':
            print('Correct! You are riding down the path of the Dragon')
            third_choice_frani()
        elif second_choice_f == '2':
            print('Sorry, wrong answer, try again.')
            life()
        elif second_choice_f == '3':
            print('Sorry, wrong answer, try again.')
            life()
        elif second_choice_f == '4':
            print('Sorry, wrong answer, try again.')
            life()
        elif second_choice_f == 'h':
            if hint > 0:
                print('Alright, here is your hint. It is a mythical animal')
                hint_()
                print('Now you have', hint, 'hint(s)')
                sleep(2)
                second_choice_frani()
            else:
                print("You don't have any more hints")
                second_choice_frani()
        else:
            print('Sorry, didnt catch that')



def first_choice_frani():
    first_choice_f = None
    while first_choice_f not in ("1", "2", "3", "4", "h"):
        first_choice_f = input('''


                      {}
                     .--.
                    /.--.\                        #### Sir Frani has made it to the stables and is looking ####
                    |====|                        #### for a horse to ride back to the castle. The stables ####
                    |`::`|                        #### are locked and there is no key in sight but a sign  ####
                .-;`\..../`;-.                    #### hangs from the door 'If the door you want to unlock ####
               /  |...::...|  \                   #### the riddle you must solve'                          ####
              |   /'''  '''\   |
              ;--'\   ::   /\--;                  ####    Which is the largest island in the world?        #### 
              <__>,>._::_.<,<__>                  
              |  |/   ^^   \|  |
              \::/|        |\::/
              |||\|        |/|||
                  |___/\___| 
                   \_ || _/
                   <_ >< _>
                   |  ||  |
                   |  ||  |
                  _\.:||:./_
                 /____/\____\



        [1] Sumatra
        [2] Greenland
        [3] Great Britain
        [4] Borneo
        [H] Take hint

        ''').lower()
        if first_choice_f == '2':
            print('Correct! You unlocked the door and stole a horse! Here starts your ride back to the caslte')
            second_choice_frani()
        elif first_choice_f == '1':
            print('Sorry, wrong answer, try again.')
            life()
        elif first_choice_f == '3':
            print('Sorry, wrong answer, try again.')
            life()
        elif first_choice_f == '4':
            print('Sorry, wrong answer, try again.')
            life()
        elif first_choice_f == 'h':
            if hint > 0:
                print('Alright, here is your hint. This island is located in the Arctic Ocean')
                hint_()
                print('Now you have', hint, 'hint(s)')
                sleep(2)
                first_choice_frani()
            else:
                print("You don't have any more hints")
                first_choice_frani()
        else:
            print('Sorry, didnt catch that')




def main():
    while True:
        try:
            age = int(input("ENTER YOUR AGE "))
            break
        except ValueError:
            print('Sorry your age must be a number')
    if age < 18:
        print('Sorry mate, you are only', age, '...too young for this. See you later.')
    else:
        print('You are old enough to be legally prosecutable!')
        want_to_play()



if __name__ == "__main__":
    main()
