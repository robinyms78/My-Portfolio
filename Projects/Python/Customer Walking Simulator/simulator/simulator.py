import pygame
import math
import json
import itertools
import thorpy
from simulator import assets
from simulator.assets import MapDrawer
from simulator.person import Person
from simulator.assets import Wall
from simulator.assets import RobotWall
from simulator.weather import Weather


class Simulator(object):

    def __init__(self, map_drawer, fps=60):
        self.map_drawer = map_drawer
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.person_list = []
        self.weather = Weather(place="NA", cloud="NA", humidity="NA", wind="NA", rain="NA", temperature="NA")
        self.all_sprites_list = pygame.sprite.Group()  # Create a list to contain all the sprites
        self.wall = Wall(600, 2, 200, 400)
        self.robotwall = RobotWall()

    def run(self):
        self.map_drawer.paint()
        self.map_drawer.draw_passing_position()
        self.map_drawer.draw_order_position()
        self.map_drawer.draw_cooking_position()
        self.map_drawer.draw_pickup_position()

        # Create inserter for age
        self.inserter1 = thorpy.Inserter(name="Age: ", value=" ", size=(25, 20))
        self.box1 = thorpy.Box(elements=[self.inserter1])
        self.menu1 = thorpy.Menu(self.box1)
        thorpy.store(self.box1, x=5, y=1, align="left")
        self.menu1.surface = self.map_drawer.screen

        #Create radio buttons for person ID
        self.button1 = thorpy.make_button(" ID1 ", func=self.add_person_ID1)  # Person ID1
        self.button2 = thorpy.make_button(" ID2 ", func=self.add_person_ID2)  # Person ID2
        self.button3 = thorpy.make_button(" ID3 ", func=self.add_person_ID3)  # Person ID3
        self.button4 = thorpy.make_button(" ID4 ", func=self.add_person_ID4)  # Person ID4
        self.button5 = thorpy.make_button(" ID5 ", func=self.add_person_ID5)  # Person ID5
        self.button6 = thorpy.make_button(" ID6 ", func=self.add_person_ID6)  # Person ID6
        self.button7 = thorpy.make_button(" ID7 ", func=self.add_person_ID7)  # Person ID7
        self.button8 = thorpy.make_button(" ID8 ", func=self.add_person_ID8)  # Person ID8
        self.button9 = thorpy.make_button(" ID9 ", func=self.add_person_ID9)  # Person ID9
        self.button10 = thorpy.make_button("ID10", func=self.add_person_ID10)  # Person ID10
        self.box2 = thorpy.Box(elements=[self.button1, self.button2, self.button3, self.button4, self.button5,
                                        self.button6, self.button7, self.button8, self.button9, self.button10])
        self.menu2 = thorpy.Menu(self.box2)
        thorpy.store(self.box2, x=5, y=1, align="left")
        for element in self.menu1.get_population():
           element.surface = self.map_drawer.screen

        # Create radio buttons for gender
        self.button1 = thorpy.make_button("  Male  ", func=self.add_gender_male)  # Male
        self.button2 = thorpy.make_button("Female", func=self.add_gender_female)  # Female
        self.box3 = thorpy.Box(elements=[self.button1, self.button2])
        self.menu3 = thorpy.Menu(self.box3)
        thorpy.store(self.box3, x=5, y=1, align="left")
        for element in self.menu3.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for emotion
        self.button3 = thorpy.make_button("  Happy  ", func=self.add_emotion_happy)  # Happy
        self.button4 = thorpy.make_button("    Sad    ", func=self.add_emotion_sad)  # Sad
        self.button5 = thorpy.make_button(" Surprise", func=self.add_emotion_surprise)  # Surprise
        self.button6 = thorpy.make_button("   Angry  ", func=self.add_emotion_angry)  # Angry
        self.button7 = thorpy.make_button(" Neutral  ", func=self.add_emotion_neutral)  # Neutral
        self.box4 = thorpy.Box(elements=[self.button3, self.button4, self.button5, self.button6, self.button7])
        self.menu4 = thorpy.Menu(self.box4)
        thorpy.store(self.box4, x=5, y=1, align="left")
        for element in self.menu4.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for passing zone
        self.button8 = thorpy.make_button(" 1 ", func=self.add_position_1)  # Passing (1)
        self.button9 = thorpy.make_button(" 2 ", func=self.add_position_2)  # Passing (2)
        self.button10 = thorpy.make_button(" 3 ", func=self.add_position_3)  # Passing (3)
        self.button11 = thorpy.make_button(" 4 ", func=self.add_position_4)  # Passing (4)
        self.button12 = thorpy.make_button(" 5 ", func=self.add_position_5)  # Passing (5)
        self.button13 = thorpy.make_button(" 6 ", func=self.add_position_6)  # Passing (6)
        self.button14 = thorpy.make_button(" 7 ", func=self.add_position_7)  # Passing (7)
        self.button15 = thorpy.make_button(" 8 ", func=self.add_position_8)  # Passing (8)
        self.button16 = thorpy.make_button(" 9 ", func=self.add_position_9)  # Passing (9)
        self.button17 = thorpy.make_button("10", func=self.add_position_10)  # Passing (10)
        self.button18 = thorpy.make_button("11", func=self.add_position_11)  # Passing (11)
        self.box5 = thorpy.Box(elements=[self.button8, self.button9, self.button10, self.button11, self.button12,
                                         self.button13, self.button14, self.button15, self.button16, self.button17,
                                         self.button18])
        self.box5.set_main_color(assets.LIGHTBLUE)
        self.menu5 = thorpy.Menu(self.box5)
        thorpy.store(self.box5, x=5, y=1, align="left")
        for element in self.menu5.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for order zone
        self.button19 = thorpy.make_button("12", func=self.add_position_12)  # Order (12)
        self.button20 = thorpy.make_button("13", func=self.add_position_13)  # Order (13)
        self.box6 = thorpy.Box(elements=[self.button19, self.button20])
        self.box6.set_main_color(assets.PINK)
        self.menu6 = thorpy.Menu(self.box6)
        thorpy.store(self.box6, x=5, y=1, align="left")
        for element in self.menu6.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for cooking zone
        self.button21 = thorpy.make_button("14", func=self.add_position_14)  # Cooking (14)
        self.button22 = thorpy.make_button("15", func=self.add_position_15)  # Cooking (15)
        self.button23 = thorpy.make_button("16", func=self.add_position_16)  # Cooking (16)
        self.button24 = thorpy.make_button("17", func=self.add_position_17)  # Cooking (17)
        self.button25 = thorpy.make_button("18", func=self.add_position_18)  # Cooking (18)
        self.box7 = thorpy.Box(elements=[self.button21, self.button22, self.button23, self.button24, self.button25])
        self.box7.set_main_color(assets.YELLOW)
        self.menu7 = thorpy.Menu(self.box7)
        thorpy.store(self.box7, x=5, y=1, align="left")
        for element in self.menu7.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for pickup zone
        self.button26 = thorpy.make_button("19", func=self.add_position_19)  # Pickup (19)
        self.button27 = thorpy.make_button("20", func=self.add_position_20)  # Pickup (20)
        self.box8 = thorpy.Box(elements=[self.button26, self.button27])
        self.box8.set_main_color(assets.GREEN)
        self.menu8 = thorpy.Menu(self.box8)
        thorpy.store(self.box8, x=5, y=1, align="left")
        for element in self.menu8.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for handwave
        self.button28 = thorpy.make_button("Wave", func=self.add_handwave_true)  # True
        self.button29 = thorpy.make_button(" Stop ", func=self.add_handwave_false)  # False
        self.box9 = thorpy.Box(elements=[self.button28, self.button29])
        self.menu9 = thorpy.Menu(self.box9)
        thorpy.store(self.box9, x=5, y=1, align="left")
        for element in self.menu9.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for human movement
        self.button30 = thorpy.make_button("LU", func=self.move_left_up)  # Move left-up
        self.button31 = thorpy.make_button(" L ", func=self.move_left)  # Move left
        self.button32 = thorpy.make_button("LD", func=self.move_left_down)  # Move left-down
        self.button33 = thorpy.make_button(" U ", func=self.move_up)  # Move up
        self.button34 = thorpy.make_button("    ")  # Dummy button
        self.button35 = thorpy.make_button(" D ", func=self.move_down)  # Move down
        self.button36 = thorpy.make_button("RU", func=self.move_right_up)  # Move right-up
        self.button37 = thorpy.make_button(" R ", func=self.move_right)  # Move right
        self.button38 = thorpy.make_button("RD", func=self.move_right_down)  # Move right-down
        self.box10 = thorpy.Box(elements=[self.button30, self.button31, self.button32])
        self.box11 = thorpy.Box(elements=[self.button33, self.button34, self.button35])
        self.box12 = thorpy.Box(elements=[self.button36, self.button37, self.button38])
        self.menu10 = thorpy.Menu(self.box10)
        self.menu11 = thorpy.Menu(self.box11)
        self.menu12 = thorpy.Menu(self.box12)
        thorpy.store(self.box10, x=5, y=1, align="left")
        thorpy.store(self.box11, x=5, y=1, align="left")
        thorpy.store(self.box12, x=5, y=1, align="left")
        for element in self.menu10.get_population():
            element.surface = self.map_drawer.screen
        for element in self.menu11.get_population():
            element.surface = self.map_drawer.screen
        for element in self.menu12.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for weather information
        self.button39 = thorpy.make_button("       Clear        ", func=self.add_clear)
        self.button40 = thorpy.make_button("Partially cloudy", func=self.add_partially_cloudy)
        self.button41 = thorpy.make_button("      Cloudy       ", func=self.add_cloudy)

        self.button42 = thorpy.make_button("           Dry          ", func=self.add_dry)
        self.button43 = thorpy.make_button("        Humid        ", func=self.add_humid)
        self.button44 = thorpy.make_button("Extremely humid", func=self.add_extremely_humid)

        self.button45 = thorpy.make_button("      Light wind      ", func=self.add_light_wind)
        self.button46 = thorpy.make_button(" Gentle moderate ", func=self.add_gentle_moderate_wind)
        self.button47 = thorpy.make_button("     Fresh wind      ", func=self.add_fresh_wind)
        self.button48 = thorpy.make_button("    Strong wind     ", func=self.add_strong_wind)
        self.button49 = thorpy.make_button("           Gale          ", func=self.add_gale)
        self.button50 = thorpy.make_button("    Whole gale      ", func=self.add_whole_gale)
        self.button51 = thorpy.make_button("      Hurricane       ", func=self.add_hurricane)

        self.button52 = thorpy.make_button("       No rain      ", func=self.add_no_rain)
        self.button53 = thorpy.make_button("     Light rain    ", func=self.add_light_rain)
        self.button54 = thorpy.make_button(" Moderate rain ", func=self.add_moderate_rain)
        self.button55 = thorpy.make_button("    Heavy rain   ", func=self.add_heavy_rain)
        self.button56 = thorpy.make_button("  Intense rain   ", func=self.add_intense_rain)
        self.button57 = thorpy.make_button(" Torrential rain ", func=self.add_torrential_rain)

        self.box13 = thorpy.Box(elements=[self.button39, self.button40, self.button41])
        self.box14 = thorpy.Box(elements=[self.button42, self.button43, self.button44])
        self.box15 = thorpy.Box(elements=[self.button45, self.button46, self.button47, self.button48, self.button49, self.button50, self.button51])
        self.box16 = thorpy.Box(elements=[self.button52, self.button53, self.button54, self.button55, self.button56, self.button57])

        self.menu13 = thorpy.Menu(self.box13)
        self.menu14 = thorpy.Menu(self.box14)
        self.menu15 = thorpy.Menu(self.box15)
        self.menu16 = thorpy.Menu(self.box16)
        thorpy.store(self.box13, x=5, y=1, align="left")
        thorpy.store(self.box14, x=5, y=1, align="left")
        thorpy.store(self.box15, x=5, y=1, align="left")
        thorpy.store(self.box16, x=5, y=1, align="left")
        for element in self.menu13.get_population():
            element.surface = self.map_drawer.screen
        for element in self.menu14.get_population():
            element.surface = self.map_drawer.screen
        for element in self.menu15.get_population():
            element.surface = self.map_drawer.screen
        for element in self.menu16.get_population():
            element.surface = self.map_drawer.screen

        # Create radio buttons for temperature information
        self.button58 = thorpy.make_button("Very cold", func=self.add_very_cold)
        self.button59 = thorpy.make_button("    Cold   ", func=self.add_cold)
        self.button60 = thorpy.make_button("   Good   ", func=self.add_good)
        self.button61 = thorpy.make_button("    Hot     ", func=self.add_hot)
        self.button62 = thorpy.make_button("Very hot ", func=self.add_very_hot)
        self.box17 = thorpy.Box(elements=[self.button58, self.button59, self.button60, self.button61, self.button62])
        self.menu17 = thorpy.Menu(self.box17)
        thorpy.store(self.box17, x=5, y=1, align="left")
        for element in self.menu17.get_population():
            element.surface = self.map_drawer.screen

        # Create inserter for place
        self.inserter2 = thorpy.Inserter(name="Place: ", value=" ", size=(75, 20))
        self.box18 = thorpy.Box(elements=[self.inserter2])
        self.menu18 = thorpy.Menu(self.box18)
        thorpy.store(self.box18, x=5, y=1, align="left")
        self.menu18.surface = self.map_drawer.screen

        # Create radio buttons for JSON output
        #self.button30 = thorpy.make_button("Age & Gender Output", func=self.get_json_age_gender)
        #self.button31 = thorpy.make_button("Emotion Output", func=self.get_json_emotion)
        #self.button32 = thorpy.make_button("Position Output", func=self.get_json_reid)
        #self.box11 = thorpy.Box(elements=[self.button30, self.button31, self.button32])
        #self.menu11 = thorpy.Menu(self.box11)
        #thorpy.store(self.box11, x=5, y=1, align="left")
        #for element in self.menu11.get_population():
        #    element.surface = self.map_drawer.screen

        # temp_fix
        #keyboard_handlers = [
        #    'move_person',
        #    'move_person_keypad'
        #]

        #handler_iterator = itertools.cycle(keyboard_handlers)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        running = False
                    if keys[pygame.K_F1]:
                        self.add_person(1, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F2]:
                        self.add_person(2, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F3]:
                        self.add_person(3, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F4]:
                        self.add_person(4, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F5]:
                        self.add_person(5, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F6]:
                        self.add_person(6, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F7]:
                        self.add_person(7, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F8]:
                        self.add_person(8, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                    if keys[pygame.K_F9]:
                        self.add_person(9, "False", "Neutral", "Female", "20", assets.DARKBLUE, 20, 20)
                        self.add_age()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_1]:
                            person = self.person_list[0]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_1]:
                            person = self.person_list[0]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_2]:
                            person = self.person_list[1]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_2]:
                            person = self.person_list[1]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_3]:
                            person = self.person_list[2]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_3]:
                            person = self.person_list[2]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_4]:
                            person = self.person_list[3]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_4]:
                            person = self.person_list[3]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_5]:
                            person = self.person_list[4]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_5]:
                            person = self.person_list[4]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_6]:
                            person = self.person_list[5]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_6]:
                            person = self.person_list[5]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_7]:
                            person = self.person_list[6]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_7]:
                            person = self.person_list[6]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_8]:
                            person = self.person_list[7]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_8]:
                            person = self.person_list[7]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                    if event.button == 1:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_9]:
                            person = self.person_list[8]
                            print("Person waves!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "True"
                    if event.button == 3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_9]:
                            person = self.person_list[8]
                            print("Person not waving!")
                            person.handwave = pygame.mouse.get_pos()[0]
                            person.handwave = "False"
                self.menu1.react(event)
                self.menu2.react(event)
                self.menu3.react(event)
                self.menu4.react(event)
                self.menu5.react(event)
                self.menu6.react(event)
                self.menu7.react(event)
                self.menu8.react(event)
                self.menu9.react(event)
                self.menu10.react(event)
                self.menu11.react(event)
                self.menu12.react(event)
                self.menu13.react(event)
                self.menu14.react(event)
                self.menu15.react(event)
                self.menu16.react(event)
                self.menu17.react(event)
                self.menu18.react(event)

            #for person, handler in zip(self.all_sprites_list, handler_iterator):
            #    getattr(person, handler)()
            #    person.draw(self.map_drawer.screen)

            # Move selected person using keyboard
            for person in self.person_list:
                person.draw(self.map_drawer.screen)
                self.move_select_person()
                if person.rect.colliderect(self.wall.rect):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect1):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect2):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect3):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect4):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect5):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect6):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect7):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect8):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect9):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect10):
                    print("Collision!")
                    self.person_list.remove(person)
                if person.rect.colliderect(self.robotwall.rect11):
                    print("Collision!")
                    self.person_list.remove(person)

            self.all_sprites_list.update()  # Update the person's position
            milliseconds = self.clock.tick(self.fps)
            self.map_drawer.asset.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                    self.clock.get_fps(), " " * 5, self.playtime))
            self.playtime += milliseconds / 1000.0
            self.map_drawer.draw_map()
            self.get_json_reid()
            self.get_json_emotion()
            self.get_json_age_gender()
            self.get_json_weather()
            self.box1.set_topleft((50, 60))
            self.box2.set_topleft((20, 130))
            self.box3.set_topleft((100, 130))
            self.box4.set_topleft((100, 290))
            self.box5.set_topleft((1000, 60))
            self.box6.set_topleft((1100, 60))
            self.box7.set_topleft((1200, 60))
            self.box8.set_topleft((1300, 60))
            self.box9.set_topleft((1270, 300))
            self.box10.set_topleft((1100, 300))
            self.box11.set_topleft((1140, 300))
            self.box12.set_topleft((1180, 300))
            self.box13.set_topleft((1400, 60))
            self.box14.set_topleft((1550, 60))
            self.box15.set_topleft((1710, 60))
            self.box16.set_topleft((1400, 210))
            self.box17.set_topleft((1570, 210))
            self.box18.set_topleft((1710, 350))
            self.box1.blit()
            self.box2.blit()
            self.box3.blit()
            self.box4.blit()
            self.box5.blit()
            self.box6.blit()
            self.box7.blit()
            self.box8.blit()
            self.box9.blit()
            self.box10.blit()
            self.box11.blit()
            self.box12.blit()
            self.box13.blit()
            self.box14.blit()
            self.box15.blit()
            self.box16.blit()
            self.box17.blit()
            self.box18.blit()
            self.box1.update()
            self.box2.update()
            self.box3.update()
            self.box4.update()
            self.box5.update()
            self.box6.update()
            self.box7.update()
            self.box8.update()
            self.box9.update()
            self.box10.update()
            self.box11.update()
            self.box12.update()
            self.box13.update()
            self.box14.update()
            self.box15.update()
            self.box16.update()
            self.box17.update()
            self.box18.update()
            pygame.display.flip()
            self.map_drawer.screen.blit(self.map_drawer.background, (0, 0))
            self.map_drawer.screen.blit(self.wall.image, (self.wall.rect.x, self.wall.rect.y))
            self.map_drawer.screen.blit(self.robotwall.image1, (self.robotwall.rect1.x, self.robotwall.rect1.y))
            self.map_drawer.screen.blit(self.robotwall.image2, (self.robotwall.rect2.x, self.robotwall.rect2.y))
            self.map_drawer.screen.blit(self.robotwall.image3, (self.robotwall.rect3.x, self.robotwall.rect3.y))
            self.map_drawer.screen.blit(self.robotwall.image4, (self.robotwall.rect4.x, self.robotwall.rect4.y))
            self.map_drawer.screen.blit(self.robotwall.image5, (self.robotwall.rect5.x, self.robotwall.rect5.y))
            self.map_drawer.screen.blit(self.robotwall.image6, (self.robotwall.rect6.x, self.robotwall.rect6.y))
            self.map_drawer.screen.blit(self.robotwall.image7, (self.robotwall.rect7.x, self.robotwall.rect7.y))
            self.map_drawer.screen.blit(self.robotwall.image8, (self.robotwall.rect8.x, self.robotwall.rect8.y))
            self.map_drawer.screen.blit(self.robotwall.image9, (self.robotwall.rect9.x, self.robotwall.rect9.y))
            self.map_drawer.screen.blit(self.robotwall.image10, (self.robotwall.rect10.x, self.robotwall.rect10.y))
            self.map_drawer.screen.blit(self.robotwall.image11, (self.robotwall.rect11.x, self.robotwall.rect11.y))

        pygame.quit()

    def add_person(self, id="NA", handwave="NA", emotion="NA", gender="NA", age="NA", color="NA", width="NA", height="NA"):
         self.person = Person(id, handwave, emotion, gender, age, color, width, height)
         self.person.label_id(id, 20)
         self.all_sprites_list.add(self.person)
         self.person_list.append(self.person)
         return self.person

    def move_select_person(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.person = self.person_list[0]
            self.person.move_person()
        if keys[pygame.K_2]:
            self.person = self.person_list[1]
            self.person.move_person()
        if keys[pygame.K_3]:
            self.person = self.person_list[2]
            self.person.move_person()
        if keys[pygame.K_4]:
            self.person = self.person_list[3]
            self.person.move_person()
        if keys[pygame.K_5]:
            self.person = self.person_list[4]
            self.person.move_person()
        if keys[pygame.K_6]:
            self.person = self.person_list[5]
            self.person.move_person()
        if keys[pygame.K_7]:
            self.person = self.person_list[6]
            self.person.move_person()
        if keys[pygame.K_8]:
            self.person = self.person_list[7]
            self.person.move_person()
        if keys[pygame.K_9]:
            self.person = self.person_list[8]
            self.person.move_person()

    def move_left_up(self):
        self.person.rect.x -= 5
        self.person.rect.y -= 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_up(self):
        self.person.rect.y -= 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_right_up(self):
        self.person.rect.x += 5
        self.person.rect.y -= 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_right(self):
        self.person.rect.x += 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_right_down(self):
        self.person.rect.x += 5
        self.person.rect.y += 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_left(self):
        self.person.rect.x -= 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_left_down(self):
        self.person.rect.x -= 5
        self.person.rect.y += 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def move_down(self):
        self.person.rect.y += 5
        return (self.person.rect.x - 500) / 100, -(self.person.rect.y - 400) / 100

    def add_position(self):
        self.zone = input("Enter zone number (order - 1 | cooking - 2 | pickup - 3 | passing - 4): ")
        if self.zone == "2":
            self.x_coordinate = input("Enter x position: ")
            self.z_coordinate = input("Enter z position: ")
            if self.x_coordinate == "0" and self.z_coordinate == "1":
                self.person.rect.x = 500
                self.person.rect.y = 300
            if self.x_coordinate == "0" and self.z_coordinate == "2":
                self.person.rect.x = 500
                self.person.rect.y = 200
        elif self.zone == "1":
            self.x_coordinate = input("Enter x position: ")
            self.z_coordinate = input("Enter z position: ")
            if self.x_coordinate == "-2" and self.z_coordinate == "0":
                self.person.rect.x = 300
                self.person.rect.y = 400
            if self.x_coordinate == "-1" and self.z_coordinate == "1":
                self.person.rect.x = 400
                self.person.rect.y = 300
            if self.x_coordinate == "-1" and self.z_coordinate == "0":
                self.person.rect.x = 400
                self.person.rect.y = 400
        elif self.zone == "3":
            self.x_coordinate = input("Enter x position: ")
            self.z_coordinate = input("Enter z position: ")
            if self.x_coordinate == "1" and self.z_coordinate == "0":
                self.person.rect.x = 600
                self.person.rect.y = 400
            if self.x_coordinate == "1" and self.z_coordinate == "1":
                self.person.rect.x = 600
                self.person.rect.y = 300
            if self.x_coordinate == "2" and self.z_coordinate == "0":
                self.person.rect.x = 700
                self.person.rect.y = 400
        elif self.zone == "4":
            self.x_coordinate = input("Enter x position: ")
            self.z_coordinate = input("Enter z position: ")
            if self.x_coordinate == "-3" and self.z_coordinate == "1":
                self.person.rect.x = 200
                self.person.rect.y = 300
            if self.x_coordinate == "-3" and self.z_coordinate == "0":
                self.person.rect.x = 200
                self.person.rect.y = 400
            if self.x_coordinate == "-2" and self.z_coordinate == "1":
                self.person.rect.x = 300
                self.person.rect.y = 300
            if self.x_coordinate == "-2" and self.z_coordinate == "2":
                self.person.rect.x = 300
                self.person.rect.y = 200
            if self.x_coordinate == "-1" and self.z_coordinate == "3":
                self.person.rect.x = 400
                self.person.rect.y = 100
            if self.x_coordinate == "-1" and self.z_coordinate == "2":
                self.person.rect.x = 400
                self.person.rect.y = 200
            if self.x_coordinate == "0" and self.z_coordinate == "3":
                self.person.rect.x = 500
                self.person.rect.y = 100
            if self.x_coordinate == "1" and self.z_coordinate == "2":
                self.person.rect.x = 600
                self.person.rect.y = 200
            if self.x_coordinate == "1" and self.z_coordinate == "3":
                self.person.rect.x = 600
                self.person.rect.y = 100
            if self.x_coordinate == "2" and self.z_coordinate == "2":
                self.person.rect.x = 700
                self.person.rect.y = 200
            if self.x_coordinate == "2" and self.z_coordinate == "1":
                self.person.rect.x = 700
                self.person.rect.y = 300
            if self.x_coordinate == "3" and self.z_coordinate == "0":
                self.person.rect.x = 800
                self.person.rect.y = 400
            if self.x_coordinate == "3" and self.z_coordinate == "1":
                self.person.rect.x = 800
                self.person.rect.y = 300
        return self.person.rect.x, self.person.rect.y

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

    # Cooking zone
    def add_position_0_1(self):
        self.person.rect.x = 500
        self.person.rect.y = 300
        return self.person.rect.x, self.person.rect.y

    def add_position_0_2(self):
        self.person.rect.x = 500
        self.person.rect.y = 200
        return self.person.rect.x, self.person.rect.y

    # Order zone
    def add_position_minus2_0(self):
        self.person.rect.x = 300
        self.person.rect.y = 400
        return self.person.rect.x, self.person.rect.y

    def add_position_minus1_1(self):
        self.person.rect.x = 400
        self.person.rect.y = 300
        return self.person.rect.x, self.person.rect.y

    def add_position_minus1_0(self):
        self.person.rect.x = 400
        self.person.rect.y = 400
        return self.person.rect.x, self.person.rect.y

    # Pickup zone
    def add_position_1_0(self):
        self.person.rect.x = 600
        self.person.rect.y = 400
        return self.person.rect.x, self.person.rect.y

    def add_position_1_1(self):
        self.person.rect.x = 600
        self.person.rect.y = 300
        return self.person.rect.x, self.person.rect.y

    def add_position_2_0(self):
        self.person.rect.x = 700
        self.person.rect.y = 400
        return self.person.rect.x, self.person.rect.y

    # Passing zone
    def add_position_1(self):
        self.person.rect.x = 258
        self.person.rect.y = 325
        return self.person.rect.x, self.person.rect.y

    def add_position_2(self):
        self.person.rect.x = 282
        self.person.rect.y = 265
        return self.person.rect.x, self.person.rect.y

    def add_position_3(self):
        self.person.rect.x = 320
        self.person.rect.y = 218
        return self.person.rect.x, self.person.rect.y

    def add_position_4(self):
        self.person.rect.x = 372
        self.person.rect.y = 176
        return self.person.rect.x, self.person.rect.y

    def add_position_5(self):
        self.person.rect.x = 432
        self.person.rect.y = 150
        return self.person.rect.x, self.person.rect.y

    def add_position_6(self):
        self.person.rect.x = 498
        self.person.rect.y = 140
        return self.person.rect.x, self.person.rect.y

    def add_position_7(self):
        self.person.rect.x = 562
        self.person.rect.y = 150
        return self.person.rect.x, self.person.rect.y

    def add_position_8(self):
        self.person.rect.x = 623
        self.person.rect.y = 175
        return self.person.rect.x, self.person.rect.y

    def add_position_9(self):
        self.person.rect.x = 672
        self.person.rect.y = 215
        return self.person.rect.x, self.person.rect.y

    def add_position_10(self):
        self.person.rect.x = 710
        self.person.rect.y = 265
        return self.person.rect.x, self.person.rect.y

    def add_position_11(self):
        self.person.rect.x = 735
        self.person.rect.y = 325
        return self.person.rect.x, self.person.rect.y

    def add_position_12(self):
        self.person.rect.x = 350
        self.person.rect.y = 355
        return self.person.rect.x, self.person.rect.y

    def add_position_13(self):
        self.person.rect.x = 365
        self.person.rect.y = 315
        return self.person.rect.x, self.person.rect.y

    def add_position_14(self):
        self.person.rect.x = 419
        self.person.rect.y = 260
        return self.person.rect.x, self.person.rect.y

    def add_position_15(self):
        self.person.rect.x = 454
        self.person.rect.y = 245
        return self.person.rect.x, self.person.rect.y

    def add_position_16(self):
        self.person.rect.x = 495
        self.person.rect.y = 242
        return self.person.rect.x, self.person.rect.y

    def add_position_17(self):
        self.person.rect.x = 534
        self.person.rect.y = 245
        return self.person.rect.x, self.person.rect.y

    def add_position_18(self):
        self.person.rect.x = 570
        self.person.rect.y = 262
        return self.person.rect.x, self.person.rect.y

    def add_position_19(self):
        self.person.rect.x = 625
        self.person.rect.y = 315
        return self.person.rect.x, self.person.rect.y

    def add_position_20(self):
        self.person.rect.x = 639
        self.person.rect.y = 350
        return self.person.rect.x, self.person.rect.y

    def add_emotion(self):
        emotion = input("Enter emotion (Happy - 1 | Sad - 2 | Surprise - 3 | Angry = 4 | Neutral = 5): ")
        if emotion == "1":
            self.person.emotion = "Happy"
        if emotion == "2":
            self.person.emotion = "Sad"
        if emotion == "3":
            self.person.emotion = "Surprise"
        if emotion == "4":
            self.person.emotion = "Angry"
        if emotion == "5":
            self.person.emotion = "Neutral"
        return self.person.emotion

    def add_emotion_happy(self):
        self.person.emotion = "Happy"
        print("Happy!")
        return self.person.emotion

    def add_emotion_sad(self):
        self.person.emotion = "Sad"
        print("Sad!")
        return self.person.emotion

    def add_emotion_surprise(self):
        self.person.emotion = "Surprise"
        print("Surprise!")
        return self.person.emotion

    def add_emotion_angry(self):
        self.person.emotion = "Angry"
        print("Angry!")
        return self.person.emotion

    def add_emotion_neutral(self):
        self.person.emotion = "Neutral"
        print("Neutral!")
        return self.person.emotion

    def add_gender(self):
        gender = input("Enter gender (Male - 1 | Female - 2): ")
        if gender == "1":
            self.person.gender = "Male"
        if gender == "2":
            self.person.gender = "Female"
        return self.person.gender

    def add_gender_male(self):
        self.person.gender = "Male"
        return self.person.gender

    def add_gender_female(self):
        self.person.gender = "Female"
        return self.person.gender

    def add_age(self):
        self.person.age = self.inserter1.get_value()
        print("Age:", self.person.age)
        return self.person.age

    def add_handwave_true(self):
        self.person.handwave = "True"
        return self.person.handwave

    def add_handwave_false(self):
        self.person.handwave = "False"
        return self.person.handwave

    def add_light_wind(self):
        self.weather.wind = "Light wind"
        return self.weather.wind

    def add_gentle_moderate_wind(self):
        self.weather.wind = "Gentle moderate wind"
        return self.weather.wind

    def add_fresh_wind(self):
        self.weather.wind = "Fresh wind"
        return self.weather.wind

    def add_strong_wind(self):
        self.weather.wind = "Strong wind"
        return self.weather.wind

    def add_gale(self):
        self.weather.wind = "Gale"
        return self.weather.wind

    def add_whole_gale(self):
        self.weather.wind = "Whole gale"
        return self.weather.wind

    def add_hurricane(self):
        self.weather.wind = "Hurricane"
        return self.weather.wind

    def add_clear(self):
        self.weather.cloud = "Clear"
        return self.weather.cloud

    def add_partially_cloudy(self):
        self.weather.cloud = "Partially cloudy"
        return self.weather.cloud

    def add_cloudy(self):
        self.weather.cloud = "Cloudy"
        return self.weather.cloud

    def add_dry(self):
        self.weather.humidity = "Dry"
        return self.weather.humidity

    def add_humid(self):
        self.weather.humidity = "Humid"
        return self.weather.humidity

    def add_extremely_humid(self):
        self.weather.humidity = "Extremely humid"
        return self.weather.humidity

    def add_no_rain(self):
        self.weather.rain = "No rain"
        return self.weather.rain

    def add_light_rain(self):
        self.weather.rain = "Light rain"
        return self.weather.rain

    def add_moderate_rain(self):
        self.weather.rain = "Moderate rain"
        return self.weather.rain

    def add_heavy_rain(self):
        self.weather.rain = "Heavy rain"
        return self.weather.rain

    def add_intense_rain(self):
        self.weather.rain = "Intense rain"
        return self.weather.rain

    def add_torrential_rain(self):
        self.weather.rain = "Torrential rain"
        return self.weather.rain

    def add_very_cold(self):
        self.weather.temperature = "Very cold"
        return self.weather.temperature

    def add_cold(self):
        self.weather.temperature = "Cold"
        return self.weather.temperature

    def add_good(self):
        self.weather.temperature = "Good"
        return self.weather.temperature

    def add_hot(self):
        self.weather.temperature = "Hot"
        return self.weather.temperature

    def add_very_hot(self):
        self.weather.temperature = "Very hot"
        return self.weather.temperature

    def add_place(self):
        self.weather.place = self.inserter2.get_value()
        return self.weather.place

    def get_timestamp(self):
        self.timestamp = pygame.time.get_ticks()
        return self.timestamp

    def get_json_reid(self):
        person_information = {"Header": {"stamp": {"secs": round(self.get_timestamp())}},
                                "Text": {}
                             }
        person_dict = {"NumberOfPersons": len(self.all_sprites_list),
                       "Person": {}
                       }
        for index, person in enumerate(self.all_sprites_list):
            person_dict['Person'][str(index)] = {
                "center_x": (person.rect.x - 500) / 100,
                "center_z": -(person.rect.y - 400) / 100,
                "global_ID": person.id,
                "hand-waving": person.handwave,
            }

        person_information['Text'] = person_dict
        person_information = json.dumps(person_information)
        print("CAM REID CALLED:", person_information)

    def get_json_emotion(self):
        person_emotion = {"Header": {"stamp": {"secs": round(self.get_timestamp())}},
                          "emotions": {}
                          }
        person_emotion_dict = {"emotion": {}
                               }
        for index, person in enumerate(self.all_sprites_list):
            person_emotion_dict['emotion'][str(index)] = {
                "emotion": person.emotion
            }

        person_emotion['emotions'] = person_emotion_dict
        person_emotion = json.dumps(person_emotion)
        print("CAM EMOTION CALLED:", person_emotion)

    def get_json_age_gender(self):
        person_age_gender = {"Header": {"stamp": {"secs": round(self.get_timestamp())}},
                            }
        person_age_gender_dict = {"objects": {}
                                 }
        for index, person in enumerate(self.all_sprites_list):
            person_age_gender_dict['objects'][str(index)] = {
                "gender": person.gender,
                "age": person.age
            }

        person_age_gender['objects'] = person_age_gender_dict
        person_age_gender = json.dumps(person_age_gender)
        print("CAM AGE_GENDER CALLED:", person_age_gender)

    def get_json_weather(self):
        weather = {"timestamp": self.get_timestamp(), "place": self.add_place(), "cloud": self.weather.cloud, "wind": self.weather.wind, "rain": self.weather.rain, "humidity": self.weather.humidity, "temperature": self.weather.temperature}
        weather = json.dumps(weather)
        print("WEATHER CALLED:", weather)