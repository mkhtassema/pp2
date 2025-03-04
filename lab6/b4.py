import time
import math
def delayed_square_root(number,delay):
    time.sleep(delay/1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")
    num = int(input)
    delay = int(input)
    delayed_square_root(num, delay)
