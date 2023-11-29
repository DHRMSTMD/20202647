#스케줄러(scheduler)
# 정해진 일정에 맞춰서 프로그램을 동작
# ex) 12시간에 한번, 5분마다, 특정일자


#스케줄러 + 프로그램 -> 완성 -> 서버(동작)
# apscheduler
# 1. blocking
# - 스케줄러 + 프로그램만 동작
# 2. background
# - 동작을 하되 뒤에서 조용히!
#

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def print_today():
    print(datetime.now())

#1. 스케줄러 생성
scheduler = BlockingScheduler()

scheduler.add_job(print_today, "interval", seconds=5)
scheduler.start()



