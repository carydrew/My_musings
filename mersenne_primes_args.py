import sys

def range_with_arg(start, end):
    name = input("Hello. What is your name? ")
    if start < 0 or end < 0:
        print('\nI am sorry I cannot use numbers that are negative. Everything shown will be for positive numbers starting at 1.')
    if end <= start:
        end1 = end
        start1 = start
        start = end
        end = start1
    print('\n{name}, I will now find all prime numbers between {start} and {end}.'.format(name= name, start = start, end = end))
    mathing(start, end)

def range_without_arg():
    name = input("Hello. What is your name? ")
    start = int(input("\nHello {}. What is the starting Number? ".format(name)))
    end = int(input("\nWhat is the ending number? "))
    if start < 0 or end < 0:
        print('\nI am sorry I cannot use numbers that are negative. Everything shown will be for positive numbers starting at 1.')
    elif end <= start:
        end1 = end
        start1 = start
        start = end
        end = start1
    print('\n{name}, I will now find all prime numbers between {start} and {end}.'.format(name= name, start = start, end = end))
    mathing(start, end)
    
def mathing(start, end):
    first_num = start
    primes = []
    mersenne_num = []
    mersenne_list = []
    #Start of the prime Number math function
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
    print("\nThe Prime Numbers between {start} and {end} are {primes}".format(start=start, end=end, primes=primes))
    # Start of the Mersenne Numbers Math 
    print('\nI am now looking for the Mersenne Numbers in the range of {} to {}'.format(start,end))
    for num in primes:
        mer = 2 ** num - 1 
        mersenne_list.append(mer)
    
    for i in mersenne_list:
        if i in primes:
            mersenne_num.append(i) 
    print('\nThe Mersenne Numbers are {}'.format(mersenne_num))
    writing(start, end, primes, mersenne_num)
    
def writing(start, end, primes, mersenne_num):
    write_or_no = input('\nWould you like to write this to a file?(y/n)\n> ')
    if write_or_no.lower() == 'y':
        writefile(start, end, primes, mersenne_num)
    elif write_or_no.lower() == 'n':
        print('\nOk, I will not write to a file then')
        run_again()
    else:
        print('\nPlease make a valid selection.')
        writing(start, end, primes, mersenne_num)
    


def writefile(start, end, primes, mersenne_num):
    file_name = input('\nWhat is the full path and name of the file you\'d like to write to? Do not inlcude any parenthisis for spaces.\n> ')
    print('\nThe answers will be appended to the {} file'.format(file_name))
    with open(file_name, 'a') as f: 
        f.write("The Prime Numbers between {start} and {end} are {primes}\nThe Mersenne Numbers are {mer}".format(start=start, end=end, primes=primes, mer=mersenne_num))
        print('\nWriting has been completed!')
    run_again()

def run_again():
    again = input('\nWould you like to run this program again with new numbers?(y/n)\n >')
    if again.lower() == 'y':
        print('Have fun!')
        main()
    elif again.lower() == 'n':
        print('Sounds Good! Have a fantastic day!')
    else:
        print('Please make a valid selection')
        run_again()
     



def main():
    n = len(sys.argv)
    if n == 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        range_with_arg(start, end)
    elif n == 1:
        range_without_arg()
    else:
        print('This program will only accept zero or two arguements.\nThe first arguement is the starting number.\nThe second arguement is the end number.\nExample:\'py program.py 1 10\'')
    

main()


