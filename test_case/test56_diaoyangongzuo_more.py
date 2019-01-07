#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class diaoyangongzuo_moreTest(MyTest):

    def test_click_diaoyangongzuo_more(self):
        '''调研工作栏“更多”按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_diaoyangongzuo()
        pagehome.click_diaoyangongzuo_more()   #点击链接
        wait_title(self, pagehome.diaoyangongzuo_more_title)
        #判断新页面的title是否与预设的title相同
        assert(pagehome.driver.title == pagehome.diaoyangongzuo_more_title), "标题不是“%s”，测试不通过" % \
                                                                             pagehome.diaoyangongzuo_more_title


if __name__ == '__main__':
    unittest.main()