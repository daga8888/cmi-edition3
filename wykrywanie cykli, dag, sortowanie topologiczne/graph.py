from typing import Optional, List

class Graph(object):

    def __init__(self, vertices :List[int], edges: Optional[List[int]]=None, is_directed: Optional[bool] = False):
        self.vertices = vertices
        self.edges = edges
        self.is_tree = None
        self.is_connected = None
        self.is_directed = is_directed

    def __str__(self):
        return f'''Graph[Vertex[{self.vertices}], Edges[{self.edges}], Is Tree {self.is_tree}]'''

    def is_edge(self, beg : int, end: int):
        if beg == end:
            return False #graph must be simple
        elif self.is_directed:
            return (beg, end) in self.edges
        else:
            return {beg, end} in self.edges

    def has_a_cycle(self):
        if self.is_tree:
            return False
        elif self.is_connected:
            return len(self.vertices)-1 != len(self.edges)
        return None

    def check_tree(self):
        if not self.has_a_cycle() and self.is_connected:
            self.is_tree = True
        elif not self.is_connected:
            self.is_tree = False
        elif self.has_a_cycle():
            self.is_tree = False

    def bfs(
            self,
            begin: int
    ):
        if self.is_tree:
            return self._bfs_tree(begin)
        else:
            return self._bfs_graph(begin)

    def dfs(
            self,
            begin: int,
    ):
        if self.is_tree:
            return self._dfs_tree(begin)
        else:
            return self._dfs_graph(begin)

    def _bfs_graph(
            self,
            begin : int
    ):
        result = {begin: None}
        grey = [begin]
        black = []
        while True:
            if not grey:
                break
            # pick first grey
            current = grey.pop(0)
            # match neibours
            neighbors = [ vertex for vertex in self.vertices if self.is_edge(current, vertex) and vertex not in black]
            result.update({ neighbor : current for neighbor in neighbors})
            grey.extend(neighbors)
            black.append(current)
        self.is_connected = (sorted(black) == sorted(self.vertices))
        if not self.is_connected:
            self.is_tree = False
        return result

    def _bfs_tree(
            self,
            begin : int
    ):
        result = {begin: None}
        grey = [ (begin, None) ]
        black = []
        while True:
            if not grey:
                break
            # pick first grey
            current, previous = grey.pop(0)
            # match neibours
            neighbors = [
                (vertex, current)
                for vertex in self.vertices
                if (self.is_edge(current, vertex) and ( vertex != previous if previous is not None else True))
            ]
            result.update({neighbor: prev for neighbor, prev in neighbors})
            grey.extend(neighbors)
            black.append(current)
        return result

    def _dfs_graph(
            self,
            begin: int
    ):
        result = {begin: None}
        visited = set({begin})

        def inner_dfs(visited, result, node):
            neighbors = [vertex for vertex in self.vertices if self.is_edge(node, vertex)]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result[neighbor] = node
                    inner_dfs(visited, result, neighbor)

        inner_dfs(visited, result, begin)
        self.is_connected = (sorted(visited) == sorted(self.vertices))
        if not self.is_connected:
            self.is_tree = False
        return result

    def _dfs_tree(
            self,
            begin: int
    ):
        result = {begin: None}
        last = None

        def inner_dfs(last, result, node):
            neighbors = [
                vertex
                for vertex in self.vertices
                if self.is_edge(node, vertex) and (vertex != last if last is not None else True)]
            for neighbor in neighbors:
                result[neighbor] = node
                inner_dfs(node, result, neighbor)

        inner_dfs(last, result, begin)
        return result

    def _vertex_with_no_incoming_edge(self):
        candidates = self.vertices.copy()
        for _, end in self.edges:
            if end in candidates:
                candidates.remove(end)
        return candidates

    def topological_sort_kahn(self):
        sorted_list = []
        g = Graph(self.vertices.copy(), self.edges.copy(), is_directed=True)
        while True:
            candidates = g._vertex_with_no_incoming_edge()
            if len(candidates) == 0:
                break
            sorted_list.extend(candidates)
            edges = [(beg, end) for beg, end in g.edges if beg not in candidates ]
            vertices = [vertex for vertex in g.vertices if vertex not in candidates]
            g = Graph(vertices, edges=edges, is_directed=True)
        if len(g.edges):
            raise Exception("Graph has edges")
        return sorted_list