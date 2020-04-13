import gensim
import networkx as nx
import matplotlib.pyplot as plt

model = gensim.models.Word2Vec.load("mystem_texts_model.model")
model.init_sims(replace = True)

words = model.wv.index2entity
top10 = words[:10]

G = nx.Graph()

for v in top10:
    for i in model.wv.most_similar(positive = [v], topn = 10):
        G.add_edge(v, i[0])


pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='gray', node_size=10)
nx.draw_networkx_edges(G, pos, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='DejaVu Sans')
plt.axis('off')
plt.plot(figsize=(20,10))
plt.savefig('mystem_graph_plot.pdf')
plt.savefig('mystem_graph_plot.png')
plt.show()

try:
    radius = "Radius: " + str(nx.radius(G))
except Exception:
    radius = "The radius can't be calcualted because the graph is not connected."

try:
    diameter = "Dameter: " + str(nx.diameter(G))
except Exception:
    diameter = "The diameter can't be calcualted because the graph is not connected."

n_nodes = "Number of nodes: " + str(G.number_of_nodes())
n_edges = "Number of edges: " + str(G.number_of_edges())
density = "Density: " + str(nx.density(G))
degree_cor = "Degree Pearson correlation coefficient: " + str(nx.degree_pearson_correlation_coefficient(G))
avg_cluster = "Average clustering: " + str(nx.average_clustering(G))
trans = "Transitivity: " + str(nx.transitivity(G))
deg = "Degree centrality: " + str(nx.degree_centrality(G))
deg2 = nx.degree_centrality(G)
important_nodes10 = []
for nodeid in sorted(deg2, key=deg2.get, reverse=True)[:10]:
    important_nodes10.append(nodeid)

report_parts = [radius, diameter, n_nodes, n_edges, density, degree_cor, avg_cluster, trans, deg]

file = open('report.md', 'a', encoding='utf-8')
for part in report_parts:
    file.write(part + "\n")
file.write("Top 10 most important nodes:" + "\n")
for node in important_nodes10:
    file.write(node + "\n")
file.close()
