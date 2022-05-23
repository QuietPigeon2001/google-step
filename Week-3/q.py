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

def signs(index, tokens):
    if index + 1 < len(tokens):
        if tokens[index + 1]['type'] == 'MULTIPLY' or tokens[index + 1]['type'] == 'DIVIDE':
            return True
    return False

def brackets(tokens, index):
    # Finds bracket pair
    while index < len(tokens):
        if tokens[index]['type'] == 'CBRACKET':
            return index
        index += 1

def ranged(tokens, index):
    # first number in operation
    if tokens[index + 2]['type'] == 'OBRACKET':
        n = nested(tokens, index)[0]
    else:
        n = tokens[index + 2]['number']
    if tokens[index + 1]['type'] == 'MULTIPLY':
        answer = tokens[index]['number'] * n
    elif tokens[index + 1]['type'] == 'DIVIDE':
        answer = tokens[index]['number'] / n
    return answer

def calc(tokens, start, end, answer):
    flag = False
    while start < end:
        if tokens[start]['type'] == 'NUMBER' or tokens[start]['type'] == 'OBRACKET':
            if tokens[start]['type'] == 'NUMBER':
                n = tokens[start]['number']
                print("n",n)
                print("@", start)
            else:
                print("in")
                flag = True
                n = nested(tokens, start)[0]
                print("nested", n)
            if tokens[start - 1]['type'] == 'PLUS':
                print("plus")
                if signs(start, tokens):
                    answer += ranged(tokens, start)
                    start += 3
                else:
                    answer += n
                    print(answer)
                    if flag == True:
                        start = nested(tokens, start)[1]

            elif tokens[start - 1]['type'] == 'MINUS':
                print("minus")
                if signs(start, tokens):
                    answer -= ranged(tokens, start)
                    start += 3
                else:
                    answer -= n
                    if flag == True:
                        start = nested(tokens, start)[1] 

            elif tokens[start - 1]['type'] == 'MULTIPLY':
                print("times")
                print("n2", n)
                answer *= n
        start += 1
    return answer

def nested(tokens, start):
    # Finds end bracket
    end = brackets(tokens, start)
    # Moves 1 step forward to get number 
    start += 1
    while tokens[start]['type'] != 'NUMBER':
        start += 1
    answer = tokens[start]['number']
    print("first in nested", answer)
    return calc(tokens, start, end, answer), end


def evaluate(tokens):
    index = 1 
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    return calc(tokens, index, len(tokens), answer)
    

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
    test("1-(5+1)")
    test("(5+2)*2")
    test("2*(5+2)")
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
