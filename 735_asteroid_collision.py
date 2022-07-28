class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        idx = 0
        new_asteroids = []
        for asteroid in asteroids:
            new_asteroids.append(asteroid)
            idx += 1
            # print(new_asteroids)

            if new_asteroids[-1] > 0:
                # print("Adding pos asteroid %i" % new_asteroids[-1])
                continue

            # print("Adding neg asteroid %i" % new_asteroids[-1])



            while True:
                if len(new_asteroids) == 1 or len(new_asteroids) == 0:
                    break
                if new_asteroids[-2] < 0:
                    break

                if new_asteroids[-1] > 0 and new_asteroids[-2] > 0:
                    # print("stable %s" % str(new_asteroids))
                    break

                if abs(new_asteroids[-1]) > new_asteroids[-2]:
                    # print("Left consumes right")
                    new_asteroids.pop(-2)
                elif abs(new_asteroids[-1]) < new_asteroids[-2]:
                    # print("Right consumes left")
                    new_asteroids.pop(-1)
                else:
                    # print("Both explode")
                    new_asteroids.pop(-1)
                    new_asteroids.pop(-1)






        return new_asteroids
            
