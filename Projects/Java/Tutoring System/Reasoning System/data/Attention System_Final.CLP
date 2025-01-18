;----------------
;  Student State
;----------------

(deftemplate student-state
	(slot external-state-emotion)
	(slot external-state-gaze)
	(slot external-state-body)
	(slot external-state-head)
	(slot internal-state-answer)
	(slot internal-state-time)
	(slot internal-state-repeat)
	(slot internal-state-consistent)
	(slot state-motivation)
	(slot state-concentration)
	(slot state-misconception)
	(slot state-knowledge)
	(slot state-capacity))

(deffacts student-state-facts
	(student-state (external-state-emotion happy))
	(student-state (external-state-emotion sad))
	(student-state (external-state-gaze straight))
	(student-state (external-state-gaze sideway))
	(student-state (external-state-body forward))
	(student-state (external-state-body backward))
	(student-state (external-state-head nodding))
	(student-state (external-state-head shaking))
	(student-state (internal-state-answer correct))
	(student-state (internal-state-answer wrong))
	(student-state (internal-state-time long))
	(student-state (internal-state-time short))
	(student-state (internal-state-repeat one))
	(student-state (internal-state-repeat many))
	(student-state (internal-state-consistent consistent))
	(student-state (internal-state-consistent inconsistent))
	(student-state (state-motivation low))
	(student-state (state-motivation high))
	(student-state (state-concentration low))
	(student-state (state-concentration high))
	(student-state (state-misconception low))
	(student-state (state-misconception high))
	(student-state (state-knowledge low))
	(student-state (state-knowledge high))
	(student-state (state-capacity low))
	(student-state (state-capacity high)))

;----------------------------------------------
; Determine student's state from sensory system
;----------------------------------------------

;;;Determine emotional level of student
(defrule get-emotion
	=>
	(printout t "What is the emotional state of the student? [happy | sad]" crlf)
	(bind ?emotion (read))
	(assert (student-state (external-state-emotion ?emotion)))
	(printout t "The emotional state of the student is " ?emotion "!" crlf))

;;;Determine gaze direction of student
(defrule get-gaze
	(or (student-state (external-state-emotion happy))
	    (student-state (external-state-emotion sad)))
	=>
	(printout t "What is the gaze direction of the student? [straight | sideway]" crlf)
	(bind ?gaze (read))
	(assert (student-state (external-state-gaze ?gaze)))
	(printout t "The student is looking " ?gaze crlf))

;;;Student has high concentration level if gazing straight
(defrule gaze-concentration-high
	(student-state (external-state-gaze straight))
	=>
	(assert (student-state (state-concentration high)))
	(printout t "The student has high concentration level!" crlf))

;;;Student has low concentration level if gazing sideway
(defrule gaze-concentration-low
	(student-state (external-state-gaze sideway))
	=>
	(assert (student-state (state-concentration low)))
	(printout t "The student has low concentration level!" crlf))

;;;Determine body posture of student
(defrule get-body
	(or (student-state (external-state-gaze straight))
	    (student-state (external-state-gaze sideway)))
	=>
	(printout t "Is the student leaning his body forward or backward [forward | backward]" crlf)
	(bind ?body (read))
	(assert (student-state (external-state-body ?body)))
	(printout t "The student is leaning his body " ?body crlf))

;;;Student has low motivation level if leaning body backwards
(defrule body-motivation-low
	(student-state (external-state-body backward))
	=>
	(assert (student-state (state-motivation low)))
	(printout t "The student has low motivation level!" crlf))

;;;Student has high motivation level if leaning body forward
(defrule body-motivation-high
	(student-state (external-state-body forward))
	=>
	(assert (student-state (state-motivation high)))
	(printout t "The student has high motivation level!" crlf))

;;;Determine head gesture of student
(defrule get-head
	(or (student-state (external-state-body forward))
	    (student-state (external-state-body backward)))
	=>
	(printout t "Is the student nodding or shaking his head? [nodding | shaking]" crlf)
	(bind ?head (read))
	(assert (student-state (external-state-head ?head)))
	(printout t "The student is " ?head " his head!" crlf))

;;;Student has low knowledge level if shaking head
(defrule head-knowledge-low
	(student-state (external-state-head shaking))
	=>
	(assert (student-state (state-knowledge low)))
	(printout t "The student has low knowledge level!" crlf))

;;;Student has high knowledge level if nodding head
(defrule head-knowledge-high
	(student-state (external-state-head nodding))
	=>
	(assert (student-state (state-knowledge high)))
	(printout t "The student has high knowledge level!" crlf))

;------------------------------------------------
; Determine student's state from reasoning system
;------------------------------------------------

