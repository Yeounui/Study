line_num = int(input())
result = ''

for i in range(line_num):
    line = input()
    meaningful = ''

    no_less_5, upper_included, lower_included = True, False, False

    for digit in line:
        if not digit.isalnum():
            if no_less_5 is True and (upper_included, lower_included) != (True, True):
                result += meaningful
            else:
                result += '.'*len(meaningful)
            result += '.'
            meaningful = ''
            no_less_5, upper_included, lower_included = True, False, False
        else:
            if digit.isnumeric():
                if int(digit) < 5:
                    no_less_5 = False
            elif digit.isupper():
                upper_included = True
            elif digit.islower():
                lower_included = True

            meaningful += digit

    if no_less_5 is True and (upper_included, lower_included) != (True, True):
        result += meaningful
    else:
        result += '.' * len(meaningful)
    result += '\n'

print(result.strip())






"""
the sequence contains no digits less than 5
the sequence contains either
no letters
only uppercase letters
only lowercase letters
"""

"""
21
111  1  2 11     
    6EQUJ5 11  1 
 111 2 3111      
 61 2411  4344111
                 
211  3613  1 1 1 
        1 1      
      1      1   
     1  3        
     22    11   1
  1     1 1  1   
        1 1   1  
 1   1131 3 11   
             1   
1  332 7 1 11  1 
    111 1      1 
        1 2   2  
4 1  1 1 1  11  1
 111    1   11114
          1  1   
3 1   1 1 1      
"""