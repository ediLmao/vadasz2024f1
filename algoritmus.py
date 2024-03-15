


from classes import gyongy, vector3

def optimum_search(gyongyok: list[gyongy], dist: float) -> list[int]: # bekéri a gyongyok listáját, visszaadja az optimális úton áthaladó gyöngyök idjait
    # dist: még megtehető távolság

    optimum: list[int] = []

    # mohó algoritmus, e érték alapján szortírozom
    gyongyok_sorted: list[gyongy] = sorted(
        gyongyok,
        key=lambda x: x.e,
        reverse=True
    )
    
    position = vector3(0, 0, 0)

    for gy in gyongyok_sorted:
        relative_distance: float = gy.distance(position)
        if dist - relative_distance - gy.zero_distance >= 0:
            position = gy.position
            dist -= relative_distance
            optimum.append(gy.id)
    
    return optimum