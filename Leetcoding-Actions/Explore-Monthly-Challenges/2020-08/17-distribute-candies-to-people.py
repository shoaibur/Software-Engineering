class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        distribution = [0] * num_people
        idx = 0
        giveCandy = 1
        while candies > 0:
            if candies >= giveCandy:
                distribution[idx] += giveCandy
            else:
                distribution[idx] += candies
            candies -= giveCandy
            giveCandy += 1
            idx += 1
            if idx == num_people:
                idx = 0
        return distribution
