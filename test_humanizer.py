import unittest
from humanizer import *

class Test_humanizer(unittest.TestCase):

    def test_lat_lng(self):
        self.assertEqual(f_lat_lng("|d W0910335|e W0910335|f N0332432|g N0332432|2 geonames"), "91.0335, 33.2432")
        self.assertEqual(f_lat_lng("|d W0051240|e W0051240|f N0373555|g N0373555|2 ngn"), "5.124, 37.3555")
        self.assertEqual(f_lat_lng("|d E0020143|e E0020143|f N0412156|g N0412156|2 geonames"), "2.0143, 41.2156")

    def test_mon_per_id(self):
        self.assertEqual(mon_per_id("|0 XX45333"), "XX45333")

    def test_ser_key_title(self):
        self.assertEqual(ser_key_title(""), None)
        self.assertEqual(ser_key_title(None), None)
        self.assertEqual(ser_key_title("|a XX|b DD"), "XX DD")
        self.assertEqual(ser_key_title("|a XX"), "XX")
        self.assertEqual(ser_key_title("|b XX"), "XX")
    def test_country_of_publication(self):
        '''|a 900725u196u    sp ar        s0   b0spa  '''
        '''|a 070418d18691869sp uu pe      0   b0spa  '''
        self.assertEqual(country_of_publication("|a 900725u196u    sp ar        s0   b0spa  "), "España")
        self.assertEqual(country_of_publication("|a 070418d18691869sp uu pe      0   b0spa  "), "España")
    def test_per_other_names(self):
        self.assertEqual(per_other_names("|a Abad Gallego, Juan Carlos|d 1960- /**/ |a Abad Gallego, Xoán C.|d 1960-"), "Abad Gallego, Juan Carlos, ( 1960-) /**/ Abad Gallego, Xoán C., ( 1960-)")

    def test_physical_description(self):
        self.assertEqual(vid_physical_description("|a vc*cb|ho|", "soporte"), "Cartucho de película")
        self.assertEqual(vid_physical_description("|a vr*cb|ho|", "soporte"), "Bobina de película")
        self.assertEqual(vid_physical_description("|a vc*ub|ho|", "color"), "Desconocido")
        self.assertEqual(vid_physical_description("|a vc*hb|ho|", "color"), "Coloreado a mano")
        self.assertEqual(vid_physical_description("|a vc*cbaho|", "sonido"), "Sonido incorporado")
        self.assertEqual(vid_physical_description("|a", "sonido"), None)
        self.assertEqual(vid_physical_description(None, "soporte"), None)
        self.assertEqual(vid_physical_description(None, "color"), None)
        self.assertEqual(vid_physical_description(None, "sonido"), None)
    
    def test_get_multi_dollar(self):
        self.assertEqual(get_multi_dollar(None, ("a","c")), None)
        self.assertEqual(get_multi_dollar("|aX|b|cDD", ("a","c")), "X, DD")
    
    def test_notes(self):
        self.assertEqual(notes(["|a Vídeo didáctico", "|a X"]), "Vídeo didáctico /**/  X")

if __name__ == "__main__":
    unittest.main()