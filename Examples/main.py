import requests

json_data = {
    'script': 'https://newassets.hcaptcha.com/c/278beb8b/hsw.js',
    'req': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiJyTXhsVmlVbEhCMmd0eEduVVVhQ1gxaFRQNkZFVXZydDNFVWFUWlgwMnA0SkZRTVd2aWx1Rml4MnJqS3V4eHhBRWEzYzJDZTJuSmZOWVdCeUUycW9zWTRaelVHem9EbiswNWJIZDRNeEEzOWxDWVZZb0JRb2VrVGJaQ1ZldVF1blhCa1hnMHRlZ05FTVk0MWdOMGJuOGh2UXprbmNtUXZkbEJRRGFiV1BBb1U0YnpjTXViQVdndm1GM3c9PWtmcDhiMEdWeU54N3VjMDkiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvYzI2NTk5NTIiLCJlIjoxNjY0MjU2NzUxLCJuIjoiaHN3In0.rm1eXBWzwvGp6_6EA6E9Kolx26T8_YUjJJPcfYSSdFY'
}

response = requests.post('https://hcaptcha.vxxx.cf/hsw', json=json_data).json()
if response.get('error'):
  raise Exception(response['message'])
  
print(f'Result: {response["result"]}')
