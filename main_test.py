import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '35 5 10 20 40 15'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    for i in range(len(lines)):
        if lines[i].startswith(('h', 'H')):
            result = lines[i]
            break

    # print(lines)

    # ret = main.main()

    regex_string = r'[\w,\W]*[h,H]ello'
    regex_string += r'[\w,\W]*[w,W]orld'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, result)
    assert res != None
    print(res.group())
