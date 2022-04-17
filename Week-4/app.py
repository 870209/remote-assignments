import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, Response, jsonify, json, session, url_for, redirect, render_template
from flask_bcrypt import generate_password_hash, check_password_hash


app = Flask(__name__)
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='870209',
    database='assignment'
    )

my_cursor=mydb.cursor()
#my_cursor.execute("CREATE TABLE user (id INTEGER AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255),password VARCHAR(255))")

def insert(params):
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='870209',
    database='assignment'
    )

    my_cursor=mydb.cursor()
    query = "INSERT INTO user (email, password) VALUEs (%s, %s)"
    try:
        my_cursor.execute(query, params)
        mydb.commit()
        mydb.close()
        return True
        
    except:
        mydb.rollback()
        mydb.close()
        return False

def get(params):
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='870209',
    database='assignment'
    )


    cursor = mydb.cursor(mysql.cursors.DictCursor)
    query = "SELECT * FROM user WHERE email = %s"
    cursor.execute(query, params)
    entries = cursor.fetchall()

    return entries[0]

def check(params):

    query = "SELECT EXISTS(SELECT * FROM user WHERE email= %s)"
    my_cursor.execute(query, params)

    if my_cursor.fetchall()[0][0]:
        return True
    else:
        return False
    

app = Flask(__name__)


@app.route('/')
def home():
    if 'username' in session:
        user_id = session['username']
        return render_template('index.html')
       
    else:
        return render_template('login.html')


@app.route('/login', methods =['POST'])
def login():
    login_info = json.loads(request.data)
    email = login_info['email']
    password = login_info['password']
    
    if check(email):
        try:
            user_info = get(email)
            if check_password_hash(user_info['password'], password):
                session['username'] = user_info['id']
                return render_template('index.html')
            else:
                return 'The password is wrong'
        except:
            return Response(status=401)
    else:
        return  "Couldn't find your account"
    


@app.route('/register', methods=['POST'])
def register():
    user_info = json.loads(request.data)
    email = user_info['email']
    password = user_info['password']
    comfirm_password = user_info['confirm_password']

    if check(email):
        return 'The email is taken. Please try another.'
    
    else:
        if password == comfirm_password:
            password_hash = generate_password_hash(password)

            if insert((email, password_hash)):
                return render_template('login.html')
                
            else:
                return 'Failed'
        else:
            return 'Your new and confirm password are different. Please enter your passwords again.'



if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
