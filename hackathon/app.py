from flask import Flask, request, render_template, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__) #object

client = MongoClient('mongodb://localhost:27017/', 27017)
db = client['farmdb']
collection_cropdata = db['cropdata']
user_collection = db["user"]



@app.route('/data')
def index():
    user =  request.args.get('user')

    return render_template('person.html',user = user )


   

@app.route("/login_data", methods=['POST'])
def login_data():
    phno = request.form["phno"]
    password = request.form["password"]
    
    user = user_collection.find_one({"phno": phno, "password": password}, {"_id": 0}) #object
    
    if user:
        return render_template('person.html',user=user)
    else:
        return "phone number or password is incorrect"

@app.route("/")
def login():
    return render_template("login.html")



def calculate(nutrients,soil_nutrients):
    inorganic_values = []
    result = {} 

    for i in range(len(nutrients)):
        diff = abs(nutrients[i][1] - (soil_nutrients[i][0]+soil_nutrients[i][1])//2 )
        if nutrients[i][1] <= soil_nutrients[i][1] and nutrients[i][1] >= soil_nutrients[i][0]:

            result[nutrients[i][0]] = "is within accurate range ✅"

            inorganic_values.append(0)


        elif nutrients[i][1] < soil_nutrients[i][0]:

            result[nutrients[i][0]] = f"is deficient by {diff} units ❌"

            inorganic_values.append(diff)

        else:
            result[nutrients[i][0]] = f"is excess by {diff} units ❌"
            inorganic_values.append(0)

    return (result,inorganic_values) #({},[])
   

        
    

    

@app.route("/page2",methods=['POST'])
def page2():

    soiltype = request.form["soiltype"]
    croptype = request.form["croptype"]
    n = float(request.form["n"])
    k = float(request.form["k"])
    p = float(request.form["p"])

    cropdata = collection_cropdata.find_one({"crop":croptype,soiltype: {"$exists": True}},{'_id':0})

    if cropdata:

        x = calculate([["Nitrogen",n],["Phosphorus",p],["Potassium",k]],cropdata[soiltype])
        result = x[0]
        inorganic_values = x[1]

        return render_template('page2.html',result = result.items(),organic = cropdata["organic"],inorganic_values = inorganic_values)
    
    else:
         return "Crop data not found"









if __name__ == '__main__':
    app.run(debug=True)
