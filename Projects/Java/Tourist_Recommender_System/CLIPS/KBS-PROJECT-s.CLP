;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; KBS-PROJECT
;; Intelligence Tourist Aid
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Sight-seeing or Entertainment?                ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule QL1
=>	(printout t "Would you like to go sight-seeing?" crlf)
	(printout t "1. Yes, I like to." crlf)
	(printout t "2. No, I want to go somewhere for entertainment." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AL1 ?answer)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                Sight-seeing                    ;;;  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule QSL2.1
	(AL1 1) 
=>	(printout t "What would you like to see?" crlf)
	(printout t "1. I like to see something about nature." crlf)
	(printout t "2. I like to see the culture." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL2.1 ?answer)))

(defrule QEL2.2
	(AL1 2) 
=>	(printout t "What kind of entertainment do you like?" crlf)
	(printout t "1. I like to go shopping." crlf)
	(printout t "2. I like to go to some amusement place." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (AEL2.2 ?answer)))

(defrule QSL3.1.1
	(ASL2.1 1) 
=>	(printout t "Do you like to see the scenary or do you like to experience wildlife?" crlf)
	(printout t "1. I like to see the scenary." crlf)
	(printout t "2. I like to experience wildlife." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL3.1.1 ?answer)))

(defrule QSL3.1.2
	(ASL2.1 2) 
=>	(printout t "Would you like to see the buildings?" crlf)
	(printout t "1. Yes, I would to see famous buildings in Singapore." crlf)
	(printout t "2. No, is there a festival I can visit?" crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL3.1.2 ?answer)))

(defrule QSL4.1.1.1
	(ASL3.1.1 1) 
=>	(printout t "What kind of scenaries do you like?" crlf)
	(printout t "1. I like to go to a park." crlf)
	(printout t "2. I like to see a beach." crlf)
	(printout t "3. I like to see a natural reserve." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL4.1.1.1 ?answer)))

(defrule QSL4.1.1.2
	(ASL3.1.1 2) 
=>	(printout t "What kind of wildlife would you like to experience?" crlf)
	(printout t "1. I like to see animals." crlf)
	(printout t "2. I like to see birds." crlf)
	(printout t "3. I like to see insects" crlf)
	(printout t "4. I like to see fishes" crlf)
	(printout t "5. I like to see greenery" crlf)
	(printout t "Choose answer [1/2/3/4/5]" crlf)
	(bind ?answer (read))
	(assert (ASL4.1.1.2 ?answer)))

(defrule QSL4.1.2.1
	(ASL3.1.2 1)  
=>	(printout t "Which famous buildings would you like to see?" crlf)
	(printout t "1. I like to visit the places of worships." crlf)
	(printout t "2. I like to visit a museum." crlf)
	(printout t "3. I like to visit a landmark." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL4.1.2.1 ?answer)))

(defrule QSL4.1.2.2
	(ASL3.1.2 2) 
=>	(printout t "Which festival would you like to visit?" crlf)
	(printout t "1. I like to see a Chinese festival." crlf)
	(printout t "2. I like to see a Malay festival." crlf)
	(printout t "3. I like to see an Indian festival" crlf)
	(printout t "4. I like to see some other festivals" crlf)
	(printout t "Choose answer [1/2/3/4]" crlf)
	(bind ?answer (read))
	(assert (ASL4.1.2.2 ?answer)))

(defrule QSL5.1.1.1.1
	(ASL4.1.1.1 1) 
=>	(printout t "What kind of park would you like to visit?" crlf)
	(printout t "1. I like to visit a park with a rich culture and history." crlf)
	(printout t "2. I like to see any park." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.1.1 ?answer)))

(defrule QSL5.1.1.1.2
	(ASL4.1.1.1 2) 
=>	(printout t "What would you like to do over there?" crlf)
	(printout t "1. I like to play sports there." crlf)
	(printout t "2. I like to do some sightseeing on an island." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.1.2 ?answer)))

(defrule QSL5.1.1.1.3
	(ASL4.1.1.1 3) 
=>	(printout t "What kind of natural reserve would you like to see?" crlf)
	(printout t "1. I like to see a forest reserve." crlf)
	(printout t "2. I like to see a wetland reserve." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.1.3 ?answer)))

