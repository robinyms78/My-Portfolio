;Direction A
;
(deftemplate simple-rule
(slot v-name)
(slot v-value)

)

(deftemplate roughgoal
	(slot ID))

(deffacts Fire-A
	(roughgoal (ID A)))

(defrule question-A
	(roughgoal (ID A))
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. Island." crlf)
	(printout t "2. Wildlife." crlf)
	(bind ?answer (read))
	(assert (A-A ?answer)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-A1
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

(defrule like-chinese-temple
	(declare (salience 1000))
	(User-Like-Answer 1)
=>
	(assert (simple-rule (v-name User-Like)(v-value chinese-temple)))
)

(defrule like-marine-life
	(declare (salience 1000))
	(User-Like-Answer 2)
=>
	(assert (simple-rule (v-name User-Like)(v-value marine-life)))
)

(defrule like-beautiful-sceneries
	(declare (salience 1000))
	(User-Like-Answer 3)
=>
	(assert (simple-rule (v-name User-Like)(v-value beautiful-sceneries)))
)

(defrule like-nearby
	(declare (salience 1000))
	(User-Site-Answer 1)
=>
	(assert (simple-rule (v-name User-Site)(v-value nearby)))
)

(defrule like-far-off
	(declare (salience 1000))
	(User-Site-Answer 2)
=>
	(assert (simple-rule (v-name User-Site)(v-value far-off)))
)


(defrule question-A1
	(A-A 1)
	=>
	(printout t "What is your age group? [1/2/3/4]" crlf)
	(printout t "1. Kid." crlf)
	(printout t "2. Young." crlf)
	(printout t "3. Adult." crlf)
	(printout t "4. Senior." crlf)
	(bind ?answer1 (read))
	(assert (User-Age-Answer ?answer1))
	(assert (A1a 1))
)

(defrule question-A1a
	(A1a 1)
	=>
	(printout t "What would you like to see there? [1/2/3]" crlf)
	(printout t "1. Chinese Temple." crlf)
	(printout t "2. Marine Life." crlf)
	(printout t "3. Beautiful Sceneries." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer ?answer2))
	(assert (A1b 1)))

(defrule question-A1b
	(A1b 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. Nearby Islands." crlf)
	(printout t "2. Far off Islands." crlf)
	(bind ?answer2 (read))
	(assert (User-Site-Answer ?answer2))
	(assert (A1c 1)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;A1 - CF calculation
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deftemplate goal-cf
(slot type (default ""))
(slot goal-name)
(slot cf-list)
(slot priority (default 0))
)

(deffacts locations-cf
	(goal-cf (goal-name "Pulau Ubin") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0.8 marine-life 0.7 beautiful-sceneries 0.6 nearby 0.9 far-off 0.1"))
	(goal-cf (goal-name "Kusu Island") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 1.0 marine-life 0.6 beautiful-sceneries 0.7 nearby 0.4 far-off 0.6"))
	(goal-cf (goal-name "Sisters Island") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.8 nearby 0.2 far-off 0.8"))
	(goal-cf (goal-name "Pulau Hantu") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.5 chinese-temple 0 marine-life 0.9 beautiful-sceneries 0.8 nearby 0.1 far-off 0.9"))
	(goal-cf (goal-name "St John's Island") (cf-list "kid 0.5 young 0.7 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.7 nearby 0.5 far-off 0.5"))
	(goal-cf (goal-name "Pulau Semakau") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.6 nearby 0.2 far-off 0.8"))
	(goal-cf (goal-name "Sentosa - Palawan Beach / Siloso Beach / Tanjong Beach") (cf-list "kid 0.7 young 0.8 adult 0.7 senior 0.6 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.8 nearby 0.9 far-off 0.1"))
)

(defrule cf-calculator
	(A1c 1) 
=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type "")))

;loop through all locations to calculate the CFs

(loop-for-count (?cnt1 1 7) do
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

(deffunction location-sort ()
;get the list of locations
;get the priority of each location
;create a multislot 
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-A2
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-A2
	(A-A 2)
	=>
	(printout t "What kind of wildlife would you like to experience? [1/2/3/4]" crlf)
	(printout t "1. Animals." crlf)
	(printout t "2. Birds." crlf)
	(bind ?answer (read))
	(assert (A2-A ?answer)))

(defrule question-A2a
	(A2-A 1)
	=>
	(printout t "A2a Singapore Zoo" crlf))

(defrule question-A2b
	(A2-A 2)
	=>
	(printout t "A2b Jurong Birdpark" crlf)
	
)