;;;Determine student's knowledge and misconception level from questioning
(defrule get-answer
	(or (student-state (external-state-head shaking))
	    (student-state (external-state-head nodding)))
	=>
	(printout t "Is the student's answer correct or incorrect? [correct | incorrect]" crlf)
	(bind ?answer (read))
	(assert (student-state (internal-state-answer ?answer)))
	(printout t "The student's answer is " ?answer " !" crlf))

;;;Student has low knowledge level if answer incorrectly
(defrule answer-knowledge-low
	(student-state (internal-state-answer incorrect))
	=>
	(assert (student-state (state-knowledge low)))
	(printout t "The student has low knowledge level!" crlf))

;;;Student has high knowledge level if answer correctly
(defrule answer-knowledge-high
	(student-state (internal-state-answer correct))
	=>
	(assert (student-state (state-knowledge high)))
	(printout t "The student has high knowledge level!" crlf))

;;;Student has high misconception level if answer incorrectly
(defrule answer-misconception-high
	(student-state (internal-state-answer incorrect))
	=>
	(assert (student-state (state-misconception high)))
	(printout t "The student has high misconception level!" crlf))

;;;Student has low misconception level if answer correctly 
(defrule answer-misconception-low
	(student-state (internal-state-answer correct))
	=>
	(assert (student-state (state-misconception low)))
	(printout t "The student has low misconception level!" crlf))

;;;Determine student's learning capacity from answering time
(defrule answer-time
	(or (student-state (internal-state-answer correct))
	    (student-state (internal-state-answer incorrect)))
	=>
	(printout t "Did the student take a long or short time to answer the question correctly? [long | short]")
	(bind ?time (read))
	(assert (student-state (internal-state-time ?time)))
	(printout t "The student takes a " ?time " time!" crlf))

;;;Student has low learning capacity if takes a long time to answer question correctly
(defrule time-capacity-low
	(student-state (internal-state-time long))
	=>
	(assert (student-state (state-capacity low)))
	(printout t "The student has low learning capacity!" crlf))

;;;Student has high learning capacity if takes a short time to answer question correctly
(defrule time-capacity-high
	(student-state (internal-state-time short))
	=>
	(assert (student-state (state-capacity high)))
	(printout t "The student has high learning capacity!" crlf))

;;;Determine student's concentration level from repeating similar questions 
(defrule repeat-question
	(or (student-state (internal-state-time long))
	    (student-state (internal-state-time short)))
	=>
	(printout t "Did the student ask to repeat similar questions one time or many times? [one | many]" crlf)
	(bind ?repeat (read))
	(assert (student-state (internal-state-repeat ?repeat)))
	(printout t "The student ask to repeat similar questions " ?repeat " time(s)!" crlf))

;;;Student has low concentration level if student ask to repeat similar questions more than once
(defrule repeat-concentration-low
	(student-state (internal-state-repeat many))
	=>
	(assert (student-state (state-concentration low)))
	(printout t "The student has low concentration level!" crlf))

;;;Student has high concentration level if ask to repeat question only once
(defrule repeat-concentration-high
	(student-state (internal-state-repeat one))
	=>
	(assert (student-state (state-concentration high)))
	(printout t "The student has high concentration level!" crlf))

;;;Determine motivation level of student from consistency in answering questions correctly
(defrule answer-consistent
	(or (student-state (internal-state-repeat one))
	    (student-state (internal-state-repeat many)))
	=>
	(printout t "Is the student consistent or inconsistent in getting the answer right? [consistent | inconsistent]" crlf)
	(bind ?consistent (read))
	(assert (student-state (internal-state-consistent ?consistent)))
	(printout t "The student is " ?consistent " in getting the right answer!" crlf))

;;;Student has high motivation level if consistent in answering questions correctly
(defrule consistent-motivation-high
	(student-state (internal-state-consistent consistent))
	=>
	(assert (student-state (state-motivation high)))
	(printout t "The student high motivation level!" crlf))

;;;Student has low motivation level if inconsistent in answering questions correctly
(defrule consistent-motivation-low
	(student-state (internal-state-consistent inconsistent))
	=>
	(assert (student-state (state-motivation low)))
	(printout t "The student low motivation level!" crlf))

;---------------------------------------------------------------------
;Determine salient student's state and activate planner and recognizer
;--------------------------------------------------------------------- 

