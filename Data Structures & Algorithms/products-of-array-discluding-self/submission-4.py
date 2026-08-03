class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        altproduct=1
        output=[]
        count=0
        for num in nums:
            if num==0:
                count+=1
            else:
                altproduct*=num
            product*=num
        for i in nums:
            if i==0:
                if count>1:
                    output.append(0)
                if count==1:
                    output.append(altproduct)
            else:
                output.append(product//i)
        return output


        
            

        return output

        '''
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        '''
        '''
        array nums. to return product of all except num

        '''
        



        
        



        