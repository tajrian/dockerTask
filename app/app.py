from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import yaml 

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
        cursor.execute("INSERT INTO appUser(first_name, last_name, email, phone_number, active) VALUES(%s, %s,%s, %s, %s)",(first_name, last_name, email, phone_number,active))
        conn.commit()
        return render_template("editSuccess.html", message = "user created!")
        


    conn = mysql.connect()
    cursor =conn.cursor()
    userValue = cursor.execute("select * from appUser")
    if userValue > 0:
        userDetails = cursor.fetchall()
        
        return render_template('home.html',userDetails = userDetails)

    

    return render_template("home.html")

@app.route('/delete/<int:id>', methods=['get', 'post'])
def delete(id):
    
    return ("Here to delete")
    


@app.route('/edit/<int:id>', methods=['get', 'post'])
def edit(id):
    
    return "Here to edit! "
    

@app.route('/update',methods = ['GET','POST'])
def update():

    return ("Here to update!")




if __name__ == "__main__":
    app.run(debug=True)