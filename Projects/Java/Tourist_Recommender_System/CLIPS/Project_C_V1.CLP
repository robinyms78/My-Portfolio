;Direction A
;
(deftemplate simple-rule
(slot v-name)
(slot v-value)
)

(deftemplate roughgoal
	(slot ID))

(deffacts Fire-C
	(roughgoal (ID C)))

(deftemplate goal-cf
(slot goal-name)
(slot cf-list)
(slot type (default ""))
(slot priority (default 0))
)

(deffacts locations-cf
(goal-cf (goal-name "East Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.9 pavilion 0.6 east 0.9 west 0.1")(type C2))
(goal-cf (goal-name "West Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.1 west 0.9")(type C2))
(goal-cf (goal-name "Pasir Ris Park") (cf-list "palm-trees 0.9 water-ponds 0.3 pavilion 0.9 east 0.9 west 0.1")(type C2))
(goal-cf (goal-name "Changi Beach") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.9 west 0.1")(type C2))
)



;::::::::::::::rules for user-input

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

(defrule question-C
	(roughgoal (ID C))
	=>
	(printout t "Which is your favourite? [1/2/3]" crlf)
	(printout t "1. Walking along the river and enjoy the beautiful night." crlf)
	(printout t "2. Walking along the beach and enjoy the fresh air." crlf)
	(printout t "3. Uniquely Singapore! Come close tonight and enjoy the wonderful experience with Night Safari!" crlf)
	(bind ?answer (read))
	(assert (C-A ?answer)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-C1
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-C1
	(C-A 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. City Hall." crlf)
	(printout t "2. Kallang." crlf)
	(bind ?answer2 (read))
	(assert (C1a 1)))

(defrule question-C1a
	(C1a 1)
	=>
	(printout t "C1a Singapore River" crlf))

(defrule question-C1b
	(C1a 2)
	=>
	(printout t "C1b Kallang River" crlf))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;question-C2
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule question-C2
	(C-A 2)
	=>
	(printout t "What would you like to see at the beach? [1/2/3]" crlf)
	(printout t "1. Palm Trees." crlf)
	(printout t "2. Water ponds." crlf)
	(printout t "3. Pavilion." crlf)
	(bind ?answer1 (read))
	(assert (User-Like-Answer ?answer1))
	(assert (C2a 1)))

(defrule question-C2a
	(C2a 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. East." crlf)
	(printout t "2. West." crlf)
	(bind ?answer2 (read))
	(assert (User-Site-Answer ?answer2))
	(assert (C2CF 1)))

;;;;;;;;;;;;;;;;;
;CF question-B3 ;
;;;;;;;;;;;;;;;;;

(defrule cf-calculator-C2
	(C2CF 1) 
=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type C2)))

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
;question-C3
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defrule question-C3
	(C-A 3)
	=>
	(printout t "C3c Singapore Zoo- Night Safari" crlf))




