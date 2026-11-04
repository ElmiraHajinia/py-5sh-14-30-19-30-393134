

GameBoard=[" "]*9
def posiiition(location,playerrr):
    """_summary_

    Args:
        location (_int_): index in GameBoard
        playerrr (_str_): current player

    Returns:
        _str_: next player
    """
    GameBoard[location]=playerrr
    if playerrr=="X":
        print("O turn")
        playerrr="O"
    else:
        print("X turn")
        playerrr="X" 
    return playerrr    