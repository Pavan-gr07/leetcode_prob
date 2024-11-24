# def fibinocci(n):
#     a = 0
#     b = 1
#     sum=0
#     result=[a,b]
#     for i in range(0,n-2):
#         sum = a+b
#         a=b
#         b=sum
#         result.append(sum)
#     return result   
        
# x = fibinocci(4)
# print(x)
def fibonacci(n):
    a, b = 0, 1  # Initialize first two terms
    result = [a, b]  # Store the sequence in a list

    for _ in range(n - 2):  # Loop to generate the rest of the terms
        a, b = b, a + b  # Update 'a' and 'b'
        result.append(b)  # Add the new term to the list

    return result  # Return the Fibonacci sequence as a list

# Get input from the user
N = int(input("Enter the number of terms: "))
print(fibonacci(N))  # Print the Fibonacci sequence
