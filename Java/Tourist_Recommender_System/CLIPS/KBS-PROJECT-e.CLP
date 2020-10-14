;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                     Entertainment                      ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule QEL2.2
	(AL1 2)
=>	(printout t "What kind of entertainment do you like?" crlf)
	(printout t "1. I like to go for shopping." crlf)
	(printout t "2. I like to visit an amusement place." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL2.2 ?answer)))


(defrule QEL3.2.1
	(AEL2.2 1) 
=>	(printout t "What is your shopping kind?" crlf)
	(printout t "1. I love going to the mall." crlf)
	(printout t "2. I like to buy something of local culture." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL3.2.1 ?answer)))

(defrule QEL3.2.2
	(AEL2.2 2) 
=>	(printout t "What is your purpose, to relax or to spend excess energy?" crlf)
	(printout t "1. I like places for relaxation." crlf)
	(printout t "2. I think I need more active amusement." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL3.2.2 ?answer)))

(defrule QEL4.2.1.1
	(AEL3.2.1 1) 
=>	(printout t "Singapore is a shopping paradise, following are the famous places to shop:" crlf)
	(printout t "1. Marina Bay" crlf)
	(printout t "2. Orchard" crlf)
	(printout t "3. Clark Quay & River side" crlf)
	(printout t "4. HarbourFront Pricinct" crlf)
	(printout t "5. Holland Village" crlf)
	(printout t "Choose answer [1/2/3/4/5]" crlf)
	(bind ?answer (read))
	(assert (AEL4.2.1.1 ?answer)))

(defrule QEL4.2.1.2
	(AEL3.2.1 2) 
=>	(printout t "Which of these cultures do you find interesting?" crlf)
	(printout t "1. Peranakan" crlf)
	(printout t "2. Chinese" crlf)
	(printout t "3. Malay" crlf)
	(printout t "4. Indian" crlf)
	(printout t "Choose answer [1/2/3/4]" crlf)
	(bind ?answer (read))
	(assert (AEL4.2.1.2 ?answer)))


(defrule QEL4.2.2.1
	(AEL3.2.2 1) 
=>	(printout t "What is your type?" crlf)
	(printout t "1. Theater is a good choice for me." crlf)
	(printout t "2. I heard night life in Singapore is interesting." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL4.2.2.1 ?answer)))

(defrule QEL4.2.2.2
	(AEL3.2.2 2) 
=>	(printout t "Would you like to visit a theme park?" crlf)
	(printout t "1. Yes, I like that idea but I need to know more about it." crlf)
	(printout t "2. No, that is not my type." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL4.2.2.2 ?answer))
)

(defrule QEL5.2.1.1.1
	(AEL4.2.1.1 1) 
=>	(printout t "Within Marina Bay you can see following places:" crlf)
	(printout t "1. Raffles City" crlf)
	(printout t "2. City Link" crlf)
	(printout t "3. Marina Square" crlf)
	(printout t "4. Millenia Walk" crlf)
)

(defrule QEL5.2.1.1.2
	(AEL4.2.1.1 2) 
=>	(printout t "On Orchard Road, you can see following places:" crlf)
	(printout t "1. The Centre Point" crlf)
	(printout t "2. Duty Free Shops (DFS)" crlf)
	(printout t "3. Scotts Shopping Centre" crlf)
	(printout t "4. Plaza Singapura" crlf)
	(printout t "5. The Heeren" crlf)
	(printout t "6. Wisma Atria" crlf)
	(printout t "7. Paragon Shopping Centre" crlf)
	(printout t "8. Ngee Ann city" crlf)
)

(defrule QEL5.2.1.1.3
	(AEL4.2.1.1 3) 
=>	(printout t "Clark Quay is a good place to go for shopping." crlf)
)

(defrule QEL5.2.1.1.4
	(AEL4.2.1.1 4) 
=>	(printout t "HarbourFront is a good place to go for shopping." crlf)
)

(defrule QEL5.2.1.1.5
	(AEL4.2.1.1 5) 
=>	(printout t "Holland Village is a good place to go for shopping." crlf)
)

(defrule QEL5.2.1.2.1
	(AEL4.2.1.2 1) 
=>	(printout t "For Peranakan Culture, you can see following places" crlf)
	(printout t "1. Peranakan Trails" crlf)
	(printout t "2. Joo Chiat" crlf)
	(printout t "3. Katong Antique" crlf)
)

(defrule QEL5.2.1.2.2
	(AEL4.2.1.2 2) 
=>	(printout t "Chinatown is a good place to see Chinese culture." crlf)
	
)

(defrule QEL5.2.1.2.3
	(AEL4.2.1.2 3) 
=>	(printout t "For Malay Culture, you can see following places" crlf)
	(printout t "1. Geylang Serai" crlf)
	(printout t "2. Kampong Glam" crlf)
)

