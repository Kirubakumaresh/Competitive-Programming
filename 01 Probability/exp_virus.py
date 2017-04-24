"""
A recent lab accident resulted in the creation of an extremely dangerous virus that replicates so rapidly it's hard to predict exactly how many cells it will contain after a given period of time. However, a lab technician made the following observations about its growth per millisecond:

The probability of the number of virus cells growing by a factor of  is .
The probability of the number of virus cells growing by a factor of  is .
Given , , and knowing that initially there is only a single cell of virus, calculate the expected number of virus cells after  milliseconds. As this number can be very large, print your answer modulo .
"""

def growth(a, b, t):
    """
    a - Initial value
    b - Growth Factor
    t - Time period
    """
    return a*(b**t)

def expected_value(p1,a1,p2,a2):
    return int((p1*a1 + p2*a2) % (10**9+7))

if __name__ == '__main__':
    inputs = input().split()
    growth_rate_a = int(inputs[0])
    growth_rate_b = int(inputs[1])
    time_period = int(inputs[2])
    init = 1 #assumption provided as part of problem statement
    prob_a = 0.5 #assumption provided as part of problem statement
    prob_b = 0.5 #assumption provided as part of problem statement
    growth_a = growth(init, growth_rate_a, time_period)
    growth_b = growth(init, growth_rate_b, time_period)
    print(expected_value(prob_a,growth_a,prob_b,growth_b))

