

from classes import gyongy


def read() -> list[gyongy]:
    gyongyok: list[gyongy] = []
    with open("gyongyok.txt") as file:
        for sor in file.readlines()[1:]:
            adatok = sor.rstrip().split(";")
            gyongyok.append(gyongy(
                adatok[0],
                adatok[1],
                adatok[2],
                adatok[3]
            ))
    return gyongyok


def test():
    gyongyok: list[gyongy] = read()
    for gy in gyongyok:
        print(gy.x, gy.y, gy.z, gy.e)

if __name__ == '__main__':
    test()