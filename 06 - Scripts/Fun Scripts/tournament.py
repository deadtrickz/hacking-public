import random
import time

def create_ascii_banner(text):
    """
    This function generates a simple banner from text by padding with dashes and stars
    """
    banner_width = len(text) + 4
    top_bottom = "-" * banner_width
    sides = f"* {text} *"
    return f"{top_bottom}\n{sides}\n{top_bottom}"

def fight(names, wins, round_num=1):
    if len(names) == 1:
        return names[0]

    if len(names) == 2:
        return names[0], names[1], None

    winners = []
    bye_message = None

    if len(names) % 2 != 0:
        bye = random.choice(names)
        names.remove(bye)
        winners = [bye]
        bye_message = f"{bye} gets a bye this round."

    random.shuffle(names)
    pairs = [names[i:i+2] for i in range(0, len(names), 2)]

    print(create_ascii_banner(f"Round {round_num}"))
    time.sleep(2)

    if bye_message:
        print(bye_message)
        time.sleep(1)
    
    for pair in pairs:
        name1, name2 = pair
        winner = random.choice(pair)
        loser = name1 if winner == name2 else name2 
        wins[winner] = wins.get(winner, 0) + 1
        messages = [
            f'\033[32m{winner}\033[0m ({wins[winner]}) fought \033[31m{loser}\033[0m ({wins.get(loser, 0)}) and won with a fierce uppercut!',
            f'\033[32m{winner}\033[0m ({wins[winner]}) fought \033[31m{loser}\033[0m ({wins.get(loser, 0)}) and emerged victorious after a grueling battle!',
            f'\033[32m{winner}\033[0m ({wins[winner]}) fought \033[31m{loser}\033[0m ({wins.get(loser, 0)}) and proved to be the superior fighter!',
            f'\033[32m{winner}\033[0m ({wins[winner]}) fought \033[31m{loser}\033[0m ({wins.get(loser, 0)}) and came out on top with a series of quick jabs!',
            f'\033[32m{winner}\033[0m ({wins[winner]}) fought \033[31m{loser}\033[0m ({wins.get(loser, 0)}) and earned a hard-fought victory!'
        ]
        
        print(random.choice(messages))
        time.sleep(0.5)

        winners.append(winner)

    if len(winners) == 2:
        return winners[0], winners[1], bye_message
    
    return fight(winners, wins, round_num + 1)

def best_of_3(contestant1, contestant2, wins):
    scores = {contestant1: 0, contestant2: 0}
    round_count = 1
    while round_count <= 3:
        winner = random.choice([contestant1, contestant2])
        loser = contestant1 if winner == contestant2 else contestant2
        scores[winner] += 1
        round_count += 1
    if scores[contestant1] > scores[contestant2]:
        final_winner = contestant1
        opponent = contestant2
        rounds_won = scores[contestant1]
    else:
        final_winner = contestant2
        opponent = contestant1
        rounds_won = scores[contestant2]

    print(f'Congratulations \033[32m{final_winner}\033[0m ({wins[final_winner]}), you won {rounds_won} of 3 rounds against \033[31m{opponent}\033[0m and arise victorious!')


def main():
    with open('names.txt', 'r') as f:
        names = [line.strip() for line in f]    
    wins = {}
    contestant1, contestant2, bye_message = fight(names, wins, round_num=1)
    print(create_ascii_banner("FINAL BATTLE"))
    time.sleep(2)
    print(create_ascii_banner(contestant1))
    time.sleep(2)
    print(create_ascii_banner("VS"))
    time.sleep(2)
    print(create_ascii_banner(contestant2))
    time.sleep(2)
    print(create_ascii_banner("FIGHT!!"))
    time.sleep(1)

    print('''
             X
      |_O   / \\  O_\\
        |`-/   \\-'\\
        |\\       / |
       /  |      |  \\
    ''')
    time.sleep(1)
    print('''
           \\ /
      |_O   X  O_\\
        |`-/ \\-'\\
        |\\     / |
       /  |    |  \\
    ''')
    time.sleep(1)
    print('''
             /
       /_O  X
        /`-/ \\  O_\\
       _| \\    \\-'\\
          /      / |
                |  \\
    ''')
    time.sleep(1)
    print('''
             /
       /_O  X
        /`-/ \\   O_\\
       | \\    \\-'_\\
      /  /       \\ |_ 
    ''')
    time.sleep(1)
    print('''
      ----+  
      |_O_|
        |
       / \\       _/\\v-o 
      |   |       _-|
    ''')
    time.sleep(1)

    best_of_3(contestant1, contestant2, wins)

if __name__ == '__main__':
    main()

