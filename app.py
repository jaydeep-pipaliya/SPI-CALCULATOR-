from crypt import methods
from flask import render_template,Flask,request,redirect
import Spi_Calculator as g
import Data as d


app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("Home.html")


@app.route("/branch")
def Branch():
    type='branch'
    data_branch=d.Get_Branch_List()
    data_sem=d.Get_Branch_Semester_List()
    # jsonify(message)
    return render_template("SPI.html",type=type,branchlist=data_branch,semlist=data_sem,action='/semester')


@app.route("/semester",methods=['POST'])
def Semester():
    Branch=request.values.get("branch")
    Semester=request.values.get("semester")
    print(Branch,Semester)
    # print(request.values)
    type='semester'
    # print("zeel")
    print(type)
    return render_template("SPI.html",type=type)

@app.route("/SPI")
def SPI():
    type='spi'
    # d=request.form.getlist('car2')
    # a=g.SPI(f,d)
    return render_template("SPI.html",type=type)
app.run(debug=True)



