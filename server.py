import requests, urllib, json
from flask import Flask, request
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
API_KEY = json.load(open('geocode-api.json')).get('key')
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/geocode', methods=['POST'])
# @payment.required(1) #For testing
@payment.required(1000)
def geocode():
    params = {
        'address': request.form.get('address'),
        'key': API_KEY
    }
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?' + urllib.parse.urlencode(params))
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

