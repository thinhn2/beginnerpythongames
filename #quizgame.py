#quizgame

begin = input('Are you ready to begin? (y/n):\n')
begin = begin.lower()

point = 0

while True:
    if begin == 'y':
        q1 = input('Question 1: What is the largest animal in the world?\n')
        if q1.lower() == 'whale':
            point += 1
            print(f"Correct! Your score is: {point}")
        else:
            print("Incorrect")
        
        q2 = input("Who was the first president of the United States?\n")
        if q2.lower() == 'george washington':
            point += 1
            print(f"Correct! Your score is: {point}")
        else:
            print("Incorrect")

        q3 = input("What is the name of the British boyband that sings Story of My Life?\n")
        if q3.lower() == 'one direction':
            point += 1
            print(f"Correct! Your score is: {point}")
        else:
            print("Incorrect")

        q4 = input("What continent does Vietnam belong in?\n")
        if q4.lower() == 'asia':
            point += 1
            print(f"Correct! Your score is: {point}")
        else:
            print("Incorrect")

        q5 = input("Who is the famous artist behind Starry Night?\n")
        if q5.lower() == 'picasso':
            point += 1
            print(f"Correct! Your score is: {point}")
        else:
            print("Incorrect")
        
    if point < (3/5):
        print(f"You scored {point} out of 5. Please try again :(")
    else:
        print(f"Congrats! You scored {point} out of 5 :)")

    again = input('Would you like to try again? (y/n):\n')
    if again.lower() != 'y':
        break



