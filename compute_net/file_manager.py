import importlib.util

import igraph as ig

def load_gml(from_file):
    loaded_graph = ig.Graph.Load(from_file, format="gml")
    return loaded_graph

def save_gml(graph, to_file):
    graph.write(to_file, format="gml")
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