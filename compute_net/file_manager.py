import importlib.util

import igraph as ig

def load_graph(from_file):
    graph_format = from_file.split(".")[-1]
    loaded_graph = ig.Graph.Load(from_file, format=graph_format)
    return loaded_graph

def save_graph(graph, to_file):
    graph_format = to_file.split(".")[-1]
    graph.write(to_file, format=graph_format)
    return 

def import_function(file_path, function_name):
    # Load the module from the specified file
    spec = importlib.util.spec_from_file_location("module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the function object
    func = getattr(module, function_name, None)
    if not func:
        raise AttributeError(f"Function '{function_name}' not found in '{file_path}'")

    # Return the function
    return func