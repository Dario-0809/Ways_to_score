# CHECKING BRACKETS WHETHER THEY'RE BALANCE OR IMBALANCE
def balance_bracket(brackets):
    stack = [] 

    for character in brackets:     
        if character in "({[":
            stack.append(character)

        elif character in ")}]":
            if not stack:
                return False 
            
            character_opposite = stack.pop()
            if (character == ')' and character_opposite != '(') or \
            (character == '}' and character_opposite != '{') or \
            (character == ']' and character_opposite != '['):
                return False 

    return not stack 

if __name__ == "__main__":
    flag = []
    number_string = int(input())

    if number_string > 0 and number_string <= 100:
        for i in range(number_string):       
            bracket_string = str(input())
            if len(bracket_string) < 100000:
                if balance_bracket(bracket_string):
                    flag.append("true")
                else:
                    flag.append("false")

    for i in range(len(flag)):
        print(flag[i])


# Input:
# 5
# ( )
# { [ ( ) ] }
# { [ ( ) } ]
# ( ) (
# ] ( ) [

# Output:
# true
# true
# false
# false
# false