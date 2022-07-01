from flask import Flask, render_template, url_for, request
import requests

import fiscal

app = Flask(__name__)
URL = "https://monitoring.e-kassa.gov.az/pks-portal/1.0.0/documents/"
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == 'POST':
    form = request.form
    cashback = {'fiscal_id': form['fiscal_id'], 'order_value': get_result(form)[0], 'cashback':get_result(form)[1]}
    return render_template('s-page.html', cashback = cashback)

  return render_template('f-page.html')

def get_result(form):
  order_value=get_order_value(form)
  cashback=get_cashback(form)
  return (order_value, cashback)

def get_cashback(form):
  return fiscal.backend(form['fiscal_id'])

def get_order_value(form):
  return fiscal.get_order_value(form['fiscal_id'])

if __name__ == "__main__":
  app.run(debug=True)