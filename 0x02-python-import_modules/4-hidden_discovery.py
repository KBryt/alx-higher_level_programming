#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    import hidden_4 as hidden
    list = dir(hidden)
    for x in range(len(list)):
        if(list[x][0] != '_'):
            print(list[x])
=======
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
>>>>>>> 1a721d418c7b14909554c4a27ac51cfebda74167
