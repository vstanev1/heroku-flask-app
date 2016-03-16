from flask import Flask, render_template, request, redirect
import pandas as pd
import simplejson as json
import datetime
from datetime import datetime

#from bokeh.io import push_notetbook
from bokeh.plotting import figure

import numpy as np
#from ipywidgets import interact

#from bokeh.plotting import figure
from bokeh.resources import CDN
#rom bokeh.embed import file_html
from bokeh.embed import components 


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


# add a circle renderer with a size, color, and alpha
     p = figure()
     p.circle([1,2], [3,4])
     script, div = components(p) 
 #  return render_template('graph.html', script=script, div=div)    
     return render_template('graph.html', script=script, div=div)

    # plot = figure()
     # plot.circle([1,2], [3,4])
        
     # html = file_html(plot, CDN, "my plot")
     # Html_file= open("templates/index3.html","w")
     # Html_file.write(html)  
     # Html_file.close()
    #return render_template('index5.html')
   #plot_snippet = build_plot()
  #  return render_template(plot_snippet)
    #return render_template('plots.html', snippet=plot_snippet)
  
   
def build_plot():   
   #utput_file('plot.html', title='Plot')
 # x_data = np.arange(1, 101)
 # y_data = np.random.randint(0, 101, 100)

    # Create a line plot from our data.

 # line(x_data, y_data)
     
     #snippet = curplot().create_html_snippet(embed_base_url='../static/js/', embed_save_loc='./static/js')
   snippet =  'index4.html'
    # Return the snippet we want to place in our page.

   return snippet


if __name__ == '__main__':
  app.run(port=33507)
