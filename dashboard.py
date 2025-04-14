import pygame
import sys
from datetime import datetime

pygame.init()

# Set up screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Standby Dashboard")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (140, 146, 172)

# Fonts
big_font = pygame.font.SysFont(None, 120)
small_font = pygame.font.SysFont(None, 50)
tiny_font = pygame.font.SysFont(None, 30)

# Get message from argument
custom_message = sys.argv[1] if len(sys.argv) > 1 else ""

running = True
while running:
    screen.fill(black)

    # Time & date
    now = datetime.now()
    time_str = now.strftime("%I:%M:%S %p")
    date_str = now.strftime("%A, %B %d, %Y")

    # Render text
    text_standby = big_font.render("STAND BY MODE", True, white)
    text_custom = small_font.render(custom_message, True, white)
    text_date = small_font.render(date_str, True, white)
    text_channels = small_font.render("Channel 1: Google TV  |  Channel 2: Switch  |  Channel 3: Standby", True, white)
    text_madeby = tiny_font.render("MADE BY CJC - POWERED BY RASPBERRY PI 3", True, gray)

    # Get screen size
    sw, sh = screen.get_size()

    # Blit text to screen
    screen.blit(text_standby, (sw//2 - text_standby.get_width()//2, 100))
    screen.blit(text_custom, (sw//2 - text_custom.get_width()//2, 220))
    screen.blit(text_date, (sw//2 - text_date.get_width()//2, 300))
    screen.blit(text_channels, (sw//2 - text_channels.get_width()//2, 380))
    screen.blit(text_madeby, (sw - text_madeby.get_width() - 20, sh - text_madeby.get_height() - 20))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
           event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

pygame.quit()
