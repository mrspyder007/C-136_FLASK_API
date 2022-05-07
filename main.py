from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"sucess"
    }),200#give msg 200                                   #world to change [return  "name to be shown"]


@app.route("/planet")

def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data,
        "message":"sucess"
    }),200#give msg 200                                   #world to change [return  "name to be shown"]


if __name__=="__main__":
    app.run()

# to see 2api do
#   http://127.0.0.1:5000/planet?name=11%20Comae%20Berenices%20b
#localhost : code : / planet?name=-----
 