"""
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
n=list(range(1,51))
total_sum=0
for i in n:
    total_sum+=i
    print("The sum of all integers is", total_sum)