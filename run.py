from siulenuem import add_to_cart
from threading import Thread as th
import time
import logging

logging.basicConfig(level=logging.INFO, filename="Buy.log", filemode="w")
logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")


def run_all():
    th(target=add_to_cart, args=["джинсы", "102137348", "26"]).start()
    # th(target=add_to_cart, args=['джинсы', '53575732', '36']).start()
    # th(target=add_to_cart, args=['джинсы', '53575732', '36']).start()
    logging.info("Try to add to cart good 142907858")
    # res = add_to_cart('джинсы', '53575732', '36')
    # while res != 1:
    #     res = add_to_cart('джинсы', '53575732', '36')


run_all()
