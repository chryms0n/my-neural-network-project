import sys, os


def get_current_path():
    """
    Get the path to the current directory.
    Assumes the file structure /[project]/[Nielson's repo] , [my repo]
    """
    return os.path.dirname(os.path.abspath(__file__))

def get_resource_path(dire):
    """
    get the path to Michael Nieson's git repository.
    Assumes the file structure /[project]/[Nielson's repo] , [my repo].
    """
    
    return os.path.abspath(get_current_path() + "/../neural-networks-and-deep-learning/" + dire)


module_path = get_resource_path("src")
data_path = get_resource_path("data")
current_path = get_current_path()

if __name__ == "__main__":

    print(module_path)
    print(data_path)
    print(current_path)
