####Dominick Sileo UCLA Python Final Project 
####Text-Based Adventure Game:
####Indiana Damien and the Riddles of Ra

import random

player_name = ""
treasure_bag = []

def game_start():
    global player_name
    print("\nWelcome to our adventure, 'Indiana Damien and the Riddles of Ra!'\n\nThis is a story about a legendary treasure hunter named Indiana Damien! He travels all around the world finding mysterious treasures in ancient pyramids, tombs, and ruins.\n\nToday we find him in the burial chamer of Ra, the ancient Egyptian God of the Sun! He is in search of Ra's secret treasures, but the tomb is also cursed and full of booby traps!\n\nCan our hero Damien make it out of the tomb with Ra's treasure or will he be trapped there forever? Let's find out!\n\nAre you ready to begin your adventure? Please type ok")
    game_start = input()

    while game_start != "ok": 
       print("\n\nYou're not ready?! Well, you better hurry up and get ready for your adventure! Please type ok.")
       game_start = input()

###Input Player Name
    player_name =  input("What is your name?")
    if player_name == "Damien":
        print(f"\nYour name is {player_name}?! THE {player_name}?! The legendary treasure hunter?? I can't believe it!! Ok. Ok. Calm down. It's just a game...")
    else:
        print(f"\nYour name is...{player_name}...? Who is that...? I wanted Damien, the legendary treasure hunter to play! Oh, well. I guess you will do...")
     

###CHAMBER OF RA - LEVEL 1
def chamber_room():
    global treasure_bag
    chamber_treasures = ["red jewels" , "blue jewels" , "green jewels"]

    print(f"\n\nAfter searching for hours in Ra's ancient pyramid, {player_name} and his trusty dog Bento find a secret lever that opens a hidden door. The room is pitch black. You enter into the dark room and almost as soon as you walk through the door, you hear a loud SLAM behind you! The door is locked shut and you can't get back out!!\n\n{player_name} knows that there is always a secret way to open trap doors, though! So, you light your torch to see inside. After lighting your torch, you suddenly realize that THIS is the burial chamber of Ra!\n\nHis chamber is littered with gold, jewels, and ancient treasures as far as the eye can see. Mounds of gold coins are piled up like the dunes of the deserts of Egypt and ancient hierogliphics are painted along the wall telling the story of this ancient god.\n\nOf endless amounts of ancient treasures that make this room shine in a gold light, you notice three that stand out above the rest: Three pairs of jewels; one red, one blue, and the other green. These jewels are embeded in the eye pieces of three giant statues of cobra snakes! These are Ancient Eyes of Ra! Magic jewels from his favorite magic pet cobra snakes!\n\nBringing back just one pair of these will make you rich and famous beyond your wildest dreams!\n\nYou ready your knife to try to pry off one of the jewels, but have a strange feeling these could be booby trapped...")
    jewels_picked = ""
   
    while jewels_picked != "blue":
        jewels_picked = input("\nWhich jewel color do you want to take: red, blue, or green?")

        #JEWELS
        if jewels_picked == "red":
            if "red jewels" in chamber_treasures:
                print(f"\n\nYou walk up to the large cobra statue with the red jewels for eyes. You climb to the top of it and with a prying of {player_name}'s knife, you loosen the red jewels and put it into your pocket.\n\nSuddenly, the chamber starts to shake! Like an earthquake rocking the ground! Where the two red jewels once were you see two golden eyes with two black slits peering right at you! Then the statue begins to move! This is no statue! It's a GIANT cobra snake! It's alive and REALLY hungry!\n\nIt cocks it's head back, fangs glistening in the light of your torch, and in a flash snaps at you and swallows you up! You scream out for Bento to save you, but he just pees on the wall and doesn't seem to listen. Silly dog.\n\nLuckily, you don't taste very good and the snake spits you out after sloshing you in it's gross, wet mouth for 5 minutes. You fall on the floor and are covered in snake slime. Bento comes over and licks the slime off your face. Yuck!\n\nThe snake then yawns and goes back to sleep. You put the jewels in your treasure bag.")
                treasure_bag.append("red jewels")
                chamber_treasures.remove("red jewels")
            else:
                print("\n\nYou already have these jewels!")
            
        elif jewels_picked == "green":
            if "green jewels" in chamber_treasures:
                print(f"\n\nYou walk up to the large cobra statue with the green jewels for eyes. You climb to the top of it and with a prying of {player_name}'s knife, you loosen the green jewels and put it into your pocket.\n\nThe statue itself suddenly starts to rumble. It's giant stone mouth slowly opens and a MILLION cobra snakes start to fall out of it's mouth!\n\nAs the statue rumbles, you fall off and land on your stomach! OUCH!\n\nAs soon as you land, you realize you land on the tail of a very large and very scary cobra snake! You look at each other right in the eye and are too afraid to move. He suddenly leaps at you and tries to bite you right in the nose, but you flip backwards and take out your trusty whip to scare him away! That was a close one!!\n\nBento was hiding scared the whole time. He is scardy pup. You put the jewels in your treasure bag.")  
                treasure_bag.append("green jewels")
                chamber_treasures.remove("green jewels")
            else:
                print("\n\nYou already have these jewels!")
            
        elif jewels_picked == "blue":
            print(f"\n\nYou walk up to the large cobra statue with the blue jewels for eyes. You climb to the top of it and with a prying of {player_name}'s knife, you loosen the blue jewels and slowly put them in your pocket.\n\nWorried this will spring a trap. You close your eyes in fear, but only hear a small click then the sound of a door opening.\n\nIt's the exit to the chamber! You put the jewels in your treasure bag.")
            treasure_bag.append("blue jewels")
            chamber_treasures.remove("blue jewels")
        
        else:
            print("\n\nThose aren't the jewel colors! Let's try again.")


    print("\n\nYou can get out now! Lucky you! Please type ok to leave.")
    next_room = input()
    while next_room != "ok": 
       print("\n\nI think we should leave the room before it gets too dangerous! Type ok!")
       next_room = input()
       
