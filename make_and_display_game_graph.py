import pprint
import matplotlib.pyplot as plt
import networkx as nx


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

color_list = ['green', 'red', 'purple']

def create_game_board(continent, color_list):
    """list of all the countries in the continent and a list of the colors base on number of players"""
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

game_board = create_game_board(europe, color_list)

game_graph = generate_game_graph(game_board)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(europe_graph)

city_nodes = create_city_nodes(game_graph)
#print(city_nodes)

city_edges = create_city_edges(game_graph)
#print(city_edges)

label_dictionary = create_label_dict(city_nodes)
#print(label_dictionary)

edge_labels = create_edge_labels(game_board)
print(edge_labels)

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


#draw nodes and edges
nx.draw_networkx_nodes(G, pos,node_size=300, nodelist=pos.keys(), node_color='w')
nx.draw_networkx_edges(G,pos,alpha=0.5,width=3, edgelist= city_edges, edge_color='w')

#draw lables on nodes and edges
nx.draw_networkx_labels(G,pos,labels=label_dictionary, font_color = 'purple', font_size=16,font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, label_pos=0.5)


plt.axis('off')
#plt.savefig("europe.png") # save as png
plt.show() # display