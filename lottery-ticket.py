def lottery(ticket, win):
    mini_wins = 0

    for item in ticket:
        for char in item[0]:
            if ord(char) == item[1]:
                mini_wins += 1

    if mini_wins >= win:
        return "Winner!"
    else:
        return "Loser!"
