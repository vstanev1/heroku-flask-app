# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:31:45 2016

@author: Valentin
"""

from bokeh.plotting import *

import numpy as np


# Define a function that will return an HTML snippet.
def build_plot():   
     output_file('plot.html', title='Plot')
     x_data = np.arange(1, 101)
     y_data = np.random.randint(0, 101, 100)

    # Create a line plot from our data.

     line(x_data, y_data)
     
     #snippet = curplot().create_html_snippet(embed_base_url='../static/js/', embed_save_loc='./static/js')
     snippet =  'index2.html'
    # Return the snippet we want to place in our page.

     return snippet
 