print('''
                       /                            )
                      (                             |\
                     /|                              \\
                    //                                \\
                   ///                                 \|
                  /( \                                  )\
                  \\  \_                               //)
                   \\  :\__                           ///
                    \\     )                         // \
                     \\:  /                         // |/
                      \\ / \                       //  \
                       /)   \     ___..-'         ((  \_|
                      //     /  .'  _.'           \ \  \
                     /|       \(  _\_____          \ | /
                    (| _ _  __/          '-.       ) /.'
                     \\ .  '-.__ \          \_    / / \
                      \\_'.     > '-._   '.   \  / / /
                       \ \      \     \    \   .' /.'
                        \ \  '._ /     \  /   / .' |
                         \ \_     \_   |    .'_/ __/
                          \  \      \_ |   / /  _/ \_
                           \  \       / _.' /  /     \
                           \   |     /.'   / .'       '-,_
                            \   \  .'   _.'_/             \
               /\    /\      ) ___(    /_.'           \    |
              | _\__// \    (.'      _/               |    |
              \/_  __  /--'`    ,                   __/    /
              (_ ) /b)  \  '.   :            \___.-:_/ \__/
              /:/:  ,     ) :        (      /_.'_/-' |_ _ /
             /:/: __/\ >  __,_.----.__\    /        (/(/(/
            (_(,_/V .'/--'    _/  __/ |   /
             VvvV  //`    _.-' _.'     \   \
               n_n//     (((/->/        |   /
               '--'         ~='          \  |
                                          | |_,,,
                             snd          \  \  /
                                           '.__)
''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

# Flow Chart
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload