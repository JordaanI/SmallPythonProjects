import random

def investigate(seq,num,prisoner,guesses,count=0):
    ticket = seq[num]
    if ticket != prisoner:
        num = seq[num]
        count += 1
        if count > guesses:
            return 0, -1
        else:
            return investigate(seq,num,prisoner,count)
    else:
        return 1, count

def initialize(n):
    seq = random.sample(range(n),n)
    unique_prisoners = list(range(n))
    return seq, unique_prisoners

def one_run(num_of_prisoners,guesses):
    seq, unique_prisoners = initialize(num_of_prisoners)
    res = []
    counts = []
    while unique_prisoners:
        num = random.choice(unique_prisoners)
        result, count = investigate(seq,num,num,guesses)
        res.append(result)
        counts.append(count)
        unique_prisoners.remove(num)
    if sum(res)/len(res) == 1:
        return 1, counts
    else:
        return 0, counts

def many_runs(number_of_runs,number_of_prisoners,guesses):
    res = []
    counts = []
    for i in range(number_of_runs):
        result, count = one_run(number_of_prisoners,guesses)
        res.append(result)
        counts.append(count)
    return res, counts