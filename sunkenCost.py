import math
import time

def main():
    start_time = (2018, 1, 1, 0, 0, 0, 0, 1, 1)
    monthly_wage = 3000000
    seconds_in_month = 60 * 60 * 24 * 30

    wps = monthly_wage/seconds_in_month
    passed_seconds = time.time() - time.mktime(start_time)

    sunken_cost = int(round(wps * passed_seconds, -3))
    passed_time = time.strftime('%ddays %Hhours %Mminutes %Sseconds ', time.gmtime(passed_seconds))

    print( str(passed_time) + ' have passed from the begining.')
    print('Sunken cost is about %d won.' % sunken_cost)

if __name__ == '__main__':
    main()