(defrule QSL5.1.1.2.1
	(ASL4.1.1.2 1) 
=>	(printout t "Would you like to visit a farm?" crlf)
	(printout t "1. Yes, I like to do so." crlf)
	(printout t "2. No, I would like to see a zoo." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.2.1 ?answer)))

(defrule QSL5.1.1.2.2
	(ASL4.1.1.2 2) 
=>	(printout t "I would recommend you to visit the Jurong Bird Park" crlf)
)

(defrule QSL5.1.1.2.3
	(ASL4.1.1.2 3) 
=>	(printout t "I would recommend you to visit the Fireflies Health Farm" crlf)
)

(defrule QSL5.1.1.2.4
	(ASL4.1.1.2 4) 
=>	(printout t "Would you like to see some marine fishes?" crlf)
	(printout t "1. Yes, I like to do so." crlf)
	(printout t "2. No, I would like to see fish farms." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.2.4 ?answer)))

(defrule QSL5.1.1.2.5
	(ASL4.1.1.2 5) 
=>	(printout t "What would you like to see?" crlf)
	(printout t "1. I would like to see flowers." crlf)
	(printout t "2. I would like to see vegetables." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.1.2.5 ?answer)))

(defrule QSL5.1.2.1.1
	(ASL4.1.2.1 1)  
=>	(printout t "Which places of worship would you like to visit?" crlf)
	(printout t "1. I like to visit Chinese temples." crlf)
	(printout t "2. I like to visit churches." crlf)
	(printout t "3. I like to visit Indian temples." crlf)
	(printout t "4. I like to visit mosques." crlf)
	(printout t "Choose answer [1/2/3/4]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.1.1 ?answer)))

(defrule QSL5.1.2.1.2
	(ASL4.1.2.1 2)  
=>	(printout t "Which kind of museums would you like to visit?" crlf)
	(printout t "1. I would to know more about the different ethnic groups in Singapore." crlf)
	(printout t "2. I would like to know more about Singapore history." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.1.2 ?answer)))

(defrule QSL5.1.2.1.3
	(ASL4.1.2.1 3)  
=>	(printout t "Which kind of landmarks would you like to see?" crlf)
	(printout t "1. I would like to see some historical landmarks." crlf)
	(printout t "2. I would like to see some famous modern landmarks." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.1.3 ?answer)))

(defrule QSL5.1.2.2.1
	(ASL4.1.2.2 1) 
=>	(printout t "Which Chinese festival would you like to know more about?" crlf)
	(printout t "1. I like to know more about the Chinese New Year." crlf)
	(printout t "2. I like to know more about the Dragon Boat Festival ." crlf)
	(printout t "3. I like to know more about the Hungry Ghost Festival" crlf)
	(printout t "4. I like to know more about the Mid-Autumn Festival" crlf)
	(printout t "5. I like to know more about the Vesak Day" crlf)
	(printout t "Choose answer [1/2/3/4/5]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.2.1 ?answer)))

(defrule QSL5.1.2.2.2
	(ASL4.1.2.2 2) 
=>	(printout t "Which Malay festival would you like to know more about?" crlf)
	(printout t "1. I like to know more about Hari Raya Haji." crlf)
	(printout t "2. I like to know more about Hari Raya Puasa." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.2.2 ?answer)))

(defrule QSL5.1.2.2.3
	(ASL4.1.2.2 3) 
=>	(printout t "Which Indian festival would you like to know more about?" crlf)
	(printout t "1. I like to know more about Thaipusam." crlf)
	(printout t "2. I like to know more about Deepavali." crlf)
	(printout t "3. I like to know more about Pongal." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.2.3 ?answer)))

(defrule QSL5.1.2.2.4
	(ASL4.1.2.2 4) 
=>	(printout t "Which other festival would you like to know more about?" crlf)
	(printout t "1. I like to know more about Christmas." crlf)
	(printout t "2. I like to know more about Chingay Parade." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL5.1.2.2.4 ?answer)))

(defrule QSL6.1.1.1.1.1
	(ASL5.1.1.1.1 1) 
=>	(printout t "Which park interest you more?" crlf)
	(printout t "1. I like to visit a Chinese style pavilions." crlf)
	(printout t "2. I like to visit a rich varieties of plant species." crlf)
	(printout t "3. I like to visit some left-behind monuments of World War II." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.1.1.1.1 ?answer)))