(defrule QEL5.2.1.2.4
	(AEL4.2.1.2 4) 
=>	(printout t "Little India is a good place to see Indian culture." crlf)
	
)

(defrule QEL5.2.2.1.1
	(AEL4.2.2.1 1) 
=>	(printout t "What do you like to see in a theater?" crlf)
	(printout t "1. I like to see some live performance." crlf)
	(printout t "2. I like to see some film." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL5.2.2.1.1 ?answer))
)

(defrule QEL5.2.2.1.2
	(AEL4.2.2.1 2) 
=>	(printout t "What do you like to see in a theater?" crlf)
	(printout t "1. I like to go to a night club." crlf)
	(printout t "2. I like to enjoy my time on seaside." crlf)
	(printout t "3. I like to go to a zoo safari." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (AEL5.2.2.1.2 ?answer))
)

(defrule QEL5.2.2.2.1
	(AEL4.2.2.2 1) 
=>	(printout t "Do you want to just look around or would you like to do some exercise too?" crlf)
	(printout t "1. I just like to walk around and see what interests me." crlf)
	(printout t "2. I would like some challenging experiences." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL5.2.2.2.1 ?answer))
)

(defrule QEL5.2.2.2.2
	(AEL4.2.2.2 2) 
=>	(printout t "What do you like?" crlf)
	(printout t "1. I like sports and games." crlf)
	(printout t "2. I like karaoke." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL5.2.2.2.2 ?answer))
)

(defrule QEL6.2.2.1.1.1
	(AEL5.2.2.1.1 1) 
=>	(printout t "What kind of a performance do you like?" crlf)
	(printout t "1. I like drama." crlf)
	(printout t "2. I like music and dance." crlf)
	(printout t "3. I like some free performances." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (AEL6.2.2.1.1.1 ?answer))
)

(defrule QEL6.2.2.1.1.2
	(AEL5.2.2.1.1 2) 
=>	(printout t "Whould you like to see a film festival?" crlf)
	(printout t "1. No, I will like to watch a new movies in cinema." crlf)
	(printout t "2. Yes, tell me more about it." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL6.2.2.1.1.2 ?answer))
)

(defrule QEL6.2.2.1.2.1
	(AEL5.2.2.1.2 1) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Zouk" crlf)
	(printout t "2. St. James Power House" crlf)
	(printout t "3. Clark Quay" crlf)
)
(defrule QEL6.2.2.1.2.2
	(AEL5.2.2.1.2 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Sentosa" crlf)
	(printout t "2. Boat Quay" crlf)
	(printout t "3. Clark Quay" crlf)
)

(defrule QEL6.2.2.1.2.3
	(AEL5.2.2.1.2 3) 
=>	(printout t "Alright, then you can visit the Night Safari within the Singapore Zoo" crlf)
)

(defrule QEL6.2.2.2.1.1
	(AEL5.2.2.2.1 1) 
=>	(printout t "Do you like water theme park?" crlf)
	(printout t "1. Yes" crlf)
	(printout t "2. No" crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL6.2.2.2.1.1 ?answer))
)

(defrule QEL6.2.2.2.1.2
	(AEL5.2.2.2.1 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Escape Theme Park" crlf)
	(printout t "2. Reverse Bungee Jumping" crlf)
	(printout t "3. Megazip Adventure" crlf)
)

(defrule QEL6.2.2.2.2.1
	(AEL5.2.2.2.2 1) 
=>	(printout t "What do you like in sports?" crlf)
	(printout t "1. I like to go for an outdoor sport." crlf)
	(printout t "2. I like to do some indoor sport." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL6.2.2.2.2.1 ?answer))
)

