;Direction B
;
(deftemplate roughgoal
	(slot ID))

(deffacts Fire-B
	(roughgoal (ID B)))

(deftemplate simple-rule
(slot v-name)
(slot v-value)
)

(deftemplate goal-cf
(slot goal-name)
(slot cf-list)
(slot type (default ""))
(slot priority (default 0))
)

(deffacts locations-cf
(goal-cf (goal-name "East Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.9 pavilion 0.6 east 0.9 west 0.1")(type B3))
(goal-cf (goal-name "West Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.1 west 0.9")(type B3))
(goal-cf (goal-name "Pasir Ris Park") (cf-list "palm-trees 0.9 water-ponds 0.3 pavilion 0.9 east 0.9 west 0.1")(type B3))
(goal-cf (goal-name "Changi Beach") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.9 west 0.1")(type B3))
(goal-cf (goal-name "Sungei Buloh Wetland Reserve") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.7 greenery 0.7 hills 0.1 water 0.8 north 0.9 centre 0.1 east 0.1 west 0.7"))
(goal-cf (goal-name "Mount Faber / Hortpark / Southern Ridge") (cf-list "kid 0.5 young 0.6 adult 0.8 senior 0.6 greenery 0.9 hills 0.9 water 0.2 north 0.1 centre 0.7 east 0.1 west 0.1"))
(goal-cf (goal-name "Labrador Nature Reserve") (cf-list "kid 0.5 young 0.7 adult 0.7 senior 0.8 greenery 0.9 hills 0.8 water 0.6 north 0.1 centre 0.6 east 0.1 west 0.7"))
(goal-cf (goal-name "Bukit Batok Nature Reserve") (cf-list "kid 0.6 young 0.6 adult 0.7 senior 0.8 greenery 0.9 hills 0.9 water 0.7 north 0.3 centre 0.3 east 0.1 west 0.8"))
(goal-cf (goal-name "Bukit Timah Nature Reserve") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.6 greenery 0.9 hills 0.9 water 0.1 north 0.3 centre 0.3 east 0.1 west 0.8"))
(goal-cf (goal-name "Upper and Lower Pierce Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.7 centre 0.1 east 0.1 west 0.6"))
(goal-cf (goal-name "Seletar Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.6 centre 0.1 east 0.1 west 0.4"))
(goal-cf (goal-name "Kranji Countryside") (cf-list "kid 0.6 young 0.9 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.9 centre 0.1 east 0.1 west 0.7"))
(goal-cf (goal-name "MacRitchie Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.6 centre 0.3 east 0.1 west 0.6"))
(goal-cf (goal-name "Singapore Botanical Garden") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.1 water 0.7 north 0.4 centre 0.6 east 0.1 west 0.1"))
(goal-cf (goal-name "Chinese / Japanese Garden") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.8 greenery 0.8 hills 0.3 water 0.8 north 0.1 centre 0.4 east 0.1 west 0.9"))
)



;::::::::::::::rules for user-input
(defrule age-kid
	(declare (salience 1000))
	(User-Age-Answer 1)
=>

	(assert (simple-rule (v-name User-Age)(v-value kid)))

)

(defrule age-young
	(declare (salience 1000))
	(User-Age-Answer 2)
=>
	(assert (simple-rule (v-name User-Age)(v-value young)))
)
(defrule age-adult
	(declare (salience 1000))
	(User-Age-Answer 3)
=>
	(assert (simple-rule (v-name User-Age)(v-value adult)))
)
(defrule age-senior
	(declare (salience 1000))
	(User-Age-Answer 4)
=>
	(assert (simple-rule (v-name User-Age)(v-value senior)))
)

(defrule like-greenery
	(declare (salience 1000))
	(User-Like-Answer-B1 1)
=>
	(assert (simple-rule (v-name User-Like)(v-value greenery)))
)

(defrule like-hills
	(declare (salience 1000))
	(User-Like-Answer-B1 2)
=>
	(assert (simple-rule (v-name User-Like)(v-value hills)))
)

(defrule like-water
	(declare (salience 1000))
	(User-Like-Answer-B1 3)
=>
	(assert (simple-rule (v-name User-Like)(v-value water)))
)
(defrule like-north-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 1)
=>
	(assert (simple-rule (v-name User-Site)(v-value north)))
)

(defrule like-centre-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 2)
=>
	(assert (simple-rule (v-name User-Site)(v-value centre)))
)

(defrule like-east-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 3)
=>
	(assert (simple-rule (v-name User-Site)(v-value east)))
)

(defrule like-west-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 4)
=>
	(assert (simple-rule (v-name User-Site)(v-value west)))
)
;:::::::::::: B3 rules for user input
(defrule like-palm-trees
	(declare (salience 1000))
	(User-Like-Answer 1)
=>
	(assert (simple-rule (v-name User-Like)(v-value palm-trees)))
)

(defrule like-water-ponds
	(declare (salience 1000))
	(User-Like-Answer 2)
=>
	(assert (simple-rule (v-name User-Like)(v-value water-ponds)))
)

(defrule like-pavilion
	(declare (salience 1000))
	(User-Like-Answer 3)
=>
	(assert (simple-rule (v-name User-Like)(v-value pavilion)))
)

(defrule like-east
	(declare (salience 1000))
	(User-Site-Answer 1)
=>
	(assert (simple-rule (v-name User-Site)(v-value east)))
)

(defrule like-west
	(declare (salience 1000))
	(User-Site-Answer 2)
=>
	(assert (simple-rule (v-name User-Site)(v-value west)))
)

;::::::::::::::::::::::end of user-input-rules

(defrule question-B
	(roughgoal (ID B))
	=>
	(printout t "Which is your favourite? [1/2/3/4]" crlf)
	(printout t "1. Natural Parks/Reserve." crlf)
	(printout t "2. Wildlife." crlf)
	(printout t "3. Beach." crlf)
	(printout t "4. Plants Farms." crlf)
	(bind ?answer (read))
	(assert (B-A ?answer)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-B1
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-B1
	(B-A 1)
	=>
	(printout t "What is your age group? [1/2/3/4]" crlf)
	(printout t "1. Kid." crlf)
	(printout t "2. Young." crlf)
	(printout t "3. Adult." crlf)
	(printout t "4. Senior." crlf)
	(bind ?answer1 (read))
	(assert (User-Age-Answer ?answer1))
	(assert (B1a 1))
)
(defrule question-B1a
	(B1a 1)
	=>
	(printout t "What kind of scenery attract you more? [1/2/3]" crlf)
	(printout t "1. Greenery." crlf)
	(printout t "2. Hills." crlf)
	(printout t "3. Water." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer-B1 ?answer2))
	(assert (B1b 1))
)

(defrule question-B1b
	(B1b 1)
	=>
	(printout t "Which location is more convenient for you? [1/2/3/4]" crlf)
	(printout t "1. North." crlf)
	(printout t "2. Central." crlf)
	(printout t "3. East." crlf)
	(printout t "4. West." crlf)
	(bind ?answer2 (read))
	(assert (User-Site-Answer-B1 ?answer2))
	(assert (B1CF 1))
)
;::::::::::::::calculate B1 certainity factor

(defrule cf-calculator-b1
	(B1CF 1) 
=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type "")))

