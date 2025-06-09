"""Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 """
    
def square_sum(numbers):
    #your code here
    sum = 0
    
    for num in numbers:
        num = num ** 2
        sum += num
        
    return sum

print(square_sum([1,2]), 5)
print(square_sum[0, 3, 4, 5], 50)
print(square_sum([]), 0)
print(square_sum([-1,-2]), 5)
print(square_sum([-1,0,1]), 2)