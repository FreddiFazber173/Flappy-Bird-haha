import pygame
import sys
from button import ImageButton

pygame.init()

width = 960
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Флапи бёрд из кыргызстана")
background = pygame.image.load("R.jpg")

def main_menu():
    start_button = ImageButton(width/2-(252/2)), 150, 252, 74, "играть", "green_fon.jpg", "click.mp"
    settings_button = ImageButton(width/2-(252/2)), 250, 252, 74, "настройки", "green_fon.jpg", "click.mp"
    exit_button = ImageButton(width/2-(252/2)), 350, 252, 74, "выйти", "green_fon.jpg",  "click.mp"
    pass
def settigs_menu():
    pass
def new_game():
    pass
if __name__ == "__main__":
    main_menu()