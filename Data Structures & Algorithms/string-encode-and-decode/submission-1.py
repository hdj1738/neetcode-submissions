class Solution:

    def encode(self, strs: List[str]) -> str:
        strfinal=""
        for string in strs:
            strfinal+=','+str(len(string))
        return strfinal+'#'+''.join(strs)

    def decode(self, s: str) -> List[str]:
        listfinal=[]
        nottuple=list(s.partition ('#'))
        for i in nottuple[0].split(',')[1:]:
            listfinal.append(nottuple[2][:int(i)])
            nottuple[2]=nottuple[2][int(i):]
        return listfinal



            
