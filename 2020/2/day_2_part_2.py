"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to 
be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the 
password policy rules from his old job at the sled rental place down the 
street! The Official Toboggan Corporate Policy actually works a little 
differently.

Each policy actually describes two positions in the password, where 1 means 
the first character, 2 means the second character, and so on. (Be careful; 
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of 
these positions must contain the given letter. Other occurrences of the 
letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

def check_policy(item):
    raw_item = item.split(' ')
    raw_policy = raw_item[0].split('-')
    
    # sub 1 to align index
    char_pos_1 = int(raw_policy[0]) - 1
    char_pos_2 = int(raw_policy[1]) - 1

    target_character = raw_item[1].strip(':')

    # strip newline
    password = raw_item[2].strip()

    # get the characters at the test positions
    pos_1 = password[char_pos_1:char_pos_1 + 1]
    pos_2 = password[char_pos_2:char_pos_2 + 1]

    # Boolean test to see if position contains desired character
    check_pos_1 = (pos_1 == target_character)
    check_pos_2 = (pos_2 == target_character)
    
    if check_pos_1 != check_pos_2:
        return True

    return False

count = 0
with open('./input.txt', 'r') as f:
    for item in f.readlines():
        if check_policy(item):
            count += 1
print(f'Compliant passwords {count}')
