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

        # if character is invalid
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        
        tokens.append(token)

    return tokens

def signs(ls, index, tokens):
    if index + 1 < ls:
        if tokens[index + 1]['type'] == 'MULTIPLY' or tokens[index + 1]['type'] == 'DIVIDE':
            return True
    return False

def ranged(tokens, index):
    # first number in operation
    if tokens[index + 1]['type'] == 'MULTIPLY':
        answer = tokens[index]['number'] * tokens[index + 2]['number']
    elif tokens[index + 1]['type'] == 'DIVIDE':
        answer = tokens[index]['number'] / tokens[index + 2]['number']
    return answer


def evaluate(tokens):
    index = 1 
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    while index < len(tokens):
        if tokens[index]['type'] == 'OBRACKET':
            print("as")
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                if signs(len(tokens), index, tokens):
                    answer += ranged(tokens, index)
                    index += 3
                else:
                    answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                if signs(len(tokens), index, tokens):
                    answer -= ranged(tokens, index)
                    index += 3
                else:
                    answer -= tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MULTIPLY':
                answer *= tokens[index][number]
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


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
    test("2+9/3")
    test("2-9*2")
    test("2*3")
    test("6/4")
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
