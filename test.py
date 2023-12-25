from redemet.redemet import Redemet

# airports = Redemet().airports("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "BRASIL")
# print(airports)

# airports_status = Redemet().airports_status("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "BRASIL")
# print(airports_status)

# airport_info = Redemet().airport_info("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "SBJU")
# print(airport_info)

# sigwx = Redemet().product_sigwx("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv")
# print(sigwx)

# taf = Redemet().messages_taf("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", ["SBJU"])
# print(taf)

# sigmet = Redemet().messages_sigmet("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv")
# print(sigmet)

# meteograma = Redemet().product_messages_meteograma(
#    "5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "SBJU"
# )
# print(meteograma)

# metar = Redemet().product_messages_metar(
#    "5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", ["SBJU"]
# )
# print(metar)

gamet = Redemet().messages_gamet("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv")
print(gamet)
