# need to install requests via command: pip install requests
import requests


def what_is_country(ip):
    api = "https://api.ip2country.info/ip?{}"
    response = requests.get(api.format(ip))

    # convert to dictionary
    data = response.json()
    return data["countryName"]


print("Please, put IP address: ")

ip_address = input()

print("Country with IP address: {} is {}".format(ip_address, what_is_country(ip_address)))
