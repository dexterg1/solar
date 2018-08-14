import sched, time, datetime
import spa_mod

scheduler = sched.scheduler(time.time, time.sleep)

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, actionargs))
    action(*actionargs)

def sense():
    print('sense')

def track():
    current_time = datetime.datetime.now()
    position =  spa_mod.calculate_position(current_time.year,current_time.month,current_time.day,current_time.hour,current_time.minute,current_time.second,53.4,-6.14)
    print('periodic ' + str(current_time) )
    if position['status'] == 0:
        print(position)

periodic(scheduler, 10, track)
periodic(scheduler, 2, sense)

scheduler.run()

