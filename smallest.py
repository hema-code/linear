def push(self,x):
    self.s.append(x)

def pop(self):
    if len(self.s)>0:
        return self.s.pop()
    return -1
    
def getMin(self):
	if len(self.s)>0:
          return min(self.s)
    return -1