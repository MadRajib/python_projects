import gi
import sched, time
import os

gi.require_version('Notify', '0.7')
from gi.repository import Notify

delay = 60*20;
def notify():

    Notify.init("BreakTime")
    Hello = Notify.Notification.new("Hello MadRajib!", "Time To Take A break!.", "dialog-information")
    Hello.set_timeout(10000);
    Hello.show()
    pass

if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        if(os.system("gnome-screensaver-command -q | grep 'is inactive'") == 0):
            notify()
            s.enter(delay, 1, do_something, (sc,))
        else:
            s.enter(10, 1, do_something, (sc,))

    s.enter(1, 1, do_something, (s,))
    s.run()