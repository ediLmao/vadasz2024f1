


from custom_modules import gyongy, vector3, v3_distance

def optimum_search(gyongyok: list[gyongy], travellable_distance: float) -> list[int]: # bekéri a gyongyok listáját, visszaadja az optimális úton áthaladó gyöngyök idjait
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
        distance: float = v3_distance(position, gy.position)
        if travellable_distance - distance - gy.zero_distance >= 0:
            position = gy.position
            travellable_distance -= distance
            optimum.append(gy.id)
    
    return optimum