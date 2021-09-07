from flask import Flask,render_template,redirect,request,url_for
import mysql.connector
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='saidb'
mysql=MySQL(app)
@app.route('/')
def student():
    return render_template("app2_index.html")
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form.to_dict()
        name=result['name']
        physics=int(result['physics'])
        chemistry=int(result['chemistry'])
        maths=int(result['maths'])
        s=str(physics+chemistry+maths)
        result["total"]=s
        #total=result['total']
        mycur = mysql.connection.cursor()
        mycur.execute("insert into priyanka(name,physics,chemistry,maths,total) values(%s,%s,%s,%s,%s)",(name,physics,chemistry,maths,total))
        mysql.connection.commit()
        mycur.close()
        return redirect(url_for("/getting"))
    return render_template("app2_index.html")
@app.route('/getting')
def get():
    mycur=mysql.connection.cursor()
    res=mycur.execute("SELECT * FROM priyanka")
    if res>0:
        res1=mycur.fetchall()
        return render_template("app2_result.html",res1=res1)
app.run(debug=True)
