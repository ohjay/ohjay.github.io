; Discussion Quiz 7

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
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (finish-sort lst)
  (cond 
    ((or (null? lst)
         (null? (cdr lst))) lst)
    ((> (car lst) (cadr lst)) (append (list (cadr lst))
                                      (list (car lst))
                                      (cddr lst)))
    (else (let ((rest (finish-sort (cdr lst))))
               (if (< (car lst) (car rest))
                   (cons (car lst) rest)
                   (append (list (car rest))
                           (list (car lst))
                           (cdr rest)))))
  )
)
