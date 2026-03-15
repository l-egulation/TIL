import sys

def get_score(sg, opp):
    if sg == opp: return 1
    if (sg == 'S' and opp == 'P') or \
       (sg == 'R' and opp == 'S') or \
       (sg == 'P' and opp == 'R'):
        return 2
    return 0

R = int(sys.stdin.readline())
sg_hands = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
friends_hands = [sys.stdin.readline().strip() for _ in range(N)]

actual_total = 0
max_total = 0

for r in range(R):
    for i in range(N):
        actual_total += get_score(sg_hands[r], friends_hands[i][r])

    round_scores = []
    for my_choice in ['S', 'R', 'P']:
        current_choice_score = 0
        for i in range(N):
            current_choice_score += get_score(my_choice, friends_hands[i][r])
        round_scores.append(current_choice_score)

    max_total += max(round_scores)

print(actual_total)
print(max_total)