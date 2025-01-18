;------------------------
;	Question E	
;------------------------
(defrule question-E
	(ID E)
	=>
	(printout t "Which is your favourite? [1/2/3]" crlf)
	(printout t "1. Famous Landmarks" crlf)
	(printout t "2. Cultural Parks." crlf)
	(printout t "2. Worship Places." crlf)
	(bind ?answer (read))
	(assert (E-A ?answer)))

;------------------------
;	Question E1	
;------------------------
(defrule question-E1
	(E-A 1)
	=>
	(printout t "What is your age group? [1/2/3/4]" crlf)
	(printout t "1. Kid." crlf)
	(printout t "2. Young." crlf)
	(printout t "3. Adult." crlf)
	(printout t "4. Senior." crlf)
	(bind ?answer1 (read))
	(assert (User-Age-Answer ?answer1))
	(assert (E1a 1)))

(defrule question-E1a
	(E1a 1)
	=>
	(printout t "What would you like to see there? [1/2/3/4]" crlf)
	(printout t "1. Modern Buildings." crlf)
	(printout t "2. Historical Buildings." crlf)
	(printout t "3. Memorials." crlf)
	(printout t "4. Other interesting places." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer-E ?answer2))
	(assert (E1b 1)))

;------------------------
;	Question E2	
;------------------------
(defrule question-E2
	(or (E-A 2)(E-Module-CulturePark 1))
	=>
	(printout t "Which place interest you more?  [1/2/3]" crlf)
	(printout t "1. Greenery." crlf)
	(printout t "2. Pavilions." crlf)
	(printout t "3. World War II Monument" crlf)
	(bind ?answer (read))
	(assert (E2a ?answer)))

(defrule question-E2a
	(E2a 1)
	=>
	(printout t "Chinese Garden / Japanese Garden" crlf))

(defrule question-E2b
	(E2a 2)
	=>
	(printout t "Singapore Botanical Garden" crlf))

(defrule question-E2c
	(E2a 3)
	=>
	(printout t "Fort Canning Park" crlf))

;------------------------
;	Question E3	
;------------------------
(defrule question-E3
	(E-A 3)
	=>
	(printout t "Which place interest you more?  [1/2/3/4]" crlf)
	(printout t "1. Chinese Temple." crlf)
	(printout t "2. Christian Churches." crlf)
	(printout t "3. Hindu Temples" crlf)
	(printout t "4. Mosques" crlf)
	(bind ?answer (read))
	(assert (E3a ?answer)))

(defrule question-E3a
	(E3a 1)
	=>
	(printout t "Thian Hock Keng Temple" crlf)
	(printout t "Buddha Tooth Relic and Museum" crlf))

(defrule question-E3b
	(E3a 2)
	=>
	(printout t "Armenian Church" crlf)
	(printout t "St Andrew's Cathedral" crlf))

(defrule question-E3c
	(E3a 3)
	=>
	(printout t "Sri Mariammam Temple" crlf)
	(printout t "Sri Veeramakaliammam Temple" crlf))

(defrule question-E3d
	(E3a 4)
	=>
	(printout t "Sultan Mosque" crlf)
	(printout t "Jamae Mosque" crlf))

;------------------------
;	Question F	
;------------------------
(defrule question-F
	(ID F)
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. Amazing night city." crlf)
	(printout t "2. Special experience." crlf)
	(bind ?answer (read))
	(assert (F-A ?answer)))

(defrule question-F1
	(F-A 1)
	=>
	(printout t "Singapore Night city tour" crlf))

