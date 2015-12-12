

"""
this is testing of bokeh for our implementation

"""

from random import random
from bokeh.models import callbacks,CustomJS,ColumnDataSource,HoverTool,Circle
from bokeh.plotting import output_file,figure,show, hplot

def main():

    output_file("testbokeh.html")

    # # x = [random() for x in range(500)]
    # # y = [random() for y in range(500)]
    # #
    # s1 = ColumnDataSource(data=dict(x=[], y=[]))
    # # p1 = figure(plot_width=400, plot_height=400, tools="lasso_select", title="Select Here")
    # # p1.circle('x', 'y', source=s1, alpha=0.6)
    #
    source = ColumnDataSource(data=dict(x=[], y=[]))
    # p2 = figure(plot_width=400, plot_height=400, x_range=(0, 1), y_range=(0, 1),
    #             tools="", title="move your pointer")
    # # p2.circle('x', 'y', source=source, size = 8, alpha=0.6)
    #
    # # s2.callback = CustomJS(args=dict(s2=s2), code="""
    # #         var inds = cb_obj.get('selected')['1d'].indices;
    # #         var d1 = cb_obj.get('data');
    # #         var d2 = s2.get('data');
    # #         d2['x'] = []
    # #         d2['y'] = []
    # #         for (i = 0; i < inds.length; i++) {
    # #             d2['x'].push(d1['x'][inds[i]])
    # #             d2['y'].push(d1['y'][inds[i]])
    # #         }
    # #         s2.trigger('change');
    # #     """)
    source.callback = CustomJS(args=dict(source=source), code="""

            var data = source.get('data');
            var index = cb_data['index'];

            var x = index['x']
            var y = index['y']

            data['x'].push(x)
            data['y'].push(y)

            source.trigger('change');
        """)
    # layout = hplot(p1, p2)
    # p2.circle('x', 'y', source=source, size = 8, alpha=0.6)
    # show(p2)
    #

    x= xrange(0,600)
    y= xrange(0,300)
    # Basic plot setup
    p = figure(width=600, height=300, tools="hover", toolbar_location=None, title='Hover')
    # p.
    # p.line(x, y, line_dash="4 4", line_width=1, color='gray')

    # Add a circle, that is visible only when selected
    # source = ColumnDataSource({'x': [], 'y': []})
    invisible_circle = Circle(x='x', y='y', fill_color='gray', fill_alpha=0.05, line_color=None, size=20)
    visible_circle = Circle(x='x', y='y', fill_color='firebrick', fill_alpha=0.5, line_color=None, size=20)
    # cr = p.add_glyph(source, invisible_circle, selection_glyph=visible_circle, nonselection_glyph=invisible_circle)
    cr = p.add_glyph(source,invisible_circle)
    # cr = p.circle('x','y',source = source,size = 8,alpha = 0.6)

    # Add a hover tool, that selects the circle
    code = "source.set('selected', cb_data['index']);"
    callback = CustomJS(args={'source': source}, code=code)
    p.add_tools(HoverTool(tooltips=None, callback=callback, renderers=[cr], mode='mouse'))

    show(p)


if __name__ == '__main__': main()