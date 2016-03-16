from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
   #return redirect('/index' ,methods=['GET','POST'])
   return render_template('index2.html')  

@app.route('/index')
def index():
  if request.method == 'GET':  
     return render_template('index2.html', methods=['GET','POST'])
  else:  
      app.vars['stock_tkr'] = request.form['stock_tkr']   
      return render_template('index.html' ,methods=['GET','POST'])
@app.route('/result')
def result():
      return render_template('index.html' ,methods=['GET','POST'])  

if __name__ == '__main__':
  app.run(port=33507)
