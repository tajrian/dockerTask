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
        phone_number = userInfo["phone_number"]
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO appUser(first_name, last_name, email, phone_number) VALUES(%s, %s,%s, %s)",(first_name, last_name, email, phone_number))
        conn.commit()
        return "done"


    conn = mysql.connect()
    cursor =conn.cursor()
    userValue = cursor.execute("select * from appUser")
    if userValue > 0:
        userDetails = cursor.fetchall()
        
        return render_template('home.html',userDetails = userDetails)
    
    return render_template("home.html")


@app.route('/edit/<int:id>', methods=['get', 'post'])
def edit(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    #print(type(id))
    userValue = cursor.execute("SELECT user_id,first_name,last_name,email,phone_number FROM appUser WHERE user_id=%s",id)
    if userValue > 0:
        userDetails = cursor.fetchall()

    if userDetails:
        return render_template("edit.html", userDetails = userDetails ) 

    return "We are lost dr kim! :("

@app.route('/update',methods = ['GET','POST'])
def update():

    if request.method == "POST" :
        userInfo = request.form
        id = userInfo['id']
        first_name = userInfo["first_name"]
        last_name = userInfo["last_name"]
        email = userInfo["email"]
        phone_number = userInfo["phone_number"]
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute ("""UPDATE appUser SET first_name=%s, last_name=%s, email=%s, phone_number=%s WHERE user_id=%s""", (first_name,last_name,email,phone_number,id))
        conn.commit()
    
    return render_template("editSuccess.html")




if __name__ == "__main__":
    app.run(debug=True)