# redemet

Redemet Wrapper Python

The REDEMET API is a product of application programming interfaces (APIs), which will provide access to various meteorological products, currently available on the REDEMET website, quickly and safely to be used for various purposes.

## Commands Dev

```bash
make install-dev
make format
make lint
make test
make coverage
```

## Use Guide

```python
from redemet.redemet import Redemet

airports = Redemet().airports("your_api_key", "BRASIL")
print(airports)

airports_status = Redemet().airports_status("your_api_key", "BRASIL")
print(airports_status)

airport_info = Redemet().airport_info("your_api_key", "SBJU")
print(airport_info)

sigwx = Redemet().product_sigwx("your_api_key")
print(sigwx)

taf = Redemet().messages_taf("your_api_key", ["SBJU"])
print(taf)

sigmet = Redemet().messages_sigmet("your_api_key")
print(sigmet)

meteograma = Redemet().product_messages_meteograma(
   "your_api_key", "SBJU"
)
print(meteograma)

metar = Redemet().product_messages_metar(
   "your_api_key", ["SBJU"]
)
print(metar)

gamet = Redemet().messages_gamet("your_api_key")
print(gamet)
```

## Credits

![assets/img/logo-redemet.png](assets/img/logo-redemet.png)