% Course Prerequisites in Prolog
% A simple model of course dependencies in a computer science curriculum

% course(Code, Name, Credits)
course(cs101, "Introduction to Programming", 3).
course(cs102, "Data Structures", 4).
course(cs201, "Algorithms", 4).
course(cs210, "Computer Organization", 3).
course(cs220, "Database Systems", 3).
course(cs230, "Software Engineering", 4).
course(cs310, "Operating Systems", 4).
course(cs340, "Artificial Intelligence", 3).
course(cs350, "Computer Networks", 3).
course(math101, "Calculus I", 4).
course(math102, "Calculus II", 4).
course(math201, "Discrete Mathematics", 3).

% prerequisite(Course, Prerequisite)
% To take Course, you must have completed Prerequisite
prerequisite(cs102, cs101).
prerequisite(cs201, cs102).
prerequisite(cs201, math201).
prerequisite(cs210, cs101).
prerequisite(cs220, cs102).
prerequisite(cs230, cs102).
prerequisite(cs310, cs210).
prerequisite(cs310, cs201).
prerequisite(cs340, cs201).
prerequisite(cs350, cs210).
prerequisite(math102, math101).
prerequisite(math201, math101).

% Transitive prerequisite relationship: 
% A course is a prerequisite if it's directly required or required for a prerequisite
prereq_chain(Course, Prereq) :- 
    prerequisite(Course, Prereq).
prereq_chain(Course, Prereq) :- 
    prerequisite(Course, Intermediate), 
    prereq_chain(Intermediate, Prereq).

% Find all prerequisites for a course
all_prerequisites(Course, Prerequisites) :-
    findall(Prereq, prereq_chain(Course, Prereq), Prerequisites).

% Check if a student can take a course given their completed courses
can_take(Course, CompletedCourses) :-
    course(Course, _, _),
    findall(Prereq, prerequisite(Course, Prereq), Prerequisites),
    subset(Prerequisites, CompletedCourses).

% Find all courses a student can take given their completed courses
available_courses(CompletedCourses, AvailableCourses) :-
    findall(Course, (course(Course, _, _), can_take(Course, CompletedCourses)), AvailableCourses).

% Sample query to find prerequisites for Artificial Intelligence course
:- write('Prerequisites for Artificial Intelligence:'), nl,
   all_prerequisites(cs340, Prerequisites),
   write(Prerequisites), nl, nl.

% Sample query to find available courses for a student who completed cs101 and math101
:- write('Available courses after completing cs101 and math101:'), nl,
   available_courses([cs101, math101], Available),
   write(Available), nl.
   