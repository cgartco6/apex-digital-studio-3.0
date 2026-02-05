import networkx as nx

class TaskGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_task(self, task_id, handler):
        self.graph.add_node(task_id, handler=handler)

    def link(self, parent, child):
        self.graph.add_edge(parent, child)

    def run(self, start_task, payload):
        current = start_task
        result = payload
        for node in nx.topological_sort(self.graph):
            handler = self.graph.nodes[node]["handler"]
            result = handler(result)
        return result
