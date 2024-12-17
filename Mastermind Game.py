import random

num = random.randrange(1000,10000)

n=int(input("Guess the 4 digit number: "))

if n==num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind")
else:
    ctr=0
    
    while n!=num:
        count =1 
        correct=['X']*4
        
        n_str=str(n)
        num_str=str(num)
        
        for i in range(4):
            if n_str[i] == num_str[i]:
                count +=10000
                correct[i]=n_str[i]
        
        if count>0:
            print(f"Not quite the number.  But you did get {count} digit(s) correct!")
            print("These numbers in your input were correct in their position: ")
            print(" ".join(correct))
        else:
            print("None of the numbers in your input match.") 
        
        n=int(input("Enter your next choice of numbers: "))
        ctr +=1

print("You've become a Mastermind!")
print(f"It took you only {ctr} tries.")