

from custom_modules import gyongy, vector3


def read() -> list[gyongy]:
    gyongyok: list[gyongy] = []
    with open("gyongyok.txt") as file:
        id: int = 0
        for sor in file.readlines()[1:]:
            adatok = sor.rstrip().split(";")
            gyongyok.append(gyongy(
                vector3(
                    int(adatok[0]),
                    int(adatok[1]),
                    int(adatok[2])
                ),
                int(adatok[3]),
                id
            ))
            id += 1
    return gyongyok

# Test cases:
def test():
    gyongyok: list[gyongy] = read()
    for gy in gyongyok:
        print(gy.position.x, gy.position.y, gy.position.z, gy.e)

if __name__ == '__main__':
    test()