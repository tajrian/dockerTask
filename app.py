from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
 

mysql = MySQL()
mysql.init_app(app)



@app.route('/',methods = ['GET','POST'])
def home():

    if request.method == "POST" :
        userInfo = request.form
        first_name = userInfo["first_name"]
        last_name = userInfo["last_name"]
        email = userInfo["email"]
        mobile_number = userInfo["mobile_number"]
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO flask_user(first_name, last_name, email, phone_number) VALUES(%s, %s,%s, %s)",(first_name, last_name, email, mobile_number))
        conn.commit()
        return "done"

        return "Hi " + first_name
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)