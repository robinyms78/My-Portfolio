;------------------------
;  	  Main		
;------------------------
(deftemplate roughgoal
	(slot ID)
	(slot answer1)
	(slot answer2))

(deffacts myroughgoal
	(roughgoal (ID A)(answer1 1)(answer2 1))
	(roughgoal (ID B)(answer1 1)(answer2 2))
	(roughgoal (ID C)(answer1 1)(answer2 3))
	(roughgoal (ID D)(answer1 2)(answer2 1))
	(roughgoal (ID E)(answer1 2)(answer2 2))
	(roughgoal (ID F)(answer1 2)(answer2 3))
	(roughgoal (ID G)(answer1 3)(answer2 1))
	(roughgoal (ID H)(answer1 3)(answer2 2))
	(roughgoal (ID I)(answer1 3)(answer2 3))
	(roughgoal (ID J)(answer1 4)(answer2 1))
	(roughgoal (ID K)(answer1 4)(answer2 2))
	(roughgoal (ID L)(answer1 4)(answer2 3))
	(roughgoal (ID M)(answer1 5)(answer2 1))
	(roughgoal (ID N)(answer1 5)(answer2 2))
	(roughgoal (ID O)(answer1 5)(answer2 3))
	(roughgoal (ID usergoal)(answer1 NA)(answer2 NA)))

;------------------------
;	Question 1		
;------------------------

(defrule Start-question1
	(declare (salience 1000))
	?f <- (roughgoal (ID usergoal)(answer1 NA)(answer2 NA))
	=>
	(printout t "What's your main purpose for the travelling? [1/2/3/4/5]" crlf)
	(printout t "1. Go close to nature to relax my mind." crlf)
	(printout t "2. Have a look of Singapore cultural landscape." crlf)
	(printout t "3. Go to entertainment place to have fun." crlf)
	(printout t "4. Increase knowledge of local culture and science." crlf)
	(printout t "5. I hope to do some sports this time." crlf)
	(bind ?answer1 (read))
	(modify ?f (answer1 ?answer1)))

;------------------------
;	Question 2		
;------------------------
(defrule Start-question2
	?f <- (roughgoal (ID usergoal)(answer2 NA))
	=>
	(printout t "What is your time schedule for that?[1/2/3]" crlf)
	(printout t "1. I like the place that I can spend a whole day there." crlf)
	(printout t "2. Better within half a day. I'd like to visit 2 more places per day." crlf)
	(printout t "3. Can I make it at night?" crlf)
	(bind ?answer2 (read))
	(modify ?f (answer2 ?answer2)))

;------------------------
;	Match Dirction		
;------------------------
(defrule match-roughgoal
	(roughgoal (ID usergoal)(answer1 ?answer1)(answer2 ?answer2))
	(roughgoal (ID ?ID&~usergoal)(answer1 ?answer1)(answer2 ?answer2))
	=>
	(printout t "The ID is " ?ID " !" crlf)
	(assert (ID ?ID)))

;---------------------------------------
;	General Template For CF			
;---------------------------------------
(deftemplate simple-rule
	(slot v-name)
	(slot v-value))

(deftemplate goal-cf
	(slot goal-name)
	(slot cf-list)
	(slot type (default ""))
	(slot priority (default 0)))

;------------------------
;	Get A Facts			
;------------------------

;Age rule is for public	

(defrule age-kid
	(declare (salience 1000))
	(User-Age-Answer 1)
	=>
	(assert (simple-rule (v-name User-Age)(v-value kid))))

(defrule age-young
	(declare (salience 1000))
	(User-Age-Answer 2)
	=>
	(assert (simple-rule (v-name User-Age)(v-value young))))

(defrule age-adult
	(declare (salience 1000))
	(User-Age-Answer 3)
	=>
	(assert (simple-rule (v-name User-Age)(v-value adult))))

(defrule age-senior
	(declare (salience 1000))
	(User-Age-Answer 4)
	=>
	(assert (simple-rule (v-name User-Age)(v-value senior))))

(defrule like-chinese-temple	
	(declare (salience 1000))
	(User-Like-Answer-A 1)
	=>
	(assert (simple-rule (v-name User-Like-A)(v-value chinese-temple))))

(defrule like-marine-life
	(declare (salience 1000))
	(User-Like-Answer-A 2)
	=>
	(assert (simple-rule (v-name User-Like-A)(v-value marine-life))))