### THE RIDDLES OF RA - LEVEL 2

#SHADOW GHOST RIDDLE       
def shadow_question():
    
    print(f"\n\nThe Shadow Ghost looks at {player_name} and let's out a spooky laugh and says, 'Answer this riddle and the treasure is yoursssss!' ")
    shadow_choice = input("Who is the Egyptian God of the Dead? osiris, anubis, or dominick? Please check your spelling!")
    if shadow_choice == "osiris":
        print("\n\nThe Shadow Ghost hisses and says, 'That is correct!' ")
    elif shadow_choice == "dominick":
        print("\n\nThe Shadow Ghost laughs and says, 'DOMINICK?! THAT guy?! Not him! He is pretty cool, though. Try againnnnnn!' ")
    elif shadow_choice == "anubis":
        print("\n\nThe Shadow Ghost thinks really hard for a minute and says, 'Hmmmmmm. Anubis? Hmmmmm. You know, that is REALLY close. Maybe you should try again.' ")
    else:
        print("\n\nThat's not one of the choices I asked you! Try again!")
    return shadow_choice

#FIRE GHOST RIDDLE
def fire_question():
    print(f"\n\nThe Fire Ghost looks at {player_name} spins around and moonwalk, 'Answer this riddle and the treasure is yours. Ah-heee-hee!' ")
    fire_choice = input("\n\nWhat do you call an Egpytian King? penguin, pharaoh, prince? Please check your spelling!")
    if fire_choice == "penguin":
        print("\nThe Fire Ghost looks confused and then says,'A penguin?! It's way too hot in Egypt for them! Try again!' ")
    elif fire_choice == "pharaoh":
        print("\n\nThe Fire Ghost let's screams 'Heee-hee!' and says, 'That is correct! YEOW!!!' ")   
    elif fire_choice == "prince":
        print("\n\nThe Fire Ghost smiles at you and says, 'Incorrect, but I love his music!' ")
    else:
        print("\nThat's not one of the choices I asked you! Try again!")
    return fire_choice
    
