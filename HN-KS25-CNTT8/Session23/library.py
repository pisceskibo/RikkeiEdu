# Thư viện trong python
"""
from filename import ....
import ....
"""

## Thư viện toán học
### Cách 1: chưa biết rõ function mình cần lấy
import math
print(math.sqrt(9))

### Cách 2: nên sử dụng 
from math import sqrt
print(sqrt(9))

## Thư viện về thời gian
from datetime import datetime
print(datetime.now())


# Thư viện bên thứ ba
"""
1. Terminal:
    pip install <tên thư viện muốn cài>

2. Xuất thư viện như bình thường
"""
import numpy 
print(numpy.mean(numpy.array([1, 2, 3, 4])))

## Thư viện math
"""
Lưu ý: hạn chế sử dụng import *
"""
from math import *

"""
Cách 1:
from folder import filename
filename.function()

Cách 2:
from folder.filename import function
functon()

Cách 3:
import function
function()

Cách 4: bí danh (đổi tên cho thư viện)
import library as <tên mới>
VD: thư viện numpy => np, matplotlib => plt, pandas => pd
"""
import pandas as pd
import numpy as np
print(np.mean(np.array([1, 2, 3, 4])))


"""
Phân cấp thư mục
. : trả về thư mục cùng cấp
.. : trả về thư mục cấp cha mẹ
"""