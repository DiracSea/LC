class Solution:
    def compareVersion(self, version1: str, version2: str) -> int: 
        if version1 == '0' and version2 != '0': 
            return -1 
        elif version2 == '0' and version1 != '0': 
            return 1 
        elif version1 == version2: 
            return 0 
        
        
        versions1 = [int(v) for v in version1.split(".")] # 01 == 1
        versions2 = [int(v) for v in version2.split(".")]
        
        
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


    def compareVersion1(self, version1: str, version2: str) -> int:
        
        a = version1.split(".")
        b = version2.split(".")
        
        
        if len(a)>len(b):
            b+= ["0"]*(len(a)-len(b))
            
        if len(b)>len(a):
            a+=["0"]*(len(b)-len(a))
        
        
        for a,b in zip(a,b):
            
            if int(a)>int(b):
                return 1
            elif int(b)>int(a):
                return -1
        return 0