#LIGHTNING GHOST RIDDLE
def lightning_question():
    print(f"\n\nThe Lighting Ghost looks at {player_name} and Bento and in a deep, heavy breathing, Darth Vader voice asks says, 'SHHHHHH-HAAAAA, answer this riddle and you may have this magic treasure.' ")
    lightning_choice = input("What do you call the giant triangle-shaped buildings in Egypt? pizza hut, damien's house, pyramid? Please check your spelling! ")
    if lightning_choice == "damien's house":
        print("\n\nThe Lightining Ghost says, 'Damien's house?! You wish! Try again!' ")
    elif lightning_choice == "pizza hut":
        print("\n\nThe Lightning Ghost rubs his lightning belly and says, 'Mmmmmm. I love pizza. Let's go get some...NO! WAIT! WRONG ANSWER! Try again!' ")
    elif lightning_choice == "pyramid":
        print("\n\nThe Lightining Ghost looks surprised and says, 'That's correct! How did you know that?! Did you use the force or something?!' You get one of our treasures! ")
    else:
        print("\n\nThat's not one of the choices I asked you! Try again!")
    return lightning_choice
                    

#GHOST ROOM LISTS    
def ghost_room():
    global treasure_bag
    ghosts = ["fire", "shadow" , "lightning"]
    ghost_treasures = ["Jeweled Spear of Ra", "Golden Idol of Ra", "Diamond Mask of Ra"]
    print(f"\nAs {player_name} and Bento escape the room they suddenly realize the room had changed. What was once an empty, dusty hall now has three different treasure chests in each corner of the room. Lucky!!\n\nAs soon as you take a step towards the treasure chest, the door closes behind you. Bento lets out a bark! He didn't like the loud bang it made! Poor boy.\n\nYou look over at the treasure chests and see three ghosts appear out of thin air and hover above them. 'Only he who has collected all three treasures of Ra and answered our riddles will be able to escape this room!' boast the ghosts.\n\nThe ghosts then cast a magic spell and huge walls creating a giant maze now surround the entire room!\n\n{player_name} and Bento may be trapped here forever! I think you need to find the ghosts and answer their riddles!")

    collected_ghost_treasures = ""
   
    while ghost_treasures:
        collected_ghost_treasures = input("Which ghost will you go to? shadow, fire, lightning.")

        #SHADOW GHOST TREASURE
        if collected_ghost_treasures == "shadow":
            if "shadow" in ghosts:
                print(f"\n\n{player_name} and Bento continues down the path of the winding maze. After twists, turns, and a million dead ends, they find a treasure box and the Shadow Ghost vanishing back and forth in the air! Is this a ninja ghost?!\n\nBento tries to jump on it and kiss it, but falls through the ghost because he is just a ghost. The ghost gives Bento a ninja bandana though. It seems like they are friends.") 
                shadow_choice = shadow_question()
                while shadow_choice !="osiris":
                    shadow_choice = shadow_question()
                treasure_index = random.randint(0, len(ghost_treasures)-1)
                treasure_bag.append(ghost_treasures[treasure_index])
                ghost_treasures.remove(ghost_treasures[treasure_index])
                ghosts.remove("shadow")
                        
        #FIRE GHOST TREASURE
        if collected_ghost_treasures == "fire":
            if "fire" in ghosts:
                print(f"\n\n{player_name} and Bento continues down the path of the winding maze. After twists, turns, and a million dead ends, they find a treasure box and the Fire Ghost flying and dancing above it!\n\nHe is twirling like Michael Jackson and listening to 'Remember the Time' on his ghost radio! He is even wearing the costume from the music video!\n\nYou and Bento start to have a dance party with him.\n\nWait! Now is no time to dance! You have to get the treasure and get out of here!")
                fire_choice = fire_question()
                while fire_choice !="pharaoh":
                    fire_choice = fire_question()
                treasure_index = random.randint(0, len(ghost_treasures)-1)
                treasure_bag.append(ghost_treasures[treasure_index])
                ghost_treasures.remove(ghost_treasures[treasure_index])
                ghosts.remove("fire")
        
        #LIGHTNING GHOST TREASURE
        if collected_ghost_treasures == "lightning":
            if "lightning" in ghosts:
                print(f"\n\n{player_name} and Bento continues down the path of the winding maze. After twists, turns, and a million dead ends, they find a treasure box and with a flash of light and loud thunder, BAM! The lightning ghost appears!!\n\nHe kind of looks like Darth Vader and can use lightning magic! You ask to see if he can do his lightning magic and he puts on a fireworks show for you and Bento.\n\nBento doesn't like the loud noises. He hides behind the treasure chest and The Lightning Ghost apologizes and rubs his belly. The shocks tickle Bento. Silly dog.") 
                lighting_choice = lightning_question()
                while lighting_choice !="pyramid":
                    lighting_choice = lightning_question()
                treasure_index = random.randint(0, len(ghost_treasures)-1)
                treasure_bag.append(ghost_treasures[treasure_index])
                ghost_treasures.remove(ghost_treasures[treasure_index])
                ghosts.remove("lightning")
                    
    print(f"\n\nAfter collecting your treasures, the exit to the room opens. You are free!\n\nAs you walk to the door, the three ghosts fly up in the air and laugh. 'We are not letting you out of here that easily,' proclaim the ghosts. All of a sudden, the room starts to shake! Another earthquake!?\n\nBento starts barking and runs out of the room. What is he running from?? You look behind you and see a giant bolder coming right at you! It's going to crush you if you don't run!!\n\nYou run away as fast as you can, holding your favorite hat on your head! Just as you arrive to the door, the ground underneath you breaks and shows a massive pit of spikes! You have to think quick, that giant bolder is going to make a {player_name} sandwich!\n\nYou grab your trusty whip and whip it above you onto a old Ra statue and swing over the spikes and fly straight through the door!\n\nYour hat flies off, but you are able to reach back in the doorway and grab it just before the boulder flattens it! Phew!! ")
    print("\n\nYou are home free and have escaped the tomb of Ra! The warm sun feels great on your face after being in a dark, cold tomb. Bento is letting out a big smile and rolling on his back looking for belly rubs.")