(defrule like-beautiful-sceneries
	(declare (salience 1000))
	(User-Like-Answer-A 3)	
	=>
	(assert (simple-rule (v-name User-Like-A)(v-value beautiful-sceneries))))

(defrule like-nearby
	(declare (salience 1000))
	(User-Site-Answer-A 1)
	=>
	(assert (simple-rule (v-name User-Site-A)(v-value nearby))))

(defrule like-far-off
	(declare (salience 1000))
	(User-Site-Answer-A 2)
	=>
	(assert (simple-rule (v-name User-Site-A)(v-value far-off))))

;----------------------------
;	Calculate A CF
;----------------------------

(defrule cf-calculator-a
	(A1c 1) 
	=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type A)))

;loop through all locations to calculate the CFs
(loop-for-count (?cnt1 1 7) do
	(bind ?f1 (nth$ ?cnt1 ?list)) 							; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)))				; break the cf list into multifield array

;get the value of User-Age certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Age)))		; find the user-age rule 
	(bind ?aa (fact-slot-value (nth$ 1 ?fact)  v-value))				; get the value of user-age
	(bind ?i (member$ ?aa ?ccc))							; get the index of user age in cf list
	(bind ?cf-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf1 (* ?cf-const-val 0.5))

;get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like-A)))	; find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-like
	(bind ?i (member$ ?user-like ?ccc))						; get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 1))

;get the value of User-Site certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Site-A)))	; find the user-site rule 
	(bind ?user-site (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-site
	(bind ?i (member$ ?user-site ?ccc))						; get the index of user site in cf list
	(bind ?cf3-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf3 (* ?cf3-const-val 0.6))

;calculate CFs
	(bind ?cf4 (+ ?cf1 (- ?cf2 (* ?cf1 ?cf2))))
	(bind ?cf5 (+ ?cf4 (- ?cf3 (* ?cf4 ?cf3))))
	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf5 crlf)	

;change the priority of the location in wm
	(modify ?f1 (priority ?cf5)))							; end of loop	
)

;------------------------
;	Get B1 Facts	
;------------------------

;Age rule is public (see A)

(defrule like-greenery
	(declare (salience 1000))
	(User-Like-Answer-B1 1)
	=>
	(assert (simple-rule (v-name User-Like-B1)(v-value greenery))))

(defrule like-hills
	(declare (salience 1000))
	(User-Like-Answer-B1 2)
	=>
	(assert (simple-rule (v-name User-Like-B1)(v-value hills))))

(defrule like-water
	(declare (salience 1000))
	(User-Like-Answer-B1 3)
	=>
	(assert (simple-rule (v-name User-Like-B1)(v-value water))))

(defrule like-north-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 1)
	=>
	(assert (simple-rule (v-name User-Site-B1)(v-value north))))

(defrule like-centre-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 2)
	=>
	(assert (simple-rule (v-name User-Site-B1)(v-value centre))))

(defrule like-east-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 3)
	=>
	(assert (simple-rule (v-name User-Site-B1)(v-value east))))

(defrule like-west-B1
	(declare (salience 1000))
	(User-Site-Answer-B1 4)
	=>
	(assert (simple-rule (v-name User-Site-B1)(v-value west))))

;------------------------
;	Get B3 Facts
;------------------------

(defrule like-palm-trees
	(declare (salience 1000))
	(User-Like-Answer-B3 1)
	=>
	(assert (simple-rule (v-name User-Like-B3)(v-value palm-trees))))

(defrule like-water-ponds
	(declare (salience 1000))
	(User-Like-Answer-B3 2)
	=>
	(assert (simple-rule (v-name User-Like-B3)(v-value water-ponds))))

(defrule like-pavilion
	(declare (salience 1000))
	(User-Like-Answer-B3 3)
	=>
	(assert (simple-rule (v-name User-Like-B3)(v-value pavilion))))

(defrule like-east-B3
	(declare (salience 1000))
	(User-Site-Answer-B3 1)
	=>
	(assert (simple-rule (v-name User-Site-B3)(v-value east))))

(defrule like-west-B3
	(declare (salience 1000))
	(User-Site-Answer-B3 2)
	=>
	(assert (simple-rule (v-name User-Site-B3)(v-value west))))

