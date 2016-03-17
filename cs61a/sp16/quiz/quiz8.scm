; 1(d)
(define (remainder m n)
  (if (> n m) m (remainder (- m n) n)))
  
; 2
(+ (and 0 (or #f 1)) 2)
(cons 5 6)

(define x (+))
(define y +)
; (x 3 4)

(y 3 4)

(define (mystery lst)
  (cond ((null? lst) nil)
    ((= (modulo (car lst) 2) 1) (cons (car lst) (mystery (cdr lst))))
    (else (mystery (cdr lst)))))
(mystery (list 1 2 3 4))
