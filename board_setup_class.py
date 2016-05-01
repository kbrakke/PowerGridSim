import pprint
import matplotlib.pyplot as plt
import networkx as nx
import random


""" this file would contain all the functions to create a random playing board given the continent and number of players.
    so given either north america or europe and the number of players it will randomly choose the right number of contiguous colored ares
     and generate the board graph.  continents are not complete yet"""


def generate_color_graph(game_colors):
    """a list of colors and edges   returns a graph of connected colors"""

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



def random_choose_play_area(number_of_players, color_graph):
    """input number of players and a graph of area colors of the continent and returns a randomly chosen color list based on the
    dictionary of players per areas"""

    areas_per_player_dict = {2:3, 3:3, 4:4, 5:5, 6:5}
    path_lists = []
    for k in color_graph.keys():
        for ki in color_graph[k].keys():
            for kj in color_graph[ki].keys():
                if set([k, ki, kj]) not in path_lists:
                    path_lists.append(set([k, ki, kj]))
                for kk in color_graph[kj].keys():
                    if set([k, ki, kj, kk]) not in path_lists:
                        path_lists.append(set([k, ki, kj, kk]))
                        for kl in color_graph[kk].keys():
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



# list of colors, nodes, edges and costs
europe = [(("red", "Lisboa"), ("red", "Madrid"), 13), (("red", "Madrid"), ("red", "Bordeaux"), 16), (("red", "Barcelona"), ("red", "Marseille"), 11), (("red", "Barcelona"), ("red", "Madrid"), 14),
          (("red", "Barcelona"), ("red", "Bordeaux"), 15), (("red", "Marseille"), ("red", "Bordeaux"), 12),(("red", "Bordeaux"), ("red", "Paris"), 12),
          (("red", "Marseille"), ("red", "Lyon"), 8), (("red", "Bordeaux"), ("red", "Lyon"), 12), (("purple", "London"), ("red", "Paris"), 16),
          (("red", "Paris"), ("red", "Lyon"), 11), (("red", "Paris"), ("purple", "Rhein-Ruhr"), 10), (("red", "Paris"), ("purple", "Rhein-Ruhr"), 10),
          (("red", "Paris"), ("purple", "Vlaanderen"), 7), (("purple", "Ranstad"), ("purple", "London"), 18), (("purple", "Rhein-Ruhr"), ("purple", "Vlaanderen"), 4),
          (("purple", "Vlaanderen"), ("purple", "London"), 15),(("purple", "London"), ("purple", "Birmingham"), 4),(("purple", "Birmingham"), ("purple", "Glasgow"), 13),
          (("purple", "Birmingham"), ("purple", "Dublin"), 15), (("purple", "Dublin"), ("purple", "Glasgow"), 17), (("purple", "Ranstad"), ("purple", "Vlaanderen"), 4),
          (("red", "Paris"), ("green", "Stuttgart"), 14),(("purple", "Ranstad"), ("green", "Bremen"), 8),(("purple", "Vlaanderen"), ("green", "Bremen"), 10),
          (("purple", "Vlaanderen"), ("green", "Rhein-Main"), 6),(("purple", "Rhein-Ruhr"), ("green", "Rhein-Main"), 3),(("purple", "Rhein-Ruhr"), ("green", "Stuttgart"), 5),
          (("green", "Rhein-Main"), ("green", "Stuttgart"), 3),(("green", "Rhein-Main"), ("green", "Berlin"), 10),(("green", "Rhein-Main"), ("green", "Praha"), 10),
          (("green", "Rhein-Main"), ("green", "Muchen"), 6),(("green", "Stuttgart"), ("green", "Muchen"), 4),(("green", "Berlin"), ("green", "Bremen"), 6),
          (("green", "Praha"), ("green", "Muchen"), 8),(("green", "Praha"), ("green", "Katowice"), 8),(("green", "Praha"), ("green", "Berlin"), 7)]


