from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())
listibensin = []
cheap95 = {"bensin95":data["results"][0]["bensin95"],"stadur":data["results"][0]["name"],"fyrirtaeki":data["results"][0]["company"]}
cheapD = {"diesel":data["results"][0]["diesel"],"stadur":data["results"][0]["name"],"fyrirtaeki":data["results"][0]["company"]}
for x in data["results"]:
    if x["bensin95"] < cheap95["bensin95"]:
        cheap95 = {"bensin95":x["bensin95"],"stadur":x["name"],"fyrirtaeki":x["company"]}
    if x["diesel"] < cheapD["diesel"]:
        cheapD = {"diesel":x["diesel"],"stadur":x["name"],"fyrirtaeki":x["company"]}
    listibensin.append(x)
date = data["timestampPriceCheck"]
myndir = {"Atlantsolía":"/static/atlantsolia.png","Costco Iceland":"/static/costco.png","Dælan":"/static/daelan.png","N1":"/static/n1.png","ÓB":"/static/ob.png","Olís":"/static/olis.png","Orkan":"/static/orkan.png"}
    

@app.errorhandler(404)
def error404(error):
    return render_template("error.html"),404

@app.route("/")  
def index():
    return render_template("index.html", date=date, diesel=cheapD, oktan=cheap95, listi=listibensin, s=[], dictM = myndir)

@app.route("/data")
def gogn():
    return data

@app.route("/gas/<id>")  
def fyrirtaeki(id):
    return render_template("gas.html",listi=listibensin, nafn = id)

if __name__ == "__main__":
    app.run(debug = True)
