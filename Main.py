#imports are done
from Questions import *
def main():
    queDic = questions()
    print("!!!Welcome to the Naruto Quiz!!!")
    print("Let's get started...\n")
    score = 0
    for i in queDic:
        print(i)
        answer = int(input("Enter the right option\n"))
        if queDic.get(i) == answer:
            print("Correct answer\n")
            score += 20
        else:
            print("Wrong answer\n")
    print("As a Shinobi you are categorized into different levels of rank depending on your score:-\n"
          "a) 0 - Failed Student\n"
          "b) 20 - Academy Student\n"
          "c) 40 - Genin\n"
          "d) 60 - Chūnin\n"
          "e) 80 - Jōnin\n"
          "f) 100 - Kage\n "
          )
    if score == 0:
        print("You are not a true shinobi\n")
    elif score == 20:
        print("Congratulations!!! You have been selected as an Academy Student\n")
    elif score == 40:
        print("Congratulations!!! You are a Genin now\n")
    elif score == 60:
        print("Congratulations!!! You are a Chūnin now\n")
    elif score == 80:
        print("Congratulations!!! You are a Jōnin now\n")
    elif score == 100:
        print("Congratulations!!! You are a Kage now\n")
    print("!!!Arigatou!!!")

main()