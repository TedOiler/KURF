import matlab
import matlab.engine

class DOptimalInitial:
    def generate_initial_samples(self, low=[-50,-50], high=[50, 50], n=1):
        eng = matlab.engine.start_matlab()
        nfactor = matlab.double(2)
        nruns = matlab.double(8)
        design = eng.cordexch(nfactor,nruns)
        return designx