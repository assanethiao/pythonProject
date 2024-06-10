import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joyeux Anniversaire!")

# Couleurs
background_color = (10, 10, 50)  # Bleu nuit
bubble_colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]  # Différentes couleurs pour les bulles
star_color = (255, 255, 255)  # Blanc

# Paramètres des bulles et des étoiles
num_bubbles = 50
num_stars = 100
bubble_min_radius = 10
bubble_max_radius = 50
bubble_speed = 2
star_speed = 1

# Génération des bulles et des étoiles
def generate_bubbles(num_bubbles):
    bubbles = []
    for _ in range(num_bubbles):
        radius = random.randint(bubble_min_radius, bubble_max_radius)
        x = random.randint(radius, width - radius)
        y = random.randint(radius, height - radius)
        color = random.choice(bubble_colors)
        bubbles.append([x, y, radius, color])
    return bubbles

def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, width)
        y = random.randint(0, height)
        stars.append([x, y])
    return stars

# Affichage du texte
def display_text():
    screen.blit(text1, (width//2 - text1.get_width()//2, height//2 - text1.get_height()))
    screen.blit(text2, (width//2 - text2.get_width()//2, height//2 + text1.get_height()//2))
    screen.blit(text3, (width//2 - text3.get_width()//2, height//2 + text1.get_height()))
    screen.blit(text4, (width//2 - text4.get_width()//2, height//2 + text1.get_height() + text3.get_height()))

# Mise à jour des étoiles
def update_stars(stars):
    for star in stars:
        pygame.draw.circle(screen, star_color, (star[0], star[1]), 2)
        star[1] += star_speed
        if star[1] > height:
            star[1] = 0
            star[0] = random.randint(0, width)

# Mise à jour des bulles
def update_bubbles(bubbles):
    for bubble in bubbles:
        pygame.draw.circle(screen, bubble[3], (bubble[0], bubble[1]), bubble[2])
        bubble[1] -= bubble_speed
        if bubble[1] < -bubble[2]:
            bubble[1] = height + bubble[2]
            bubble[0] = random.randint(bubble[2], width - bubble[2])

# Générer les bulles et les étoiles
bubbles = generate_bubbles(num_bubbles)
stars = generate_stars(num_stars)

# Police de texte
font = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 48)
text1 = font.render("Joyeux Anniversaire!!!!!!!!", True, (0, 255, 255))
text2 = font_small.render("Daba Jooooooooooooooooooo", True, (255, 0, 255))
text3 = font_small.render("Que cette journée soit remplie de bonheur 🎈", True, (255, 255, 0))
text4 = font_small.render("Et de moments magiques, de moments inoubliables ! 🎈", True, (255, 0, 0))

# Boucle principale
running = True
while running:
    screen.fill(background_color)
    
    display_text()
    update_stars(stars)
    update_bubbles(bubbles)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
