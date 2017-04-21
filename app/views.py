from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Awesome User'}  # fake user
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
	if request.method == 'POST':
		symbol = request.form['SYM']
		allotment = request.form['ALT']
		fsp = request.form['FSP']
		sc = request.form['SC']
		isp = request.form['ISP']
		bc = request.form['BC']
		cg = request.form['CG']
		return render_template('calculate.html', title='Result', symbol=symbol, allotment=allotment, fsp=fsp, sc=sc, isp=isp, bc=bc, cg=cg)

"""
va10 = raw_input("Ticket Symbol:\n")
var1 = int(raw_input("Allotment:\n"))
var2 = float(raw_input("Final Share Price:\n"))
var3 = round(float(raw_input("Sell Commission:\n")),2)
var4 = round(float(raw_input("Initial Share Price:\n")),2)
var5 = round(float(raw_input("Buy Commission:\n")),2)
var6 = round(float(raw_input("Capital Gain Tax Rate(%):\n")),2)
Proceeds = round((var1)*(var2),2)
Total_Purchase_price = round((var1)*(var4),2)
CapitalGain = round(Proceeds-Total_Purchase_price-(var3)-(var5),2)
TaxOnCapitalGain = round(((var6)*CapitalGain)/100.0,2)
NetProfit = round(CapitalGain-TaxOnCapitalGain,2)
cost = round(Total_Purchase_price + (var5) + (var3) + TaxOnCapitalGain,2)
ReturnOnInvestment = round((NetProfit*100.0)/cost,2)
breakeven = round((Total_Purchase_price + (var5) + (var3))/(var1),2)
var11 = "%" 
"""
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
      	symbol = request.form['SYM']
      	allotment = float(request.form['ALT'])
      	fsp = float(request.form['FSP'])
      	sc = float(request.form['SC'])
      	isp = float(request.form['ISP'])
      	bc = float(request.form['BC'])
      	cg = float(request.form['CG'])
      	proceeds = round((allotment*fsp), 2)
        purchase_price = round((allotment)*(isp),2)
        CapitalGain = round(proceeds-purchase_price-(sc)-(bc),2)
        TaxOnCapitalGain = round(((cg)*CapitalGain)/100.0,2)
        NetProfit = round(CapitalGain-TaxOnCapitalGain,2)
        cost = round(purchase_price + (bc) + (sc) + TaxOnCapitalGain,2)
        ReturnOnInvestment = round((NetProfit*100.0)/cost,2)
        breakeven = round((purchase_price + (bc) + (sc))/(allotment),2)
      	return render_template('result.html',symbol=symbol, title='Result', result=result, proceeds=proceeds, pp = purchase_price, CapitalGain=CapitalGain, TaxOnCapitalGain=TaxOnCapitalGain, NetProfit=NetProfit, cost=cost, ReturnOnInvestment=ReturnOnInvestment, breakeven=breakeven)

if __name__ == '__main__':
   app.run(debug = True)
