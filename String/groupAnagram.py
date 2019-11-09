class Solution:
    def groupAnagrams(self, strs): 
        d = {} 
        idx = 0 
        output = [] 
        for s in strs: 
            ss = ''.join(sorted(s)) 
            if ss not in d: 
                d[ss] = idx 
                idx += 1 
                output.append([s]) 
            else: 
                output[d[ss]].append(s)
        return output   
    
    def groupAnagrams1(self, strs): 
        res_map = {}
        for str_ in strs:
            s = ''.join(sorted(str_))
            if s not in res_map:
                res_map[s] = [str_]
            else:
                res_map[s] += [str_] # == append 
        return [res_map[i] for i in res_map] # or list(res_map.value())