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
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNjkxZWFlY2E2MzBiN2U2MDY5NGQ2MzNjOThkNTk1NDEwMWY2ZjBkNTI4N2U4MWY5YWE5Zjk2MTRkZDI4MzA2ZjdkZGI1YjY5NDdmY2U5NmIiLCJpYXQiOjE3MDk2NTU5NDIuNjI3ODIzMTE0Mzk1MTQxNjAxNTYyNSwibmJmIjoxNzA5NjU1OTQyLjYyNzgyNzg4Mjc2NjcyMzYzMjgxMjUsImV4cCI6MTc0MTE5MTk0Mi42MjEyMjk4ODcwMDg2NjY5OTIxODc1LCJzdWIiOiI0OSIsInNjb3BlcyI6W119.m6RiNlZE56zWc8HpoHorQCeXDUt3e7TfUl2q-JdFwcirP8L1twpjDLuNYpVGhpMCExLTNh8fRKI7MDNoH54kYF3nxf9CKMf0FeJJ5Yw8addRH7VuOE9tkqYVUtCIM62HvO3o-vpb50x33aw4U2mtpG_ZoYvTiQ-Ka8LuR1Mpp46Mi4IEI9OKd7B7l3ZHes_EgHwAbjzIqzvaP2zQciVwRnhb_qYePQNhEX_0YIuV6mYFp7PKztHZvFFVfiOG6b2Cusxro-vqqLrAxbv5SA8VERiqrXCUDbVNjv-V3_YFkJ8Wr4xwIElG_jauZGsdy8cHmwGSFrOUPOXkk-CfQb4pxHm0-2J8rz0QqikrpxTq5-dSHmBU2Ak3AI1Aqo6WYfoQ2Q0r_ql9P8ImyM3IBc_-l4MOHDhrR85d8S0rI5Xe5b5gfjX7aZ6U34BHvCyZMS6mCDt1xSxCGzkIuChW7IiKd0BonFrh-p9x136aFi65Xp4-n5cAZRVgaoYBGdGssAGaMStqy1WYz-It9yaiGvOrA0TRAkk82q-_i5SSe1gZtQfTeJlVPWCaWaGHuRNkcdcW3794DDRpx4UzPIb5k95drIlxIG81_SpRIDjQpNOVblzAyj9WPu5kHxK8CnnSNwa_5mhRrC32Tr8DuMFzrR98EA3eYXRg1AmWlqVWZgKktXY",
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
        
        
    # def parse_type(self,value, parent: str, name: str) -> DataType :
    #     pass
    #
    # def _list_parser(self,value, parent: str, name: str) -> str:
    #     pass

# if __name__ == '__main__':
#     unittest.main()
