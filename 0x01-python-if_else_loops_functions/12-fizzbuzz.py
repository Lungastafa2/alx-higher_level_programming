#!/usr/bin/python3

fizz = "Fizz"
buzz = "Buzz"


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (fizz, buzz), end=' ')
        elif (number % 3):
            print("%s" % (fizz), end=' ')
        elif (number % 5):
            print("%s" % (buzz), end=' ')
        else:
            print("%d" % (number), end=' ')
