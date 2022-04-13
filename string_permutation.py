class Permutations(object):

    def is_permutation(self, str1, str2):
        #Permutations is defined by same lenght and exact same characters and same case
        if not str1 or not str2:
            return False

        if len(str1) != len(str2):
            return False
        
        for c in str1:
            if not c in str2:
                return False
        
        return True
            
