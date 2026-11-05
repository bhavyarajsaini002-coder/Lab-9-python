balls = input("Enter balls: ").split()

total_runs = 0
wickets = 0
boundaries = 0
over_runs = 0
ball_count = 0
overs_list = []

for b in balls:
    if b == 'W' or b == 'w':
        wickets = wickets + 1
    else:
        r = int(b)
        total_runs = total_runs + r
        over_runs = over_runs + r
        if r == 4 or r == 6:
            boundaries = boundaries + 1
            
    ball_count = ball_count + 1
    if ball_count == 6:
        overs_list.append(over_runs)
        over_runs = 0
        ball_count = 0

if ball_count > 0:
    overs_list.append(over_runs)

print("Total Runs:", total_runs)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", overs_list)