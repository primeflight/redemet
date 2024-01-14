from os import getenv
from dotenv import load_dotenv

load_dotenv()

from redemet.redemet import Redemet


airports_status = Redemet().airport_info(getenv("API_KEY"), "sbfz", taf="sim")
print(airports_status)
