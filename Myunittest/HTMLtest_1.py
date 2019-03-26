#-*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner



# class logintest(unittest.TestCase):
#     def setUp(self):
#         self.a= 1
#
#     def test1(self):
#         b= 2
#         c= 3
#         self.assertEqual(self.a+b,c)
#
#     def test2(self):
#         b= 2
#         c= 4
#         self.assertEqual(self.a+b,c)
#
#
#
# def suite():
#     # logintestcase= unittest.TestSuite()
#     # logintestcase.addTest(logintest('test1'))
#     # logintestcase.addTest(logintest('test2'))
#     logintestcase= unittest.makeSuite(logintest,'test')
#     return logintestcase



if __name__ == '__main__':
    fr= open('res1.html','wb')
    # runner= HTMLTestRunner.HTMLTestRunner(stream= fr,title= '测试报告',description= '详情')
    # runner.run(suite())