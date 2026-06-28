print(r"""

    ____________________________________________________________________

 / \-----     ---------  -----------     -------------- ------    ----\

 \_/__________________________________________________________________/

 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|

 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|

 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |

 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|

 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|

 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|

 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|

 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |

 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|

 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|

 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |

 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|

 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|

 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |

 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|

 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|

 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |

 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|

 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|

 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|

 / \----- ----- ------------  ------- ----- -------  --------  -------\

 \_/__________________________________________________________________/

""")

print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")



Q1 = (input("You stand at a crossroad. The 'right' path leads to an abandoned theme park with strange, nostalgic music. The 'left' path leads to a dark, silent forest. Which do you choose? Type 'left' or 'right' ").lower())

if Q1 == "left":
  Q2 = (input(" You walk through the dark trees and reach an infinite pool with white tiles. The treasure lies beyond the water. Type 'swim' or 'wait'").lower())

  # --- اتاق بزرگ (Q2) ---
  if Q2 == "wait":
    Q3 = (input(" You were patient! The water parts, revealing a glass bridge to the final hall. There are three giant doors here: Type 'Red' or 'Blue' 'Yellow' ").lower())  

    # --- اتاق کوچک (Q3) ---
    if Q3 == "red":
      print("game over")  
    elif Q3 == "yellow":  
      print("You wake up! 📼🏆 You Win!")
    elif Q3 == "blue":  
      print("game over")
    else:    
      # این else برای کلمات اشتباه در Q3 است
      print("game over")
    # --- پایان اتاق کوچک ---

  else:  
    # این else برای کلمات اشتباه در Q2 است
    print("game over")
  # --- پایان اتاق بزرگ ---

else:
  print("Fall into a hole. \ngame over.")


#Wrong shit
# # if Q1 == "left":
# #   Q2 = (input(" ?Type 'swim' or 'wait'").lower())
# #   if Q2 == "swim":
# #     print("Attacked by trouit.\nGame over.")
# #   if Q2 == "wait":
# #     Q3 = (input(" ?Type 'Red' or 'Blue' 'Yellow' ").lower())  
# #     if Q3 == "red":
# #       print("game over")  
# #     elif Q3 == "yellow":  
# #       print("win")
# #     elif Q3 == "blue":  
# #       print("game over")
# #   else:  
# #     print("game over")  
# #     else:    
# #       print("game over")
# # else:
# #   print("Fall into a hole. \ngame over.") 

