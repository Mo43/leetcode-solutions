class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        maxx = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxx:
                results.append(True)
            else:
                results.append(False)
                
        return (results)



##easy 
        