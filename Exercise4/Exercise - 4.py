#Write a program that asks the user “What is the capital of france?” and waits for their response.
question1=input("whats is the captial of france:")
answer="paris"
if question1 == answer :
    print ("Correct!")
else:
    print("Wrong!")
#Ignore Capitalization:
question1=input("whats is the captial of france:")
answer="paris"
if question1.lower() == answer.lower():
    print ("Correct!")
else:
    print("Wrong!")