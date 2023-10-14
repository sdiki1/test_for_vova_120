from siulenuem import add_to_cart
from threading import Thread as th
import time

def run_sync(target, args):

    time.sleep(1)

def run_all():
    add_to_cart('джинсы', '163808147')
run_all()