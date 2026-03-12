;; Lisp member check (Simplified from Text)
(defun my-member (atm a_list)
  (cond
    ((null a_list) nil)                  ; Case 1: Empty list (False)
    ((eq atm (car a_list)) t)            ; Case 2: Match found (True)
    (t (my-member atm (cdr a_list)))))   ; Case 3: Recurse on tail

;; Display sample results when this file is run.
(format t "Is B in (A B C)? ~A~%" (my-member 'B '(A B C)))
(format t "Is Z in (A B C)? ~A~%" (my-member 'Z '(A B C)))