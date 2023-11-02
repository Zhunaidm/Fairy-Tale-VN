# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pleb = Character("Pleb")
define bingus = Character("Bingus")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg abandoned_scene
    play music "soft_rain.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pleb neutral at left

    # These display lines of dialogue.

    pleb "You've created a new Ren'Py game."

    pleb "Once you add a story, pictures, and music, you can release it to the world!"


    show bingus neutral at right

    bingus "STFU Pleb"

    pleb "You're a bitch Bingus"
    bingus "No u"

menu:
    "True Fam":
        play sound "<from 0 to 1>pleb_cry.mp3"
        show pleb sad at left
        pleb "bro..."
        jump post_choice
    "Dem Bingus why you such a fucker":
        play sound "owned.mp3"          
        bingus "It how it do be"
        jump bingus_death
        

label bingus_death:
    play sound "bonk.mp3"    
    call screen_flash
    show bingus dead at right    
    bingus "dem..."
    show pleb devious at left
    pleb "hehe"



label post_choice:
    



    # This ends the game.

    return
