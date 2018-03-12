# NAME: David Huang
# DATE: 10 / 4 / 2017
# ID Number: 0239637
# Change log: 1.0
# reference source: https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
# reference source: https://stackoverflow.com/questions/15047116/an-iterative-algorithm-for-fibonacci-numbers
# reference source: https://stackoverflow.com/questions/23085008/python-usage-of-variables-and-their-difference-a-b-0-1-vs-a-0-b

# MAIN
# defining fibonacci sequence function
def fib_seq (n):
    # first, the sequence ALWAYS starts with 0 and 1
    start_num = 0
    next_num = 1
    # second, after the first two values, it needs to add the preceding values
    for i in range(0, n):
        prev_num = start_num # as we move up on the sequence, we pass the starting value to the previous slot
        start_num = next_num # we pass the next value to the start_num slot
        next_num += prev_num # we add the previous to the next value to form a+b
        # a simplified solution is a, b = b, a+b
    return next_num # return start_num starts the sequence at 0, return next_num starts at 1

for i in range(50): # 50 is passed to n, capping the sequence at 50
    print (fib_seq(i), end=' ') # print the sequence out
