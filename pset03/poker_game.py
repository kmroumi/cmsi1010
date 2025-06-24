from cards import deal, poker_classification


def main():
    while True:
        user_input = input(
            "Enter the number of players(2–10): ").strip().lower()
        if user_input in ("bye", "exit"):
            break
        try:
            num_players = int(user_input)
            if num_players < 2 or num_players > 10:
                print("Please enter a number between 2 and 10.")
                continue
            hands = deal(num_players, 5)
            for hand in hands:
                sorted_hand = sorted(hand, key=lambda card: card.rank)
                hand_str = " ".join(str(card) for card in sorted_hand)
                classification = poker_classification(hand)
                print(f"{hand_str} is a {classification}")
        except ValueError:
            print("Invalid number of players. Please enter a number between 2 and 10.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
