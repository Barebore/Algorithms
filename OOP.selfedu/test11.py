import requests

def get_ip():
    response = requests.get('http://ifconfig.me/ip')
    return response.text
