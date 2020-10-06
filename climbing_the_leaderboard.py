def climbingLeaderboard(scores,alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores) - 1
    while score_index != len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index > -1:
            highscore_index -= 1
            if scores[highscore_index] != scores[highscore_index + 1]:
                currentrank -= 1
        if alice[score_index] == scores[highscore_index]:
            yield currentrank 
        else:
            yield currentrank + 1
        score_index += 1

        
input()
scores = list(map(int,input().split()))
input()
alice = list(map(int,input().split()))

print(*climbingLeaderboard(scores,alice),sep="\n")






        
