# Welcome to Mars
# by Peter Siri

# I have learned to write this script through this book: Mission Python by Sean McManus
# Images by Rafael Pimenta

# variable_name = value
WIDTH = 1275
HEIGHT = 1000
player_x = 525
player_y = 312

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))

def gameLoop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

clock.schedule_interval(gameLoop, 0.03)
