from flask import Flask, render_template, request, redirect
import pandas as pd
import simplejson as json
import numpy as np
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
      stock_tick = 'GOOG' 
      web_adr = 'https://www.quandl.com/api/v3/datasets/WIKI/' + stock_tick + '.json'
      r = requests.get(web_adr)
 #     json_data = r.json()
      parsed_data = json.loads(r.text)
      new_data = pd.DataFrame(parsed_data['dataset']['data'])
        #parsed_data['dataset']['data']
        
        #calendar.day_name[datetime.strptime('01/26/2016', '%m/%d/%Y').date().weekday()]
      datetime.strptime(new_data[0][0], '%Y-%m-%d').date()
      f = lambda x: datetime.strptime(x, '%Y-%m-%d').date()
      new_data['Date'] = new_data[0].map(f)
        
      plot = figure(title= 'simple figure', x_axis_type="datetime")
      r = plot.line(new_data['Date'][1:30].values, new_data[1][1:30].values)
        
      html = file_html(plot, CDN, "my plot")
      Html_file= open("templates/index3.html","w")
      Html_file.write(html)
      Html_file.close()
      return render_template('index3.html')  

if __name__ == '__main__':
  app.run(port=33507)