;loop through all locations to calculate the CFs

(loop-for-count (?cnt1 1 11) do
	(bind ?f1 (nth$ ?cnt1 ?list)) ; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)));break the cf list into multifield array

;::::::::::::::get the value of User-Age certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Age))); find the user-age rule 
	(bind ?aa (fact-slot-value (nth$ 1 ?fact)  v-value)); get the value of user-age
	(bind ?i (member$ ?aa ?ccc)); get the index of user age in cf list
	(bind ?cf-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf1 (* ?cf-const-val 0.5))

;::::::::::::::get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like))); find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value)); get the value of user-like
	(bind ?i (member$ ?user-like ?ccc)); get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 1))

;::::::::::::::get the value of User-Site certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Site))); find the user-site rule 
	(bind ?user-site (fact-slot-value (nth$ 1 ?fact)  v-value)); get the value of user-site
	(bind ?i (member$ ?user-site ?ccc)); get the index of user site in cf list
	(bind ?cf3-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf3 (* ?cf3-const-val 0.6))

;::::::::::::::calculate CFs
	(bind ?cf4 (+ ?cf1 (- ?cf2 (* ?cf1 ?cf2))))
	(bind ?cf5 (+ ?cf4 (- ?cf3 (* ?cf4 ?cf3))))
	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf5 crlf)	
