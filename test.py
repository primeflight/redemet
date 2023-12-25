from redemet.redemet import Redemet

# airports = Redemet().airports("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "BRASIL")
# print(airports)

# airports_status = Redemet().airports_status("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "BRASIL")
# print(airports_status)

airport_info = Redemet().airport_info("5gmpLVuFBdcHCSf928dhXqdpenJdTZ5jGSNSAugv", "SBJU")
print(airport_info)
