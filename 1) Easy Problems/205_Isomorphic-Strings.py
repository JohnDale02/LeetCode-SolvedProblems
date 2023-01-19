class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # need to verify both directions for isomorphic strings
        st = {}  # mapping from s to t
        ts = {}  # mapping from t to s
        
        for currS, currT in zip(s, t):  # for each cooresponding index in s and t 
            
           # Case 1: Neither character mapped in dictionary 
            if (currS not in st) and (currT not in ts):
                st[currS] = currT  # set mapping 
                ts[currT] = currS  # set mapping
             
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both   
                     
            elif st.get(currS) != currT or ts.get(currT) != currS:
                return False  
            
        return True
      
      
''' Other solution 
 
 class Solution:
    
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
      
'''
