; Direcion F

(deftemplate roughgoal
	(slot ID))

(deffacts Fire-F
	(roughgoal (ID F)))

(defrule question-F
	(roughgoal (ID F))
	=>
	(printout t "Which is your favourite? [1/2]" crlf)
	(printout t "1. Amazing night city." crlf)
	(printout t "2. Special experience." crlf)
	(bind ?answer (read))
	(assert (F-A ?answer))
)

(defrule question-F1
	(F-A 1)
	=>
	(printout t "Singapore Night city tour" crlf))

(defrule question-F2
	(F-A 2)
	=>
	(printout t "Singapore Flyer" crlf))

