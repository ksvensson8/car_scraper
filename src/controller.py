from torrequest import TorRequest
import requests
import stem
from bs4 import BeautifulSoup


def get_carmax_page_api():
    """Get data for a page of 20 vehicles from the CarMax API."""
    # make a GET request to the vehicles endpoint
    page_url = 'https://api.carmax.com/v1/api/vehicles?apikey=adfb3ba2-b212-411e-89e1-35adab91b600'
    response = requests.get(page_url)

    # get JSON from requests and return the results subsection
    return response.json()['Results']

# tr = TorRequest(password='test12345')
# SocksPort = 9052
#
# response = requests.get('http://ipecho.net/plain')
# print("My Original IP Address:", response.text)
#
# tr.reset_identity() #Reset Tor
# response = tr.get('http://ipecho.net/plain')
# print("New Ip Address", response.text)
#
# tor_process = stem.process.launch_tor_with_config(
#     tor_cmd = 'D:\\Tor Browser\\Browser.app\\Tor\\tor.real',
#     config = { SocksPort+': str(SOCKS_PORT),'ExitNodes': '{ru}',},
#     init_msg_handler = print_bootstrap_lines,
# )