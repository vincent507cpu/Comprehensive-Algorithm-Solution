class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        length = len(key)
        hash_val = 0
        
        for i in range(len(key)):
            hash_val = hash_val * 33 % HASH_SIZE + ord(key[i])
            
        return hash_val % HASH_SIZE