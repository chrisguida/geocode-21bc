import requests, urllib, json, yaml
from flask import Flask, request
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment
from flask import send_from_directory

app = Flask(__name__, static_folder='static')
API_KEY = json.load(open('geocode-api.json')).get('key')
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/geocode', methods=['POST'])
# @payment.required(1) #For testing
@payment.required(1000)
def geocode():
    '''
    Geocodes an address
    '''
    params = {
        'address': request.form.get('address'),
        'key': API_KEY
    }
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?' + urllib.parse.urlencode(params))
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

@app.route('/manifest')
def docs():
    '''
    Provides the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

@app.route('/client')
def client():
    '''
    Provides an example client script.
    '''
    import os
    print(os.getcwd())
    return send_from_directory('/home/twenty/geocode-21bc/static', 'client.py')

