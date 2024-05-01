from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
import smtplib
from random import *
import random  
import os
from hamming import same_person_eyes
local_server=True
app = Flask(__name__)
app.secret_key = os.urandom(24)


login_manager=LoginManager(app)
login_manager.login_view='login'



@login_manager.user_loader
def load_user(user_id):
    return Ausers.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/votingdb'
db = SQLAlchemy(app)



class Admin(db.Model):
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False,primary_key=True)

class Cand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), unique=True, nullable=False)
    pname = db.Column(db.String(100), unique=True, nullable=False)
    img=db.Column(db.LargeBinary)

class Ausers(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    adno = db.Column(db.String(100), unique=True, nullable=False)
    eimg= db.Column(db.String(100), unique=True, nullable=False)

class Result(db.Model):
    c = db.Column(db.Integer)
    cname = db.Column(db.String(100), unique=True, nullable=False)
    pname = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    loc = db.Column(db.String(100), unique=True, nullable=False)
    uname = db.Column(db.String(100), primary_key=True, nullable=False)

class Finalresult(db.Model):
   
    cname = db.Column(db.String(100), primary_key=True, nullable=False)
    pname = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    loc = db.Column(db.String(100), unique=True, nullable=False)
    ccount = db.Column(db.String(100), unique=True, nullable=False)



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/vucandi")
def vucandi():
    data=db.engine.execute(f"select * from `cand`")
    return render_template("/vucandi.html",data1=data)

      
@app.route("/vuusers")
def vuusers():
    email=current_user.email
    data=db.engine.execute(f"select * from `ausers` where email='{email}'")
    return render_template("/vuusers.html",data1=data)
  


@app.route("/admin",methods=['POST','GET'])
def admin():
    if request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        aadmin=Admin.query.filter_by(username=username,password=password).first()
        if aadmin:
            return render_template("/menu2.html")
            
        else:
            return render_template("/admin.html",a="Invalid username & password")
    
    return render_template("admin.html")

@app.route("/acandi",methods=['POST','GET'])
def acandi():
    if request.method=='POST':
        cname=request.form.get("cname")
        pname=request.form.get("pname")
        img=request.form.get("img")
        loc=request.form.get("loc")
        user=Cand.query.filter_by(cname=cname).first()
        if user:
            return render_template("/acandi.html",a="Candidate already added")
        new_user=db.engine.execute(f"INSERT INTO `Cand`(`cname`,`pname`,`img`,`loc`)VALUES('{cname}','{pname}','{img}','{loc}')")
        return render_template("acandi.html",a="Candidate Added Successfully")
    return render_template("acandi.html")

@app.route("/vcandi")
def vcandi():
    data=db.engine.execute(f"select * from `cand`")
    return render_template("vcandi.html",data1=data)

@app.route("/calc")
def calc():
    data=db.engine.execute(f"select * from `result`")
    return render_template("calc.html",data1=data)



@app.route("/ausers",methods=['POST','GET'])
def ausers():
    if request.method=='POST':
        uname=request.form.get("uname")
        email=request.form.get("email")
        adno=request.form.get("adno")
        eimg=request.form.get("eimg")
        user=Ausers.query.filter_by(email=email).first()
        if user:
            print("user already Exist")
            return render_template("/ausers.html",a="Email Already Exist")

        new_user=db.engine.execute(f"INSERT INTO `Ausers`(`uname`,`email`,`adno`,`eimg`)VALUES('{uname}','{email}','{adno}','{eimg}')")
        return render_template("/ausers.html",a="User added successfully")
    return render_template("ausers.html")


@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        uname=request.form.get("uname")
        email=request.form.get("email")        
        eimg=request.form.get("eimg")
        session['uname'] = request.form['uname']
        otp=''.join([str(randint(0,9)) for i in range(4)])
        print(otp)
        data=db.engine.execute(f"select `eimg` from `ausers` where `uname`='{uname}'")
        for d in data:
            img=d.eimg      
         
        imgae1="C://Users//Mrida//Documents//2021//final voting//static//images//" +eimg
        image2="C://Users//Mrida//Documents//2021//final voting//static//images//" + img
        print(imgae1)
        print(image2)
        verify = same_person_eyes(imgae1,image2)
        print("Dddddfdfdfdfddfdfdfdffffffffffffffffffffffffffffffffffffffffffffff")
        print(verify)
        if verify == verify:
            print("Dvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            new_user=db.engine.execute(f"INSERT INTO `otpverify`(`username`,`otp`)VALUES('{uname}','{otp}')")
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('helloraj67@gmail.com','helloraj@123')
            msg='Hello your otp is '+str(otp)
            server.sendmail('helloraj67@gmail.com',email,msg)
            server.quit()
            return render_template("/averify.html")
        else:
            return render_template("/login.html",a="Invald User")
        
    return render_template("login.html")


@app.route("/averify",methods=['POST','GET'])
def averify():
    
    
    uotp=request.form.get("otp")
    
    data=db.engine.execute(f"select `username` from `otpverify` where `otp`='{uotp}'")
    for d in data:
        uname=d.username
    if session['uname'] ==  uname:
        return render_template("menu.html",a="Transaction Success ")
    else:
        return render_template("averify.html",a="Invalid OTP ") 





@app.route("/vusers")
def vusers():
    
    data=db.engine.execute(f"select * from `Ausers`")
    return render_template("/vusers.html",data1=data)

@app.route("/analysis")
def analysis():
    
    data=db.engine.execute(f"select * from `finalresult`")
    return render_template("/analysis.html",data1=data)


@app.route("/fresults")
def fresults():
    data=db.engine.execute(f"select cname,pname,img,loc,ccount from `finalresult` where ccount=(select max(ccount) from `finalresult`)")
    return render_template("/fresults.html",data1=data)



@app.route("/uactivate",methods=['POST','GET'])
def uactivate():
    
    c = 1
    uname=  session['uname']
    cname = request.args.get('cname')
    print(cname)
    pname = request.args.get('pname')
    print(pname)
    img = request.args.get('img')
    loc = request.args.get('loc')
    print(loc)
    user=Result.query.filter_by(uname=uname).first()
    if user:
        print("user already Voted")
        return render_template("/vucandi.html",a="user already voted")

    new_user=db.engine.execute(f"INSERT INTO `result`(`c`,`cname`,`pname`,`img`,`loc`,`uname`)VALUES('{c}','{cname}','{pname}','{img}','{loc}','{uname}')")
    return render_template("/vucandi.html",a="User voted successfully")



@app.route("/calcu",methods=['POST','GET'])
def calcu():
    

    cname = request.args.get('cname')
    print(cname)
    pname = request.args.get('pname')
    print(pname)
    img = request.args.get('img')
    loc = request.args.get('loc')
    print(loc)
   
    ccount=db.engine.execute(f"select COUNT(c) from `result` where `cname`='{cname}'")
    print("1111111111")
    ccount = ccount.fetchall()
    print(ccount)
    new_user=db.engine.execute(f"INSERT INTO `finalresult`(`cname`,`pname`,`img`,`loc`,`ccount`)VALUES('{cname}','{pname}','{img}','{loc}','{ccount[0][0]}')")
    return render_template("/calc.html",a="User added successfully")
  

'''
@app.route("/insmarks",methods=['POST','GET'])
def insmarks():
    if request.method=='POST':
        usn=request.form.get("usn")
        username=request.form.get("username")
        phy=request.form.get("phy")
        che=request.form.get("che")
        phy=request.form.get("phy")
        mat=request.form.get("mat")
        user=Insmarks.query.filter_by(usn=usn).first()
        if user:
            print("already marks inserted")
            return render_template("/insmarks.html",a="marks already inserted for the usn:",b=usn)
        new_user=db.engine.execute(f"INSERT INTO `insmarks`(`usn`,`username`,`phy`,`che`,`mat`)VALUES('{usn}','{username}','{phy}','{che}','{mat}')")
        return render_template("/insmarks.html",c="Marks inserted successfully")

    return render_template("insmarks.html")


@app.route("/showall")
def showall():
    data=db.engine.execute(f"select * from `insmarks`")
    return render_template("/showall.html",data1=data)
   

@app.route("/search",methods=['POST','GET'])
def search():
    if request.method=='POST':
        usn=request.form.get("usn")
        data=db.engine.execute(f" select * from `insmarks` where `usn`='{usn}'")
        return render_template("/search.html",data1=data)
    return render_template("/search.html")

@app.route("/update",methods=['POST','GET'])
def update():
    if request.method=='POST':menu
        usn=request.form.get("usn")
        data=db.engine.execute(f" select * from `insmarks` where `usn`='{usn}'")
        return render_template("/update2.html",data1=data)
        #usn=request.form.get("usn")
        #username=request.form.get("username")
       #phy=request.form.get("phy")
        #che=request.form.get("che")
        #phy=request.form.get("phy")
        #mat=request.form.get("mat")
        #data=db.engine.execute(f"update `insmarks` set `username`='{username}',`phy`='{phy}',`che`='{che}',mat='{mat}' where `usn`='{usn}';")
        #return render_template("/showall.html")
    return render_template("update.html")

@app.route("/update2",methods=['POST','GET'])
def update2():
    user=Insmarks.query.filter_by().first()
    if request.method=='POST':
        usn=request.form.get("usn")
        username=request.form.get("username")
        phy=request.form.get("phy")
        che=request.form.get("che")
        phy=request.form.get("phy")
        mat=request.form.get("mat")
        db.engine.execute(f"UPDATE `insmarks` SET `username`='{username}',`phy`='{phy}',`che`='{che}',`mat`='{mat}' WHERE `usn`='{usn}'")
        data=db.engine.execute(f"select * from `insmarks`")
        return render_template("/showall.html",data1=data)
    return render_template("update2.html")
    
@app.route("/delete",methods=['POST','GET'])
def delete():
    if request.method=='POST':
        usn=request.form.get("usn")
        db.engine.execute(f"delete from `insmarks` where `usn`='{usn}'")
        data=db.engine.execute(f"select * from `insmarks`")
        return render_template("/showall.html",data1=data)
    return render_template("/delete.html")'''

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000,use_reloader = False)
