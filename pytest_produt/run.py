import pytest
import time
import os


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    times = time.strftime('%Y_%m_%d %H:%M:%S', time.localtime())
    os.system("allure generate ./temps -o ./reports --clean")


