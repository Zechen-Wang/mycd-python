import unittest
from io import StringIO
from unittest import mock

from mycd import my_cd


@mock.patch('sys.stdout', new_callable=StringIO)
class MyTestCase(unittest.TestCase):
    def test1(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/ abc'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc\n')

    def test2(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def    ghi'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc/def/ghi\n')

    def test3(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def   ..'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc\n')

    def test4(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def   /abc'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc\n')

    def test5(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def   /abc/klm'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc/klm\n')

    def test6(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def    ../..'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/\n')

    def test7(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def    ../../..'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/\n')

    def test8(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def  .'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc/def\n')

    def test9(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def   ..klm'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '..klm: No such file or directory\n')

    def test10(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def    //////'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/\n')

    def test11(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def   ......'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '......: No such file or directory\n')

    def test12(self, mock_stdout):
        with mock.patch('builtins.input', return_value='/abc/def    ../gh///../klm/.'):
            my_cd()
            self.assertEqual(mock_stdout.getvalue(), '/abc/klm\n')


if __name__ == '__main__':
    unittest.main()
