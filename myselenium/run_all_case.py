import unittest,HTMLTestRunner
import os

case_path = os.path.join(os.getcwd(),"case")
report_path = os.path.join(os.getcwd(),"report")

def all_case():
    disccover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(disccover)
    return disccover

if __name__ == "__main__":
    #runner = unittest.TextTestRunner()
    #runner.run(all_case())
    report_abspath = os.path.join(report_path, "result.html")
    f = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="UI自动化测试报告,测试结果如下：",description="用例执行情况：")

    # 调用add_case函数返回值
    runner.run(all_case())
    f.close()