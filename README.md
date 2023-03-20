# Bitly API

This code provides a Python wrapper for the Bitly API, which can be used to shorten URLs 
and track clicks on shortened links.

## Requirements
* Python 3.x
* requests module
* dotenv module to load token and group_guid variables from the enviroment
## Installation
1. Clone the repository:

```bash
git clone https://github.com/kashaeva-dev/bitly-links.git
```
2. Install the required packages:

```bash
pip install -r requirements.txt
```
3. Create a virtual environment:

```bash
python -m venv env
```
4. Activate the virtual environment:

For Windows:

```bash
.\env\Scripts\activate
```
For Linux or macOS:

```bash
source env/bin/activate
```
Set up environment variables:

Create a .env file in the project directory.

5. Add the following lines to the .env file:

```bash
BITLY_TOKEN=<your Bitly access token>
GROUP_GUID=<your Bitly group GUID>
```
## How to use
To use this code first you should receive a Bitly API access token on the
https://app.bitly.com/settings/api/ webpage. Then you should save it in the
.env file in the following format:

BITLY_TOKEN=token_you_get

without any quaters.
Then you should get a group_guid. For this purpose you can run "connection.py"
file:
```python
python connection.py
```
Then you should use the default_group_guid value to add the GROUP_GUID variable in the
.env file. The format of the GROUP_GUID variable is the same as the BITLY_TOKEN. You should
add to the .env file:

GROUP_GUID=default_group_guid_value

To shorten URLs and track clicks on shortened links you can use either the main.py
file or import separate functions from it.
### Just run main.py file:
You can just run the main.py file:
```python
python main.py
```
You will be prompted to enter a URL. If the URL is a Bitly link, the script
will return the total number of clicks on that link. If the URL is not 
a Bitly link, the script will use Bitly's API to shorten the URL and 
return the shortened link.
###Import the necessary functions from the main.py file:
```python
from main import shorten_link, count_clicks, is_bitlink
```
Use the shorten_link function to shorten a URL:
```python
short_url = shorten_link(long_url)
```
The long_url argument is the URL you want to shorten.
The function returns a shortened URL, or an error message if the Bitly service is unavailable or the URL is invalid.

Use the count_clicks function to get the number of clicks on a shortened URL:
```python
clicks = count_clicks(short_url)
```
The short_url argument is the URL you want to track clicks on.
The function returns the number of clicks on the URL, or an error message if the Bitly service is unavailable or the URL is invalid.

Use the is_bitlink function to check if a given URL is a Bitly link:
```python
is_bitly = is_bitlink(url)
```
The url argument is the URL you want to check.
The function returns True if the URL is a Bitly link, False otherwise.

## Contributing
If you have suggestions for how this code could be improved, please open an issue or 
a pull request. We welcome contributions from the community!
