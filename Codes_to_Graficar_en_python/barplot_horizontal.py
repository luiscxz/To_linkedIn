import plotly.graph_objects as go
import plotly.colors as pc
import plotly.express as px
def plotbar(df, y, x, colors, labels, text_fmt, title):
    fig = px.bar(
        df,
        y=y,
        x=x,
        orientation='h',
        labels=labels,
        title=title,
        color_discrete_sequence=colors,
        color=y,
        text_auto='.2f',
        height=600,
    )

    fig.update_traces(texttemplate=text_fmt)

    fig.update_layout(
        title=dict(
            x=0.5,
            font=dict(size=18, family='Arial', color='black')
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=False,
        bargap=0.2,
        xaxis=dict(
            title_font=dict(size=14, family='Arial', color='black'),
            tickfont=dict(size=12, family='Arial', color='black'),
            showgrid=True,
            gridcolor='lightgrey',
            zerolinecolor='lightgrey'
        ),
        yaxis=dict(
            title='',
            tickfont=dict(size=12, family='Arial', color='black'),
            autorange='reversed',
            ticklen=10,
            showline=True,
            linecolor='black',
            automargin=True,
            ticksuffix="   "
        ),
        hoverlabel=dict(
            bgcolor='white',
            font_size=12,
            font_family='Arial'
        )
    )
    
    return fig


pie_colors = pc.qualitative.Plotly
bar_fig = plotbar(df=caracteristicas_seleccionadas,
                  colors=pie_colors,
                  y='Caracteristica',
                  x='Importancia_abs',
            labels={'Importancia_abs': 'Importancia_abs'},
            text_fmt ='<b>%{x:.2f}%</b>', # muestra 2 decimales y el simbolo %
            title=''

            )
bar_fig.show()