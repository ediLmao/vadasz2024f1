
# ebbe a fileba csak a classokat tároljuk hogy több fáljba is be tudjuk
# őket importálni

class gyongy:
    def __init__(self, x: int, y: int, z: int, e: int, id: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.e: int = e
        self.id: int = id
        # A (0, 0, 0) - tól való távolság (3d-s pythagorasz tétel)
        self.distance: float = (x*x+y*y+z*z) ** (1/3)

