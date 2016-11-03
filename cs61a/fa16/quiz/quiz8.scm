; Discussion Quiz 8

; Q1a
(define (copy lst result)
  (if (null? lst)
      result
      ((lambda (copy) copy)
        (copy (cdr lst)
              (append result (list (car lst)))
        )
      )
  )
)

; Q1b
(define (broken lst) (broken (broken lst)))

; Q1c
(define (is-ascending lst last-num)
  (if (null? lst)
      #t
      (and (is-ascending (cdr lst)
                         (car lst))
           (> (car lst) last-num)
      )
  )
)

; Q2
(define (hailstone n)
  (define (hs-helper n lst)
    (cond ((= n 1) (append lst (list 1)))
          ((even? n) (hs-helper (/ n 2)
                                (append lst (list n))))
          (else (hs-helper (+ 1 (* 3 n))
                           (append lst (list n))))
    )
  )
  (hs-helper n '())
)
