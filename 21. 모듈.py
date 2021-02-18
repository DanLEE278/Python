'''
모듈은 만들어진 다른 파일을 불러와서 쓰는 역할을 한다
내가 만든 일종의 라이브러리를 불러온다고 생각하면 쉽다
모듈을 import하는 방법은 크게 세가지가 있다
 '''

# 모듈 import 방법 1
import module_theater

module_theater.price(3)
module_theater.price_soldiers(6)
module_theater.price_morning(30)

# 모듈 import 방법 2
import module_theater as tm # 모듈 import 방법 2
tm.price(3)
tm.price_morning(5)
tm.price_soldiers(7)

# 모듈 import 방법 3
from module_theater import * # theater_moudle에 있는 모든 것을 사용할때
price(3)
price_morning(4)
price_soldiers(6)

# 원하는 모듈만 가져오고 싶을 때
from module_theater import price, price_morning
price(7)
price_morning(3)

# 원하는 모듈만 빼서 따로 이름을 지어 줄 수 있음
from module_theater import price_soldiers as price
price(5)