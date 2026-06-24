class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:

                if stack[-1] < -a:
                    stack.pop()      # top asteroid explodes
                    continue

                elif stack[-1] == -a:
                    stack.pop()      # both explode

                break

            else:
                stack.append(a)

        return stack