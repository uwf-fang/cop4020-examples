% Einstein's Riddle Solver in Prolog
% https://www.rd.com/article/einsteins-riddle-solve-it/
% The puzzle: There are 5 houses in 5 different colors. In each house lives a person
% of a different nationality. These 5 owners drink a certain beverage, smoke a certain
% brand of cigar, and keep a certain pet. No owners have the same pet, smoke the same
% brand of cigar, or drink the same beverage.

% The question: Who owns the zebra?

% The clues:
% 1. The Brit lives in the red house.
% 2. The Swede keeps dogs as pets.
% 3. The Dane drinks tea.
% 4. The green house is on the left of the white house.
% 5. The green house owner drinks coffee.
% 6. The person who smokes Pall Mall keeps birds.
% 7. The owner of the yellow house smokes Dunhill.
% 8. The man living in the center house drinks milk.
% 9. The Norwegian lives in the first house.
% 10. The man who smokes Blend lives next to the one who keeps cats.
% 11. The man who keeps horses lives next to the man who smokes Dunhill.
% 12. The owner who smokes Blue Master drinks beer.
% 13. The German smokes Prince.
% 14. The Norwegian lives next to the blue house.
% 15. The man who smokes Blend has a neighbor who drinks water.

% Define the solution structure
solution(Houses) :-
    % Houses is a list of 5 houses
    length(Houses, 5),
    
    % Each house is represented as house(Color, Nationality, Pet, Drink, Smoke)
    member(house(red, brit, _, _, _), Houses),            % Clue 1
    member(house(_, swede, dogs, _, _), Houses),          % Clue 2
    member(house(_, dane, _, tea, _), Houses),            % Clue 3
    left_of(house(green, _, _, _, _), house(white, _, _, _, _), Houses), % Clue 4
    member(house(green, _, _, coffee, _), Houses),        % Clue 5
    member(house(_, _, birds, _, 'Pall Mall'), Houses),   % Clue 6
    member(house(yellow, _, _, _, dunhill), Houses),      % Clue 7
    Houses = [_, _, house(_, _, _, milk, _), _, _],       % Clue 8
    Houses = [house(_, norwegian, _, _, _) | _],          % Clue 9
    next_to(house(_, _, _, _, blend), house(_, _, cats, _, _), Houses), % Clue 10
    next_to(house(_, _, horses, _, _), house(_, _, _, _, dunhill), Houses), % Clue 11
    member(house(_, _, _, beer, 'Blue Master'), Houses),  % Clue 12
    member(house(_, german, _, _, prince), Houses),       % Clue 13
    next_to(house(_, norwegian, _, _, _), house(blue, _, _, _, _), Houses), % Clue 14
    next_to(house(_, _, _, _, blend), house(_, _, _, water, _), Houses), % Clue 15
    
    % The rest of the constraints to ensure unique values
    member(house(_, _, zebra, _, _), Houses),
    
    % Ensure each house has a unique color
    findall(Color, member(house(Color, _, _, _, _), Houses), Colors),
    all_different(Colors),
    
    % Ensure each nationality occurs exactly once
    findall(Nation, member(house(_, Nation, _, _, _), Houses), Nations),
    all_different(Nations),
    
    % Ensure each pet occurs exactly once
    findall(Pet, member(house(_, _, Pet, _, _), Houses), Pets),
    all_different(Pets),
    
    % Ensure each drink occurs exactly once
    findall(Drink, member(house(_, _, _, Drink, _), Houses), Drinks),
    all_different(Drinks),
    
    % Ensure each smoke brand occurs exactly once
    findall(Smoke, member(house(_, _, _, _, Smoke), Houses), Smokes),
    all_different(Smokes).

% Helper predicate: X is to the left of Y in the list
left_of(X, Y, List) :-
    append(_, [X, Y | _], List).

% Helper predicate: X is next to Y in the list
next_to(X, Y, List) :-
    append(_, [X, Y | _], List).
next_to(X, Y, List) :-
    append(_, [Y, X | _], List).

% Helper predicate: All elements in a list are different
all_different([]).
all_different([H | T]) :-
    \+ member(H, T),
    all_different(T).

% Query to find out who owns the zebra
zebra_owner(Owner) :-
    solution(Houses),
    member(house(_, Owner, zebra, _, _), Houses).

% Query to find out who drinks water
water_drinker(Owner) :-
    solution(Houses),
    member(house(_, Owner, _, water, _), Houses).

% Run the complete solution and print it out nicely
solve_and_print :-
    solution(Houses),
    write('Houses from left to right:'), nl,
    print_houses(Houses),
    zebra_owner(ZebraOwner),
    water_drinker(WaterDrinker),
    write('The '), write(ZebraOwner), write(' owns the zebra.'), nl,
    write('The '), write(WaterDrinker), write(' drinks water.'), nl.

% Helper predicate to print houses in a readable format
print_houses([]).
print_houses([house(Color, Nation, Pet, Drink, Smoke) | Rest]) :-
    write('House: '), write(Color), nl,
    write('  Nationality: '), write(Nation), nl,
    write('  Pet: '), write(Pet), nl,
    write('  Drink: '), write(Drink), nl,
    write('  Smoke: '), write(Smoke), nl, nl,
    print_houses(Rest).

% Main entry point
:- solve_and_print.
