import datetime
import time
from function import sayHello

# Pip module
from camelcase import CamelCase

today = datetime.date.today()
timestamp = time.process_time()

c=CamelCase()
print(c.hump('hello bro kaisa hai tu'))

sum= sayHello(5,5)
print(sum)