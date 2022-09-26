#import datetime
#
#def print_current_data():
#    current_date = datetime.date.today()
#    print(current_date)
#
#
#print_current_data()
#
#def print_game_character(character, game):
#    print(f"{character} is a character in the game {game}")
#
#print_game_character("link","shit")
#from cmath import log
##
##def woof():
##    print("WOOF WOOF BARK")
##
###def dog_to_human_age(dog_age):
###    human_equvilant = 16*log(dog_age) + 31
###    return round(human_equvilant)
##
##def dog_to_human_age(dog_age):
##    human_equvilant_age = 16*log(dog_age)+31
##    woof()
##    return round(human_equvilant_age)
##
#dog_to_human_age(5)#


#def movie_marathon(movie_list):
#    while movie_list:
#        print(f"Watching: {my_movies.pop()}!")
#    print(my_movies)
#
#movies =["The Matrix", "12 Angry Men", "Pulp Fiction","Into The Wild","Wall-E",]
#
#my_movies = movies[:]
#
#print(movies)
#print(my_movies)
#
#my_movies.pop(1)
#
#print(movies)
#print(my_movies)#
#import random
#
#def pick_picker_boardgame(boardgames):
#    boardgame_index = random.randrange(len(board_games))
#    return boardgames.pop(boardgame_index)
#
#
#def print_list(list_to_print):
#    for element in list_to_print:
#        print(element)
#
#
#
#board_games = ["udungo","Pandemic","Ticket to Ride","Monopoly","Risk"]
#
#print("\nBoard games")
#print_list(board_games)
#
#random_list = [42,9421,4.21,"norway","python"]
#print("\nRandom list")
#
#print_list(random_list)
#
#picked_boardgame = pick_picker_boardgame(board_games)
#print(f"you picked {picked_boardgame}. Have fun playing!")#

#Oblig 3 oppgave 3 se på





#from cmath import sqrt
#
#
#def hypotenus(a,b):
#    c = sqrt(a**2+b**2)
#    return c
#
#print(hypotenus(2,2))#






from cmath import log


def woof_woof_bark():
    print("Woof Woof Bark")


def dog_to_human_age(dog_age):
    human_equivalent_age = 16 * log(dog_age) + 31
    return int(human_equivalent_age)

print(dog_to_human_age(20))