# comprehensive solution
# https://leetcode.com/problems/design-hashset/discuss/494792/Two-python-sol.-based-on-bytearray-and-bit-manipulation.-85%2B-With-Explanation

class MyHashSet:
    # Mehotd_#1
    # Python solution based on native bytearray, faster but need more (redundant )space.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = bytearray(1000001)

        
    def add(self, key: int) -> None:
        
        if not self.hash_set[key]:
		
			# set to True for existence of incoming element
            self.hash_set[key] = True

            
    def remove(self, key: int) -> None:
        
        if self.hash_set[key]:
		
			# clear to False for removal
            self.hash_set[key] = False

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
		# check the flag for existence judgement
        if self.hash_set[key]:
            return True
			
        else:
            return False
        
    # Mehotd_#2
    # Python solution based on native bytearray with bit-manipulation.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = bytearray(125001)

        
    def add(self, key: int) -> None:
        
        quotient, remainder = divmod(key, 8)
		
        if not self.hash_set[quotient] & (1 << remainder):
			
			# set to True for existence of incoming element
            self.hash_set[quotient] |= (1 << remainder)

            
    def remove(self, key: int) -> None:
        
        quotient, remainder = divmod(key, 8)
		
        if self.hash_set[quotient] & (1 << remainder):
		
			# clear to False for removal
            self.hash_set[quotient] &= ~(1 << remainder)

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
		
        quotient, remainder = divmod(key, 8)
		
		# check the flag for existence judgement
        if self.hash_set[quotient]& (1 << remainder):
            return True
			
        else:
            return False