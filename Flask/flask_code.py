from flask import Flask,render_template,request
from registration import Register
from loginenc import LoginEnc
from logindec import LoginDec
from PublicKeys import PublicKeys
app=Flask(__name__)
@app.route('/')
@app.route('/index')
def content():
    message=None
    return render_template("index.html",message=message)
@app.route('/register',methods=['GET','POST'])
def register():
    message = None
    valid=0
    if request.method =="POST" and 'username' in request.form and 'password' in request.form :
        username= request.form['username']
        password = request.form['password']
        valid = Register().register(username,password)
        if valid == -1:
                message = "Please enter the correct password"
        elif valid ==-2:
                message = 'Username already exists'
        else :
                message = 'Registration Successful'

    return render_template('register.html',message=message,valid=valid)

@app.route('/login',methods=['GET','POST'])
def login():
    message=None
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if not PublicKeys.is_present(username):
            return render_template('login.html',message ="The username does not exist")
        obj1=LoginEnc()
        encrypted_msg=obj1.get_encrypt(username)
        obj2=LoginDec()
        decrypted_msg=obj2.decrypt(encrypted_msg,password)
        if obj1.isValid(decrypted_msg):
            return render_template('index.html',message=username)
        else:
            return render_template('login.html',message ="Wrong Password")

    return render_template('login.html')

app.run(port=3001,debug=True)

