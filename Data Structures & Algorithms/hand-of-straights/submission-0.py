from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        
        
        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]
                
                for i in range(card, card + groupSize):
                    if count[i] < needed:
                        return False
                    count[i] -= needed
                    
        return True