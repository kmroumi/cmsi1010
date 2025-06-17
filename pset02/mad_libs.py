import random

templates = [
    {"text": "The :adjective :animal jumped over the :color fence to steal a :noun.",
        "author": "Khaleefa"},
    {"text": "At the :place, I saw a :adjective :person eating a giant :food.",
        "author": "Khaleefa"},
    {"text": "My best friend gave me a :adjective gift wrapped in :material and tied with a :color ribbon.", "author": "Omar"},
    {"text": "Suddenly, the :vehicle exploded into :number pieces of flying :plural_noun!", "author": "Dalal"},
    {"text": "Before sunrise, the :occupation danced on the :adjective hill with a :noun.", "author": "Tariq"},
    {"text": "Every :weekday, I wear my lucky :color socks to impress my :noun.",
        "author": "Fatma"},
    {"text": "I opened the fridge and a :adjective :animal leapt out, holding a :food.", "author": "Lulu"},
    {"text": "The :celebrity ran into the room yelling ':exclamation!' and holding a :object.", "author": "Noura"},
    {"text": "To bake a :adjective cake, you need a pinch of :spice and a lot of :emotion.", "author": "Wadha"},
    {"text": "We traveled through the :adjective jungle on the back of a :animal to find the lost :noun.", "author": "Ali"}
]

yes_answers = {"yes", "y", "yeah", "yup",
               "sure", "ok", "okay", "oui", "si", "sí"}


def get_user_input(prompt):
    while True:
        response = input(f"Enter a {prompt}: ").strip()
        if 1 <= len(response) <= 30:
            return response
        print("Please enter a word between 1 and 30 characters.")


def play_game():
    template = random.choice(templates)
    text = template["text"]
    author = template["author"]

    placeholders = {word[1:] for word in text.split() if word.startswith(":")}
    user_words = {}

    for placeholder in placeholders:
        user_words[placeholder] = get_user_input(placeholder)

    final_text = text
    for key, val in user_words.items():
        final_text = final_text.replace(f":{key}", val)

    print("\n" + final_text)
    print(f"\n— Template by {author}\n")


def main():
    print("Welcome to Mad Libs!\n")
    while True:
        play_game()
        again = input("Would you like to play again? ").strip().lower()
        if again not in yes_answers:
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
