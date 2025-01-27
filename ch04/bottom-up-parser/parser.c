/* lr_parser.c - an LR parser for arithmetic expressions */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Maximum sizes */
#define MAX_STACK 100
#define MAX_LEXEME 100
#define MAX_INPUT 1000

/* Character classes */
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99

/* Token codes */
#define ID 1
#define PLUS 2
#define MULT 3
#define LPAREN 4
#define RPAREN 5
#define END 6

/* Grammar symbols (for GOTO table) */
#define E 0
#define T 1
#define F 2

/* Action types */
#define SHIFT 's'
#define REDUCE 'r'
#define ACCEPT 'a'
#define ERROR 'e'

/* Grammar rules */
#define NUM_RULES 6
struct {
    int lhs;        /* Left-hand side nonterminal */
    int rhs_length; /* Number of symbols on right-hand side */
} rules[NUM_RULES + 1] = {
    {0, 0},    /* Rule 0 - not used */
    {E, 3},    /* Rule 1: E -> E + T */
    {E, 1},    /* Rule 2: E -> T */
    {T, 3},    /* Rule 3: T -> T * F */
    {T, 1},    /* Rule 4: T -> F */
    {F, 3},    /* Rule 5: F -> ( E ) */
    {F, 1}     /* Rule 6: F -> id */
};

/* Parser tables */
char action[12][7] = {
    /*          id  +   *   (   )   $  */
    /* 0  */ {'s', ' ', ' ', 's', ' ', ' '},  /* s5, s4 */
    /* 1  */ {' ', 's', ' ', ' ', ' ', 'a'},  /* s6, accept */
    /* 2  */ {' ', 'r', 's', ' ', 'r', 'r'},  /* r2, s7, r2 */
    /* 3  */ {' ', 'r', 'r', ' ', 'r', 'r'},  /* r4, r4, r4 */
    /* 4  */ {'s', ' ', ' ', 's', ' ', ' '},  /* s5, s4 */
    /* 5  */ {' ', 'r', 'r', ' ', 'r', 'r'},  /* r6, r6, r6 */
    /* 6  */ {'s', ' ', ' ', 's', ' ', ' '},  /* s5, s4 */
    /* 7  */ {'s', ' ', ' ', 's', ' ', ' '},  /* s5, s4 */
    /* 8  */ {' ', 's', ' ', ' ', 's', ' '},  /* s6, s11 */
    /* 9  */ {' ', 'r', 's', ' ', 'r', 'r'},  /* r1, s7, r1 */
    /* 10 */ {' ', 'r', 'r', ' ', 'r', 'r'},  /* r3, r3, r3 */
    /* 11 */ {' ', 'r', 'r', ' ', 'r', 'r'}   /* r5, r5, r5 */
};

int action_value[12][7] = {
    {5, 0, 0, 4, 0, 0},
    {0, 6, 0, 0, 0, 0},
    {0, 2, 7, 0, 2, 2},
    {0, 4, 4, 0, 4, 4},
    {5, 0, 0, 4, 0, 0},
    {0, 6, 6, 0, 6, 6},
    {5, 0, 0, 4, 0, 0},
    {5, 0, 0, 4, 0, 0},
    {0, 6, 0, 0, 11, 0},
    {0, 1, 7, 0, 1, 1},
    {0, 3, 3, 0, 3, 3},
    {0, 5, 5, 0, 5, 5}
};

int goto_table[12][3] = {
    /*    E  T  F */
    /* 0  */ {1, 2, 3},
    /* 1  */ {0, 0, 0},
    /* 2  */ {0, 0, 0},
    /* 3  */ {0, 0, 0},
    /* 4  */ {8, 2, 3},
    /* 5  */ {0, 0, 0},
    /* 6  */ {0, 9, 3},
    /* 7  */ {0, 0, 10},
    /* 8  */ {0, 0, 0},
    /* 9  */ {0, 0, 0},
    /* 10 */ {0, 0, 0},
    /* 11 */ {0, 0, 0}
};

/* Global variables */
int stack[MAX_STACK];       /* Parser stack */
int top = -1;              /* Stack top pointer */
char input[MAX_INPUT];     /* Input string */
int input_pos = 0;         /* Current position in input */
char lexeme[MAX_LEXEME];   /* Current lexeme */
int token;                 /* Current token */

/* Function declarations */
void push(int value);
int pop(void);
void error(char *message);
int lex(void);
void parse(void);
int get_token_code(char *lexeme);
void print_stack(void);
void print_production(int rule);

/* Stack operations */
void push(int value) {
    if (top >= MAX_STACK - 1) {
        error("Stack overflow");
    }
    stack[++top] = value;
}

int pop(void) {
    if (top < 0) {
        error("Stack underflow");
    }
    return stack[top--];
}

/* Error handling */
void error(char *message) {
    printf("Error: %s\n", message);
    exit(1);
}

/* Lexical analyzer */
int lex(void) {
    char c;
    int i = 0;

    /* Skip whitespace */
    while (input[input_pos] == ' ' || input[input_pos] == '\t') {
        input_pos++;
    }

    /* Check for end of input */
    if (input[input_pos] == '\0') {
        return END;
    }

    c = input[input_pos++];

    /* Build lexeme */
    lexeme[0] = c;
    lexeme[1] = '\0';

    /* Return token */
    switch (c) {
        case '+': return PLUS;
        case '*': return MULT;
        case '(': return LPAREN;
        case ')': return RPAREN;
        default:
            if (isalpha(c)) {
                return ID;
            }
            error("Invalid character");
    }
    return 0;
}

/* Parser */
void parse(void) {
    int state, t, next_state, rule_number;
    char action_type;

    /* Initialize */
    push(0);    /* Push initial state */
    token = lex();

    while (1) {
        state = stack[top];
        action_type = action[state][token - 1];
        next_state = action_value[state][token - 1];

        printf("\nStack: ");
        print_stack();
        printf("Input: %s, Token: %d\n", lexeme, token);
        printf("Action: %c%d\n", action_type, next_state);

        switch (action_type) {
            case SHIFT:
                push(token);      /* Push symbol */
                push(next_state); /* Push state */
                token = lex();
                break;

            case REDUCE:
                rule_number = next_state;
                print_production(rule_number);

                /* Pop 2 * rhs_length items */
                for (t = 0; t < 2 * rules[rule_number].rhs_length; t++) {
                    pop();
                }

                /* Push LHS */
                state = stack[top];
                push(rules[rule_number].lhs);
                push(goto_table[state][rules[rule_number].lhs]);
                break;

            case ACCEPT:
                printf("\nInput accepted!\n");
                return;

            case ERROR:
            default:
                error("Syntax error");
        }
    }
}

/* Print functions */
void print_stack(void) {
    int i;
    for (i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

void print_production(int rule) {
    printf("Reduce by rule %d: ", rule);
    switch (rule) {
        case 1: printf("E -> E + T\n"); break;
        case 2: printf("E -> T\n"); break;
        case 3: printf("T -> T * F\n"); break;
        case 4: printf("T -> F\n"); break;
        case 5: printf("F -> ( E )\n"); break;
        case 6: printf("F -> id\n"); break;
        default: printf("Unknown rule\n");
    }
}

/* Main function */
int main() {
    printf("Enter an arithmetic expression (use 'i' for identifiers): ");
    fgets(input, MAX_INPUT, stdin);
    input[strcspn(input, "\n")] = 0;  /* Remove newline */

    printf("\nStarting parse...\n");
    parse();

    return 0;
}