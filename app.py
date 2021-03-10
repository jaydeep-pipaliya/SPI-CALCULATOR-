from flask import render_template,Flask,request,redirect
import get as g
app = Flask(__name__)
isGo=True
isSem=True
sem=""
f=1
l=[]

# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))
@app.route("/")
def Home():
    return render_template("Home.html")
@app.route("/SPI")
def SPI():
    isSem=False
    isAns=False
    return render_template("SPI.html",t=isGo,f=isSem,a=isAns)
@app.route("/SPI",methods=["POST"])
def SPISub():
    sem=request.values.get("cars")
    isGo=False
    isSem=True
    isAns=False
    f=g.getNumber(sem)
    l=g.getList(f)
    return render_template("SPI.html",t=isGo,f=isSem,a=isAns,sub=l,n=len(l),s=sem)
@app.route("/SPI2",methods=["POST"])
def SPIANS():
    isGo=False
    isSem=False
    isAns=True
    d=[]
    d=request.form.getlist('car2')
    a=g.SPI(f,d)
    return render_template("SPI.html",t=isGo,f=isSem,a=isAns,ans=a)

app.run(debug=True)



