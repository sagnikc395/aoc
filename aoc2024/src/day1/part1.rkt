
#lang racket

(define (main)
  ;; Read file contents
  (define p (file->string "input.txt"))
  ;; Split the input into lines and then split each line into numbers
  (define lines (map (λ (line)
                       (map string->number (string-split line)))
                     (string-split p "\n")))

  ;; Separate ll and rr from lines
  (define ll (map first lines))
  (define rr (map second lines))

  ;; Sort ll and rr
  (define sorted-ll (sort ll <))
  (define sorted-rr (sort rr <))

  ;; Calculate the sum of absolute differences
  (define ans (for/sum ([l sorted-ll] [r sorted-rr])
               (abs (- l r))))

  ;; Print the result
  (displayln ans))

;; Run the main function
(main)

