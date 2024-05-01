import unittest
from ..src.parser import Parser



class TestParser(unittest.TestCase):
    def test_type_parser(self):
        value1 = 1
        value2 = "1"
        value3 = [1,2,3]
        value4 =  1.1
        value5 = True
        value6 = {
                "id": 49,
                "name": "asdasd",
                "phone": "123120",
                "email": "fgsd01fg@yahoo.com",
                "image": "https://tablefinder.top/Voucher_App/storage/image/80875091707126500lBvuPXFbe1apybjUdXeMQcdOWxZB4zwA55nkHBqU.png",
                "role": 2,
                "role_name": "Customer"
            }
        parser = Parser()
        self.assertEqual(parser.type_parser(value1), "int");
        self.assertEqual(parser.type_parser(value2), "String");
        self.assertEqual(parser.type_parser(value3), "");
        self.assertEqual(parser.type_parser(value4), "double");
        self.assertEqual(parser.type_parser(value5), "bool");
        self.assertEqual(parser.type_parser(value6), "");

    def test_list_parser(self):
        value1 = [1]
        value2 = ["1"]
        value3 = [True]
        value4 = [{"hi": 1}] 
        parser = Parser()
        self.assertEqual(parser.list_parser(value1, "user", "hi"), "List<int>");
        self.assertEqual(parser.list_parser(value2, "user", "hi"), "List<String>");
        self.assertEqual(parser.list_parser(value3, "user", "hi"), "List<bool>");
        self.assertEqual(parser.list_parser(value4, "user", "hi"), "List<UserHiModel>");
        
        
