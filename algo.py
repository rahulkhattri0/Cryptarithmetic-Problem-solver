class cryp:
    def __init__(self) -> None:
        self.flag = False
    def makenum(self,map:dict,str:str):
        s = ""
        for i in str:
            s = s + map[i].__str__()
        return int(s)
    
    def helper(self,map:dict,unique:str,used:list,words:list,result:str,target:int)->None:
        # base case
        if(target==len(unique)):
            sum=0
            for i in words:
                sum = sum + self.makenum(map,i)
            res = self.makenum(map,result)
            if(sum==res):
                self.flag = True
                print(map)
            return
        ch = unique[target]
        for i in range(0,10):
            if(used[i]==False):
                map[ch] = i
                used[i] = True
                self.helper(map,unique,used,words,result,target+1)
                used[i] = False
    def isSolvable(self,words:list,result:str)->bool:
        map = {}
        unique = ""
        for i in words:
            for j in i:
                if((j in map)==False):
                    map[j] = -1
                    unique = unique+j
        for i in result:
            if((i in map)==False):
                map[i] = -1
                unique =unique + i
        print(unique)
        if(len(unique)>10):
            return False
        used=[]
        for i in range(0,10):
            used.append(False)
        self.helper(map,unique,used,words,result,target=0)
        print(len(map))
        return self.flag

words = ["SCOOBY","DUTE"]
res = "BUSTED"
ob = cryp()
print(ob.isSolvable(words,res))
                