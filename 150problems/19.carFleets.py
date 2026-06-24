class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        fleets = 0
        maxTime = 0

        for pos, spd in reversed(cars):
            timeTaken = float(target - pos) / spd

            if timeTaken > maxTime:
                fleets += 1
                maxTime = timeTaken
            
        return fleets