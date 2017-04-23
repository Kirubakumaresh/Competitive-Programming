# -*- coding: utf-8 -*-

"""
Isaac has to buy a new HackerPhone for his girlfriend Amy. He is exploring the shops in the town to compare the prices whereupon he finds a shop located on the first floor of a building, that has a unique pricing policy. There are N steps leading to the shop. A numbered ball is placed on each of the steps. 
The shopkeeper gives Isaac a fair coin and asks him to toss the coin before climbing each step. If the result of the toss is a 'Heads', Isaac should pick up the ball, else leave it and proceed to the next step.

The shopkeeper then asks Isaac to find the sum of all the numbers he has picked up (let's say S). The price of the HackerPhone is then the expected value of S. Help Isaac find the price of the HackerPhone.
"""


def expected_value(numberedBalls):
    #Since this is a fair coin, expected value of head/tail is 0.5
    return sum(numberedBalls)/2

if __name__ == '__main__':
    steps = input()
    assert steps.isdigit(), 'steps:not a valid number'
    steps = int(steps)
    assert steps>=1 and steps<=40, 'steps:out of range'
    numberedBalls =[]
    for i in range(steps):
        ball = input()
        assert ball.isdigit(), 'ball:not a valid number'
        ball = int(ball)
        assert ball>=1 and ball<=10**9, 'ball:out of range'
        numberedBalls.append(ball)
    print(expected_value(numberedBalls))