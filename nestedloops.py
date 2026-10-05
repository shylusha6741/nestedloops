# 1. # Sum of Prime Numbers
# Find the sum of all prime numbers between 20 and 150.
sum=0
print("Print the sum of all prime numbers between 20 and 150")
for j in range(20,151,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if count==2:
        sum=sum+n
print(sum)

      
# 2. # Average of Perfect Numbers
# # Find the average of all perfect numbers between 1 and 1000.
sum=0
count=0
for j in range(1,1001,1):
    n=j
    total=0
    for i in range(1,n,1):
        if(n%i==0):
            total=total+i
    if total==n:
       sum=sum+n
       count=count+1
avg=sum/count
print(avg)


# 3. # Leap Years in a Range(Not Nested Loop Logic)
# # Print all leap years between 1900 and 2026.
print("Leap years between 1900 and 2026")
for i in range(1900,2027,1):
    if(i%400==0 or i%4==0 and i%100!=0):
        print(i)


# 4. # Palindrome Numbers
# # Print all palindrome numbers between 100 and 500.
for j in range(100,501,1):
    n=j
    rev=0
    while n!=0:
        last_digit=n%10
        rev=rev*100+last_digit
        n=n//10
    if rev==j:
        print(j)

# 5. # Digit Sum = 10
# # Print all numbers between 120 and 850 whose digit sum is exactly 10
print("Numbers between 120 and 850 whose digit sum is exactly 10 :")
for j in range(120,851,1):
    n=j
    sum=0
    for i in range(1,n+1,1):
        last_digit=n%10
        sum=sum+last_digit
        n=n//10
    if sum==10:
        print(j)


    
# 6. # Pairs with Target Sum
# Print all pairs (a, b) between 1 and 50 whose sum is 30. Print each pair only once
for j in range(1,51,1):
    for i in range(j,51,1):
        if(i+j==30):
            # print(f"a={i} b={j}")
            print(f"{i,j}")

    
# 7. # Exactly 3 Factors
# Print all numbers between 10 and 300 that have exactly 3 factors.
print("numbers between 10 and 300 that have exactly 3 factors.")
for j in range(10,301,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if count==3:
        print(n)

# 8. # Prime Factors
# # Print the prime factors of every number between 20 and 50.
for j in range(20,51,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if count==2:
        print(i)