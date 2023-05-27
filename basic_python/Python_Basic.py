import unittest

class TestValidation(unittest.TestCase):
    #membandingkan 2 nomor yang sama
    def test_verify_number(self):
        self.assertNotEqual(888, 914)
    
    #membandingkan 2 list yang berbeda
    def test_verify_list(self):
        self.assertNotEqual('haha', 'hahaa')
    
    #mengecek 2 value yang muncul
    def test_verify_value(self):
        self.assertIn('ea', 'eoooo')
    
    #memandingkan 2 list yang sama
    def test_verify_List(self):
        self.assertEqual('[sirsak,jeruk]','[sirsak,jeruk]')

        
if __name__ == '__main__':
    unittest.main(exit=False)
