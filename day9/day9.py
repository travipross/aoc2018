from collections import defaultdict

with open('data9.txt') as f:
    raw = f.read()

players = int(raw.split('players')[0])
last_marble_val = int(raw.split('points')[0].split('worth')[1])

players = 10
last_marble_val = 1618

player_scores = defaultdict(int)
last_marble_idx = 1
current_circle = [0, 1]
marble_num = 2
player_num = 2

args = current_circle, last_marble_idx, marble_num, player_num

def get_insertion_idx(circle, last_idx):
    if last_idx + 1 >= len(circle):
        return last_idx - len(circle) + 2
    else:
        return last_idx + 2


def get_pop_idx(circle, last_idx):
    if last_idx - 7 < 0:
        return last_idx - 7 + len(circle)
    else:
        return last_idx - 7


def play_turn(current_circle, last_marble_idx, marble_num, player_num, last_score = 0):
    if marble_num % 23 == 0:
        # special case
        last_marble_idx = get_pop_idx(current_circle, last_marble_idx) # get new idx
        last_score = marble_num + current_circle.pop(last_marble_idx)
        player_scores[player_num] += last_score
    else:
        # regular case
        # get insertion index
        last_marble_idx = get_insertion_idx(current_circle, last_marble_idx)
        current_circle.insert(last_marble_idx, marble_num)

    marble_num += 1
    player_num = player_num + 1 if player_num < players else 1
    return current_circle, last_marble_idx, marble_num, player_num, last_score


while True:
    args = play_turn(*args)
    if args[4] >= last_marble_val:
        break

winner = max(player_scores)
score = player_scores[winner]
print(args[4], winner, score)