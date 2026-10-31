class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:
            keys = "".join(sorted(word))

            if keys not in group:
                group[keys] =[]

            group[keys].append(word)    

        return list(group.values())                              
 

                                                                        