from flask import Flask, render_template, request
import config1
import numpy as np
from credit_app import function1

user = 'maddy'
password ='12345'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('log1.html')

@app.route('/login', methods = ['POST'])

def login():
    u1 = str(request.form.get('username'))
    p1 = str(request.form.get('password'))
    
    if user == u1 and password== p1:
        return render_template('index1.html')

    else:
        return render_template('log1.html')
    # return "pass"

@app.route('/predict',methods = ['POST'])
def credit_app():
    


    LIMIT_BAL = int(request.form.get('LIMIT_BAL'))
    SEX = int(request.form.get('SEX'))
    EDUCATION = int(request.form.get('EDUCATION'))
    MARRIAGE = int(request.form.get('MARRIAGE'))
    AGE = int(request.form.get('AGE'))
    
    Repayment_status_in_September = int(request.form.get('Repayment_status_in_September'))
    Repayment_status_in_August = int(request.form.get('Repayment_status_in_August'))
    Repayment_status_in_July = int(request.form.get('Repayment_status_in_July'))
    Repayment_status_in_June = int(request.form.get('Repayment_status_in_June'))
    Repayment_status_in_May = int(request.form.get('Repayment_status_in_May'))
    Repayment_status_in_April = int(request.form.get('Repayment_status_in_April'))

    Amount_of_bill_statement_in_September = int(request.form.get('Amount_of_bill_statement_in_September'))
    Amount_of_bill_statement_in_August = int(request.form.get('Amount_of_bill_statement_in_August'))
    Amount_of_bill_statement_in_July = int(request.form.get('Amount_of_bill_statement_in_July'))
    Amount_of_bill_statement_in_June = int(request.form.get('Amount_of_bill_statement_in_June'))
    Amount_of_bill_statement_in_May = int(request.form.get('Amount_of_bill_statement_in_May'))
    Amount_of_bill_statement_in_April = int(request.form.get('Amount_of_bill_statement_in_April'))

    Amount_of_previous_payment_in_September = int(request.form.get('Amount_of_previous_payment_in_September'))
    Amount_of_previous_payment_in_August = int(request.form.get('Amount_of_previous_payment_in_August'))
    Amount_of_previous_payment_in_July = int(request.form.get('Amount_of_previous_payment_in_July'))
    Amount_of_previous_payment_in_June = int(request.form.get('Amount_of_previous_payment_in_June'))
    Amount_of_previous_payment_in_May = int(request.form.get('Amount_of_previous_payment_in_May'))
    Amount_of_previous_payment_in_April = int(request.form.get('Amount_of_previous_payment_in_April'))

    print(LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,Repayment_status_in_September,
    Repayment_status_in_August,Repayment_status_in_July,Repayment_status_in_June,
    Repayment_status_in_May,Repayment_status_in_April,Amount_of_bill_statement_in_September,
    Amount_of_bill_statement_in_August,Amount_of_bill_statement_in_July,Amount_of_bill_statement_in_June,
    Amount_of_bill_statement_in_May,Amount_of_bill_statement_in_April,Amount_of_previous_payment_in_September,
    Amount_of_previous_payment_in_August,Amount_of_previous_payment_in_July,Amount_of_previous_payment_in_June,
    Amount_of_previous_payment_in_May,Amount_of_previous_payment_in_April)
    data = np.array([[LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,Repayment_status_in_September,
    Repayment_status_in_August,Repayment_status_in_July,Repayment_status_in_June,
    Repayment_status_in_May,Repayment_status_in_April,Amount_of_bill_statement_in_September,
    Amount_of_bill_statement_in_August,Amount_of_bill_statement_in_July,Amount_of_bill_statement_in_June,
    Amount_of_bill_statement_in_May,Amount_of_bill_statement_in_April,Amount_of_previous_payment_in_September,
    Amount_of_previous_payment_in_August,Amount_of_previous_payment_in_July,Amount_of_previous_payment_in_June,
    Amount_of_previous_payment_in_May,Amount_of_previous_payment_in_April]])
    result =  function1.credit_prediction(data)

            
    


    
    return render_template('index1.html',Credit_Card_result=result)

if __name__ == "__main__":
    app.run(debug=True, host=config1.HOST_NAME,port=config1.PORT_NUMBER)
