import networkx as nx
import matplotlib.pyplot as plt


def hits(graph, iterations):
    hubs = dict.fromkeys(graph, 1)
    authorities = dict.fromkeys(graph, 1)
    # power iteration, which stops after given iterations or reaching tolerance
    for _ in range(iterations):
        last_hubs = hubs
        last_authorities = authorities
        hubs = dict.fromkeys(last_hubs.keys(), 0)
        authorities = dict.fromkeys(last_hubs.keys(), 0)
        hub_total = 0
        authority_total = 0
        for node in hubs:
            for neighbor in graph[node]:
                authorities[neighbor] += last_hubs[node] * graph[node][neighbor].get('weight', 1)
        for node in hubs:
            for neighbor in graph[node]:
                hubs[node] += last_authorities[neighbor] * graph[node][neighbor].get('weight', 1)
        for node in hubs:
            hub_total+=hubs[node]
        for node in authorities:
            authority_total+=authorities[node]
        for node in hubs:
            hubs[node]/=hub_total
        for node in authorities:
            authorities[node]/=authority_total
    return hubs, authorities


G = nx.DiGraph()

G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
                  ('C', 'E'), ('C', 'G'), ('D', 'F'), ('D', 'G'),
                  ('E', 'G'), ('E', 'H'), ('F', 'A'), ('F', 'G'),
                  ('G', 'H'), ('H', 'A')])

plt.figure(figsize=(10, 10))
nx.draw_networkx(G, with_labels=True)

result_hubs_1_iter, result_authorities_1_iter = hits(G, 1)
result_hubs_2_iter, result_authorities_2_iter = hits(G, 2)
pagerank = nx.pagerank(G, alpha=1)
# The in-built hits function returns two dictionaries keyed by nodes
# containing hub scores and authority scores respectively.

print("Hub Scores 1 iter: ", result_hubs_1_iter)
print("Authority Scores 1 iter: ", result_authorities_1_iter)
print("Hub Scores 2 iter: ", result_hubs_2_iter)
print("Authority Scores 2 iter: ", result_authorities_2_iter)
print("Pagerank: ", pagerank)
