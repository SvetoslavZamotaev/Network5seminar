from time import sleep
from datetime import datetime
import threading


def boilledWater():
    sleep(4)


def timeforCook():
    sleep(4)


def openFood():
    sleep(2)


def throwFood():
    sleep(1)


def Normal():
    start = datetime.now()
    openFood()
    throwFood()
    boilledWater()
    timeforCook()
    end = datetime.now()
    print(end - start)


Normal()


start = datetime.now()
threading.Thread(target=boilledWater).start()

openFood()
throwFood()
timeforCook()
end = datetime.now()
print(end - start)
