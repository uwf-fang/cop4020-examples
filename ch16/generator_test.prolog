% 1. THE GENERATOR
% This creates an infinite stream of candidate integers (0, 1, 2...).
is_integer(0).
is_integer(X) :-
    is_integer(Y),
    X is Y + 1.

% 2. THE TESTER
% Checks if the generated integer solves our specific math problem.
is_valid_solution(X) :-
    X > 100,            % Test A: Must be greater than 100
    0 is X mod 7,       % Test B: Must be divisible by 7
    0 is X mod 13.      % Test C: Must be divisible by 13

% 3. THE COMPLETE STRATEGY
% Combines generating, testing, and the "Hard Stop".
find_answer(X) :-
    is_integer(X),      % Generate a candidate
    is_valid_solution(X), % Test the candidate
    !.                  % THE CUT: Stop the search once found.