north_america = [(("blue", "Portland"), ("blue", "San Francisco"), 12), (("blue", "San Francisco"), ("blue", "Los Angeles"), 12),
          (("blue", "San Francisco"), ("blue", "Las Vegas"), 16), (("blue", "Las Vegas"), ("blue", "Salt Lake City"), 14),
          (("blue", "Salt Lake City"), ("blue", "Denver"), 14), (("blue", "Las Vegas"), ("blue", "Denver"), 25),
          (("blue", "Las Vegas"), ("blue", "Los Angeles"), 7)]



def create_game_board(continent, color_list):
    """input list of all the countries in the continent and a list of the colors base on number of players returns eligible nodes"""
    game_board = []
    for city in continent:
        if city[0][0] in color_list and city [1][0] in color_list:
            game_board.append(city)
    return game_board




def generate_game_graph(game_board):
    """included countries list:  color, nodes, edges and costs  returns game_graph"""

    def make_link(G, node1, node2, cost):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = cost
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = cost
        return G

    G = {}
    for (x,y,z) in game_board: make_link(G,x,y,z)
    return G



# list of colors, nodes, edges
na_areas = [('yellow', 'blue'), ('yellow', 'brown'), ('blue', 'purple'), ('blue', 'brown'), ('purple', 'brown'), ('purple', 'orange'), ('brown', 'orange'), ('brown', 'red'), ('orange', 'red'), ('green', 'red')]
#europe areas need to be created
eur_areas = [('green', 'red'), ('green', 'purple'),  ('purple', 'red')]

G=nx.Graph()
# explicitly set positions
pos={'Lisboa':(0,0),
     'Madrid':(0.4,0.5),
     'Paris':(0.75,3),
     'Lyon':(1.1,2.25),
     'Bordeaux':(0.3,2),
     'Barcelona':(1,0),
     'Marseille':(1,1),
     'Dublin':(0,4.5),
     'Glasgow':(0.2,6),
     'Birmingham':(0.4,5),
     'London':(0.5,4),
     'Ranstad':(1.25,5.3),
     'Vlaanderen':(1.25,4.3),
     'Rhein-Ruhr':(1.4,3.4),
     'Bremen':(2,5.75),
     'Berlin': (2.8, 5.2),
     'Rhein-Main': (2.1, 4.5),
     'Stuttgart': (1.8, 2.8),
     'Muchen': (2.5, 3.5),
     'Praha': (3, 4),
     'Katowice': (3.25, 4.5)}

def create_city_nodes(graph):
    """returns list of city nodes"""
    city_nodes = [a for a in graph.keys()]
    cities = [a[1] for a in city_nodes]
    return cities

def create_city_edges(graph):
    """returns a list of all edges"""
    city_edges = []
    city_nodes = [a for a in graph.keys()]
    for c in city_nodes:
        for e in graph[c]:
            city_edges.append((c[1], e[1]))
    return city_edges

def create_label_dict(city_nodes):
    """returns a dictionary of city: city key value pair"""
    label_dict = {}
    for c in city_nodes:
        label_dict[c]=c
    return label_dict

def create_edge_labels(game_board):
    """returns a dictionary of edges and costs"""
    edge_labels = {}
    for edge in game_board:
        edge_labels[(edge[0][1],edge[1][1])] = edge[2]
    return edge_labels

#*******************************************************************8
color_graph = generate_color_graph(eur_areas)

number_players = 3
#create variables for generating the graph
the_random_play_areas = random_choose_play_area(number_players, color_graph)
game_board = create_game_board(europe, the_random_play_areas)
#create the final graph (dictionary)
the_game_graph = generate_game_graph(game_board)

#create variables for drowing out the graph
city_nodes = create_city_nodes(the_game_graph)
city_edges = create_city_edges(the_game_graph)
label_dictionary = create_label_dict(city_nodes)
edge_labels = create_edge_labels(game_board)
#draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_shape='None', nodelist=pos.keys(), node_color='w')
nx.draw_networkx_edges(G, pos, alpha=0.5,width=3, edgelist= city_edges, edge_color='0.85')
#draw lables on nodes and edges
nx.draw_networkx_labels(G, pos, labels=label_dictionary, font_color = 'green', font_size=12, font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5)
#actually draw the graph  uncomment to save a png file to print
plt.axis('off')
plt.savefig("europe.png") # save as png
#plt.show() # display