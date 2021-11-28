from datetime import datetime
import time

def starting_timer():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    H_list = list(current_time)
    H_str = H_list[0]+H_list[1]
    H_int = int(H_str)
    while True:
        time.sleep(30)
        print('cheacking...')
        if(H_int - 7 == 8):
            print('yes')
        else:
            test()

starting_timer()