(defrule QSL6.1.1.1.1.2
	(ASL5.1.1.1.1 2) 
=>	(printout t "What would you like to see there?" crlf)
	(printout t "1. I like to see hills." crlf)
	(printout t "2. I like to see water reservoirs." crlf)
	(printout t "3. I like to see tropical rainforests." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.1.1.1.2 ?answer)))

(defrule QSL6.1.1.1.2.1
	(ASL5.1.1.1.2 1) 
=>	(printout t "What sports do you like?" crlf)
	(printout t "1. I like water sports." crlf)
	(printout t "2. I like to play on the sand." crlf)
	(printout t "3. I like to be on wheels." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.1.1.2.1 ?answer)))

(defrule QSL6.1.1.1.2.2
	(ASL5.1.1.1.2 2) 
=>	(printout t "What would you like to see there?" crlf)
	(printout t "1. I like to see Chinese temples." crlf)
	(printout t "2. I like to see marine life." crlf)
	(printout t "3. I like to see beautiful sceneries." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.1.1.2.2 ?answer)))

(defrule QSL6.1.1.1.3.1
	(ASL5.1.1.1.3 1) 
=>	(printout t "I would recommend you the following places:" crlf)
	(printout t "1. Bukit Timah." crlf)
	(printout t "2. Labrador Nature." crlf)
	(printout t "3. MacRitchie Nature Trails." crlf)
)

(defrule QSL6.1.1.1.3.2
	(ASL5.1.1.1.3 2) 
=>	(printout t "I would recommend you the following places:" crlf)
	(printout t "1. Sungei Buloh." crlf)
	(printout t "2. Chek Jawa." crlf)
)

(defrule QSL6.1.1.2.1.1
	(ASL5.1.1.2.1 1) 
=>	(printout t "I would recommend you the following places:" crlf)
	(printout t "1. Farmart." crlf)
	(printout t "2. Hay Daries." crlf)
)

(defrule QSL6.1.1.2.1.2
	(ASL5.1.1.2.1 2) 
=>	(printout t "I would recommend you the Singapore Zoo." crlf)

)

(defrule QSL6.1.1.2.4.1
	(ASL5.1.1.2.4 1) 
=>	(printout t "I would recommend you the Sentosa - Underwater World." crlf)
)

(defrule QSL6.1.1.2.4.2
	(ASL5.1.1.2.4 2) 
=>	(printout t "I would recommend you the Merlion Aerowanas." crlf)
)

(defrule QSL6.1.1.2.5.1
	(ASL5.1.1.2.5 1) 
=>	(printout t "Would you like to visit the flower farms?" crlf)
	(printout t "1. Yes, I like to do so." crlf)
	(printout t "2. No, I would like to visit the Botanical Garden." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.1.2.5.1 ?answer)))

(defrule QSL6.1.1.2.5.2
	(ASL5.1.1.2.5 2) 
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Agro-green Technology." crlf)
	(printout t "2. Bollywood Veges." crlf)
)

