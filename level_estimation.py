import numpy as np
from matplotlib.mlab import find

class level_estimation():
    def _addfs(self , fs):
        self.fs         = fs

    def _detection90p(self , data ):
        cumsumdatasquare = np.cumsum( data*data )
        lastvalue        = cumsumdatasquare[-1]
        idxs_deb = find(  cumsumdatasquare <= 0.05*lastvalue )
        self.idx_deb = 0
        if np.size( idxs_deb) !=0 :
            self.idx_deb = idxs_deb[-10]

        idxs_end = find(  cumsumdatasquare >= 0.95*lastvalue )
        self.idx_end = 0
        if np.size( idxs_end) !=0 :
            self.idx_end = idxs_end[0]

    def _estimation_niveau(self , data , p90 , dict_niveau ):
        if p90 :
            self._detection90p( data )
            id_b     = self.idx_deb
            id_e     = self.idx_end
            self.T90 = (self.idx_end - self.idx_deb)*1./self.fs
        else :
            id_b = 0
            id_e = np.size( data ) - 1

        if dict_niveau['SPL'] :
            self._spl( data[id_b : id_e])

        if dict_niveau['SEL'] :
            self._sel( data[id_b : id_e])

    def _spl(self , data ):
        self.spl = 10*np.log10(  abs( sum( data*data )*1./np.size( data ) ))

    def _sel(self , data ):
        # TODO verif la formule et donc le test
        T        = np.size(data)*1./self.fs
        self._spl(data)
        self.sel = self.spl - 10*np.log10(T)

    #def _mweighting(self):
        # todo ajouter
        # filtrage
        # niveau

class level_estimation_test() :
    def __init__(self):
        self.fs = 1
        self.le_class = level_estimation( self.fs)

    def _test_detection90p(self ):
        self.le_class._detection90p( np.ones( 100 ) )
        if self.le_class.idx_deb == 4 and self.le_class.idx_end == 94 :
            print("VALIDATION verification _detection90p")
        else :
            print("ERREUR verification _detection90p" , self.le_class.idx_deb ,  self.le_class.idx_end)

    def _test_spl(self ):
        self.le_class._spl( 2*np.ones(100))
        if abs(self.le_class.spl - 6.02) < 0.01   :
            print("VALIDATION verification _spl")
        else :
            print("ERREUR verification _spl" , self.le_class.spl)

    def _test_sel(self ):
        self.le_class._sel( 2*np.ones(100))
        if abs(self.le_class.sel + 13.98) < 0.01  :
            print("VALIDATION verification _sel")
        else :
            print("ERREUR verification _sel" , self.le_class.sel)

if __name__=="__main__":
    print('class level_estimation')

    class_le_test = level_estimation_test()

    class_le_test._test_detection90p()
    class_le_test._test_spl()
    class_le_test._test_sel()