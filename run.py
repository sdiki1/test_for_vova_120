from siulenuem import add_to_cart
from threading import Thread as th
import time

def run_sync(target, args):

    time.sleep(1)

def run_all():
    for i in range(1, 1000):
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
        th(target=add_to_cart, args=('джинсы', '164755810')).start()
    # th(target=add_to_cart('джинсы', '164755810')).start()
    # th(target=add_to_cart('джинсы', '164755810')).start()
    # th(target=add_to_cart('джинсы', '164755810')).start()
    # th(target=add_to_cart('джинсы', '164755810')).start()
    # th(target=add_to_cart('джинсы', '164755810')).start()

run_all()