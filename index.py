import request
from bs4 import BeautifulSoup
import pickle
from jinja2 import Template

# set the url of the website to visit
url = 'https://contoso.com'

# set the cookies to save
cookies_to_save = ['ESTSAUTH', 'ESTSAUTHPERSISTENT', 'ESTSAUTHLIGHT', 'SignInStateCookie']

# send a GET request to the website
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# extract the cookies from the response
cookies = response.cookies.get_dict()

# filter the cookies to save only the ones specified
cookies_to_save = {cookie_name: cookies[cookie_name] for cookie_name in cookies_to_save if cookie_name in cookies}

# save the cookies to a file using pickle
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies_to_save, f)

# generate the HTML content using Jinja2
with open('dashboard_template.html') as f:
    template = Template(f.read())

html_content = template.render(cookies=cookies_to_save)

# create a dashboard.html file and write the HTML content to it
with open('dashboard.html', 'w') as f:
    f.write(html_content)
