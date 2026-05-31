class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for m in asteroids:
            if mass < m:
                return False
            else:
                mass += m
        return True