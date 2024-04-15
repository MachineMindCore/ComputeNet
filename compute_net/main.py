import argparse

from igraph import Graph
from compute_net.file_manager import load_graph, save_graph, import_function


def pipeline(input_graph: Graph, function: function, *args, **kwargs) -> Graph:
    output = function(input_graph, *args, **kwargs)
    return output

def entry_pipeline(from_addr, module_addr, to_addr, function_name) -> None:
    transformer = import_function(module_addr, function_name)
    input = load_graph(from_addr)
    output = transformer(input)
    save_graph(output, to_addr)
    return

def main():
    parser = argparse.ArgumentParser(description="Transform a network in GML format using a specified function.")
    parser.add_argument("--from", dest="from_addr", required=True, help="Input GML file path")
    parser.add_argument("--module", dest="module_addr", required=True, help="Python file to take function")
    parser.add_argument("--to", dest="to_addr", required=True, help="Output GML file path")
    parser.add_argument("--function", dest="function", required=True, help="Function name of the transformation")
    args = parser.parse_args()
    
    print(f"{args.from_addr} -> [{args.function}] -> {args.to_addr}")
    entry_pipeline(args.from_addr, args.module_addr, args.to_addr, args.function)



    