;-------------------------------
;	calculate B1 CF		
;-------------------------------

(defrule cf-calculator-b1
	(B1CF 1) 
	=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type B1)))

;loop through all locations to calculate the CFs
(loop-for-count (?cnt1 1 11) do
	(bind ?f1 (nth$ ?cnt1 ?list)) 							; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)))				; break the cf list into multifield array

;get the value of User-Age certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Age)))		; find the user-age rule 
	(bind ?aa (fact-slot-value (nth$ 1 ?fact)  v-value))				; get the value of user-age
	(bind ?i (member$ ?aa ?ccc))							; get the index of user age in cf list
	(bind ?cf-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf1 (* ?cf-const-val 0.5))

;get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like-B1)))	; find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-like
	(bind ?i (member$ ?user-like ?ccc))						; get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 1))

;get the value of User-Site certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Site-B1)))	; find the user-site rule 
	(bind ?user-site (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-site
	(bind ?i (member$ ?user-site ?ccc))						; get the index of user site in cf list
	(bind ?cf3-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf3 (* ?cf3-const-val 0.6))

;calculate CFs
	(bind ?cf4 (+ ?cf1 (- ?cf2 (* ?cf1 ?cf2))))
	(bind ?cf5 (+ ?cf4 (- ?cf3 (* ?cf4 ?cf3))))
	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf5 crlf)	

;change the priority of the location in wm
	(modify ?f1 (priority ?cf5)))							; end of loop	
)

;-------------------------------
;	calculate B3 CF			
;-------------------------------

(defrule cf-calculator-b3
	(B3CF 1) 
	=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type B3)))

;loop through all locations to calculate the CFs
(loop-for-count (?cnt1 1 4) do
	(bind ?f1 (nth$ ?cnt1 ?list)) 					; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)))		;break the cf list into multifield array

;get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like-B3)))	; find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-like
	(bind ?i (member$ ?user-like ?ccc))						; get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 0.5))

;get the value of User-Site certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Site-B3)))	; find the user-site rule 
	(bind ?user-site (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-site
	(bind ?i (member$ ?user-site ?ccc))						; get the index of user site in cf list
	(bind ?cf3-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf3 (* ?cf3-const-val 1.0))

;calculate CFs
	(bind ?cf4 (+ ?cf2 (- ?cf3 (* ?cf2 ?cf3))))	
	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf4 crlf)	

;change the priority of the location in wm
	(modify ?f1 (priority ?cf4)))							; end of loop	
)

;------------------------
;	Get E1 Facts	
;------------------------

;Age is public (see A)

(defrule like-modern-building
	(declare (salience 1000))
	(User-Like-Answer-E 1)
	=>
	(assert (simple-rule (v-name User-Like-E)(v-value modern-building))))

(defrule like-historical-building
	(declare (salience 1000))
	(User-Like-Answer-E 2)
	=>
	(assert (simple-rule (v-name User-Like-E)(v-value historical-building))))

(defrule like-memorials
	(declare (salience 1000))
	(User-Like-Answer-E 3)
	=>
	(assert (simple-rule (v-name User-Like-E)(v-value memorials))))

(defrule like-other
	(declare (salience 1000))
	(User-Like-Answer-E 4)
	=>
	(assert (simple-rule (v-name User-Like-E)(v-value other))))

;-------------------------------
;	calculate E CF		
;-------------------------------

(defrule cf-calculator-e
	(E1b 1) 
	=>
	(bind ?list (find-all-facts ((?f goal-cf))(eq ?f:type E)))

;loop through all locations to calculate the CFs
(loop-for-count (?cnt1 1 29) do
	(bind ?f1 (nth$ ?cnt1 ?list))						; get the fact location from the list	
	(bind ?ccc (explode$ (fact-slot-value ?f1 cf-list)))			; break the cf list into multifield array

;get the value of User-Age certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Age)))	; find the user-age rule 
	(bind ?aa (fact-slot-value (nth$ 1 ?fact)  v-value))			; get the value of user-age
	(bind ?i (member$ ?aa ?ccc))						; get the index of user age in cf list
	(bind ?cf-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf1 (* ?cf-const-val 0.5))