(defrule question-F2
	(F-A 2)
	=>
	(printout t "Singapore Flyer" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-G		   ;
;	   Full day entertainment	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;-----------------------------
;Sub-Goal Template & Inference
;-----------------------------

(deftemplate Gsubgoal
	(slot GID)
	(slot Ganswer1)
	(slot Ganswer2))

(deffacts G-mysubgoal
	(Gsubgoal (GID GA)(Ganswer1 1)(Ganswer2 1))
	(Gsubgoal (GID GB)(Ganswer1 1)(Ganswer2 2))
	(Gsubgoal (GID GC)(Ganswer1 1)(Ganswer2 3))
	(Gsubgoal (GID GD)(Ganswer1 1)(Ganswer2 4))
	(Gsubgoal (GID GE)(Ganswer1 2)(Ganswer2 1))
	(Gsubgoal (GID GF)(Ganswer1 2)(Ganswer2 2))
	(Gsubgoal (GID GG)(Ganswer1 2)(Ganswer2 3))
	(Gsubgoal (GID GH)(Ganswer1 2)(Ganswer2 4))
	(Gsubgoal (GID Gusergoal)(Ganswer1 NA)(Ganswer2 NA)))

(defrule match-Gsubgoal
	(Gsubgoal (GID Gusergoal)(Ganswer1 ?Ganswer1)(Ganswer2 ?Ganswer2))
	(Gsubgoal (GID ?GID&~Gusergoal)(Ganswer1 ?Ganswer1)(Ganswer2 ?Ganswer2))
	=>
	(printout t "The GID is " ?GID " !" crlf)
	(assert (GID ?GID)))

;--------------------------
;	Question G
;--------------------------
(defrule question-G
	(ID G)
	?f <- (Gsubgoal (GID Gusergoal)(Ganswer1 NA)(Ganswer2 NA))
	=>
	(printout t "What is your gender? [1/2]" crlf)
	(printout t "1. Male." crlf)
	(printout t "2. Female." crlf)
	(bind ?answer1 (read))
	(modify ?f (Ganswer1 ?answer1))
	(assert (G-OK 1)))		;Sequence indicator

;--------------------------
;	Question G1
;--------------------------
(defrule question-G1
	(G-OK 1)
	?f <- (Gsubgoal (GID Gusergoal)(Ganswer2 NA))
	=>
	(printout t "What is your age group? [1/2/3/4]" crlf)
	(printout t "1. Kid." crlf)
	(printout t "2. Young." crlf)
	(printout t "3. Adult." crlf)
	(printout t "2. Senior." crlf)
	(bind ?answer2 (read))
	(modify ?f (Ganswer2 ?answer2))
	(assert (G1-OK 1)))		;Sequence indicator

;-----------------------------------------
;Sub-Goal G1a (Module-G1a Water Themepark)
;-----------------------------------------
(defrule question-G1a
	(or (GID GA) (GID GD) (GID GE) (G-Module-WaterTP 1))
	=>
	(printout t "Which place is more covenient for you? [1/2]" crlf)
	(printout t "1. Pasir Ris." crlf)
	(printout t "2. Sentosa." crlf)
	(bind ?answer (read))
	(assert (G1a-A ?answer)))

(defrule Goal-G1a1
	(G1a-A 1)
	=>
	(printout t "Downtown East" crlf))

(defrule Goal-G1a2
	(G1a-A 2)
	=>
	(printout t "Universal Studio" crlf))

;---------------------------
;	Sub-Goal G1b		
;---------------------------
(defrule question-G1b
	(or (GID GB) (GID GC))
	=>
	(printout t " Which is your favourite? [1/2]" crlf)
	(printout t "1. Challenging experiences." crlf)
	(printout t "2. Water Themepark." crlf)
	(bind ?answer (read))
	(assert (G1b-A ?answer)))

;---------------------------
;	Sub-Goal G1c
;---------------------------
(defrule question-G1c
	(or (GID GG) (GID GH))
	=>
	(printout t " Which is your favourite? [1/2]" crlf)
	(printout t "1. Shopping." crlf)
	(printout t "2. Water Themepark." crlf)
	(bind ?answer (read))
	(assert (G1c-A ?answer)))

;--------------------------------------------
;Sub-Goal G1c1 (Module-G1c1 Big Mall Shopping)
;--------------------------------------------
(defrule question-G1c1
	(G-Module-BigMall 1)
	=>
	(printout t "Which place is more covenient for you? [1/2]" crlf)
	(printout t "1. City Hall." crlf)
	(printout t "2. Orchard Road." crlf)
	(bind ?answer (read))
	(assert (G1c1-A ?answer)))

(defrule Goal-G1c1a
	(G1c1-A 1)
	=>
	(printout t "Marina Square / Millenia Walk / Raffles City / Citylink Mall" crlf))

(defrule Goal-G1c1b
	(G1c1-A 2)
	=>
	(printout t "Centrepoint / DFS Galleria / Wisma Atria / Paragon / Plaza Singapura / Ngee Ann City" crlf))

;---------------------------
;	Sub-Goal G1d
;---------------------------

(defrule question-G1d
	(GID GF)
	=>
	(printout t " Which is your favourite? [1/2/3]" crlf)
	(printout t "1. Shopping." crlf)
	(printout t "2. Water Themepark." crlf)
	(printout t "3. Challenging experiences." crlf)
	(bind ?answer (read))
	(assert (G1d-A ?answer)))

(defrule Goal-G1d1
	(or (G1d-A 1)(G1c-A 1))
	=>
	(printout t "Big Mall Shopping Module " crlf)
	(assert (G-Module-BigMall 1)))

(defrule Goal-G1d2
	(or (G1d-A 2)(G1c-A 2)(G1b-A 2))
	=>
	(printout t "Water Themeparl Module" crlf)
	(assert (G-Module-WaterTP 1)))

(defrule Goal-G1d3
	(or (G1d-A 3)(G1b-A 1))
	=>
	(printout t "Escape Themepark / Megazip Adventure" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-H		   ;
;	   Half day entertainment	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;-----------------------------
;Sub-Goal Template & Inference
;-----------------------------

(deftemplate Hsubgoal
	(slot HID)
	(slot Hanswer1)
	(slot Hanswer2))

(deffacts H-mysubGoal
	(Hsubgoal (HID HA)(Hanswer1 1)(Hanswer2 1))
	(Hsubgoal (HID HB)(Hanswer1 1)(Hanswer2 2))
	(Hsubgoal (HID HC)(Hanswer1 1)(Hanswer2 3))
	(Hsubgoal (HID HD)(Hanswer1 1)(Hanswer2 4))
	(Hsubgoal (HID HE)(Hanswer1 2)(Hanswer2 1))
	(Hsubgoal (HID HF)(Hanswer1 2)(Hanswer2 2))
	(Hsubgoal (HID HH)(Hanswer1 2)(Hanswer2 3))
	(Hsubgoal (HID HH)(Hanswer1 2)(Hanswer2 4))
	(Hsubgoal (HID Husergoal)(Hanswer1 NA)(Hanswer2 NA)))

(defrule match-Hsubgoal
	(Hsubgoal (HID Husergoal)(Hanswer1 ?Hanswer1)(Hanswer2 ?Hanswer2))
	(Hsubgoal (HID ?HID&~Husergoal)(Hanswer1 ?Hanswer1)(Hanswer2 ?Hanswer2))
	=>
	(printout t "The HID is " ?HID " !" crlf)
	(assert (HID ?HID)))

;--------------------------
;	Question H
;--------------------------

(defrule question-H
	(ID H)
	?f <- (Hsubgoal (HID Husergoal)(Hanswer1 NA)(Hanswer2 NA))
	=>
	(printout t "What is your gender? [1/2]" crlf)
	(printout t "1. Male." crlf)
	(printout t "2. Female." crlf)
	(bind ?answer1 (read))
	(modify ?f (Hanswer1 ?answer1))
	(assert (H-OK 1)))		;Sequence indicator

;--------------------------
;	Question H1
;--------------------------

(defrule question-H1
	(H-OK 1)
	?f <- (Hsubgoal (HID Husergoal)(Hanswer2 NA))
	=>
	(printout t "What is your age group? [1/2/3/4]" crlf)
	(printout t "1. Kid." crlf)
	(printout t "2. Young." crlf)
	(printout t "3. Adult." crlf)
	(printout t "4. Senior." crlf)
	(bind ?answer2 (read))
	(modify ?f (Hanswer2 ?answer2))
	(assert (H1-OK 1)))		;Sequence indicator

;---------------------------
;	Sub-Goal H1a
;---------------------------

(defrule question-H1a
	(HID HB)
	=>
	(printout t "Which is your favorite entertainment? [1/2/3/4/5/6]" crlf)
	(printout t "1. Goto the theater." crlf)
	(printout t "2. Go shopping." crlf)
	(printout t "3. Bowling." crlf)
	(printout t "4. Arcade." crlf)
	(printout t "5. Karaoke." crlf)
	(printout t "6. Reverse Bungee Jump." crlf)
	(bind ?answer (read))
	(assert (H1a-A ?answer)))

(defrule Subgoal-H1a1
	(or (H1a-A 1)(H1b-A 1)(H1c-A 1)(H1d-A 1))
	=>
	(printout t "Goto Theater Module" crlf)
	(assert (H-Module-Theater 1)))

(defrule Subgoal-H1a2
	(or (H1a-A 2)(H1b-A 2)(H1c-A 2))
	=>
	(printout t "Goto Shopping All Module" crlf)
	(assert (H-Module-ShoppingAll 1)))

(defrule Goal-H1a3
	(or (H1a-A 3)(H1b-A 3))
	=>
	(printout t "Marina Square / Downtown East / East Coast Park" crlf))		 ;bowling

(defrule Goal-H1a4
	(or (H1a-A 4)(H1d-A 2))
	=>
	(printout t "Marina Square / Orchard Cineleisure / Kallang Cineleisure" crlf))	 ;Arcade

(defrule Goal-H1a5
	(or (H1a-A 5)(H1b-A 4)(H1c-A 3)(I2-A 1)(I2b-A 1))
	=>
	(printout t "Party World / Kbox" crlf))		;Karaoke

(defrule Goal-H1a6
	(or (H1a-A 6)(H1b-A 5))
	=>
	(printout t "Clarke Quay" crlf)) 		;Reverse Bungee Jump

;---------------------------
;	Sub-Goal H1b
;---------------------------

(defrule question-H1b
	(or (HID HC)(HID HD)(HID HF)(HID HG))
	=>
	(printout t "Which is your favorite entertainment? [1/2/3/4/5]" crlf)
	(printout t "1. Goto the theater." crlf)
	(printout t "2. Go shopping." crlf)
	(printout t "3. Bowling." crlf)
	(printout t "4. Karaoke." crlf)
	(printout t "5. Reverse Bungee Jump." crlf)
	(bind ?answer (read))
	(assert (H1b-A ?answer)))

;----------------------------
;	Sub-Goal H1c
;----------------------------

(defrule question-H1c
	(HID HH)
	=>
	(printout t "Which is your favorite entertainment? [1/2/3]" crlf)
	(printout t "1. Goto the theater." crlf)
	(printout t "2. Go shopping." crlf)
	(printout t "3. Karaoke." crlf)
	(bind ?answer (read))
	(assert (H1c-A ?answer)))

;-----------------------------
;	Sub-Goal H1d
;-----------------------------

(defrule question-H1d
	(HID HA)
	=>
	(printout t "Which is your favorite entertainment? [1/2]" crlf)
	(printout t "1. Goto the theater." crlf)
	(printout t "2. Arcade." crlf)
	(bind ?answer (read))
	(assert (H1d-A ?answer)))

;------------------------------
;Sub-Goal H1e (Module-Theater)
;------------------------------

(defrule question-H1e
	(or (HID HE)(H-Module-Theater 1))
	=>
	(printout t "Which do your better? [1/2]" crlf)
	(printout t "1. Art performance." crlf)
	(printout t "2. Movie." crlf)
	(bind ?answer (read))
	(assert (H1e-A ?answer)))

(defrule question-H1e1
	(H1e-A 1)
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. Drama." crlf)
	(printout t "2. Music and dance." crlf)
	(bind ?answer (read))
	(assert (H1e1-A ?answer)))

(defrule goal-H1e2
	(H1e-A 2)
	=>
	(printout t "Golden Village Marina / Cathay Cineplexes / Shaw Cinema" crlf))			;Movie

(defrule goal-H1e1a
	(H1e1-A 1)
	=>
	(printout t "DBS Art Centre - Home of SRT / Esplanade TheatreC / Victoria Concert Hall" crlf))	;Drama

(defrule goal-H1e1b
	(H1e1-A 2)
	=>
	(printout t "Victoria Concert Hall / Esplanade Theatre / Odyssey Dance Theatre" crlf))		;Music & Dance

;---------------------------------
;Sub-Goal H1f (Module-ShoppingAll)
;---------------------------------

(defrule question-H1f
	(H-Module-ShoppingAll 1)
	=>
	(printout t "What a good choice! Singapore is a shopping paradise. Which is your favourite? [1/2/3]" crlf)
	(printout t "1. I like to visit big shopping mall." crlf)
	(printout t "2. I like to buy a souvenir of local culture." crlf)
	(printout t "3. I want to buy something else." crlf)
	(bind ?answer (read))
	(assert (H1f-A ?answer)))

(defrule question-H1f1
	(H1f-A 1)
	=>
	(assert (G-Module-BigMall 1)))

(defrule question-H1f2
	(H1f-A 2)
	=>
	(printout t "Which culture interest you? [1/2/3/4]" crlf)
	(printout t "1. Peranakan." crlf)
	(printout t "2. Chinese." crlf)
	(printout t "3. Malay." crlf)
	(printout t "4. Indian." crlf)
	(bind ?answer (read))
	(assert (H1f2-A ?answer)))

(defrule question-H1f3
	(H1f-A 3)
	=>
	(printout t "Which items are you interested in? [1/2/3/4]" crlf)
	(printout t "1. Computer Products." crlf)
	(printout t "2. Books." crlf)
	(printout t "3. Music & Video." crlf)
	(printout t "4. Electronics Products." crlf)
	(bind ?answer (read))
	(assert (H1f3-A ?answer)))

(defrule goal-H1f2a
	(H1f2-A 1)
	=>
	(printout t "Perenakan Trails / Joo Chiat - Katong / Katong Antique" crlf))	;Perenakan

(defrule goal-H1f2b
	(H1f2-A 2)
	=>
	(printout t "China Town" crlf))				;Chinese

(defrule goal-H1f2c
	(H1f2-A 3)
	=>
	(printout t "Geylang Serai / Kampong Glam" crlf))	;Malay

(defrule goal-H1f2d
	(H1f2-A 4)
	=>
	(printout t "Little India" crlf))			;Indian

(defrule goal-H1f3a
	(H1f3-A 1)
	=>
	(printout t "Funan Centre / Sim Lim Square" crlf))	;Computer Products

(defrule goal-H1f3b
	(H1f3-A 2)
	=>
	(printout t "Ngee Ann City - Kunokuniya / The Borders" crlf))	;Books

(defrule goal-H1f3c
	(H1f3-A 3)
	=>
	(printout t "HMV / Tower Records" crlf))		;Music & Video

(defrule goal-H1f3d
	(H1f3-A 4)
	=>
	(printout t "Penisula Plaza" crlf))			;Electronics Products

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-I		   ;
;	     Night entertainment	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;--------------------------
;	Question I
;--------------------------

(defrule question-I
	(ID I)
	=>
	(printout t "Do you like to go the theatre? [1/2]" crlf)
	(printout t "1. Yes." crlf)
	(printout t "2. No." crlf)
	(bind ?answer (read))
	(assert (I-A ?answer)))

(defrule question-I1
	(I-A 1)
	=>
	(printout t "Goto Theater Module" crlf)
	(assert (H-Module-Theater 1)))

(defrule question-I2
	(I-A 2)
	=>
	(printout t "What is your age? [1/2]" crlf)
	(printout t "1. Young." crlf)
	(printout t "2. Adult." crlf)
	(bind ?answer (read))
	(assert (I2-A ?answer)))

(defrule Goal-I2a
	(I2-A 1)
	=>
	(printout t "Goto KTV" crlf))

(defrule quexti-I2b
	(I2-A 2)
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. KTV." crlf)
	(printout t "2. Pubbing." crlf)
	(bind ?answer (read))
	(assert (I2b-A ?answer)))

(defrule Goal-I2b1
	(I2b-A 1)
	=>
	(printout t "Goto KTV" crlf))								;KTV

(defrule Goal-I2b2
	(I2b-A 2)
	=>
	(printout t "Zouk / St James Powerhouse / Mohamed Sultan Road / Clarke Quay" crlf))	;Pubbing

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-J		   ;
; 	      Full day knowledge	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;--------------------------
;	Question J
;--------------------------

(defrule question-J
	(ID J)
	=>
	(printout t "Which place do you like better? [1/2]" crlf)
	(printout t "1. Singapore zoo." crlf)
	(printout t "2. Jurong Birdpark." crlf)
	(bind ?answer (read))
	(assert (J-A ?answer)))

(defrule Goal-J1
	(J-A 1)
	=>
	(printout t "Singapore zoo" crlf))

(defrule Goal-J2
	(J-A 2)
	=>
	(printout t "Jurong Birdpark" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-K		   ;
;	     Half day knowledge		   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;--------------------------
;	Question K
;--------------------------

(defrule question-K
	(ID K)
	=>
	(printout t "Which is your favourite? [1/2/3/4]" crlf)
	(printout t "1. Museum." crlf)
	(printout t "2. Science Centre." crlf)
	(printout t "3. Culture Park." crlf)
	(printout t "4. Wildlife." crlf)
	(bind ?answer (read))
	(assert (K-A ?answer)))

;--------------------------
;	Question K1
;--------------------------

(defrule question-K1
	(K-A 1)
	=>
	(printout t "What would you like to know more? [1/2]" crlf)
	(printout t "1. Ethnic Culture." crlf)
	(printout t "2. Singapore History." crlf)
	(bind ?answer (read))
	(assert (K1-A ?answer)))

(defrule question-K1a
	(K1-A 1)
	=>
	(printout t "What would you like to know more? [1/2/3/4/5/6]" crlf)
	(printout t "1. Chinese." crlf)
	(printout t "2. Malay." crlf)
	(printout t "3. Indians." crlf)
	(printout t "4. Perenakans." crlf)
	(printout t "5. Eurasians." crlf)
	(printout t "6. All ethnic groups." crlf)
	(bind ?answer (read))
	(assert (K1a-A ?answer)))

(defrule question-K1b
	(K1-A 2)
	=>
	(printout t "Which Singapore history  do you have more interest? [1/2/3/4/5]" crlf)
	(printout t "1. Singapore during World War II." crlf)
	(printout t "2. Armed Forces." crlf)
	(printout t "3. Civil Defence Forces." crlf)
	(printout t "4. National Development of Singapore." crlf)
	(printout t "5. General History." crlf)
	(bind ?answer (read))
	(assert (K1b-A ?answer)))

(defrule Goal-K1a1
	(K1a-A 1)
	=>
	(printout t "Chinatown Heritage Centre / Chinese Heritage Centre / Fuk Tak Chi Museum" crlf))

(defrule Goal-K1a2
	(K1a-A 2)
	=>
	(printout t "Malay Heritage Centre" crlf))

(defrule Goal-K1a3
	(K1a-A 3)
	=>
	(printout t "Indian Muslim Heritage / Little India" crlf))

(defrule Goal-K1a4
	(K1a-A 4)
	=>
	(printout t "Perenakan Museum / Katong Antique / Baba House" crlf))

(defrule Goal-K1a5
	(K1a-A 5)
	=>
	(printout t "Eurasian Heritage Museum" crlf))

(defrule Goal-K1a6
	(K1a-A 6)
	=>
	(printout t "Asian Civilisation Museum" crlf))

(defrule Goal-K1b1
	(K1b-A 1)
	=>
	(printout t "Changi Museum / Ford Factory / Bukit Chandu / Sentosa - Images of Singapore" crlf))

(defrule Goal-K1b2
	(K1b-A 2)
	=>
	(printout t "Army Museum / Air Force Museum / Navy Museum" crlf))

(defrule Goal-K1b3
	(K1b-A 3)
	=>
	(printout t "Civil Defence Museum" crlf))

(defrule Goal-K1b4
	(K1b-A 4)
	=>
	(printout t "HDB Museum" crlf))

(defrule Goal-K1b5
	(K1b-A 5)
	=>
	(printout t "National Museum of Singapore" crlf))

;--------------------------
;	Question K2-K4
;--------------------------

(defrule Goal-K2
	(K-A 2)
	=>
	(printout t "Singapore Science Centre" crlf))

(defrule Goal-K3
	(K-A 3)
	=>
	(assert (E-Module-CulturePark 1)))

(defrule Goal-K4
	(K-A 4)
	=>
	(assert (B-Module-Wildlife 1)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-L		   ;
;	       Night knowledge		   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;--------------------------
;	Question L
;--------------------------

(defrule question-L
	(ID L)
	=>
	(printout t "Which do you like better? [1/2]" crlf)
	(printout t "1. Closer contact with wildlife at night." crlf)
	(printout t "2. Gazing at stars at night with astronomical telescope." crlf)
	(bind ?answer (read))
	(assert (L-A ?answer)))

(defrule Goal-L1
	(L-A 1)
	=>
	(printout t "Night Safari" crlf))

(defrule Goal-L2
	(L-A 2)
	=>
	(printout t "Singapore Science Centre" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-M		   ;
;	   	Full day sports		   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;-----------------------------
;Sub-Goal Template & Inference
;-----------------------------

(deftemplate Msubgoal
	(slot MID)
	(slot Manswer1)
	(slot Manswer2))

(deffacts M-mysubgoal
	(Msubgoal (MID MA)(Manswer1 1)(Manswer2 1))
	(Msubgoal (MID MB)(Manswer1 1)(Manswer2 2))
	(Msubgoal (MID MC)(Manswer1 2)(Manswer2 1))
	(Msubgoal (MID MD)(Manswer1 2)(Manswer2 2))
	(Msubgoal (MID Musergoal)(Manswer1 NA)(Manswer2 NA)))

(defrule match-Msubgoal
	(Msubgoal (MID Musergoal)(Manswer1 ?Manswer1)(Manswer2 ?Manswer2))
	(Msubgoal (MID ?MID&~Musergoal)(Manswer1 ?Manswer1)(Manswer2 ?Manswer2))
	=>
	(printout t "The MID is " ?MID " !" crlf)
	(assert (MID ?MID)))

;--------------------------
;	Question M
;--------------------------

(defrule question-M
	(ID M)
	?f <- (Msubgoal (MID Musergoal)(Manswer1 NA)(Manswer2 NA))
	=>
	(printout t "Which do you like better? [1/2]" crlf)
	(printout t "1. Professional Sports." crlf)
	(printout t "2. Common Sports." crlf)
	(bind ?answer1 (read))
	(modify ?f (Manswer1 ?answer1))
	(assert (M-OK 1)))		;Sequence indicator

;--------------------------
;	Question M1
;--------------------------

(defrule question-M1
	(M-OK 1)
	?f <- (Msubgoal (MID Musergoal)(Manswer2 NA))
	=>
	(printout t " Which do you like better?  [1/2]" crlf)
	(printout t "1. Watersports." crlf)
	(printout t "2. Landsports." crlf)
	(bind ?answer2 (read))
	(modify ?f (Manswer2 ?answer2))
	(assert (M1-OK 1)))		;Sequence indicator

;-----------------------------------------
;	Sub-Goal M1a
;-----------------------------------------

(defrule question-M1a
	(MID MA)
	=>
	(printout t "Which one attracts you more? [1/2]" crlf)
	(printout t "1. Diving." crlf)
	(printout t "2. Windsurfing." crlf)
	(bind ?answer (read))
	(assert (M1a-A ?answer)))

(defrule Goal-M1a1	;Diving
	(M1a-A 1)
	=>
	(printout t "Pulau Hantu / Kusu Island / Pulau Semakau / Sister's Island / St. John's Island" crlf))

(defrule Goal-M1a2	;Windsurfing
	(or (M1a-A 2)(and (N2-A 1)(N3-A 1)))
	=>
	(printout t "East Coast Park / Changi Beach" crlf))

;--------------------------
;	Sub-Goal M1b
;--------------------------

(defrule question-M1b
	(or (MID MB)(and (N2-A 1)(N3-A 2)))
	=>
	(printout t "Which one attracts you more? [1/2]" crlf)
	(printout t "1. Golf." crlf)
	(printout t "2. Rock Climbing." crlf)
	(bind ?answer (read))
	(assert (M1b-A ?answer)))

(defrule Goal-M1b1	;Golf
	(M1b-A 1)
	=>
	(printout t "Tanah Merah Country Club / Sentosa Golf Club" crlf))

(defrule Goal-M1b2	;Rock Climbing
	(M1b-A 2)
	=>
	(printout t "Civil Service Club / SAFRA" crlf))

;-------------------------
;	Sub-Goal M1c
;-------------------------

(defrule question-M1c
	(MID MC)
	=>
	(printout t "Which one attracts you more? [1/2]" crlf)
	(printout t "1. Canoing / Kayaking." crlf)
	(printout t "2. Swimming." crlf)
	(bind ?answer (read))
	(assert (M1c-A ?answer)))

(defrule Goal-M1c1	;Canoing / Kayaking
	(or (M1c-A 1)(N2c-A 1))
	=>
	(printout t "East Coast Park / Kallang Basin" crlf))

(defrule question-M1c2	;Swimming
	(M1c-A 2)
	=>
	(printout t "Which place do you like better? [1/2]" crlf)
	(printout t "1. Swimming near beach." crlf)
	(printout t "2. Swimming at an island (not recommended for beginners!)." crlf)
	(bind ?answer (read))
	(assert (M1e-A ?answer)))

(defrule Goal-M1e1	;Swimming near beach
	(M1e-A 1)
	=>
	(printout t "East Coast Park / Sentosa (Tanjong Beach / Palawan Beach / Siloso Beach)" crlf))

(defrule Goal-M1e2	;Swimming at an island
	(M1e-A 2)
	=>
	(printout t "Pulau Hantu / Kusu Island / Pulau Semakau / Sister's Island / St. John's Island" crlf))


;--------------------------
;	Sub-Goal M1d
;--------------------------

(defrule question-M1d
	(MID MD)
	=>
	(printout t "Which one attracts you more? [1/2/3]" crlf)
	(printout t "1. Beach-volleyball." crlf)
	(printout t "2. Cycling." crlf)
	(printout t "3. Roller blading." crlf)
	(bind ?answer (read))
	(assert (M1d-A ?answer)))

(defrule Goal-M1d1	;Beach-volleyball
	(or (M1d-A 1)(N2d-A 1))
	=>
	(printout t "East Coast Park / Sentosa (Tanjong Beach / Palawan Beach / Siloso Beach)" crlf))

(defrule question-M1d2	;Cycling
	(M1d-A 2)
	=>
	(printout t "Which location is convenient for you? [1/2/3]" crlf)
	(printout t "1. East." crlf)
	(printout t "2. Central." crlf)
	(printout t "3. West." crlf)
	(bind ?answer (read))
	(assert (M1f-A ?answer)))

(defrule Goal-M1d3	;Roller blading
	(or (M1d-A 3)(N2d-A 3))
	=>
	(printout t "East Coast Park" crlf))

(defrule Goal-M1f1	;East
	(M1f-A 1)
	=>
	(printout t "Pulau Ubin / East Coast Park / Pasir Ris Park" crlf))

(defrule Goal-M1f2	;Central
	(M1f-A 2)
	=>
	(printout t "Sentosa (Tanjong Beach / Palawan Beach / Siloso Beach)" crlf))

(defrule Goal-M1f3	;West
	(M1f-A 3)
	=>
	(printout t "West Coast Park" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-N		   ;
;	  	Half day Sports	   	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;--------------------------
;	Question N
;--------------------------

(defrule question-N
	(ID N)
	=>
	(printout t "Which do you like better? [1/2]" crlf)
	(printout t "1. Indoor Sports." crlf)
	(printout t "2. Outdoor Sports." crlf)
	(bind ?answer (read))
	(assert (N-A ?answer)))

;--------------------------
;	Question N1
;--------------------------

(defrule question-N1
	(N-A 1)
	=>
	(printout t "Which indoor sports do you like? [1/2/3]" crlf)
	(printout t "1. Ice-skating." crlf)
	(printout t "2. Archery." crlf)
	(printout t "3. Bowling." crlf)
	(bind ?answer (read))
	(assert (N1-A ?answer)))

(defrule Goal-N1a	;Ice-skating
	(N1-A 1)
	=>
	(printout t "Marina Bay Sands" crlf))

(defrule Goal-N1b	;Archery
	(N1-A 2)
	=>
	(printout t "Marina Square" crlf))

(defrule question-N1c	;Bowling
	(N1-A 3)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. Central." crlf)
	(printout t "2. East." crlf)
	(bind ?answer (read))
	(assert (N1c-A ?answer)))

(defrule Goal-N1c1	;Central
	(N1c-A 1)
	=>
	(printout t "Marina Square" crlf))

(defrule Goal-N1c2	;East
	(N1c-A 2)
	=>
	(printout t "Downtown East / East Coast Park" crlf))

;--------------------------
;	Question N2
;--------------------------

(defrule question-N2
	(N-A 2)
	=>
	(printout t "Which do you like better? [1/2]" crlf)
	(printout t "1. Professional Sports." crlf)
	(printout t "2. Common Sports." crlf)
	(bind ?answer1 (read))
	(assert (N2-OK 1))	;Sequence control
	(assert (N2-A ?answer1)))
	
(defrule question-N3
	(N2-OK 1)
	=>
	(printout t "Which do you like better? [1/2]" crlf)
	(printout t "1. Water Sports." crlf)
	(printout t "2. Land Sports." crlf)
	(bind ?answer2 (read))
	(assert (N3-A ?answer2)))

;--------------------------
;	Question N2a-N2d
;--------------------------

;Goal-N2a	Goto M1a2
;Sub-Goal-N2b	Goto M1b

(defrule question-N2c
	(and (N2-A 2)(N3-A 1))
	=>
	(printout t "Which one attracts you more? [1/2]" crlf)
	(printout t "1. Canoing / Kayaking." crlf)
	(printout t "2. Swimming." crlf)
	(bind ?answer (read))
	(assert (N2c-A ?answer)))

;Goal-N2c1	Goto M1c1

(defrule Goal-N2c2	;Swimming
	(N2c-A 2)
	=>
	(printout t "East Coast Park" crlf))

(defrule question-N2d
	(and (N2-A 2)(N3-A 2))
	=>
	(printout t "Which one attracts you more? [1/2/3]" crlf)
	(printout t "1. Beach-volleyball." crlf)
	(printout t "2. Cycling." crlf)
	(printout t "3. Roller blading." crlf)
	(bind ?answer (read))
	(assert (N2d-A ?answer)))

;Goal-N2d1	Goto M1d1
;Goal-N2d3	Goto M1d3

(defrule question-N2d2	;Cycling
	(N2d-A 2)
	=>
	(printout t "Which location is convenient for you? [1/2]" crlf)
	(printout t "1. East." crlf)
	(printout t "2. West." crlf)
	(bind ?answer (read))
	(assert (N2e-A ?answer)))

(defrule Goal-N2e1	;East
	(N2e-A 1)
	=>
	(printout t "Pulau Ubin / East Coast Park / Pasir Ris Park" crlf))

(defrule Goal-N2e2	;West
	(N2e-A 2)
	=>
	(printout t "West Coast Park" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;					   ;
;  		 RoughGoal-O		   ;
;	  	 NightSports	   	   ;
;					   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule Goal-O
	(ID O)
	=>
	(printout t "Singapore is vey famous for its night cycling sport. If you are sports fun, never miss it." crlf))


;---------------------------------
;	End of This Program	
;---------------------------------