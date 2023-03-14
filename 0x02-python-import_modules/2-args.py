#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if(args <= 1):
        print("{} arguments.".format(args - 1))
    elif(args == 2):
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    for x in range(1, args):
        print("{}: {}".format(x, sys.argv[x]))
=======

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
>>>>>>> 1a721d418c7b14909554c4a27ac51cfebda74167
