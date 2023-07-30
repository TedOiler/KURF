import pyDOE2
class FullFacIni2D:
    def generate_initial_samples(self, low=[-50,-50], high=[50, 50], n=1):
        arr = pyDOE2.fullfact([3,3])
        arr[arr==0] = low[0]
        arr[arr==2] = high[0]
        arr[arr==1] = (low[0]+high[0])/2
        X = [row for row in arr]
        print (X) 
        return X