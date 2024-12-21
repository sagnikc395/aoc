#lang racket

;; reading advent of code input from files and print

(define (load/print path
                    #:namespace (namespace (current-namespace))
                    #:printer (printer println)
                    #:supress-void (supress-void #t))

  ;; if the file starts with #lang &c , this will let it be read, but
  ;; printing won't generally be helpful in that case as it will be read usually as a single module ... form

  (parameterize* ([read-accept-reader #t]
                  [read-accept-lang #t])

    (call-with-input-file
      path
      (lamb (in)
            (for ([form (in-port (lamb (p) (read-syntax path p)) in)])
              (call-with-values
               (thunk (eval form namespace))
               (lamb vals
                     (for ([v (in-list vals)])
                       (unless (and supress-void (void? v))
                         (printer v)))))
              path)))))