###PUT A TIMER HERE
###GUARDS OF RA - LEVEL 3
#def guard_room():
#    
#    #ROOM INTRO
#    print(f"After narrowly escaping the last room, {player_name} and Bento enters into yet another chamber you haven't seen before. Is this pyramid haunted?! The rooms keep changing!! \n You notice that the room has 4 very large sarcophagus' mounted against the wall. 2 on each side. At the end of the hall is a wide open door with the sun shining through! Your escape! \n However, in the center of a room you see another TREASURE! It's so beautiful and shiny that you cannot take your eyes off it. This can't be a good idea to take it! \n  {player_name} walks over to the booby trap...I mean...treasure and lifts it from it's mantle. The sarcophagus' then start to rumble and at the same time all open! 4 huge mummy guards with very large golden armor, shields, and spears come out of the sarcophagus'. You run and hide! \n The 4 guards are now looking for you!)
#        
#    #PLAYER ACTION 
#    action_dict = {"peek":"You see the 4 mummy guards slowly moving around and searching for you. They are very big, scary, and definitely very stinky. However, they are not very fast and not very smart. Attacking them might be dangerous, but you may be able to sneak quietly towards the door. Bento starts to lick his crotch.",
#                    "sneak":"You slowly tip toe out of your hiding spot. The mummy guards haven't seem to notice you and you can see the light of day shining through the door. You start to tip toe towards the door.",
#                    "attack":"You pull out your whip and with a loud crack alert the guards to your presence. You aren't afraid of stinky mummies! Even if they ARE guards! You lift your whip and with a loud crack in the air whip the closest guard next to you!"}
#    
#    #GUARD LOOPS
#    while True:
#        action = input("What do you do? attack, peek, sneak ?")
#            print(actions_dict[action])
#            if action == "sneak":
#                print(f"You are going to make it! Suddenly, all of the TREASURE you have in your bag starts to rattle together! \n The guards hear this and look over at you! They let out a loud roar and start running towards you! Yikes! \n You run as fast as you can towards the door! One guard takes his spear and jumps at you with it! {player_name} slides underneath his legs and the guard misses you! The guard falls over and starts to cry! You don't have time to turn around, though! It seems Bento already ran through the door and left you alone to fight the guards. So, you run through the exit door to saftey!")
#                print(f"{player_name} feels the warm desert sun on their face. You know you are home free. You look in your treasure bag and find all of this TREASURE sparkling in the sun. This was a great adventure!")
#                return 
#            if action == "attack":
#                print("Your whip lashes at the guard, but seems to do no damage! He is a super mummy!! So, you run away and hide again. Bento is now snuggling with the guards and whining. They seem to like him and forget where you hid. They pet Bento and start to look for you again. Bento comes over to you smiling. Good dog.")
#        


game_start()
chamber_room()
ghost_room()
#guard_room()

print("\nYou have escaped with the treasures of Ra and have won the game! Your treasures are:")
for item in treasure_bag:
    print(item)

print(f"\nSee you next time, {player_name}!!")