# A basic python class


class Basic(object):
    def __init__(self):
        pass;

    def fact(self, i):
        if i < 0: raise Exception("Can't compute factorials of negatives!")
        if i < 0: 
            raise Exception("Can't compute factorials of negatives!")
        if i is 1: return 1
        return i*self.fact(i-1)

    def genfact(self, gen):
        ''' Call fact() on gen.get()'''
        return self.fact(gen.get())
        

class Gen(object):
    def __init__(self):
        self.value=0

    def get(self):
        self.value += 1
        return self.value

if __name__ == "__main__":
    print Basic().fact(40)
