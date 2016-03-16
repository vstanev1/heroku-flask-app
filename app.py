from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/' , methods=['GET','POST'])
def main():
   #return redirect('/index' ,methods=['GET','POST'])
   # return render_template('index2.html') 
   if request.method == 'GET':  
     return render_template('index2.html')
   else:  
      app.vars['stock_tkr'] = request.form['stock_tkr']   
      #return render_template('index.html') 

@app.route('/index')
def index():
  if request.method == 'GET':  
     return render_template('index2.html')
  else:  
      app.vars['stock_tkr'] = request.form['stock_tkr']   
      return render_template('index2.html')
      
@app.route('/result' , methods=['POST'])
def result():
      return render_template('index.html')  

if __name__ == '__main__':
  app.run(port=33507)
