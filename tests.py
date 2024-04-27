import unittest
from datetime import datetime as dt
import datetime
import random
from task import my_datetime
from task import conv_endian
from task import conv_num


class TestConvNum(unittest.TestCase):
    def test_conv_num(self):
        """ several test cases for conv_num() function"""
        test_cases = [
            ('12345', 12345),
            ('-123.45', -123.45),
            ('.45', 0.45),
            ('123.', 123.0),
            ('0xAD4', 2772),
            ('0Xad4', 2772),
            ('0xAZ4', None),
            ('12345A', None),
            ('12.3.45', None),
            ('000123', 123),
            (' ', None),
            ('1e10', None),
            ('.123.', None),
            ('-0xAD4', -2772)
        ]
        for input_string, expected_output in test_cases:
            with self.subTest(input=input_string):
                result = conv_num(input_string)
                self.assertEqual(result, expected_output)


class TestConvEndian(unittest.TestCase):
    def test_conversion(self):
        """Unit testing for conv_endian() function"""
        test_cases = [
            (954786, 'big', '0E 91 A2'),
            (954786, 'little', 'A2 91 0E'),
            (-954786, 'big', '-0E 91 A2'),
            (1234, 'big', '04 D2'),
            (1234, 'little', 'D2 04'),
            (1, 'big', '01'),
            (453891567, 'big', '1B 0D D5 EF'),
            (453891567, 'little', 'EF D5 0D 1B'),
        ]

        for num, endian, expected_result in test_cases:
            result = conv_endian(num, endian)
            self.assertEqual(result, expected_result)


class TestCase(unittest.TestCase):

    def test_my_datetime_1(self):
        """Random testing for my_datetime() function -
        may take a couple seconds to run"""
        for i in range(10000):
            seconds = random.randint(0, 32500000000)
            string_date = my_datetime(seconds)
            my_date = dt.strptime(string_date, '%m-%d-%Y').date()
            import_date = datetime.datetime.utcfromtimestamp(seconds).date()

            if my_date != import_date:
                print(f"Error: {my_date} should be {import_date}")


if __name__ == '__main__':
    unittest.main()
