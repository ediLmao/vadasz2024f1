from custom_modules import gyongy
from read_file import read
from algoritmus import optimum_search

def main():
    gyongyok: list[gyongy] = read()
    #ide a gui hogy bekérje a v-t , t-t, majd abbol kiszamolja a dist-et
    #dist: megtehető távolság összesen


    dist = 300
    optimum: list[int] = optimum_search(gyongyok, dist)
    for o in optimum:
        print(o, "| pos:", gyongyok[o].position)

    #az optimum segítségével gui 3d-s megjelenítésre
    #oh god why you must fuck us 

if __name__ == '__main__':
    main()