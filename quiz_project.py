print("Hello, Welcome to Quiz")

playing = input("Do you want to Quiz? ").lower()

if playing != "yes":
    print("Thank you! Come back after sometime.")
    quit()

print("Lets Start the quiz!")
score = 0

answer =  input("How do you spell number 1: ").lower()
if answer == "one":
    print('Correct!')
    score += 1
else:
    print('Wrong Answer!')

answer =  input("How do you spell number 2: ").lower()
if answer == "two":
    print('Correct!')
    score += 1
else:
    print('Wrong Answer!')

answer =  input("How do you spell number 3: ").lower()
if answer == "three":
    print('Correct!')
    score += 1
else:
    print('Wrong Answer!')

answer =  input("How do you spell number 4: ").lower()
if answer == "four":
    print('Correct!')
    score += 1
else:
    print('Wrong Answer!')

print("Your score: ", score)