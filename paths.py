import sys, os

module_path = os.path.dirname(os.path.abspath(__file__)) + "/../neural-networks-and-deep-learning/src"
data_path = os.path.dirname(os.path.abspath(__file__)) + "/../neural-networks-and-deep-learning/data"
### recompile paths in order to cancel out the '/../'
data_path = os.path.abspath(data_path)
module_path = os.path.abspath(module_path)

if __name__ == "__main__":

    print(module_path)
    print(data_path)
