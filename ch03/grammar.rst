Example of a simple grammar
===========================

Description
-----------
This is a simple grammar for a calculator. The calculator can handle addition,
subtraction, multiplication, and division. The grammar is described in BNF and
EBNF.

Standard EBNF
-------------
The EBNF syntax follows the ISO/IEC 14977 standard.

.. code-block::

  expr = term, { ("+" | "-"), term } ;
  term = factor, { ("*" | "/"), factor } ;
  factor = identifier | integer | "(" expr ")" ;
  identifier = letter, { letter | digit } ;
  integer = digit, { digit } ;
  letter = "A" | "B" | "C" | ... | "Z" | "a" | "b" | "c" | ... | "z" ;
  digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

Standard BNF
------------
The BNF syntax follows the ALGOL 60 report.

.. code-block::

  <expr> ::= <term> | <expr> "+" <term> | <expr> "-" <term>
  <term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
  <factor> ::= <identifier> | <integer> | "(" <expr> ")"
  <identifier> ::= <letter> | <identifier> <letter> | <identifier> <digit>
  <integer> ::= <digit> | <integer> <digit>
  <letter> ::= "A" | "B" | "C" | ... | "Z" | "a" | "b" | "c" | ... | "z"
  <digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

The following is the Dragon Book's modern BNF syntax. This syntax is more
suitable for syntax analyzer design.

.. code-block::

  expr    → term term_tail
  term    → factor factor_tail
  term_tail → + term term_tail
            | - term term_tail
            | ε
  factor_tail → * factor factor_tail
              | / factor factor_tail
              | ε
  factor  → id
          | number
          | ( expr )
  id      → letter (letter | digit)*
  number  → digit+
  letter  → A | B | C | ... | Z | a | b | c | ... | z
  digit   → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Chomsky's Formal Language Syntax
--------------------------------

.. code-block::

  S → E
  E → T | E + T | E - T
  T → F | T * F | T / F
  F → a | n | (E)
  a → L | aL | aD
  n → D | nD
  L → b
  D → c

  where:
  b ∈ {A,...,Z,a,...,z}
  c ∈ {0,...,9}
