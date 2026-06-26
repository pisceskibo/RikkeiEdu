# TÍNH TRỪU TƯỢNG
from abc import ABC, abstractmethod

## Lớp trừu tượng
class MayTinh(ABC):
    @abstractmethod
    def khoi_dong(self):
        pass 

class Dell(MayTinh):
    def khoi_dong(self):
        return "Khởi động thành công máy tính Dell"
    
class Acer(MayTinh):
    def khoi_dong(self):
        return "Khởi động thành công máy tính Acer"

class Mac(MayTinh):
    def chay(self):
        return "Chạy thành công Mac"
    
dell = Dell()
acer = Acer()
mac = Mac()
print(dell.khoi_dong())
print(acer.khoi_dong())
print(mac.chay())