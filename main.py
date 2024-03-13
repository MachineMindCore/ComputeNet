import argparse
import importlib.util
import os
import sys

from compute_net.file_manager import load_gml, save_gml, import_function


def compute(from_addr, module_addr, to_addr, function_name):
    transformer = import_function(module_addr, function_name)
    input = load_gml(from_addr)
    output = transformer(input)
    save_gml(output, to_addr)
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform a network in GML format using a specified function.")
    parser.add_argument("--from", dest="from_addr", required=True, help="Input GML file path")
    parser.add_argument("--module", dest="module_addr", required=True, help="Python file to take function")
    parser.add_argument("--to", dest="to_addr", required=True, help="Output GML file path")
    parser.add_argument("--function", dest="function", required=True, help="Function name of the transformation")
    args = parser.parse_args()

    compute(args.from_addr, args.module_addr, args.to_addr, args.function)