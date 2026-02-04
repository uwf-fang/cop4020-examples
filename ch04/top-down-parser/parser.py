import sys
from enum import Enum, auto

# =============================================================================
# 1. TOKENS
# =============================================================================

class TokenType(Enum):
    INT_LIT = auto()       # Integer literals (e.g., 10, 42)
    IDENT = auto()         # Identifiers (e.g., sum, total)
    ASSIGN_OP = auto()     # =
    ADD_OP = auto()        # +
    SUB_OP = auto()        # -
    MULT_OP = auto()       # *
    DIV_OP = auto()        # /
    LEFT_PAREN = auto()    # (
    RIGHT_PAREN = auto()   # )
    EOF = auto()           # End of File

class Token:
    def __init__(self, type_: TokenType, value: str):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)})"

# =============================================================================
# 2. ABSTRACT SYNTAX TREE (AST) NODES
# =============================================================================

class AST:
    """Base class for all AST nodes."""
    pass

class BinOp(AST):
    """Represents a binary operation (e.g., left + right)."""
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __repr__(self):
        # Format: (left op right)
        return f"({self.left} {self.op.value} {self.right})"

class Num(AST):
    """Represents an integer number."""
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f"{self.value}"

class Var(AST):
    """Represents a variable/identifier."""
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f"Var({self.value})"

# =============================================================================
# 3. LEXER
# =============================================================================

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def error(self, msg="Invalid character"):
        raise Exception(f"Lexer Error: {msg}")

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates End of Input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.INT_LIT, result)

    def identifier(self):
        """Handle identifiers (variables)."""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return Token(TokenType.IDENT, result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)"""
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char.isdigit():
                return self.integer()

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.ADD_OP, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.SUB_OP, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULT_OP, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV_OP, '/')

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LEFT_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RIGHT_PAREN, ')')

            self.error(f"Unknown character: {self.current_char}")

        return Token(TokenType.EOF, None)

# =============================================================================
# 4. PARSER (UPDATED TO BUILD AST)
# =============================================================================

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, msg="Invalid syntax"):
        raise Exception(f"Parser Error: {msg}")

    def eat(self, token_type):
        """
        Compare the current token type with the passed token type.
        If they match, 'eat' the current token and advance to the next.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type.name}, got {self.current_token.type.name}")

    def factor(self):
        """
        factor : IDENT | INT_LIT | LPAREN expr RPAREN
        """
        token = self.current_token

        if token.type == TokenType.INT_LIT:
            self.eat(TokenType.INT_LIT)
            return Num(token)  # Return a Leaf Node (Number)

        elif token.type == TokenType.IDENT:
            self.eat(TokenType.IDENT)
            return Var(token)  # Return a Leaf Node (Variable)

        elif token.type == TokenType.LEFT_PAREN:
            self.eat(TokenType.LEFT_PAREN)
            node = self.expr() # Recurse
            self.eat(TokenType.RIGHT_PAREN)
            return node        # Return the sub-tree result

        self.error("Expected identifier, integer, or left parenthesis")

    def term(self):
        """
        term : factor ((MULT | DIV) factor)*
        """
        # 1. Get the left-hand side
        node = self.factor()

        # 2. Iterate while we see * or /
        while self.current_token.type in (TokenType.MULT_OP, TokenType.DIV_OP):
            token = self.current_token
            if token.type == TokenType.MULT_OP:
                self.eat(TokenType.MULT_OP)
            elif token.type == TokenType.DIV_OP:
                self.eat(TokenType.DIV_OP)

            # 3. Create a BinOp node:
            #    Left child = the 'old' node
            #    Right child = the result of the next factor()
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
        # 1. Get the left-hand side
        node = self.term()

        # 2. Iterate while we see + or -
        while self.current_token.type in (TokenType.ADD_OP, TokenType.SUB_OP):
            token = self.current_token
            if token.type == TokenType.ADD_OP:
                self.eat(TokenType.ADD_OP)
            elif token.type == TokenType.SUB_OP:
                self.eat(TokenType.SUB_OP)

            # 3. Create a BinOp node
            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        """Main entry point."""
        if self.current_token.type == TokenType.EOF:
            return None

        result = self.expr()

        if self.current_token.type != TokenType.EOF:
            self.error("Unexpected symbols after end of expression")

        return result

# =============================================================================
# 5. MAIN DRIVER
# =============================================================================

def main():
    # Read expression from standard input
    input_text = input().strip()

    print(f"Input Expression: {input_text}")
    print("-" * 30)

    lexer = Lexer(input_text)
    parser = Parser(lexer)

    try:
        syntax_tree = parser.parse()
        print("Generated Parse Tree (AST):")
        print(syntax_tree)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
