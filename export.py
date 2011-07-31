from selenium import selenium
import unittest, time, re

class export(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://uk.yahoo.com/")
        self.selenium.start()
    
    def test_export(self):
        sel = self.selenium
        sel.open("/?p=us")
        sel.type("id=p_13838465-p", "test")
        sel.click("id=search-submit")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
