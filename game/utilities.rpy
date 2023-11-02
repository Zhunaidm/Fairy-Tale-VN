image red_screen = "red_screen.jpg"

label screen_flash:
    show red_screen with dissolve:
        xzoom 1.5 yzoom 1.5
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.1
    return