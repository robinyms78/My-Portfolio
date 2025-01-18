import pygame
import math
import thorpy

GRAD = math.pi / 180
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 128)
LIGHTBLUE = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 200, 200)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
TRANSPARENT = (255, 255, 255, 0)


class Asset:
    def __init__(self, width=1900, height=900):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.font = pygame.font.SysFont("mono", 24, bold=True)

    def label_origin(self, text):
        self.myfont = pygame.font.SysFont("Arial", 15, bold=True)
        self.label1 = self.myfont.render(text, True, BLACK)
        self.screen.blit(self.label1, (500,400))

    def label_axis(self, text_x, text_z):
        self.myfont = pygame.font.SysFont("Arial", 28, bold=True)
        self.label_x = self.myfont.render(text_x, True, BLACK)
        self.label_z = self.myfont.render(text_z, True, BLACK)
        self.screen.blit(self.label_x, (905, 380))
        self.screen.blit(self.label_z, (495, -10))

    def label_x_coordinates(self, text_1, text_2, text_3, text_4, text_5, text_6):
        self.myfont = pygame.font.SysFont("Arial", 15, bold=True)
        self.label1 = self.myfont.render(text_1, True, BLACK)
        self.label2 = self.myfont.render(text_2, True, BLACK)
        self.label3 = self.myfont.render(text_3, True, BLACK)
        self.label4 = self.myfont.render(text_4, True, BLACK)
        self.label5 = self.myfont.render(text_5, True, BLACK)
        self.label6 = self.myfont.render(text_6, True, BLACK)
        self.screen.blit(self.label1, (200,400))
        self.screen.blit(self.label2, (300,400))
        self.screen.blit(self.label3, (400,400))
        self.screen.blit(self.label4, (600,400))
        self.screen.blit(self.label5, (700,400))
        self.screen.blit(self.label6, (800,400))

    def label_z_coordinates(self, text_1, text_2, text_3):
        self.myfont = pygame.font.SysFont("Arial", 15, bold=True)
        label1 = self.myfont.render(text_1, True, BLACK)
        label2 = self.myfont.render(text_2, True, BLACK)
        label3 = self.myfont.render(text_3, True, BLACK)
        self.screen.blit(label1, (505,300))
        self.screen.blit(label2, (505,200))
        self.screen.blit(label3, (505,100))

    def draw_instruction_1(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 500))

    def draw_instruction_2(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 550))

    def draw_instruction_3(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 600))

    def draw_instruction_4(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 650))

    def draw_instruction_5(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 700))

    def draw_instruction_6(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 750))

    def draw_instruction_7(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 800))

    def draw_instruction_8(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (50, 850))

    def draw_text(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, BLACK)
        self.screen.blit(surface, (200, 450))

    def label_zone(self, text_1, text_2, text_3, text_4, text_5):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        fw, fh = self.zonefont.size(text_4)
        fw, fh = self.zonefont.size(text_5)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        surface3 = self.zonefont.render(text_3, True, BLACK)
        surface4 = self.zonefont.render(text_4, True, BLACK)
        surface5 = self.zonefont.render(text_5, True, BLACK)
        self.screen.blit(surface1, (460, 150))  # Passing
        self.screen.blit(surface2, (330, 325))  # Order
        self.screen.blit(surface3, (462, 255))  # Cooking
        self.screen.blit(surface4, (600, 325))  # Pickup
        self.screen.blit(surface5, (465, 360))  # Robot

    def label_coordinate_zone(self, text_1, text_2, text_3, text_4):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        fw, fh = self.zonefont.size(text_4)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        surface3 = self.zonefont.render(text_3, True, BLACK)
        surface4 = self.zonefont.render(text_4, True, BLACK)
        self.screen.blit(surface1, (980, 28))   # Passing
        self.screen.blit(surface2, (1090, 28))  # Order
        self.screen.blit(surface3, (1190, 28))  # Cooking
        self.screen.blit(surface4, (1290, 28))  # Pickup

    def label_passing_coordinates(self, text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12, text_13):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        pygame.draw.rect(self.screen, LIGHTBLUE, (1000, 45, 270, 240))
        pygame.draw.rect(self.screen, BLACK, (1000, 45, 270, 240), 4)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        fw, fh = self.zonefont.size(text_4)
        fw, fh = self.zonefont.size(text_5)
        fw, fh = self.zonefont.size(text_6)
        fw, fh = self.zonefont.size(text_7)
        fw, fh = self.zonefont.size(text_8)
        fw, fh = self.zonefont.size(text_9)
        fw, fh = self.zonefont.size(text_10)
        fw, fh = self.zonefont.size(text_11)
        fw, fh = self.zonefont.size(text_12)
        fw, fh = self.zonefont.size(text_13)
        surface0 = self.zonefont.render(text_0, True, BLACK)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        surface3 = self.zonefont.render(text_3, True, BLACK)
        surface4 = self.zonefont.render(text_4, True, BLACK)
        surface5 = self.zonefont.render(text_5, True, BLACK)
        surface6 = self.zonefont.render(text_6, True, BLACK)
        surface7 = self.zonefont.render(text_7, True, BLACK)
        surface8 = self.zonefont.render(text_8, True, BLACK)
        surface9 = self.zonefont.render(text_9, True, BLACK)
        surface10 = self.zonefont.render(text_10, True, BLACK)
        surface11 = self.zonefont.render(text_11, True, BLACK)
        surface12 = self.zonefont.render(text_12, True, BLACK)
        surface13 = self.zonefont.render(text_13, True, BLACK)
        self.screen.blit(surface0, (1010, 17))
        self.screen.blit(surface1, (1010, 50))    # (-3, 1)
        self.screen.blit(surface2, (1010, 100))   # (-3, 0)
        self.screen.blit(surface3, (1010, 150))   # (-2, 1)
        self.screen.blit(surface4, (1010, 200))   # (-2, 2)
        self.screen.blit(surface5, (1110, 50))    # (-1, 3)
        self.screen.blit(surface6, (1110, 100))   # (-1, 2)
        self.screen.blit(surface7, (1110, 150))   # (0, 3)
        self.screen.blit(surface8, (1110, 200))   # (1, 2)
        self.screen.blit(surface9, (1210, 50))    # (1, 3)
        self.screen.blit(surface10, (1210, 100))  # (2, 2)
        self.screen.blit(surface11, (1210, 150))  # (2, 1)
        self.screen.blit(surface12, (1210, 200))  # (3, 0)
        self.screen.blit(surface13, (1010, 250))  # (3, 1)

    def label_cooking_coordinates(self, text_0, text_1, text_2):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        pygame.draw.rect(self.screen, YELLOW, (1000, 340, 270, 50))
        pygame.draw.rect(self.screen, BLACK, (1000, 340, 270, 50), 4)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        surface0 = self.zonefont.render(text_0, True, BLACK)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        self.screen.blit(surface0, (1010, 312))
        self.screen.blit(surface1, (1010, 350))    # (0, 1)
        self.screen.blit(surface2, (1110, 350))    # (0, 2)

    def label_order_coordinates(self, text_0, text_1, text_2, text_3):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        pygame.draw.rect(self.screen, PINK, (1000, 440, 270, 50))
        pygame.draw.rect(self.screen, BLACK, (1000, 440, 270, 50), 4)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        surface0 = self.zonefont.render(text_0, True, BLACK)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        surface3 = self.zonefont.render(text_3, True, BLACK)
        self.screen.blit(surface0, (1010, 415))
        self.screen.blit(surface1, (1010, 450))    # (-2, 0)
        self.screen.blit(surface2, (1110, 450))    # (-1, 1)
        self.screen.blit(surface3, (1210, 450))    # (-1, 0)

    def label_pickup_coordinates(self, text_0, text_1, text_2, text_3):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        pygame.draw.rect(self.screen, GREEN, (1000, 540, 270, 50))
        pygame.draw.rect(self.screen, BLACK, (1000, 540, 270, 50), 4)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        surface0 = self.zonefont.render(text_0, True, BLACK)
        surface1 = self.zonefont.render(text_1, True, BLACK)
        surface2 = self.zonefont.render(text_2, True, BLACK)
        surface3 = self.zonefont.render(text_3, True, BLACK)
        self.screen.blit(surface0, (1010, 512))
        self.screen.blit(surface1, (1010, 550))    # (1, 0)
        self.screen.blit(surface2, (1110, 550))    # (1, 1)
        self.screen.blit(surface3, (1210, 550))    # (2, 0)

    def label_age(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (70, 30))

    def label_ID(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (35, 100))

    def label_gender(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (100, 100))

    def label_emotion(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (100, 260))

    def label_face_recognizer(self, text):
        pygame.draw.rect(self.screen, BLACK, (10, 30, 172, 430), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (18, 1))

    def label_person_tracking(self, text):
        pygame.draw.rect(self.screen, BLACK, (970, 30, 390, 390), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1100, 1))

    def label_movement(self, text):
        pygame.draw.rect(self.screen, BLACK, (970, 30, 390, 390), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1110, 270))

    def label_handwave(self, text):
        pygame.draw.rect(self.screen, BLACK, (970, 30, 390, 390), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1250, 270))

    def label_weather(self, text):
        pygame.draw.rect(self.screen, BLACK, (1380, 30, 490, 390), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1600, 1))

    def label_cloud(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1430, 30))

    def label_humidity(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1570, 30))

    def label_wind(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1750, 30))

    def label_rain(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1430, 180))

    def label_temperature(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1550, 180))

    def label_place(self, text):
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1750, 320))

    def label_JSON_output(self, text):
        pygame.draw.rect(self.screen, BLACK, (970, 460, 390, 140), 2)
        self.zonefont = pygame.font.SysFont("Arial", 24, bold=True)
        fw, fh = self.zonefont.size(text)
        surface = self.zonefont.render(text, True, BLACK)
        self.screen.blit(surface, (1115, 430))

    def draw_passing_position_coordinates(self, text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10):
        self.zonefont = pygame.font.SysFont("Arial", 14, bold=True)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        fw, fh = self.zonefont.size(text_4)
        fw, fh = self.zonefont.size(text_5)
        fw, fh = self.zonefont.size(text_6)
        fw, fh = self.zonefont.size(text_7)
        fw, fh = self.zonefont.size(text_8)
        fw, fh = self.zonefont.size(text_9)
        fw, fh = self.zonefont.size(text_10)
        surface1 = self.zonefont.render(text_0, True, WHITE)
        surface2 = self.zonefont.render(text_1, True, WHITE)
        surface3 = self.zonefont.render(text_2, True, WHITE)
        surface4 = self.zonefont.render(text_3, True, WHITE)
        surface5 = self.zonefont.render(text_4, True, WHITE)
        surface6 = self.zonefont.render(text_5, True, WHITE)
        surface7 = self.zonefont.render(text_6, True, WHITE)
        surface8 = self.zonefont.render(text_7, True, WHITE)
        surface9 = self.zonefont.render(text_8, True, WHITE)
        surface10 = self.zonefont.render(text_9, True, WHITE)
        surface11 = self.zonefont.render(text_10, True, WHITE)
        self.screen.blit(surface1, (258, 325))
        self.screen.blit(surface2, (282, 265))
        self.screen.blit(surface3, (320, 218))
        self.screen.blit(surface4, (372, 176))
        self.screen.blit(surface5, (432, 150))
        self.screen.blit(surface6, (498, 140))
        self.screen.blit(surface7, (562, 150))
        self.screen.blit(surface8, (623, 175))
        self.screen.blit(surface9, (672, 215))
        self.screen.blit(surface10, (710, 265))
        self.screen.blit(surface11, (735, 325))

    def draw_order_position_coordinates(self, text_0, text_1):
        self.zonefont = pygame.font.SysFont("Arial", 14, bold=True)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        surface1 = self.zonefont.render(text_0, True, WHITE)
        surface2 = self.zonefont.render(text_1, True, WHITE)
        self.screen.blit(surface1, (350, 355))
        self.screen.blit(surface2, (365, 315))

    def draw_cooking_position_coordinates(self, text_0, text_1, text_2, text_3, text_4):
        self.zonefont = pygame.font.SysFont("Arial", 14, bold=True)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        fw, fh = self.zonefont.size(text_2)
        fw, fh = self.zonefont.size(text_3)
        fw, fh = self.zonefont.size(text_4)
        surface1 = self.zonefont.render(text_0, True, WHITE)
        surface2 = self.zonefont.render(text_1, True, WHITE)
        surface3 = self.zonefont.render(text_2, True, WHITE)
        surface4 = self.zonefont.render(text_3, True, WHITE)
        surface5 = self.zonefont.render(text_4, True, WHITE)
        self.screen.blit(surface1, (419, 260))
        self.screen.blit(surface2, (454, 245))
        self.screen.blit(surface3, (495, 242))
        self.screen.blit(surface4, (534, 245))
        self.screen.blit(surface5, (570, 262))

    def draw_pickup_position_coordinates(self, text_0, text_1):
        self.zonefont = pygame.font.SysFont("Arial", 14, bold=True)
        fw, fh = self.zonefont.size(text_0)
        fw, fh = self.zonefont.size(text_1)
        surface1 = self.zonefont.render(text_0, True, WHITE)
        surface2 = self.zonefont.render(text_1, True, WHITE)
        self.screen.blit(surface1, (625, 315))
        self.screen.blit(surface2, (639, 350))


