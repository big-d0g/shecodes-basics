# EIGHTBALL OPTIONS
# Yes - definitely.
# It is decidedly so.
# Without a doubt.
# Reply hazy, try again.
# Ask again later.
# Better not tell you now.
# My sources say no.
# Outlook not so good.
# Very doubtful.
 
name = "IDIOT"
question = "Am I good at Python yet?"

import random
random_number = random.randint(1,11)


if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Nah."
elif random_number == 11:
  answer = "No way."
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)


print("Magic 8-Ball says: " + answer)