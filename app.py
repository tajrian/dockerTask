from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():

    if request.method == "POST" :
        userInfo = request.form
        first_name = userInfo["first_name"]
        last_name = userInfo["last_name"]
        email = userInfo["email"]
        mobile_number = userInfo["mobile_number"]

        return "Hi" + first_name
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)