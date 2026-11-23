class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) < stack[-1]:
                    ast = 0
                    break
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    ast = 0
                    break
                else:
                    stack.pop()

            if ast != 0:
                stack.append(ast)

        return stack