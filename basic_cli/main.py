import sys

def get_name(name:str):
    return print(f"Hi, {name}!")

if __name__ == "__main__":
    name = sys.argv[1]
    get_name(name=name)