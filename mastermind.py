#!usr/bin/python3

print ('Content type:"text/html"')
print ('')

import cgi
import random
form= cgi.FieldStorage()

reds=0 
whites=0

if "answer" in form:
    answer=form.getvalue("answer")
else:
    answer =""
    for i in range(4):
        answer += str(random.randint(0,9))

if "guess" in form:
    guess=form.getvalue("guess")
    for key,digit in enumerate(guess):
        if digit == answer[key]:
            reds +=1
        else:
            for answerDigit in answer:
                if answerDigit== digit:
                    whites +=1
                    break

else:
    guess=""





if "numberOfGuesses" in form:
    numberOfGuesses= int(form.getvalue("numberOfGuesses"))+1
else:
    numberOfGuesses=0

if numberOfGuesses==0:
    message= "I've guessed a 4 digit number. Do you think you can guess it?"
elif (reds==4):
    message= "You've guessed the number! It took you "+ numberOfGuesses+ "guesses. <a href=''> Play Again </a>"
else:
    message="You have"+ str(reds) +"correct digits in the right place and"+ str(whites) +"correct digits in the wrong place. You've had "+str(numberOfGuesses)+" number of guesses."
print ('<h1> Mastermind </h1>')
print ("<p> " + message + "  </p>")

print ('<form method="POST">')
print ('<input type="text" name="guess" value="' + guess +'">')
print ('<input type="hidden" name="answer" value="' +answer +'">')
print ('<input type="hidden" name="numberOfGuesses" value="' +str(numberOfGuesses) +'" >')
print ('<input type="submit" value="Guess!">')
print ('</form>')
