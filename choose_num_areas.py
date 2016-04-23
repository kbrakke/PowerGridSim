import pprint
import matplotlib.pyplot as plt
import networkx as nx
import random

def create_game_areas(area_list, number_players):
    """list the random area colors based on number of players"""
    game_areas = []
    for color in area_list:
        game_areas.append(color)
    return game_areas

def generate_color_graph(game_colors):
    """included countries list:  color, nodes, edges and costs  returns game_graph"""

    def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

    G = {}
    for (x,y) in game_colors:
        make_link(G,x,y)
    return G



def random_choose_play_area(number_of_players):
    areas_per_player_dict = {2:3, 3:3, 4:4, 5:5, 6:5}
    path_lists = []
    for k in game_graph.keys():
        for ki in game_graph[k].keys():
            for kj in game_graph[ki].keys():
                if set([k, ki, kj]) not in path_lists:
                    path_lists.append(set([k, ki, kj]))
                for kk in game_graph[kj].keys():
                    if set([k, ki, kj, kk]) not in path_lists:
                        path_lists.append(set([k, ki, kj, kk]))
                        for kl in game_graph[kk].keys():
                            if set([k, ki, kj, kk, kl]) not in path_lists:
                                path_lists.append(set([k, ki, kj, kk, kl]))
    area_five = []
    area_three = []
    area_four = []

    for s in path_lists:
        if len(s) == 3:
            area_three.append(list(s))
        elif len(s) == 4:
            area_four.append(list(s))
        elif len(s) == 5:
            area_five.append(list(s))
    if areas_per_player_dict[number_of_players] == 3:
        return random.choice(area_three)
    elif areas_per_player_dict[number_of_players]== 4:
        return random.choice(area_four)
    elif areas_per_player_dict[number_of_players]== 5:
        return random.choice(area_five)


# list of colors, nodes, edges
na_areas = [('yellow', 'blue'), ('yellow', 'brown'), ('blue', 'purple'), ('blue', 'brown'), ('purple', 'brown'), ('purple', 'orange'), ('brown', 'orange'), ('brown', 'red'), ('orange', 'red'), ('green', 'red')]

number_players = 4
game_graph = generate_color_graph(na_areas)

print(random_choose_play_area(number_players))



