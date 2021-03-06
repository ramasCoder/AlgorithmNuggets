class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        """
        # Works - but a scale cases of [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
#[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612] fails the logic with memory error
        # Logic - For every heater placement add the heater it covers and check whether its equal to all the house array, try with radius 1 and ....
        covered = []
        n1 = len(houses)
        n = houses[n1-1]
        h = len(heaters)
        for radius in range(1,n):
            for h in heaters:
                covered.append(h)
                if h-radius > 0 and h-radius < n:# and h-radius not in covered:
                    covered.append(h-radius)
                if h+radius < houses:# and h+radius not in covered:
                    covered.append(h+radius)
            if len(set(covered)) == n:
                print covered
                return radius
        return -1
        """
        
        """
        # 100 pass - Alternate from discussions yecyec
        
        # Sort the houses and heaters
        heaters = sorted(heaters)
        houses = sorted(houses)
        
        # Variable declaration
        radius = i = 0
        
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
                
            # When heater is placed in front of all the houses, then 0
            if i == 0:
                radius = max(radius, heaters[i] - house)
            # All the possibility of heaters have been exhausted
            if i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i] - house, house- heaters[i-1]))
        return radius
        """
        
        # 100 pass - nice understandable Solution from discussion by Jonathan82 - Smaller
        # Find the distance from the heater for each house and get the maximum from the results
        
        # Sort the houses and heaters
        heaters.sort()
        houses.sort()
        
        # Variable declaration
        radius = i = 0
        
        for house in houses:
            # Move from one heater to the next with absolute differences - at any point i has the closest heater to the house
            while i+1 < len(heaters) and abs(heaters[i+1]-house) <= abs(heaters[i]-house):
                i += 1
            # To obtain the maximum distance that have to be covered by a heater
            radius = max(radius, abs(heaters[i] - house))
        return radius
    
                
        
        
        
        
        
        
        
        
        
