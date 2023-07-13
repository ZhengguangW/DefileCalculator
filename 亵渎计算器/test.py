class triangle():
    def __init__(self,a):
        self.a=a
        

wzg=triangle(3)

def modify(t):
    t.a+=1
    
modify(wzg)
print(wzg.a)