;; Lisp member check (Simplified from Text)
(defun my-member (atm a_list)
  (cond
    ((null a_list) nil)                  ; Case 1: Empty list (False) [cite: 300]
    ((eq atm (car a_list)) t)            ; Case 2: Match found (True) [cite: 300]
    (t (my-member atm (cdr a_list)))))   ; Case 3: Recurse on tail [cite: 303]

;; (my-member 'B '(A B C)) -> Returns T