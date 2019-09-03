class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) - 2, -1, -1):
            a = s.pop(i)
            s.append(a)
        
