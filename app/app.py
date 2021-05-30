from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask import jsonify

app = Flask(__name__)



app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'db'

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
        active = 1
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO appUser(first_name, last_name, email, phone_number,active) VALUES(%s, %s,%s, %s,%s)",(first_name, last_name, email, phone_number,active))
        conn.commit()
        return render_template("editSuccess.html", message = "user created!")
        


    conn = mysql.connect()
    cursor =conn.cursor()
    userValue = cursor.execute("SELECT * FROM appUser WHERE active = 1")
    if userValue > 0:
        userDetails = cursor.fetchall()
        
        return render_template('home.html',userDetails = userDetails)

    

    return render_template("home.html")

@app.route('/delete/<int:id>', methods=['get', 'post'])
def delete(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    userValue = cursor.execute("UPDATE appUser SET active=0 WHERE user_id=%s",id)
    conn.commit()
    return render_template("editSuccess.html", message = "deleted!")



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
    
    return render_template("editSuccess.html", message = "edited !")





if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')