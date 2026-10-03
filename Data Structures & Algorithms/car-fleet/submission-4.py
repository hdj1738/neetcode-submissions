class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for i in range(len(position)):
            position[i]=[position[i],speed[i]]
        for i in position:
            stack.append([i[0],(target-i[0])/i[1]])
        stack=sorted(stack,reverse=True)
        diff=0
        fleet_time = 0
        for i in stack:
            time = i[1]
            if time > fleet_time:
                diff += 1
                fleet_time = time
        return diff

        