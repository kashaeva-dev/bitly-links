from urllib.parse import urlparse
parsed_url = urlparse(input())
print("".join([parsed_url.netloc, parsed_url.path]))