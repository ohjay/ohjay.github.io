; Discussion Quiz 8

; Q2
(define 2a '((list 2 3)))
(define 2b (list '(2 3)))
(define x (+))
(define y +)
; (define 2c (x 3 4)) [Error: cannot call: 0]
(define 2d (y 3 4))

; Q3
; (define 3a '(2 . 3 4)) [Error: expected one element after .]
(define 3b (cons (list '(two) '((3)) nil) 4))
(define 3c (cons 2 '(list nil)))
(define 3d (list (append '(2) '(3) nil) 4))
(define 3e '(2 . (3 . (4))))

; Q4
(define (take s n)
  (cond ((= n 0) (cons nil s))
        ((null? s) (cons s nil))
        (else (let ((rec (take (cdr s) (- n 1))))
              (cons (cons (car s) (car rec)) (cdr rec))))
  )
)