;get the value of User-Like certainity factor
	(bind ?fact (find-all-facts ((?f simple-rule))(eq ?f:v-name User-Like-E))); find the user-age rule 
	(bind ?user-like (fact-slot-value (nth$ 1 ?fact)  v-value))		; get the value of user-like
	(bind ?i (member$ ?user-like ?ccc))					; get the index of user like in cf list
	(bind ?cf2-const-val (nth$ (+ ?i 1) ?ccc))
	(bind ?cf2 (* ?cf2-const-val 1))

;calculate CFs
	(bind ?cf3 (+ ?cf1 (- ?cf2 (* ?cf1 ?cf2))))

	(printout t (fact-slot-value ?f1 goal-name) crlf)	
	(printout t ?cf3 crlf)	

;change the priority of the location in wm
	(modify ?f1 (priority ?cf3)))						; end of loop	
)

;-------------------------------
;get the list of locations
;get the priority of each location
;create a multislot 
;-------------------------------

;(deffunction location-sort ())



;------------------
;	Facts
;------------------

(deffacts locations-cf-A
	(goal-cf (goal-name "Pulau Ubin") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0.8 marine-life 0.7 beautiful-sceneries 0.6 nearby 0.9 far-off 0.1")(type A))
	(goal-cf (goal-name "Kusu Island") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 1.0 marine-life 0.6 beautiful-sceneries 0.7 nearby 0.4 far-off 0.6")(type A))
	(goal-cf (goal-name "Sisters Island") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.8 nearby 0.2 far-off 0.8")(type A))
	(goal-cf (goal-name "Pulau Hantu") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.5 chinese-temple 0 marine-life 0.9 beautiful-sceneries 0.8 nearby 0.1 far-off 0.9")(type A))
	(goal-cf (goal-name "St John's Island") (cf-list "kid 0.5 young 0.7 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.7 nearby 0.5 far-off 0.5")(type A))
	(goal-cf (goal-name "Pulau Semakau") (cf-list "kid 0.5 young 0.6 adult 0.7 senior 0.8 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.6 nearby 0.2 far-off 0.8")(type A))
	(goal-cf (goal-name "Sentosa - Palawan Beach / Siloso Beach / Tanjong Beach") (cf-list "kid 0.7 young 0.8 adult 0.7 senior 0.6 chinese-temple 0 marine-life 0.8 beautiful-sceneries 0.8 nearby 0.9 far-off 0.1")(type A)))

(deffacts locations-cf-B
	(goal-cf (goal-name "East Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.9 pavilion 0.6 east 0.9 west 0.1")(type B3))
	(goal-cf (goal-name "West Coast Park") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.1 west 0.9")(type B3))
	(goal-cf (goal-name "Pasir Ris Park") (cf-list "palm-trees 0.9 water-ponds 0.3 pavilion 0.9 east 0.9 west 0.1")(type B3))
	(goal-cf (goal-name "Changi Beach") (cf-list "palm-trees 0.9 water-ponds 0.1 pavilion 0.9 east 0.9 west 0.1")(type B3))

	(goal-cf (goal-name "Sungei Buloh Wetland Reserve") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.7 greenery 0.7 hills 0.1 water 0.8 north 0.9 centre 0.1 east 0.1 west 0.7")(type B1))
	(goal-cf (goal-name "Mount Faber / Hortpark / Southern Ridge") (cf-list "kid 0.5 young 0.6 adult 0.8 senior 0.6 greenery 0.9 hills 0.9 water 0.2 north 0.1 centre 0.7 east 0.1 west 0.1")(type B1))
	(goal-cf (goal-name "Labrador Nature Reserve") (cf-list "kid 0.5 young 0.7 adult 0.7 senior 0.8 greenery 0.9 hills 0.8 water 0.6 north 0.1 centre 0.6 east 0.1 west 0.7")(type B1))
	(goal-cf (goal-name "Bukit Batok Nature Reserve") (cf-list "kid 0.6 young 0.6 adult 0.7 senior 0.8 greenery 0.9 hills 0.9 water 0.7 north 0.3 centre 0.3 east 0.1 west 0.8")(type B1))
	(goal-cf (goal-name "Bukit Timah Nature Reserve") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.6 greenery 0.9 hills 0.9 water 0.1 north 0.3 centre 0.3 east 0.1 west 0.8")(type B1))
	(goal-cf (goal-name "Upper and Lower Pierce Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.7 centre 0.1 east 0.1 west 0.6")(type B1))
	(goal-cf (goal-name "Seletar Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.6 centre 0.1 east 0.1 west 0.4")(type B1))
	(goal-cf (goal-name "Kranji Countryside") (cf-list "kid 0.6 young 0.9 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.9 centre 0.1 east 0.1 west 0.7")(type B1))
	(goal-cf (goal-name "MacRitchie Reservoir") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.2 water 0.9 north 0.6 centre 0.3 east 0.1 west 0.6")(type B1))
	(goal-cf (goal-name "Singapore Botanical Garden") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.9 greenery 0.9 hills 0.1 water 0.7 north 0.4 centre 0.6 east 0.1 west 0.1")(type B1))
	(goal-cf (goal-name "Chinese / Japanese Garden") (cf-list "kid 0.6 young 0.7 adult 0.7 senior 0.8 greenery 0.8 hills 0.3 water 0.8 north 0.1 centre 0.4 east 0.1 west 0.9")(type B1)))


(deffacts locations-cf-E
	(goal-cf (goal-name "Marina Bay Sands Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.8 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Wanderlust Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Wanz Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Resort World Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.8 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "The Club Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "New Majestic Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Capalla Singapore") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Gallery Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Esplanade Theatre") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.7 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "MICA Building") (cf-list "kid 0.3 young 0.4 adult 0.7 senior 0.5 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Parkview Square") (cf-list "kid 0.3 young 0.3 adult 0.7 senior 0.3 modern-building 1.0 historical-building 0 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Chijmes") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.6 modern-building 0.8 historical-building 0.7 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Helix Bridges") (cf-list "kid 0.4 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1")(type E))
	(goal-cf (goal-name "Merlion Park") (cf-list "kid 0.4 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0.5 other 0.7")(type E))
	(goal-cf (goal-name "Lau Pa Sat") (cf-list "kid 0.4 young 0.5 adult 0.7 senior 0.6 modern-building 0.4 historical-building 0.6 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Empress place") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Old Parliament House") (cf-list "kid 0.3 young 0.4 adult 0.8 senior 0.5 modern-building 0.4 historical-building 0.7 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Goodwood Park Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Fullerton Bay Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Raffle's Hotel") (cf-list "kid 0 young 0 adult 0.7 senior 0.6 modern-building 0 historical-building 1 memorials 0 other 0.7")(type E))
	(goal-cf (goal-name "Civilian War Memorial") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.5 modern-building 0 historical-building 0 memorials 1 other 0.6")(type E))
	(goal-cf (goal-name "Kranji War Memorial") (cf-list "kid 0.3 young 0.6 adult 0.5 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.6")(type E))
	(goal-cf (goal-name "Sun Yat Sen Memorial") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0.7 memorials 0.5 other 0.7")(type E))
	(goal-cf (goal-name "Lim Bo Seng War Memorial") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.7")(type E))
	(goal-cf (goal-name "Dalhousie Obelisk") (cf-list "kid 0.3 young 0.6 adult 0.6 senior 0.6 modern-building 0 historical-building 0 memorials 1 other 0.7")(type E))
	(goal-cf (goal-name "Haw Par Villas") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.7 modern-building 0 historical-building 0 memorials 0 other 1")(type E))
	(goal-cf (goal-name "People of the River") (cf-list "kid 0.3 young 0.5 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1")(type E))
	(goal-cf (goal-name "Fort Canning - Battle Box") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0 memorials 0 other 1")(type E))	
	(goal-cf (goal-name "Sentosa - Fort Siloso") (cf-list "kid 0.3 young 0.6 adult 0.7 senior 0.6 modern-building 0 historical-building 0.7 memorials 0 other 1")(type E)))


;---------------------------------------------------------
;	Following are all the Questions From A to O
;---------------------------------------------------------

;------------------------
;	Question A
;------------------------

(defrule question-A
	(ID A)
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. Island." crlf)
	(printout t "2. Wildlife." crlf)
	(bind ?answer (read))
	(assert (A-A ?answer)))

;------------------------
;	Question-A1
;------------------------

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
	(assert (A1a 1)))

(defrule question-A1a
	(A1a 1)
	=>
	(printout t "What would you like to see there? [1/2/3]" crlf)
	(printout t "1. Chinese Temple." crlf)
	(printout t "2. Marine Life." crlf)
	(printout t "3. Beautiful Sceneries." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer-A ?answer2))
	(assert (A1b 1)))

(defrule question-A1b
	(A1b 1)
	=>
	(printout t "Which location do you have more interest? [1/2]" crlf)
	(printout t "1. Nearby Islands." crlf)
	(printout t "2. Far off Islands." crlf)
	(bind ?answer3 (read))
	(assert (User-Site-Answer-A ?answer3))
	(assert (A1c 1)))

;-------------------------------
;	question-A2		
;-------------------------------

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
	(printout t "A2b Jurong Birdpark" crlf))

;------------------------
;	Question B	
;------------------------

(defrule question-B
	(ID B)
	=>
	(printout t "Which is your favourite? [1/2/3/4]" crlf)
	(printout t "1. Natural Parks/Reserve." crlf)
	(printout t "2. Wildlife." crlf)
	(printout t "3. Beach." crlf)
	(printout t "4. Plants Farms." crlf)
	(bind ?answer (read))
	(assert (B-A ?answer)))

;------------------------
;	Question B1	
;------------------------

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
	(assert (B1a 1)))

(defrule question-B1a
	(B1a 1)
	=>
	(printout t "What kind of scenery attract you more? [1/2/3]" crlf)
	(printout t "1. Greenery." crlf)
	(printout t "2. Hills." crlf)
	(printout t "3. Water." crlf)
	(bind ?answer2 (read))
	(assert (User-Like-Answer-B1 ?answer2))
	(assert (B1b 1)))

(defrule question-B1b
	(B1b 1)
	=>
	(printout t "Which location is more convenient for you? [1/2/3/4]" crlf)
	(printout t "1. North." crlf)
	(printout t "2. Central." crlf)
	(printout t "3. East." crlf)
	(printout t "4. West." crlf)
	(bind ?answer3 (read))
	(assert (User-Site-Answer-B1 ?answer3))
	(assert (B1CF 1)))

;------------------------
;	Question B2	
;------------------------

(defrule question-B2
	(or (B-A 2)(B-Module-Wildlife 1))
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

;------------------------
;	Question B3
;------------------------

(defrule question-B3
	(or (B-A 3)(C-A 2))
	=>
	(printout t "What would you like to see at the beach? [1/2/3]" crlf)
	(printout t "1. Palm Trees." crlf)
	(printout t "2. Water ponds." crlf)
	(printout t "3. Pavilion." crlf)
	(bind ?answer1 (read))
	(assert (User-Like-Answer-B3 ?answer1))
	(assert (B3a 1)))

(defrule question-B3a
	(B3a 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. East." crlf)
	(printout t "2. West." crlf)
	(bind ?answer2 (read))
	(assert (User-Site-Answer-B3 ?answer2))
	(assert (B3CF 1)))

;------------------------
;	Question B4
;------------------------

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

;------------------------
;	Direction C
;------------------------

(defrule question-C
	(ID C)
	=>
	(printout t "Which is your favourite? [1/2/3]" crlf)
	(printout t "1. Walking along the river and enjoy the beautiful night." crlf)
	(printout t "2. Walking along the beach and enjoy the fresh air." crlf)
	(printout t "3. Uniquely Singapore! Come close tonight and enjoy the wonderful experience with Night Safari!" crlf)
	(bind ?answer (read))
	(assert (C-A ?answer)))

;------------------------
;	Question C1
;------------------------

(defrule question-C1
	(C-A 1)
	=>
	(printout t "Which location is more convenient for you? [1/2]" crlf)
	(printout t "1. City Hall." crlf)
	(printout t "2. Kallang." crlf)
	(bind ?answer2 (read))
	(assert (C1a 1)))

(defrule Goal-C1a
	(C1a 1)
	=>
	(printout t "C1a Singapore River" crlf))

(defrule Goal-C1b
	(C1a 2)
	=>
	(printout t "C1b Kallang River" crlf))

;------------------------
;	Question C2
;------------------------

; Goto B3 Beach Module

;------------------------
;	Question C3
;------------------------

(defrule question-C3
	(C-A 3)
	=>
	(printout t "C3c Singapore Zoo- Night Safari" crlf))

;------------------------
;	Question D
;------------------------

(defrule Goal-D
	(ID D)
	=>
	(printout t "Singapore City Tour." crlf))