import robin_stocks as r
import os

print(r.__file__)

RH_LOGIN = os.environ['RH_LOGIN']
RH_PASS = os.environ['RH_PASS']

login = r.login(RH_LOGIN, RH_PASS)
print(r.build_holdings())
