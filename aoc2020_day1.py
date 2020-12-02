def solve(part):
    claim_values = {0}

    data = open('data/day1-input.txt', 'r').read().split('\n') # read the file
    for line in data: # files are iterable
        claim_value = int(line)
        claim_values.add(claim_value)

    if part == 1:
        for claim_value1 in claim_values:
            for claim_value2 in claim_values:
                if (claim_value1+claim_value2) == 2020:
                    print('Claim 1 ', claim_value1, ' + ', claim_value2, ' = 2020; Claim 1 x Claim 2 = ', claim_value1*claim_value2)

                
    if part == 2:
        for claim_value1 in claim_values:
            for claim_value2 in claim_values:
                for claim_value3 in claim_values:
                    if ((claim_value1+claim_value2+claim_value3) == 2020) & ((claim_value1*claim_value2*claim_value3) > 0):
                        print('Claim 1 ', claim_value1, ' + ', claim_value2,' + ', claim_value3, ' = 2020; Claim 1 x Claim 2 x Claim 3= ', claim_value1*claim_value2*claim_value3)
