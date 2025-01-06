class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        left_box=[0] * (n+1)
        right_box=[0] * (n+1)
        lball,rball= 0, 0
        ans=[]

        for i in range(n):
            left_box[i+1]=left_box[i] + lball
            if boxes[i] == "1":
                lball+=1
        for i in range(n-1,-1,-1):
            right_box[i]=right_box[i+1] + rball
            if boxes[i] == "1":
                rball+=1
        print(left_box,right_box)
        for i in range(1,n+1):
            ans.append(left_box[i]+right_box[i-1])

        return ans