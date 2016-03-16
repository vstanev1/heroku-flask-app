from flask import Flask, render_template, request, redirect
import pandas as pd
import simplejson as json
import datetime
from datetime import datetime

#from bokeh.io import push_notetbook
from bokeh.plotting import figure
#from ipywidgets import interact

#from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

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
      return render_template('index.html') 

@app.route('/index')
def index():
  if request.method == 'GET':  
     return render_template('index2.html')
  else:  
      app.vars['stock_tkr'] = request.form['stock_tkr']   
      #?return render_template('index2.html')
      
@app.route('/result' , methods=['POST'])
def result():
     # plot = figure()
     # plot.circle([1,2], [3,4])
        
     # html = file_html(plot, CDN, "my plot")
     # Html_file= open("templates/index3.html","w")
     # Html_file.write(html)
     # Html_file.close()
      return render_template('index3.html')  

if __name__ == '__main__':
  app.run(port=33507)
