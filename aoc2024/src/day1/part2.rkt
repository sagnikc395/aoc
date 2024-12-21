#lang racket

(define (main)
  ;; Read file contents
  (define p (string-trim (file->string "input.txt")))
  ;; Split the input into lines
  (define lines (string-split p "\n"))
  ;; Initialize ll and rc (a hash table for counts)
  (define ll '())
  (define rc (make-hash))

  ;; Process each line
  (for ([line lines])
    (define-values (l r)
      (match (map string->number (string-split line))
        [(list l r) (values l r)]))
    (set! ll (cons l ll))
    (hash-set! rc r (+ 1 (hash-ref rc r 0))))

  ;; Sort ll
  (define sorted-ll (sort ll <))

  ;; Calculate the result
  (define ans 0)
  (for ([l sorted-ll])
    (set! ans (+ ans (* l (hash-ref rc l 0)))))

  ;; Print the result
  (displayln ans))

;; Run the main function
(main)
