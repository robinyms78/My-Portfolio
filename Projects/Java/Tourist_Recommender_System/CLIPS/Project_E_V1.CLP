;Direction E
;
(deftemplate simple-rule
(slot v-name)
(slot v-value)

)

(deftemplate roughgoal
	(slot ID))

(deffacts Fire-E
	(roughgoal (ID E)))

(defrule question-E
	(roughgoal (ID E))
	=>
	(printout t "Which is your favourite? [1/2/3]" crlf)
	(printout t "1. Famous Landmarks" crlf)
	(printout t "2. Cultural Parks." crlf)
	(printout t "2. Worship Places." crlf)
	(bind ?answer (read))
	(assert (E-A ?answer)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-E1
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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

(defrule like-modern-building
	(declare (salience 1000))
	(User-Like-Answer 1)
=>
	(assert (simple-rule (v-name User-Like)(v-value modern-building)))
)

(defrule like-historical-building
	(declare (salience 1000))
	(User-Like-Answer 2)
=>
	(assert (simple-rule (v-name User-Like)(v-value historical-building)))
)

(defrule like-memorials
	(declare (salience 1000))
	(User-Like-Answer 3)
=>
	(assert (simple-rule (v-name User-Like)(v-value memorials)))
)

(defrule like-other
	(declare (salience 1000))
	(User-Like-Answer 4)
=>
	(assert (simple-rule (v-name User-Like)(v-value other)))
)

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
	(assert (E1a 1))
)

(defrule question-E1a
	(E1a 1)
	=>
	(printout t "What would you like to see there? [1/2/3/4]" crlf)
	(printout t "1. Modern Buildings." crlf)
	(printout t "2. Historical Buildings." crlf)
	(printout t "3. Memorials." crlf)
	(printout t "4. Other interesting places." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer ?answer2))
	(assert (E1b 1)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;E1 - CF calculation
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deftemplate goal-cf
(slot type (default ""))
(slot goal-name)
(slot cf-list)
(slot priority (default 0))
)

(deffacts locations-cf
(goal-cf (goal-name "Marina Bay Sands Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.8 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Wanderlust Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Wanz Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Resort World Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.8 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "The Club Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "New Majestic Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Capalla Singapore") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Gallery Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Esplanade Theatre") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.7 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "MICA Building") (cf-list "kid 0.3 young 0.4 adult 0.7 senior 0.5 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7"))
(goal-cf (goal-name "Parkview Square") (cf-list "kid 0.3 young 0.3 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7"))
(goal-cf (goal-name "Chijmes") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.6 modern-building 0.8 historical-building 0.7 memorials 0 other 0.7"))
(goal-cf (goal-name "Helix Bridges") (cf-list "kid 0.4 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1"))
(goal-cf (goal-name "Merlion Park") (cf-list "kid 0.4 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0.5 other 0.7"))
(goal-cf (goal-name "Lau Pa Sat") (cf-list "kid 0.4 young 0.5 adult 0.7 senior 0.6 modern-building 0.4 historical-building 0.6 memorials 0 other 0.7"))
(goal-cf (goal-name "Empress place") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7"))
(goal-cf (goal-name "Old Parliament House") (cf-list "kid 0.3 young 0.4 adult 0.8 senior 0.5 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7"))
(goal-cf (goal-name "Goodwood Park Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7"))
(goal-cf (goal-name "Fullerton Bay Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7"))
(goal-cf (goal-name "Raffle's Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7"))
(goal-cf (goal-name "Civilian War Memorial") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.5 modern-building 0 historical-building 0 memorials 1 other 0.6"))
(goal-cf (goal-name "Kranji War Memorial") (cf-list "kid 0.3 young 0.6 adult 0.5 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.6"))
(goal-cf (goal-name "Sun Yat Sen Memorial") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0.7 memorials 0.5 other 0.7"))
(goal-cf (goal-name "Lim Bo Seng War Memorial") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.7"))
(goal-cf (goal-name "Dalhousie Obelisk") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.7"))
(goal-cf (goal-name "Haw Par Villas") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.7 modern-building 0 historical-building 0 memorials 0 other 1"))
(goal-cf (goal-name "People of the River") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1"))
(goal-cf (goal-name "Fort Canning - Battle Box") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1"))	
(goal-cf (goal-name "Sentosa - Fort Siloso") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0.7 memorials 0 other 1"))
)

(defrule cf-calculator
	(E1b 1) 
=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type "")))

;loop through all locations to calculate the CFs

(loop-for-count (?cnt1 1 29) do
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

;::::::::::::::calculate CFs
	(bind ?cf3 (+ ?cf1 (- ?cf2 (* ?cf1 ?cf2))))

	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf3 crlf)	
;::::::::::::::change the priority of the location in wm
	(modify ?f1 (priority ?cf3))

);end of loop	


)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-E2
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-E2
	(E-A 2)
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-E3
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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
	(printout t "Buddha Tooth Relic and Museum" crlf)
)

(defrule question-E3b
	(E3a 2)
	=>
	(printout t "Armenian Church" crlf)
	(printout t "St Andrew's Cathedral" crlf))


(defrule question-E3c
	(E3a 3)
	=>
	(printout t "Sri Mariammam Temple" crlf)
	(printout t "Sri Veeramakaliammam Temple" crlf)
)

(defrule question-E3d
	(E3a 4)
	=>
	(printout t "Sultan Mosque" crlf)
	(printout t "Jamae Mosque" crlf)
)