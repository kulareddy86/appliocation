from unicodedata import name
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Sonybravia@86"
app.config['MYSQL_DB'] = "infobell"
mysql = MySQL(app)
@app.route('/',methods=['GET', 'POST'])

def post():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO edetails(name,email,address,phone) VALUES (%s,%s,%s,%s)",(username,email,address,phone))
        mysql.connection.commit()
        cur.close()
        return "sucess"
    return render_template('index.html')
def get():
    if request.method == 'GET':
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM edetails")
        mysql.connection.commit()
        cur.close()
        return "sucess"
    return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
    