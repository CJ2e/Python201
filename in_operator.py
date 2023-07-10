# using the IN operator with a set

my_answer = input("Rock Paper Scissors? ").lower().strip()
options = {'rock', 'paper', 'scissors'}
if my_answer in options:
    print(f"{my_answer} is a valid option")
else:
    print(f"{my_answer} is not a valid option")
