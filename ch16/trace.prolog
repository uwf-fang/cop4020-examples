% Facts and Rules
likes(jake, sushi).
likes(jake, pizza).
likes(jake, logic).
likes(darcie, logic).
likes(darcie, pizza).
likes(bob, trout).
likes(bill, trout).
likes(bob, X) :- fish(X).
fish(trout).
fish(salmon).

/** <examples>
?- trace, likes(jake, X), likes(darcie, X).
*/
