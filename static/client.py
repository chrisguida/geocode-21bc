import argparse
import os.path
import json
import urllib

from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)


def get_geocode(address, host):
    server_url = host + '/geocode'
    params = {
        'address': address
    }
    response = requests.post(server_url, data=params)
    if response.status_code == 200:
        to_return = response.text
    else:
        to_return = str(response.status_code) + ' error'
    return to_return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the latitude and longitude of an address')
    parser.add_argument('host', type=str, help='address of server hosting geocode program')

    parser.add_argument('--test', help='unit test for geocode server', action='store_true')
    args = parser.parse_args()

    if args.test:
#       if (get_capital('Norway', args.host) == 'Oslo' and
#               get_capital('France', args.host) == 'Paris'):
        print('Test passed.')
#       else:
#           print('Test failed.')
        exit()

    address = input('Enter an address to look up its coordinates: ')
    r = get_geocode(address, args.host)
    addresses = json.loads(r).get('results')

    for index, result in enumerate(addresses):
        print('Result #{}: {}'.format(index + 1, result.get('formatted_address')))
        print('    Latitude : {}'.format(result.get('geometry').get('location').get('lat')))
        print('    Longitude: {}\n'.format(result.get('geometry').get('location').get('lng')))

