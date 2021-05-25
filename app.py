from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import yaml 

app = Flask(__name__)

yaml_file = open("/home/user/dockerPractice/docTask/dockerTask/db.yaml", 'r')
db = yaml.load(yaml_file)


app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
 

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