:- use_module(library(clpfd)).

c(D) :-
  A in 1..1000,
  B in 1..1000,
  C in 1..1000,
  A * A + B * B #= C * C,
  A + B + C #= 1000,
  A #< B,
  B #< C,
  label([A, B, C]),
  D is A * B * C.