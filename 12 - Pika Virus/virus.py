import networkx as nx
from networkx.algorithms import dijkstra_path_length, has_path


def check(original, virus, on_original, on_virus,
          inv_original, inv_virus, vertex_original):
    result = []
    visited = set()

    ids_alpha = map(lambda x: vertex_original[x],
                    sorted(vertex_original.iterkeys()))
    for i in ids_alpha:
        out_degree = original.out_degree(i)
        candidates = {}
        for j in range(len(inv_virus)):
            if j not in visited:
                out_virus = virus.out_degree(j)
                if out_degree == out_virus:
                    if dijkstra_path_length(original, 0, i) == \
                            dijkstra_path_length(virus, 0, j):
                        on_og = filter(lambda x: has_path(original_graph,
                                                          i, x),
                                       on_original)
                        on_vr = filter(lambda x: has_path(virus_graph,
                                                          j, x),
                                       on_virus)
                        if len(on_og) == len(on_vr):
                            on_og = map(lambda x:
                                        dijkstra_path_length(original_graph,
                                                             i, x), on_og)
                            on_vr = map(lambda x:
                                        dijkstra_path_length(virus_graph,
                                                             j, x), on_vr)
                            if sorted(on_og) == sorted(on_vr):
                                candidates[inv_virus[j]] = j
        if len(candidates) == 0:
            return None
        srt = [(x, candidates[x]) for x in sorted(candidates.iterkeys())]
        result.append(inv_original[i] + '/' + srt[0][0])
        visited.add(srt[0][1])
    return result


original_graph = nx.DiGraph()
original_vertex = {}
original_vertex_inv = {}
original_ongoing = set()
with open('submitInput', 'rb') as f:
    lines = f.readlines()
    lines = map(lambda x: x.replace('\n', ''), lines)
    jumps = int(lines[0]) - 1
    lines = lines[1:]

    node_id = 0
    for i in range(jumps):
        c1, c2 = lines[i].split()
        if node_id != 0:
            n1 = original_vertex[c1]
            if n1 in original_ongoing:
                original_ongoing.remove(n1)
        else:
            original_graph.add_node(node_id)
            n1 = node_id
            node_id += 1
            original_vertex[c1] = n1
            original_vertex_inv[n1] = c1
            if n1 in original_ongoing:
                original_ongoing.remove(n1)
        original_graph.add_node(node_id)
        n2 = node_id
        node_id += 1
        original_vertex[c2] = n2
        original_vertex_inv[n2] = c2
        original_ongoing.add(n2)
        original_graph.add_edge(n1, n2)

    viruses = int(lines[jumps])
    lines = lines[jumps + 1:]

with open('output.txt', 'wb') as out:
    for case in range(viruses):
        virus_graph = nx.DiGraph()
        virus_vertex = {}
        virus_vertex_inv = {}
        virus_ongoing = set()
        node_id = 0
        for jump in range(jumps):
            c1, c2 = lines[case * jumps + jump].split()
            if node_id != 0:
                n1 = virus_vertex[c1]
                if n1 in virus_ongoing:
                    virus_ongoing.remove(n1)
            else:
                virus_graph.add_node(node_id)
                n1 = node_id
                node_id += 1
                virus_vertex[c1] = n1
                virus_vertex_inv[n1] = c1
                if n1 in virus_ongoing:
                    virus_ongoing.remove(n1)
            virus_graph.add_node(node_id)
            n2 = node_id
            node_id += 1
            virus_vertex[c2] = n2
            virus_vertex_inv[n2] = c2
            virus_ongoing.add(n2)
            virus_graph.add_edge(n1, n2)

        result = check(original_graph, virus_graph,
                       original_ongoing, virus_ongoing,
                       original_vertex_inv, virus_vertex_inv, original_vertex)
        if result is None:
            out.write('Case #' + str(case + 1) + ': NO\n')
        else:
            out.write('Case #' + str(case + 1) + ': ' +
                      ' '.join(result) + '\n')
