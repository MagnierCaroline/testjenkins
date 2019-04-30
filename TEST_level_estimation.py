import numpy as np
from matplotlib.mlab import find
from p0000_Librairie.Logiciel.level_estimation import level_estimation

#https://docs.python.org/2/library/unittest.html
# lala
import unittest

class Test_level_estimation( unittest.TestCase) :

    def setUp(self):
        self.class_le_test = level_estimation( )
        self.class_le_test._addfs( 1 )
        self.vect_test = 2*np.ones(100)

    def test_detection90p(self ):
        self.class_le_test._detection90p( self.vect_test )
        self.assertEqual( self.class_le_test.idx_deb , 4  )
        self.assertEqual( self.class_le_test.idx_end , 94  )

    def test_spl(self ):
        self.class_le_test._spl( self.vect_test )
        self.assertLess( abs(self.class_le_test.spl - 6.02) , 0.01  )

    def test_sel(self ):
        self.class_le_test._sel( self.vect_test )
        self.assertLess(abs(self.class_le_test.sel + 13.98), 0.01)

if __name__=="__main__":
    print('class level_estimation')
    unittest.main()