def range():
    name = input("Hello. What is your name? ")
    start = int(input("Hello {}. What is the starting Number? ".format(name)))
    end = int(input("What is the ending number? "))
    if start < 0 or end < 0:
        print('I am sorry I cannot use numbers that are negative. Everything shown will be for positive numbers starting at 1.')
    elif end <= start:
        end1 = end
        start1 = start
        start = end
        end = start1
        #print("The ending number cannot be lower than the starting number dummy.")
    print('I will now find all prime numbers between {start} and {end}.'.format(start = start, end = end))
    mathing(start, end)
     
def mathing(start, end):
    first_num = start
    primes = []
    
    while first_num <= end:
        not_prime = []
        y = first_num
        divider = 2
        if y == 1 or y == 2:
            primes.append(y)
        ans_list = []
        while divider <= y:
            ans = y % divider
            #print('the number to check is {}.   -   {} = {} y & {}'.format(y, ans, y, divider))
            ans_list.append(ans)
            if 0 in ans_list:   
                not_prime.append(y)
            divider += 1
            if divider == y and 0 not in ans_list:
                primes.append(y)   
        first_num += 1
    print("The Prime Numbers between {start} and {end} are {primes}".format(start=start, end=end, primes=primes))

def main():
    range()

main()





#Thoughts on how to do this. 
#1. Take start, divide by every number until start and stop. 
#2. Increament start by 1 and repeat step 1. 
#3. Continue until the end and use that as the last number. 


