import random

# proper set up of a main function in Python

def printMessages(message1, messsage2):
   print(message1, "is", messsage2)

def main():
   print("Hello World!")
   message1 = "Coding"
   message2 = ["fun", "hard", "easy", "interesting"]
   printMessages(message1, message2[0])
   printMessages(message1, message2[1])
   printMessages(message1, message2[2])
   printMessages(message1, message2[3])

if __name__ == "__main__":
   main()