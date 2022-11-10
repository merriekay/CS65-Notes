import random
def roll_die(sides):
    """
    rolls a die with a specific number of sides
    
    Parameter:
        sides, the number of sides
    Return:
        a random number between 1 and sides
    """
    return random.randint(1,sides)

def player_roll():
    """
    Rolls two dice and returns the list of the result of the two rolls
    """
    roll = [roll_die(6), roll_die(6)]
    return roll

def user_interaction(roll, tiles):
    """facilitates user interaction for making a deicision of which tile to select"""
    user_choice = input("Which tiles do you want to select? ")
    user_list = user_choice.split(",")
    int_list = [(int(num)) for num in user_list]
    
    return int_list

def valid_move(user_selection, tiles):
    """not complete yet, but eventually will check to make sure a move is valid
    
    Return:
        True if it is a valid move, and False otherwise.
    """
    #insert the code to actually check if a move is valid
    if user_selection == [0]:
        return False
    else:
        return True

def mark_tiles(user_selection, tiles):
    """
    takes in a list of tiles and 'marks' off the tile if it is chosen, by changing it to a ' '
    
    Parameters:
        user_selection, the list of tiles the user chose
        tiles, the list of tiles
    Return:
        tiles, but with the updates made
    """
    for tile in user_selection:
        if tile in tiles:
            tiles[tile - 1] = ' '
    return tiles
    

def player_turn(player_num):
    """
    The mini game loop that facilitates one players turn.
    
    Parameters:
        player_num, the specific player number who is currently playing
    Returns:
        score, the score for player_num.
    """
    tiles = [1,2,3,4,5,6,7,8,9]
    roll = player_roll()
    print("Tiles: ", tiles)
    print("Your roll: ", roll)
    decision = user_interaction(roll, tiles)
    
    while(valid_move(decision, tiles)):
        tiles = mark_tiles(decision, tiles)
        
        roll = player_roll()
        print("Tiles: ", tiles)
        print()
        print("Your roll: ", roll)
        print()
        decision = user_interaction(roll, tiles)
    score = get_score(tiles)
    return score

def get_score(tiles):
    """
    Adds up the tiles that are left, and returns the score
    
    note: isnumeric takes in a string and returns T/F based on if the string is numeric or not.
    """
    score = 0
    for tile in tiles:
        if str(tile).isnumeric():
            score+=tile
    return score

def get_num_players():
    """
    does the user interaction of getting how many players
    
    Parameters:
        none
    
    returns the number of players the user inputs. 
    """
    num_players = int(input("How many players are there? (1-4)"))
    return num_players

def game_loop():
    """
    where the magic happens-- the main game loop. This function pulls all the others together.
    
    Parameters:
        none.
    Returns:
        none.
    """
    num_players = get_num_players()
    score_list = []
    for player in range(1,num_players+1):
        print("========================")
        print("Player #", player, "'s turn:", sep='')
        print()
        score = player_turn(player)
        print("Player #", player, " score: ", score, sep='')
        print()
        score_list.append(score)
    
    min_score = 100
    min_ndx = 0
    for ndx in range(len(score_list)):
        if score_list[ndx] < min_score:
            min_score = score_list[ndx]
            min_ndx = ndx
            
    winner = min_ndx + 1
    counter = 0
    for score in score_list:
        counter +=1
        print("Player #", counter, " scored ", score, sep='')
    print("Player #", winner, ' wins with score ', score_list[winner-1], sep='')
    play_again = input('want to play again?')
    if play_again == 'yes':
        game_loop()
    
game_loop()
        