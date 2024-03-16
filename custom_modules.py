
# ebbe a fileba a saját modulokat tároljuk hogy több fáljba is be tudjuk
# őket importálni



class vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class gyongy:
    def __init__(self, position: vector3, e: int, id: int) -> None:
        self.position: vector3 = position
        self.e: int = e
        self.id: int = id
        # A (0, 0, 0) - tól való távolság (3d-s pythagorasz tétel)
        self.zero_distance: float = (position.x*position.x+position.y*position.y+position.z*position.z) ** (1/3)

def v3_distance(a: vector3, b:vector3) -> float:
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return (dx*dx + dy*dy + dz*dz) ** (1/3)