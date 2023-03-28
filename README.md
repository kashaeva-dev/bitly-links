# Bitly API

This code provides a command line Python wrapper for the Bitly API, which can be used to shorten URLs 
and track clicks on shortened links.

## Requirements
* Python 3.x
* requests module
* dotenv module
## Installation
1. Clone the repository:

```bash
git clone https://github.com/kashaeva-dev/bitly-links.git
```
2. Create a virtual environment:

```bash
python -m venv env
```
3. Activate the virtual environment:

For Windows:

```bash
.\env\Scripts\activate
```
For Linux or macOS:

```bash
source env/bin/activate
```
4. Set up environment variables:

Create a .env file in the project directory.
Add the following line to the .env file:

```bash
BITLY_TOKEN=<your Bitly API token>
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## How to use
To use this code first you should receive a Bitly API access token on the
[Bitly](https://app.bitly.com/settings/api/) webpage. Then you should save it in the
.env file in the following format without any quaters:

BITLY_TOKEN=your_Bitly_API_token

To shorten URLs and track clicks on shortened links you can use either the main.py
file via command line or import separate functions from it.


**You can run the main.py file via command line:**

To use main.py, run the script with the following command:

```
python main.py <url>
```

Replace <url> with the URL you want to shorten or track clicks on.

If the URL is already a Bitlink, the script will return the number of clicks on the link. If it is a regular URL, the script will shorten it and return the Bitlink.

**Examples**

Shorten a URL:

```
python main.py https://google.com
```

Track clicks on a Bitlink:

```
python main.py https://bit.ly/3tvX5W3
```

**You can also import the necessary functions from the main.py file:**

```python
from main import shorten_link, count_clicks, is_bitlink
```
Use the shorten_link function to shorten a URL:

```python
short_url = shorten_link(long_url, token)
```
The long_url argument is the URL you want to shorten, token is <your Bitly API token>, you should load if from your
virtual environment.

The function returns a shortened URL, or an error message if the Bitly service is unavailable or the URL is invalid.

Use the count_clicks function to get the number of clicks on a shortened URL:
```python
clicks = count_clicks(short_url, token)
```
The short_url argument is the URL you want to track clicks on, token is <your Bitly API token>, you should load if from your
virtual environment.
The function returns the number of clicks on the URL.

Use the is_bitlink function to check if a given URL is a Bitly link:
```python
is_bitly = is_bitlink(url, token)
```
The url argument is the URL you want to check.
The function returns True if the URL is a Bitly link, False otherwise.

## Contributing
If you have suggestions for how this code could be improved, please open an issue or 
a pull request. We welcome contributions from the community!