(defrule QEL6.2.2.2.2.2
	(AEL5.2.2.2.2 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Party World" crlf)
	(printout t "2. KBox" crlf)
	(printout t "3. Zouk" crlf)
	(printout t "4. St. James Power House" crlf)
	(printout t "5. Mohammed Sultan Road" crlf)
	(printout t "6. Clark Quay" crlf)

)

(defrule QEL7.2.2.1.1.1.1
	(AEL6.2.2.1.1.1 1) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. DBS Art Centre - Home of SRT" crlf)
	(printout t "2. Esplanade Theater" crlf)
	(printout t "3. Drama Centre" crlf)
	(printout t "4. Victoria Concert Hall" crlf)
	(printout t "5. National Museum of Singapore, Gallery Theater" crlf)
	(printout t "6. Universal Studio" crlf)
)

(defrule QEL7.2.2.1.1.1.2
	(AEL6.2.2.1.1.1 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Odyssey Dance Theater " crlf)
	(printout t "2. Esplanade Theater" crlf)
	(printout t "3. Victoria Concert Hall" crlf)
	
)

(defrule QEL7.2.2.1.1.1.3
	(AEL6.2.2.1.1.1 3) 
=>	(printout t "Alright, then you can visit Esplanade Theater." crlf)	
)

(defrule QEL7.2.2.1.1.2.1
	(AEL6.2.2.1.1.2 1) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Golden Village Marina" crlf)
	(printout t "2. Cathay Cineplexes" crlf)
	(printout t "3. Shaw Cinema" crlf)
)


(defrule QEL7.2.2.1.1.2.2
	(AEL6.2.2.1.1.2 2) 
=>	(printout t "Alright, then you can visit the film festival in Esplanade" crlf)
)

(defrule QEL7.2.2.2.1.1.1
	(AEL6.2.2.2.1.1 1) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Downtown East" crlf)
	(printout t "2. Universal Studio" crlf)
)

(defrule QEL7.2.2.2.1.1.2
	(AEL6.2.2.2.1.1 2) 
=>	(printout t "Alright, then you can visit Universal Studios" crlf)
)

(defrule QEL7.2.2.2.2.1.1
	(AEL6.2.2.2.2.1 1) 
=>	(printout t "Which ones of these do you like better?" crlf)
	(printout t "1. Rock Climbing." crlf)
	(printout t "2. Sea Diving" crlf)
	(printout t "3. Golf" crlf)
	(printout t "4. Riding Bicycle" crlf)
	(printout t "Choose answer [1/2/3/4]" crlf)
	(bind ?answer (read))
	(assert (AEL7.2.2.2.2.1.1 ?answer))
)

(defrule QEL7.2.2.2.2.1.2
	(AEL6.2.2.2.2.1 2) 
=>	(printout t "Which ones of these do you like better?" crlf)
	(printout t "1. Ice Skating." crlf)
	(printout t "2. Archery" crlf)
	(printout t "3. Arcade" crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (AEL7.2.2.2.2.1.2 ?answer))
)

(defrule QEL8.2.2.2.2.1.1.1
	(AEL7.2.2.2.2.1.1 1) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Civil Service Club" crlf)
	(printout t "2. SAFRA" crlf)
)

(defrule QEL8.2.2.2.2.1.1.2
	(AEL7.2.2.2.2.1.1 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Pulau Hantu" crlf)
	(printout t "2. Kusu Island" crlf)
	(printout t "3. Pulau Semakau" crlf)
	(printout t "4. Sister's Island" crlf)
	(printout t "5. St. John's Island" crlf)

)

(defrule QEL8.2.2.2.2.1.1.3
	(AEL7.2.2.2.2.1.1 3) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Tanah Merah Country Club" crlf)
	(printout t "2. Sentosa Golf Club" crlf)
	
)

(defrule QEL8.2.2.2.2.1.1.4
	(AEL7.2.2.2.2.1.1 4) 
=>	(printout t "Where would you like to cycle?" crlf)
	(printout t "1. On an island." crlf)
	(printout t "2. Eastern part of Singapore" crlf)
	(printout t "3. Western Part of Singapore" crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (AEL8.2.2.2.2.1.1.4 ?answer))
)

(defrule QEL8.2.2.2.2.1.2.1
	(AEL7.2.2.2.2.1.2 1) 
=>	(printout t "Alright, then you can visit Marina Bay Sands" crlf)
	
)

(defrule QEL8.2.2.2.2.1.2.2
	(AEL7.2.2.2.2.1.2 2) 
=>	(printout t "Alright, then you can visit Marina Square" crlf)
	
)

(defrule QEL8.2.2.2.2.1.2.3
	(AEL7.2.2.2.2.1.2 3) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Marina Square" crlf)
	(printout t "2. Downtown East" crlf)
	(printout t "3. East coast Park" crlf)
)

(defrule QEL8.2.2.2.2.1.2.4
	(AEL7.2.2.2.2.1.2 4) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Marina Square" crlf)
	(printout t "2. VivoCity" crlf)
	(printout t "3. Orchard Cineleisure" crlf)
	(printout t "4. Kallang Cineleisure" crlf)
)

(defrule QEL9.2.2.2.2.1.1.4.1
	(AEL8.2.2.2.2.1.1.4 1) 
=>	(printout t "Alright, then you can visit following places" crlf)
	(printout t "1. Pulau Ubin" crlf)
	(printout t "2. Sentosa - Tanjong Beach" crlf)
	(printout t "3. Sentosa - Palawan Beach" crlf)
	(printout t "4. Sentosa - Siloso Beach" crlf)
)

(defrule QEL8.2.2.2.2.1.1.4.2
	(AEL7.2.2.2.2.1.1.4 2) 
=>	(printout t "Alright, then you can visit following places:" crlf)
	(printout t "1. Pasir Ris Park" crlf)
	(printout t "2. East Coast Park" crlf)
)

(defrule QEL8.2.2.2.2.1.1.4.3
	(AEL7.2.2.2.2.1.1.4 3) 
=>	(printout t "Alright, then you can visit West Coast Park" crlf)
)



