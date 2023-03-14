#!/usr/bin/python3
if __name__ == "__main__":
    import sys
<<<<<<< HEAD
    result = sum(int(sys.argv[x]) for x in range(1, len(sys.argv)))
    print("{}".format(result))
=======
    all = 0
    for number in range(1, len(sys.argv)):
        all += int(sys.argv[number])
    print("{}".format(all))
>>>>>>> 1a721d418c7b14909554c4a27ac51cfebda74167
