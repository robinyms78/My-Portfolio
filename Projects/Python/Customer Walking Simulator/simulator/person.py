import pygame
import json
import csv
from simulator import assets


class Person(pygame.sprite.Sprite):
    def __init__(self, id, handwave, emotion, gender, age, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Initialize movement
        self.move_x = 5
        self.move_y = 5

        # Create an image of the block and fill it with a color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.id = id
        self.handwave = handwave
        self.emotion = emotion
        self.gender = gender
        self.age = age
        self.color = color
        self.image.fill(self.color)

        # Draw rectangle
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Fetch rectangular object and update position of image
        self.rect = self.image.get_rect()

    def move_person(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.move_x
            #print("Person move right.", "x-coordinate: ", (self.rect.x - 500) / 100, ",", "z-coordinate: ", -(self.rect.y - 400) / 100)
        if self.rect.x > 800:  # Prevent person from moving out of boundary
            self.rect.x = 800
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.move_x
            #print("Person move left.", "x-coordinate: ", (self.rect.x - 500) / 100, ",", "z-coordinate: ", -(self.rect.y - 400) / 100)
        if self.rect.x < 200:  # Prevent person from moving out of boundary
            self.rect.x = 200
        if keys[pygame.K_UP]:
            self.rect.y -= self.move_y
            #print("Person move up.", "x-coordinate: ", (self.rect.x - 500) / 100, ",", "z-coordinate: ", -(self.rect.y - 400) / 100)
        if self.rect.y < 100:  # Prevent person from moving out of boundary
            self.rect.y = 100
        if keys[pygame.K_DOWN]:
            self.rect.y += self.move_y
            #print("Person move down.", "x-coordinate: ", (self.rect.x - 500) / 100, ",", "z-coordinate: ", -(self.rect.y - 400) / 100)
        if self.rect.y > 400:  # Prevent person from moving out of boundary
            self.rect.y = 400
        return (self.rect.x - 500) / 100, -(self.rect.y - 400) / 100

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, self.rect)

    def label_id(self, id, width):
        self.font = pygame.font.SysFont("Arial", 16, bold=True)
        self.label = self.font.render(str(id), True, assets.WHITE)
        self.image.blit(self.label, [width/3, 0])

    def get_emotion(self):
        radios = [thorny.Checker("radio"+str(i), type="radio") for i in range(4)]
        radio_pool = thorny.RadioPool(radios, first_value=radios[2], always_value=True)

    def get_mouse_movement(self):
        self.coordinate_list = []
        self.time_list = []
        self.timestamp = pygame.time.get_ticks()
        self.coordinate = pygame.mouse.get_rel()
        self.x_coordinate = self.coordinate[0]

        with open("x_coordinate.csv", "a") as csvfile:
            csvfile.write(str(self.x_coordinate) + "\n")

        with open("time.csv", "a") as csvfile:
            csvfile.write(str(self.timestamp / 100) + "\n")

        with open("x_coordinate.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.coordinate_list.append(int(row[0]))

        with open("time.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.time_list.append(float(row[0]))

        #print("x_coordinate_list:", self.coordinate_list)
        #print("time_list:", self.time_list)

        return self.x_coordinate

    def get_handwave(self):
        self.x_coordinate = self.get_mouse_movement()
        if int(self.x_coordinate) > 50:
            self.handwave = "true"
        else:
            self.handwave = "false"
        return self.handwave

    def add_person(self, id="NA", handwave="NA", emotion="NA", gender="NA", age="NA", color="NA", width="NA", height="NA"):
        self.person = Person(id, handwave, emotion, gender, age, color, width, height)
        self.person.label_id(id, 20)
        self.all_sprites_list.add(self.person)
        self.person_list.append(self.person)
        return self.person

    # Add person ID
    def add_person_ID1(self):
        self.person = self.add_person(1, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID2(self):
        self.person = self.add_person(2, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID3(self):
        self.person = self.add_person(3, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID4(self):
        self.person = self.add_person(4, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID5(self):
        self.person = self.add_person(5, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID6(self):
        self.person = self.add_person(6, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID7(self):
        self.person = self.add_person(7, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID8(self):
        self.person = self.add_person(8, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID9(self):
        self.person = self.add_person(9, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

    def add_person_ID10(self):
        self.person = self.add_person(10, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
        self.add_age()
        return self.person

















