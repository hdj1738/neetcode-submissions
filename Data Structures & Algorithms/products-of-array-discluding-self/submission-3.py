class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        altproduct=1
        output=[]
        for i in nums:
            product*=i
            if i!=0:
                altproduct*=i
        print(product)
        a=nums.count(0)
        for i in nums:
            if i==0:
                if a>1:
                    output.append(0)
                if a==1:
                    output.append(altproduct)
            else:
                output.append(int(product/i))
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
        



        