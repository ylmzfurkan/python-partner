import random

def get_user_choice():
    choice = int(input("Taş(1), Kağıt(2), Makas(3) - Seçiminizi yapın: "))
    while choice not in [1, 2, 3]:
        choice = int(input("Geçersiz seçim. Tekrar deneyin: "))
    return choice

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "Kazandınız!"
    else:
        return "Bilgisayar kazandı."

def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 10 and computer_score < 10:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Siz: ", user_choice)
        print("Bilgisayar: ", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "Kazandınız!":
            user_score += 1
        elif result == "Bilgisayar kazandı.":
            computer_score += 1

        print("Skor: Siz -", user_score, "Bilgisayar -", computer_score)
        print("--------------------")

    if user_score == 10:
        print("Tebrikler! Oyunu kazandınız.")
    else:
        print("Bilgisayar oyunu kazandı.")

play_game()
