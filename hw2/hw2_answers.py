
def hw2_answers(problem_number):
    if problem_number == "4.1.1":
        return "The evaluation function was based on calculating the potential value of each posiiton, by weighing each cookie that belongs to a player as 10, then add 1 for each cookie it is surrounded by to find the most favorable position. The opponents position favorability is then subtracted from the player's position favorability, and that value is returned. A trivial value is added to that total in order to prevent the players from oscillating whne reaching the last cookie. It is a good measure of how favorable a state is becuase it shows how beneficial a position may be for a player, since the object of the game is to win by acquiring more cookies, and in order to do so the player must both acquire cookies and gain more than his opponent as he went on."
    if problem_number == "4.1.2":
        return "The size of the state space is 15 * 14 * 2^13, which totals 1,720,320. This is because there are 15 positions player 0 can be in, 14 positions player 1 can be in, then 13 positions that can be labeled either '' or 'c'."

    if problem_number == "4.2.1":
        return "By expanding the entire game tree, the backed up value at the root node would tell you the favorability of your starting position."

    if problem_number == "4.3.1":
        return "When the alpha-beta player goes first against the minimax player, it almost always is ahead throughout the entire game, before eventually winning. When the alpha-beta player goes second after the minimax player, it is usually behind after a few turns, before almost always winning overall."
    if problem_number == "4.3.2":
        return "With alpha-beta pruning, only the most efficient nodes are expanded, as opposed to standard minimax which explores all potential possibile nodes."

    return "Invalid problem number"