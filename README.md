# Coinsideration

Coinsideration is a web app used to gather basic information about a cryptocurrency when queried with a cryptocurrency name. It's built with Flask, Python, HTML5, and CSS, with the Bootstrap framework. It uses the CoinmarketCap API for crypto market data.

project video
https://youtu.be/tr68P88UrLA


## Installation
First install Flask using the steps below or the documentation. [The documentation to install Flask is found here](https://flask.palletsprojects.com/en/2.2.x/installation/).

The documentation recommends creating a virtual environment to manage the dependencies for your project, both in development and in production.

#### Create an environment:

###### Mac/Linux:

```bash
mkdir myproject
```
```bash
cd myproject
```
```bash
python3 -m venv venv
```

###### Windows:

```bash
mkdir myproject
```
```bash
cd myproject
```
```bash
py -3 -m venv venv
```

#### Active your virtual environment

###### Mac/Linux:

```bash
. venv/bin/activate
```
###### Windows:

```bash
venv\Scripts\activate
```
Your terminal prompt should now be prepended with (venv) as shown below
```bash
(venv) myproject/ $
```

#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask and other required packages.

```bash
pip install Flask
```
```bash
pip install Flask-Session
```
```bash
pip install requests
```
```bash
pip install -U MarkupSafe
```
Alternatively you can check to see if each of these packages are already installed, and install them if they aren't.

```bash
pip show package_name
```
Requires [CoinMarketCap API key](https://coinmarketcap.com/api/) to provide crypto data.

Once you've obtained a CoinMarketCap API key, it is recommended to set it as an environment variable before running the app. If the API key is not set, then a Runtime Error will occur with the message "API_KEY not set".

```bash
export API_KEY='YOUR_API_KEY'
```

There is also a SECRET_KEY in the app, but it is randomly generated and included in the app.py file in order for flash messaging to work and can be changed and/or moved to an environment variable. It was left in app.py for demonstration purposes.

Once the API_KEY environment variable has been defined, then the app can be run. Make sure you are still in your project folder's root directory, and run flask
```bash
flask run
```
or you can run with a debugger
```bash
flask --debug run
```
Open the html link presented in your terminal after running flask and the app should load in the browser, while your flask development server runs in your terminal.

Enter a valid cryptocurrency name and it will provide you with information about it, including ticker symbol, price, supply, market cap, a description, and technical docs if available.