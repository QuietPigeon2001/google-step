#! /usr/bin/python3

def read_number(line, index):
    """
    Assign values to the numbers entered
    :type line: str
    :type index: int
    :rtype token: dict
    :rtype index: int
    """
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_open_bracket(line, index):
    token = {'type': 'OBRACKET'}
    return token, index + 1

def read_close_bracket(line, index):
    token = {'type': 'CBRACKET'}
    return token, index + 1


def tokenize(line):
    """
    Reads line of input
    :type: str
    :rtype: List[dict]
    """

    # Initialize list of tokens and order of token 
    tokens = []
    index = 0

    while index < len(line):
        # Check if character is a number
        if line[index].isdigit():
            (token, index) = read_number(line, index)

        # If it is an addition operation    
        elif line[index] == '+':
            (token, index) = read_plus(line, index)

        # If it is a subtraction operation
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        
        # If it is a multiplication operation
        elif line[index] == '*':
            (token, index) = read_multiply(line, index)
        
        # If it is a division operation
        elif line[index] == '/':
            (token, index) = read_divide(line, index)

        elif line[index] == '(':
            (token, index) = read_open_bracket(line, index)

        elif line[index] == ')':
            (token, index) = read_close_bracket(line, index)

        # If character is invalid
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        
        tokens.append(token)

    return tokens

def nested(tokens, start):
    """
    Calculates the value inside the parentheses and collapses the parentheses into its total value
    :type token: List[dict]
    :type start: int
    :rtype: List[dict]
    """

    def brackets(index):
        """
        Searches for the location of the close parenthesis 
        :type: int
        :rtype: int
        """
        while index < len(tokens):
            if tokens[index]['type'] == 'CBRACKET':
                return index
            index += 1

    close = brackets(start)

    # Calculates the total value inside parentheses
    num = calc(tokens, start + 1, close, tokens[start + 1]['number'])

    # Replaces open parentheses with num
    tokens[start] = {'type': 'NUMBER', 'number': num}

    # Shrinks parentheses
    del tokens[start + 1: close + 1]

    return tokens

def calc(tokens, start, end, val):
    """
    Main calculation function
    :type tokens: List[dict]
    :type start, end: int
    :type val: int or float
    :rtype answer: int or float
    """
    answer = val

    while start < end:
        if tokens[start]['type'] == 'NUMBER' or tokens[start]['type'] == 'OBRACKET':
            
            # If a pair of parentheses is found
            if tokens[start]['type'] == 'OBRACKET':
                
                # Updates tokens list and loop
                tokens = nested(tokens, start)
                end = len(tokens)
                                  
            # Value to be operated on
            n = tokens[start]['number']

            # Check if index goes out of bound
            if start + 1 < end and tokens[start + 1]['type'] == 'MULTIPLY':

                if tokens[start + 2]['type'] == 'OBRACKET':
                    bracket_start = start + 2
                    tokens = nested(tokens, bracket_start)
                    end = len(tokens)
                
                # Product of two values and shrinks the pair into the product
                n *= tokens[start + 2]['number']
                tokens[start] = {'type': 'NUMBER', 'number': n}
                del tokens[start + 1: start + 3]
                end = len(tokens)      
                    
            if start + 1 < end and tokens[start + 1]['type'] == 'DIVIDE':
                
                if tokens[start + 2]['type'] == 'OBRACKET':
                        bracket_start = start + 2
                        tokens = nested(tokens, bracket_start)
                        end = len(tokens)
                
                # Division of two values and shrinks the pair into the product
                n /= tokens[start + 2]['number']
                tokens[start] = {'type': 'NUMBER', 'number': n}
                del tokens[start + 1: start + 3]
                end = len(tokens)
            
            # Prioritises '*' and '/' operations
            if tokens[start - 1]['type'] == 'MULTIPLY':
                answer *= n
            elif tokens[start - 1]['type'] == 'DIVIDE':
                answer /= n
            elif tokens[start - 1]['type'] == 'PLUS':
                answer += n
            elif tokens[start - 1]['type'] == 'MINUS':
                answer -= n
        
        start += 1

    return answer

def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    return calc(tokens, 1, len(tokens), 0)
    
##########################################
# Check if code is correct
def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))

# Test cases
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("2+9*2")
    test("2-9*2")
    test("2*3")
    test("1-(5+1)")
    test("(5+2)*2")
    test("2*(5+2)")
    test("2+2*(5+1)")
    test("2+(5+1)*2")
    test("2+(5+2*12)*2")
    test("(2+1)*(2+1)")
    test("2*3*4")
    test("2*6/4")
    test("1")
    test("2+(2*3+2/4)")
    print("==== Test finished! ====\n")

run_test()
##########################################

while True:
    # Runs main program in an infinite loop
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