(defrule QSL6.1.2.1.1.1
	(ASL5.1.2.1.1 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Thian Hock Keng Temple." crlf)
	(printout t "2. Buddha Tooth Relic and Museum." crlf)
)

(defrule QSL6.1.2.1.1.2
	(ASL5.1.2.1.1 2)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Armenian Church." crlf)
	(printout t "2. St Andrew's Cathedral." crlf)
)

(defrule QSL6.1.2.1.1.3
	(ASL5.1.2.1.1 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Sri Mariammam Temple." crlf)
	(printout t "2. Sri Veeramakaliammam Temple." crlf)
)

(defrule QSL6.1.2.1.1.4
	(ASL5.1.2.1.1 4)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Sultan Mosque." crlf)
	(printout t "2. Jamae Mosque." crlf)
)

(defrule QSL6.1.2.1.2.1
	(ASL5.1.2.1.2 1)  
=>	(printout t "Which ethnic groups would you like to know more?" crlf)
	(printout t "1. I would to know more about the Chinese." crlf)
	(printout t "2. I would to know more about the Malay." crlf)
	(printout t "3. I would to know more about the Peranakans." crlf)
	(printout t "4. I would to know more about the Eurasians." crlf)
	(printout t "5. I would to know more about Asian Civilisation." crlf)
	(printout t "Choose answer [1/2/3/4/5]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.2.1.2.1 ?answer)))

(defrule QSL6.1.2.1.2.2
	(ASL5.1.2.1.2 2)  
=>	(printout t "What kind of history are you interested in?" crlf)
	(printout t "1. I would like to visit the main history museum in Singapore." crlf)
	(printout t "2. I would like to see the armed forces museum in Singapore." crlf)
	(printout t "3. I would like to know more about Singapore during World War II." crlf)
	(printout t "4. I would like to visit some other museums." crlf)
	(printout t "Choose answer [1/2/3/4]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.2.1.2.2 ?answer)))

(defrule QSL6.1.2.1.3.1
	(ASL5.1.2.1.3 1)  
=>	(printout t "What kind of historical landmarks would you like to visit?" crlf)
	(printout t "1. I would like to visit the buildings." crlf)
	(printout t "2. I would like to visit the memorials." crlf)
	(printout t "3. I would like to visit some other interesting places." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.2.1.3.1 ?answer)))

(defrule QSL6.1.2.1.3.2
	(ASL5.1.2.1.3 2)  
=>	(printout t "What kind of modern famous landmarks would you like to visit?" crlf)
	(printout t "1. I would like to visit the buildings." crlf)
	(printout t "2. I would like to visit the memorials." crlf)
	(printout t "3. I would like to visit some other interesting places." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL6.1.2.1.3.2 ?answer)))

(defrule QSL7.1.1.1.1.1.1
	(ASL6.1.1.1.1.1 1)  
=>	(printout t "I would recommend you to visit the Chinese Garden and Japanese Garden." crlf)
)

(defrule QSL7.1.1.1.1.1.2
	(ASL6.1.1.1.1.1 2)  
=>	(printout t "I would recommend you to visit the Botanical Garden." crlf)
)

(defrule QSL7.1.1.1.1.1.3
	(ASL6.1.1.1.1.1 3)  
=>	(printout t "I would recommend you to visit the Fort Canning Park." crlf)
)

(defrule QSL7.1.1.1.1.2.1
	(ASL6.1.1.1.1.2 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Mount Faber." crlf)
	(printout t "2. Hort Park." crlf)
	(printout t "3. Southern Ridge." crlf)
)

(defrule QSL7.1.1.1.1.2.2
	(ASL6.1.1.1.1.2 2)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Kranji Countryside." crlf)
	(printout t "2. MacRitchie Reservoir." crlf)
)

(defrule QSL7.1.1.1.1.2.3
	(ASL6.1.1.1.1.2 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Bukit Batok Nature Reserve." crlf)
	(printout t "2. Bukit Timah Nature Reserve." crlf)
	(printout t "3. Labrador Nature Reserve." crlf)
)

(defrule QSL7.1.1.1.2.1.1
	(ASL6.1.1.1.2.1 1)  
=>	(printout t "What water sports do you like?" crlf)
	(printout t "1. I like scuba diving." crlf)
	(printout t "2. I like wind surfing." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL7.1.1.1.2.1.1 ?answer)))

(defrule QSL7.1.1.1.2.1.2
	(ASL6.1.1.1.2.1 2)  
=>	(printout t "What do you like to do over there?" crlf)
	(printout t "1. I like to play beach volleyball with friends." crlf)
	(printout t "2. I like to build a castle out of sand." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL7.1.1.1.2.1.2 ?answer)))

(defrule QSL7.1.1.1.2.1.3
	(ASL6.1.1.1.2.1 3)  
=>	(printout t "What do you like?" crlf)
	(printout t "1. I like to ride a bicycle." crlf)
	(printout t "2. I like to rollerblade." crlf)
	(printout t "Choose answer [1/2]" crlf)
	(bind ?answer (read))
	(assert (ASL7.1.1.1.2.1.3 ?answer)))

(defrule QSL7.1.1.1.2.2.1
	(ASL6.1.1.1.2.2 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Pulau Ubin." crlf)
	(printout t "2. Kusu Island." crlf)
)

(defrule QSL7.1.1.1.2.2.2
	(ASL6.1.1.1.2.2 2)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Pulau Semakau." crlf)
	(printout t "2. St John's Island." crlf)
	(printout t "3. Sister's Island." crlf)
)

(defrule QSL7.1.1.1.2.2.3
	(ASL6.1.1.1.2.2 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Pulau Ubin." crlf)
	(printout t "2. Kusu Island." crlf)
	(printout t "3. Pulau Semakau." crlf)
	(printout t "4. St John's Island." crlf)
	(printout t "5. Pulau Hantu." crlf)
)

(defrule QSL7.1.1.2.5.1.1
	(ASL6.1.1.2.5.1 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Chengtai Nursery." crlf)
	(printout t "2. Ngee Phoe Flower." crlf)
	(printout t "3. Orchildville." crlf)
)

(defrule QSL7.1.1.2.5.1.2
	(ASL6.1.1.2.5.1 2)  
=>	(printout t "I would recommend you to visit the Singapore Botanical Garden." crlf)
	
)

(defrule QSL7.1.2.1.2.1.1
	(ASL6.1.2.1.2.1 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Chinatown Heritage Centre." crlf)
	(printout t "2. Chinese Heritage Centre." crlf)
	(printout t "3. Fuk Tak Chi Museum." crlf)
)

(defrule QSL7.1.2.1.2.1.2
	(ASL6.1.2.1.2.1 2)  
=>	(printout t "I would recommend you to visit the Malay Heritage Centre." crlf)

)

(defrule QSL7.1.2.1.2.1.3
	(ASL6.1.2.1.2.1 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Peranakan Museum." crlf)
	(printout t "2. Katong Antique." crlf)
	(printout t "3. Baba House." crlf)
)

(defrule QSL7.1.2.1.2.1.4
	(ASL6.1.2.1.2.1 4)  
=>	(printout t "I would recommend you to visit the Eurasian Heritage Centre." crlf)

)

(defrule QSL7.1.2.1.2.1.5
	(ASL6.1.2.1.2.1 5)  
=>	(printout t "I would recommend you to visit the Asian Civilisation Museum." crlf)

)

(defrule QSL7.1.2.1.2.2.1
	(ASL6.1.2.1.2.2 1)  
=>	(printout t "I would recommend you to visit the National Museum of Singapore." crlf)

)

(defrule QSL7.1.2.1.2.2.2
	(ASL6.1.2.1.2.2 2)  
=>	(printout t "Which armed forces museum would you like to visit?" crlf)
	(printout t "1. I like to visit the Army Museum." crlf)
	(printout t "2. I like to visit the Air Force Museum." crlf)
	(printout t "3. I like to visit the Navy Museum." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL7.1.2.1.2.2.2 ?answer)))

(defrule QSL7.1.2.1.2.2.3
	(ASL6.1.2.1.2.2 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Changi Museum." crlf)
	(printout t "2. Ford Factory." crlf)
	(printout t "3. Bukit Chandu." crlf)
	(printout t "4. Images of Singapore." crlf)
)

(defrule QSL7.1.2.1.2.2.4
	(ASL6.1.2.1.2.2 4)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. HDB Museum." crlf)
	(printout t "2. Civil Defence Museum." crlf)
)

(defrule QSL7.1.2.1.3.1.1
	(ASL6.1.2.1.3.1 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Old Parliament House." crlf)
	(printout t "2. Goodwood Park Hotel." crlf)
	(printout t "3. Fullerton Bay Hotel." crlf)
	(printout t "4. Raffle's Hotel." crlf)
	(printout t "5. Lau Ba Sat." crlf)
	(printout t "6. Fort Siliso." crlf)
)

(defrule QSL7.1.2.1.3.1.2
	(ASL6.1.2.1.3.1 2)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Civilian War Memorial." crlf)
	(printout t "2. Kranji War Memorial." crlf)
	(printout t "3. Sun Yat Sen Memorial." crlf)
	(printout t "4. Dalhousie Obelisk." crlf)
)
	
(defrule QSL7.1.2.1.3.1.3
	(ASL6.1.2.1.3.1 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Empress Place." crlf)
	(printout t "2. Haw Par Villas." crlf)
	(printout t "3. People of the River." crlf)
	(printout t "4. Battle Box." crlf)
)
	
(defrule QSL7.1.2.1.3.2.1
	(ASL6.1.2.1.3.2 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Marina Bay Sands Hotel." crlf)
	(printout t "2. Esplanade Theatre." crlf)
	(printout t "3. Capalla Singapore." crlf)
	(printout t "4. MICA Building." crlf)
	(printout t "5. Wanderlust Hotel." crlf)
	(printout t "6. Wanz Hotel." crlf)
	(printout t "7. The Club Hotel." crlf)
	(printout t "8. Resort World Hotel." crlf)
	(printout t "9. New Majestic Hotel." crlf)
	(printout t "10. Gallery Hotel." crlf)
)
	
(defrule QSL7.1.2.1.3.2.2
	(ASL6.1.2.1.3.2 2)  
=>	(printout t "I would recommend you to visit the Merlion." crlf)

)
	
(defrule QSL7.1.2.1.3.2.3
	(ASL6.1.2.1.3.2 3)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Chijmes." crlf)
	(printout t "2. Helix Bridges." crlf)
	(printout t "3. Parkview Square." crlf)
)
	
(defrule QSL8.1.1.1.2.1.1.1
	(ASL7.1.1.1.2.1.1 1)  
=>	(printout t "I would recommend you to visit Pulau Hantu." crlf)

)
	
(defrule QSL8.1.1.1.2.1.1.2
	(ASL7.1.1.1.2.1.1 2)  
=>	(printout t "I would recommend you to visit East Coast Park." crlf)

)
	
(defrule QSL8.1.1.1.2.1.2.1
	(ASL7.1.1.1.2.1.2 1)  
=>	(printout t "I would recommend you to visit the following beaches at Sentosa:" crlf)
	(printout t "1. Tanjong Beach." crlf)
	(printout t "2. Palawan Beach." crlf)
	(printout t "3. Siloso Beach." crlf)
)
	
(defrule QSL8.1.1.1.2.1.2.2
	(ASL7.1.1.1.2.1.2 2)  
=>	(printout t "I would recommend you to visit East Coast Park" crlf)

)
	
(defrule QSL8.1.1.1.2.1.3.1
	(ASL7.1.1.1.2.1.3 1)  
=>	(printout t "Where would you like to cycle?" crlf)
	(printout t "1. I like to cycle on an island." crlf)
	(printout t "2. I like to cycle at the Eastern part of Singapore." crlf)
	(printout t "3. I like to cycle at the Western part of Singapore." crlf)
	(printout t "Choose answer [1/2/3]" crlf)
	(bind ?answer (read))
	(assert (ASL8.1.1.1.2.1.3.1 ?answer)))

(defrule QSL8.1.1.1.2.1.3.2
	(ASL7.1.1.1.2.1.3 2)  
=>	(printout t "I would recommend you to visit East Coast Park" crlf)

)

(defrule QSL8.1.2.1.2.2.2.1
	(ASL7.1.2.1.2.2.2 1)  
=>	(printout t "I would recommend you to visit the Army Museum." crlf)

)
	
(defrule QSL8.1.2.1.2.2.2.2
	(ASL7.1.2.1.2.2.2 2)  
=>	(printout t "I would recommend you to visit the Air Force Museum." crlf)

)
	
(defrule QSL8.1.2.1.2.2.2.3
	(ASL7.1.2.1.2.2.2 3)  
=>	(printout t "I would recommend you to visit the Navy Museum." crlf)

)
	
(defrule QSL9.1.1.1.2.1.3.1.1
	(ASL8.1.1.1.2.1.3.1 1)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Pulau Ubin." crlf)
	(printout t "2. Sentosa (Tanjong Beach / Palawan Beach / Siliso Beach)." crlf)

)

(defrule QSL9.1.1.1.2.1.3.1.2
	(ASL8.1.1.1.2.1.3.1 2)  
=>	(printout t "I would recommend you to visit the following places:" crlf)
	(printout t "1. Pasir Ris Park." crlf)
	(printout t "2. East Coast Park." crlf)

)

(defrule QSL9.1.1.1.2.1.3.1.3
	(ASL8.1.1.1.2.1.3.1 3)  
=>	(printout t "I would recommend you to visit the West Coast Park." crlf)
	
)









