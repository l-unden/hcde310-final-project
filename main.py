from flask import Flask, render_template, request
import urllib.parse, urllib.request, urllib.error, json
import requests

# run with python 3.6

def safe_get(url):
  try:
    return urllib.request.urlopen(url)
  except urllib.error.HTTPError as e:
    app.logger.info("Error code: ", e.code)
  except urllib.error.URLError as e:
    app.logger.info("Could not reach a server. Reason: ", e.reason)
  return None

app = Flask(__name__)

# this is my apiKey acc96d29012f40f8906d15179e96e0bf if it is at its daily limit you can create your 
# own account at spoonacular.com,verify your account via email and then access your dashboard to get your apikey

baseurl = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=acc96d29012f40f8906d15179e96e0bf&"

params = {"number":"5","ranking":"1","ignorePantry":"false"}


@app.route("/")
def main():
    return render_template('web.html')

@app.route('/recipes')
def get_recipes():
  if (str(request.args.get('ingredients')).strip() != ""):
      params['ingredients'] = request.args.get('ingredients')
      paramsUrl = urllib.parse.urlencode(params)
      url = baseurl + paramsUrl
      app.logger.info(url)
      response = urllib.request.urlopen(url)
      data = json.load(response)
      app.logger.info(data)
      return render_template('recipes.html', recipes=data)
  else:
    return render_template('web.html')
    

app.run(host='localhost', debug = True, port=8000)