;;;Activate emotion planner and emotion recognizer if student is sad.
(defrule activate-emotion-planner
	(declare (salience 3000))
	(and(and(and(and(and(student-state (external-state-emotion sad))
	                    (or(student-state (state-motivation low))
			       (student-state (state-motivation high))))
			    (or(student-state (state-concentration low))
                               (student-state (state-concentration high))))
                            (or(student-state (state-knowledge low))
                               (student-state (state-knowledge high))))
                            (or(student-state (state-capacity low))
                               (student-state (state-capacity high))))
                            (or(student-state (state-misconception low))
                               (student-state (state-misconception high))))
	=>
	(printout t "Activate emotion planner!" crlf)
	(printout t "Activate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))

;;;Activate motivation planner and body posture recognizer if student is happy but unmotivated.
(defrule activate-motivation-planner
	(declare (salience 2000))
	(and(and(and(and(and(student-state (state-motivation low))
			    (student-state (external-state-emotion happy)))
			    (or(student-state (state-concentration low))
                               (student-state (state-concentration high))))
                            (or(student-state (state-knowledge low))
                               (student-state (state-knowledge high))))
                            (or(student-state (state-capacity low))
                               (student-state (state-capacity high))))
                            (or(student-state (state-misconception low))
                               (student-state (state-misconception high))))
	=>
	(printout t "Activate motivation planner!" crlf)
	(printout t "Activate posture recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))

;;;Activate concentration planner and gaze recognizer if student is happy and motivated but has low concentration level.
(defrule activate-concentration-planner
	(declare (salience 1000))
	(and(and(and(and(and(student-state (state-concentration low))
	                    (student-state (external-state-emotion happy)))
	                    (student-state (state-motivation high)))
	    	            (or(student-state (state-knowledge low))
                               (student-state (state-knowledge high))))
 		            (or(student-state (state-misconception low))
                               (student-state (state-misconception high))))
		            (or(student-state (state-capacity low))
                               (student-state (state-capacity high))))
	=>
	(printout t "Activate concentration planner!" crlf)
	(printout t "Activate gaze recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))

;;;Activate knowledge planner and capacity planner if student is happy, motivated, has high concentration level and has low misconception level but has low ;;;knowledge level and low learning capacity. 
(defrule activate-knowledge-planner-capacity-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge low)))
		            (student-state (state-misconception low)))
			    (student-state (state-capacity low)))
	=>
	(printout t "Activate knowledge planner!" crlf)
	(printout t "Activate capacity planner!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf))

;;;Activate knowledge planner if student is happy, motivated, has high concentration level, has high learning capacity and low misconception level but has ;;;low knowledge level.
(defrule activate-knowledge-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge low)))
		            (student-state (state-misconception low)))
			    (student-state (state-capacity high)))
	=>
	(printout t "Activate knowledge planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))

;;;Activate knowledge planner, misconception planner and capacity planner if student is happy, motivated, has high concentration level but has low knowledge ;;;level, high misconception level and low learning capacity. 
(defrule activate-knowledge-planner-misconception-planner-capacity-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge low)))
		            (student-state (state-misconception high)))
			    (student-state (state-capacity low)))
	=>
	(printout t "Activate knowledge planner!" crlf)
	(printout t "Activate misconception planner!" crlf)
	(printout t "Activate capacity planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf))

;;;Activate knowledge planner and misconception planner if student is happy, motivated, has high concentration level and high learning capacity but has low ;;;knowledge level. 
(defrule activate-knowledge-planner-misconception-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge low)))
		            (student-state (state-misconception high)))
			    (student-state (state-capacity high)))
	=>
	(printout t "Activate knowledge planner!" crlf)
	(printout t "Activate misconception planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))

;;;Activate capacity planner if student is happy, motivated, has high concentration level, high knowledge level and low misconception level, but has low ;;;learning capacity. 
(defrule activate-capacity-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge high)))
		            (student-state (state-misconception low)))
			    (student-state (state-capacity low)))
	=>
	(printout t "Activate capacity planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate misconception planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf))

;;;Activate misconception planner and capacity planner if student is happy, motivated, has high concentration level, high knowledge level but ;;;high misconception level and low learning capacity. 
(defrule activate-misconception-planner-capacity-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge high)))
		            (student-state (state-misconception high)))
			    (student-state (state-capacity low)))
	=>
	(printout t "Activate capacity planner!" crlf)
	(printout t "Activate misconception planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf))

;;;Activate misconception planner if student is happy, motivated, has high concentration level, has high knowledge level and high learning capacity but ;;;high misconception level. 
(defrule activate-misconception-planner-capacity-planner
	(declare (salience 0))
	(and(and(and(and(and(student-state (external-state-emotion happy))
	                    (student-state (state-motivation high)))
	                    (student-state (state-concentration high)))
		            (student-state (state-knowledge high)))
		            (student-state (state-misconception high)))
			    (student-state (state-capacity high)))
	=>
	(printout t "Activate misconception planner!" crlf)
	(printout t "Deactivate gesture recognizer!" crlf)
	(printout t "Deactivate posture recognizer!" crlf)
	(printout t "Deactivate emotion recognizer!" crlf)
	(printout t "Deactivate gaze recognizer!" crlf)
	(printout t "Deactivate emotion planner!" crlf)
	(printout t "Deactivate motivation planner!" crlf)
	(printout t "Deactivate concentration planner!" crlf)
	(printout t "Deactivate knowledge planner!" crlf)
	(printout t "Deactivate capacity planner!" crlf))













