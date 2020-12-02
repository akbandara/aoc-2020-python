def solve(part):
    password = ''
    policy_char = ''
    policy_1 = 0
    policy_2 = 0
    valid_password_count = 0

    data = open('data/day2-input.txt', 'r').read().split('\n') # read the file

    for line in data:
        if len(line)>0: #ignore blank lines
            line_items = line.split(' ')
            
            policy_bounds = line_items[0].split('-')
            policy_1 = int(policy_bounds[0])
            policy_2 = int(policy_bounds[1])

            policy_char = line_items[1][0]
            password = line_items[2]

            password_policy_chars = password.count(policy_char)

            if part == 1:
                if (policy_1 <= password_policy_chars <= policy_2):
                    valid_password_count = valid_password_count + 1
    
            if part == 2:
                if (password[policy_1-1] == policy_char) or (password[policy_2-1] == policy_char):
                    if not ((password[policy_1-1] == policy_char) and (password[policy_2-1] == policy_char)):
                        valid_password_count = valid_password_count + 1

    print('Number of valid passwords = ', valid_password_count)