class MapDrawer:
    def __init__(self, width=1400, height=900):
        pygame.display.set_caption("Simulator for Event Detector (Omotenashi Engine ver1.2)")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(WHITE)  # Fill background white
        self.font = pygame.font.SysFont("mono", 24, bold=True)
        self.asset = Asset()

    def paint(self):
        # Draw outer arc
        pygame.draw.circle(self.background, LIGHTBLUE, (500, 400), 300)
        pygame.draw.circle(self.background, BLACK, (500, 400), 300, 4)
        # Draw middle arc-1
        pygame.draw.circle(self.background, BLACK, (500, 400), 250, 2)
        # Draw middle arc-2
        pygame.draw.circle(self.background, GREEN, (500, 400), 200)
        pygame.draw.circle(self.background, BLACK, (500, 400), 200, 4)
        self.draw_segment_2()
        self.draw_segment_1()
        # Draw middle arc-3
        pygame.draw.circle(self.background, BLACK, (500, 400), 150, 2)
        # Draw inner arc
        pygame.draw.circle(self.background, RED, (500, 400), 100)
        pygame.draw.circle(self.background, BLACK, (500, 400), 100, 4)
        # Draw rectangle to slice arc
        pygame.draw.rect(self.background, WHITE, (100, 400, 1000, 800))
        # Draw z axis
        pygame.draw.line(self.background, BLACK, (500, 400), (500, 25), 3)
        pygame.draw.polygon(self.background, BLACK, ((490, 30), (510, 30), (500, 20)))
        # Draw x axis
        pygame.draw.line(self.background, BLACK, (890, 400), (200, 400), 3)
        pygame.draw.polygon(self.background, BLACK, ((890, 390), (890, 410), (900, 400)))
        # Draw Baseline
        pygame.draw.line(self.background, BLACK, (890, 400), (200, 400), 4)
        # Draw line-1
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(15 / 180 * math.pi), 400 - 300 * math.sin(15 * GRAD)), 1)
        # Draw line-2
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(30 / 180 * math.pi), 400 - 300 * math.sin(30 * GRAD)), 1)
        # Draw line-3
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(45 / 180 * math.pi), 400 - 300 * math.sin(45 * GRAD)), 1)
        # Draw line-4
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(60 / 180 * math.pi), 400 - 300 * math.sin(60 * GRAD)), 1)
        # Draw line-5
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(75 / 180 * math.pi), 400 - 300 * math.sin(75 * GRAD)), 1)
        # Draw line-6
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(105 / 180 * math.pi), 400 - 300 * math.sin(105 * GRAD)), 1)
        # Draw line-7
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(120 / 180 * math.pi), 400 - 300 * math.sin(120 * GRAD)), 1)
        # Draw line-8
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(135 / 180 * math.pi), 400 - 300 * math.sin(135 * GRAD)), 1)
        # Draw line-9
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(150 / 180 * math.pi), 400 - 300 * math.sin(150 * GRAD)), 1)
        # Draw line-10
        pygame.draw.line(self.background, BLACK, (500, 400),
                         (500 - 300 * math.cos(165 / 180 * math.pi), 400 - 300 * math.sin(165 * GRAD)), 1)

    def draw_segment_1(self):
        cx, cy, r = 500, 400, 200
        self.p = [(cx, cy)]
        for n in range(0, 226):
            self.x = cx + int(r*math.cos(n * GRAD))
            self.y = cy + int(r*math.sin(n * GRAD))
            self.p.append((self.x, self.y))
        self.p.append((cx,cy))
        if len(self.p) > 2:
            pygame.draw.polygon(self.background, PINK, self.p)
            pygame.draw.polygon(self.background, BLACK, self.p, 5)

    def draw_segment_2(self):
        cx, cy, r = 500, 400, 200
        self.p = [(cx, cy)]
        for n in range(0, 316):
            self.x = cx + int(r*math.cos(n * GRAD))
            self.y = cy + int(r*math.sin(n * GRAD))
            self.p.append((self.x, self.y))
        self.p.append((cx,cy))
        if len(self.p) > 2:
            pygame.draw.polygon(self.background, YELLOW, self.p)
            pygame.draw.polygon(self.background, BLACK, self.p, 5)

    def draw_passing_position(self):
        pygame.draw.circle(self.background, DARKBLUE, (260, 335), 8)
        pygame.draw.circle(self.background, DARKBLUE, (285, 275), 8)
        pygame.draw.circle(self.background, DARKBLUE, (323, 227), 8)
        pygame.draw.circle(self.background, DARKBLUE, (375, 185), 8)
        pygame.draw.circle(self.background, DARKBLUE, (435, 160), 8)
        pygame.draw.circle(self.background, DARKBLUE, (500, 150), 8)
        pygame.draw.circle(self.background, DARKBLUE, (565, 160), 8)
        pygame.draw.circle(self.background, DARKBLUE, (625, 185), 8)
        pygame.draw.circle(self.background, DARKBLUE, (675, 225), 8)
        pygame.draw.circle(self.background, DARKBLUE, (715, 275), 8)
        pygame.draw.circle(self.background, DARKBLUE, (740, 335), 8)

    def draw_order_position(self):
        pygame.draw.circle(self.background, RED, (355, 365), 8)
        pygame.draw.circle(self.background, RED, (370, 325), 8)

    def draw_cooking_position(self):
        pygame.draw.circle(self.background, ORANGE, (425, 270), 8)
        pygame.draw.circle(self.background, ORANGE, (460, 255), 8)
        pygame.draw.circle(self.background, ORANGE, (500, 250), 8)
        pygame.draw.circle(self.background, ORANGE, (540, 255), 8)
        pygame.draw.circle(self.background, ORANGE, (575, 270), 8)

    def draw_pickup_position(self):
        pygame.draw.circle(self.background, DARKGREEN, (630, 325), 8)
        pygame.draw.circle(self.background, DARKGREEN, (645, 360), 8)

    def draw_map(self):
        self.asset.label_origin("0")
        self.asset.label_axis("x", "z")
        self.asset.label_x_coordinates("-3", "-2", "-1", "1", "2", "3")
        self.asset.label_z_coordinates("1", "2", "3")
        self.asset.draw_instruction_1("1. Use KEYPAD NUMBER KEYS to enter person's age.")
        self.asset.draw_instruction_2("2. Use MOUSE to select person's ID.")
        self.asset.draw_instruction_3("3. Use MOUSE to select person's gender & emotion.")
        self.asset.draw_instruction_4("4. Use MOUSE to select person's zone.")
        self.asset.draw_instruction_5("5. Use NUMBER KEYS (1|2|3|4|5|6|7|8|9) & ARROW KEYS(Left|Right|Up|Down) or MOUSE to move person.")
        self.asset.draw_instruction_6("6. Use NUMBER KEYS (1|2|3|4|5|6|7|8|9) & MOUSE BUTTON(Left|Right) or MOUSE to wave person's hand.")
        self.asset.draw_instruction_7("7. Use MOUSE to select weather information.")
        self.asset.draw_instruction_8("8. Press ESC to quit.")
        self.asset.label_zone("Passing", "Order", "Cooking", "Pickup", "Robot")
        self.asset.label_coordinate_zone("Passing", "Order", "Cooking", "Pickup")
        self.asset.label_movement("Movement")
        self.asset.label_handwave("Handwave")
        self.asset.label_ID("ID")
        self.asset.label_age("Age")
        self.asset.label_emotion("Emotion")
        self.asset.label_gender("Gender")
        self.asset.label_face_recognizer("Face Recognition")
        self.asset.label_person_tracking("Person Tracking")
        self.asset.label_weather("Weather")
        self.asset.label_cloud("Cloud")
        self.asset.label_humidity("Humidity")
        self.asset.label_wind("Wind")
        self.asset.label_rain("Rain")
        self.asset.label_temperature("Temperature")
        self.asset.label_place("Place")
        #self.asset.label_JSON_output("JSON Output")
        self.asset.draw_passing_position_coordinates("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
        self.asset.draw_order_position_coordinates("12", "13")
        self.asset.draw_cooking_position_coordinates("14", "15", "16", "17", "18")
        self.asset.draw_pickup_position_coordinates("19", "20")


class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super(pygame.sprite.Sprite, self).__init__()

        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class RobotWall(pygame.sprite.Sprite):

    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()

        self.image1 = pygame.Surface((30, 30)).convert_alpha()
        self.image2 = pygame.Surface((30, 30)).convert_alpha()
        self.image3 = pygame.Surface((30, 30)).convert_alpha()
        self.image4 = pygame.Surface((30, 30)).convert_alpha()
        self.image5 = pygame.Surface((30, 30)).convert_alpha()
        self.image6 = pygame.Surface((30, 30)).convert_alpha()
        self.image7 = pygame.Surface((30, 30)).convert_alpha()
        self.image8 = pygame.Surface((30, 30)).convert_alpha()
        self.image9 = pygame.Surface((30, 30)).convert_alpha()
        self.image10 = pygame.Surface((30, 30)).convert_alpha()
        self.image11 = pygame.Surface((30, 30)).convert_alpha()
        self.image1.fill(TRANSPARENT)
        self.image2.fill(TRANSPARENT)
        self.image3.fill(TRANSPARENT)
        self.image4.fill(TRANSPARENT)
        self.image5.fill(TRANSPARENT)
        self.image6.fill(TRANSPARENT)
        self.image7.fill(TRANSPARENT)
        self.image8.fill(TRANSPARENT)
        self.image9.fill(TRANSPARENT)
        self.image10.fill(TRANSPARENT)
        self.image11.fill(TRANSPARENT)
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()
        self.rect4 = self.image4.get_rect()
        self.rect5 = self.image5.get_rect()
        self.rect6 = self.image6.get_rect()
        self.rect7 = self.image7.get_rect()
        self.rect8 = self.image8.get_rect()
        self.rect9 = self.image9.get_rect()
        self.rect10 = self.image10.get_rect()
        self.rect11 = self.image11.get_rect()
        self.rect1.center = (420, 385)
        self.rect2.center = (430, 365)
        self.rect3.center = (440, 355)
        self.rect4.center = (455, 335)
        self.rect5.center = (470, 325)
        self.rect6.center = (500, 320)
        self.rect7.center = (530, 325)
        self.rect8.center = (550, 340)
        self.rect9.center = (560, 355)
        self.rect10.center = (575, 370)
        self.rect11.center = (580, 385)