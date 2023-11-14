
define MC = Character("You")
define L = Character("Luzia", image ="Girl")

# Defining images, there has to be a better way to do this
image girl neutral:
        'Girl neutral.png'
        zoom 0.9

image girl angry:
        'Girl angry.png'
        zoom 0.9

image girl happy:
        'Girl happy.png'
        zoom 0.9

image girl laugh:
        'Girl laugh.png'
        zoom 0.9

image girl pout:
        'Girl pout.png'
        zoom 0.9

image girl sad:
        'Girl sad.png'
        zoom 0.9

image girl shocked:
        'Girl shocked.png'
        zoom 0.9

image girl sleepy:
        'Girl sleepy.png'
        zoom 0.9

image girl smile:
        'Girl smile.png'
        zoom 0.9

image girl smile2:
        'Girl smile2.png'
        zoom 0.9

image girl smug:
        'Girl smug.png'
        zoom 0.9


# The game starts here.

label start:

        "And so it begins..."
        "....."
        "..."

        show bg road with Dissolve(0.75)

        MC "Bro, I'm bored as shit."
        "He says, but there is no one around to hear him."
        "..."
        MC "I should try making a visual novel."
        MC "I mean, how hard can it be?"

        play music "bgm excited.mp3" volume 0.1

        show girl smile2 with Dissolve(0.75)

        "???" "Hi..."
        MC "Hey..."
        MC "Do I know you?"
        "???" "You can call me Luzia."
        show girl sleepy with Dissolve(0.1)
        L  "You look bored as shit."
        MC "I am bored as shit!"
        hide girl with Dissolve(0.5)
        "....."
        "They talk about being bored, as shit."
        show girl smug with Dissolve(0.5)
        L "Okay!"
        L "Hear me out..."
        L "Choose one of these doors, then we go explore."
        hide girl with Dissolve(0.5)
        "Three doors appear out of seemingly nowhere."
        "While under normal circumstances, this would be strange..."
        "you are bored as shit anyway."
        "You decide to go along."

        menu:
                "You look at the doors in front of you."

                "Door 1 looks like a water level...":
                        jump water_level

                "Door 2 sounds like its got some sort of market going on behind it.":
                        jump market_level

                "Door 3 is eery and quiet.":
                        jump nighttime_level


label water_level:
        play music "bgm underwater.mp3" fadeout 4.0 fadein 1.5 volume 0.1
        show bg deep sea with Dissolve(1.5)

        "You enter some strange under water city."
        show girl smug with Dissolve(0.5)
        "..."
        L "Pretty cool, huh?"


label market_level:
        play music "bgm market.mp3" fadeout 1.5 fadein 1.0 volume 0.1
        show bg street market with Pixellate(1.5,7)
        "..."
        "The air is thick with the aroma
        of exotic spices and the lively
        chatter of merchants haggling with customers."
        show girl sad with Dissolve(0.5)
        L "Well, now what..."