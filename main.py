from classes import gyongy
from read_file import read
from algoritmus import optimum_search

def main():
    gyongyok: list[gyongy] = read()
    #ide a gui hogy bekérje a v-t , t-t, majd abbol kiszamolja a dist-et
    #dist: megtehető távolság összesen

    
    dist = 30
    optimum: list[int] = optimum_search(gyongyok, d)

    #az optimum segítségével gui 3d-s megjelenítésre
    #oh god why you must fuck us 

if __name__ == '__main__':
    main()