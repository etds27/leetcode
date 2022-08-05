class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
            The corners are only hit when the total horizontal distance travelled is equal to a multiple of the box length p
            If the laser hit the horizontal edge (bounced) once, then it is at the top, twice, the bottom. Odd = top, even = bottom
            If the total horizontal distance is a multiple of 2 * p, then it is the left sensor and if the result of distance % (2 * p) = p then it is the right
        """

        # Distance travelled horizontally between the bottom and top or vice versa
        d_dist = p**2 / q

        bounces = 1
        while True:
            # Distance travelled for bounce, n
            t_dist = d_dist * bounces

            if not t_dist % p:
                if bounces % 2:
                    if t_dist % (2 * p):
                        return 1
                    else:
                        return 2
                else:
                    return 0
            bounces += 1
        