;::::::::::::::change the priority of the location in wm
	(modify ?f1 (priority ?cf5))

);end of loop	


)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-B2
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;B-A means answer of the question B
;B2-A means answer of the question B2
;So are the others
;


(defrule question-B2
	(B-A 2)
	=>
	(printout t "What kind of wildlife would you like to experience? [1/2/3/4]" crlf)
	(printout t "1. Animals." crlf)
	(printout t "2. Birds." crlf)
	(printout t "3. Insects." crlf)
	(printout t "4. Fishes." crlf)
	(bind ?answer (read))
	(assert (B2-A ?answer)))


(defrule question-B2a
	(B2-A 1)
	=>
	(printout t "Which attracts you more? [1/2]" crlf)
	(printout t "1. Zoo" crlf)
	(printout t "2. Farms" crlf)
	(bind ?answer (read))
	(assert (B2a-A ?answer)))

(defrule question-B2b
	(B2-A 2)
	=>
	(printout t "B2b Jurong Bird Park" crlf))

(defrule question-B2c
	(B2-A 3)
	=>
	(printout t "B2c Fireflies Health Farm" crlf))

(defrule question-B2d
	(B2-A 4)
	=>
	(printout t "B2d Merlion Aerowanas" crlf))

(defrule question-B2a1
	(B2a-A 1)
	=>
	(printout t "B2a1 Singapore Zoo" crlf))

(defrule question-B2a2
	(B2a-A 2)
	=>
	(printout t "B2a2 Farmat / Haydaries" crlf))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-B3
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-B3
	(B-A 3)
	=>
	(printout t "What would you like to see at the beach? [1/2/3]" crlf)
	(printout t "1. Palm Trees." crlf)
	(printout t "2. Water ponds." crlf)
	(printout t "3. Pavilion." crlf)
	(bind ?answer1 (read))
	(assert (User-Like-Answer ?answer1))
	(assert (B3a 1)))

(defrule question-B3a
	(B3a 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. East." crlf)
	(printout t "2. West." crlf)
	(bind ?answer2 (read))
	(assert (User-Site-Answer ?answer2))
	(assert (B3CF 1)))

;;;;;;;;;;;;;;;;;
;CF question-B3 ;
;;;;;;;;;;;;;;;;;

(defrule cf-calculator-b3
	(B3CF 1) 
=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type B3)))

;loop through all locations to calculate the CFs

(loop-for-count (?cnt1 1 4) do
	(bind ?f1 (nth$ ?cnt1 ?list)) ; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)));break the cf list into multifield array

;::::::::::::::get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like))); find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value)); get the value of user-like
	(bind ?i (member$ ?user-like ?ccc)); get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 0.5))

;::::::::::::::get the value of User-Site certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Site))); find the user-site rule 
	(bind ?user-site (fact-slot-value (nth$ 1 ?fact)  v-value)); get the value of user-site
	(bind ?i (member$ ?user-site ?ccc)); get the index of user site in cf list
	(bind ?cf3-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf3 (* ?cf3-const-val 1.0))

;::::::::::::::calculate CFs
	(bind ?cf4 (+ ?cf2 (- ?cf3 (* ?cf2 ?cf3))))
	
	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf4 crlf)	
;::::::::::::::change the priority of the location in wm
	(modify ?f1 (priority ?cf4))

);end of loop	


)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-B4
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-B4
	(B-A 4)
	=>
	(printout t "Which plant do you like? [1/2]" crlf)
	(printout t "1. Flowers." crlf)
	(printout t "2. Vegetables." crlf)
	(bind ?answer (read))
	(assert (B4-A ?answer)))

(defrule question-B4a
	(B4-A 1)
	=>
	(printout t "B4a Chengtai Nursery / Ngee Phoe Flower" crlf))

(defrule question-B4b
	(B4-A 2)
	=>
	(printout t "B4b Orchidville / Agro-green Technology / Bollywood Veges " crlf))


;	(printout t "" crlf)
