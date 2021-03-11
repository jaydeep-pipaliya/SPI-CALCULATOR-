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
    list_sub=d.Get_Branch_Semester_Sub_List(Branch,Semester)
    type='semester'
    return render_template("SPI.html",type=type,branch=Branch,semester=Semester,sublist=list_sub,action='/SPI')

@app.route("/SPI",methods=['POST'])
def SPI():
    type='spi'
    # print(request.values.get('branch-sem'))
    Branch=request.values.get('branch')
    Semester=request.values.get('sem')
    Greadlist=request.form.getlist('sublist')
    # print(sublist)
    # d=request.form.getlist('car2')
    # print(Branch,Semester)
    list_sub=d.Get_Branch_Semester_Sub_List(Branch,Semester)
    # print(list_sub)
    a='fail'
    if "F" not in list_sub:  
        a=g.SPI(list_sub,Greadlist)
    return render_template("SPI.html",type=type,result=a)
app.run(debug=True)



