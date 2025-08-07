import plotly.subplots as sp
import plotly.graph_objects as go

def plot_histograms_grid(df, exclude_cols=['Date'], bins=None, title="Distribuciones"):
    """
    Genera un grid de histogramas para cada columna numérica del DataFrame,
    excluyendo las columnas especificadas en `exclude_cols`.

    Parámetros:
        df (pd.DataFrame): DataFrame de entrada.
        exclude_cols (list): Columnas a excluir (por defecto ['Date']).
        bins (int): Número de bins para los histogramas. Si es None, se calcula automáticamente.
        title (str): Título general de la figura.
    
    Retorna:
        fig (go.Figure): Figura con los subplots.
    """
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns        # Filtrar columnas numéricas y excluir las no deseadas
    cols_to_plot = numeric_cols.difference(exclude_cols)
    n = len(cols_to_plot)
    
    if n == 0:
        raise ValueError("No hay columnas numéricas para graficar.")
    
    
    if bins is None:                                                    # Calcular bins si no se especifica
        bins = int(2 * len(df)**(1/3))                                  # Regla de Sturges modificada
    
    cols_grid = min(4, n)                                               # Configuración del grid (máximo 4 columnas para mejor visualización)
    rows_grid = int(np.ceil(n / cols_grid))
    
    # Plantilla profesional
    professional_template = {
        'layout': go.Layout(
            font=dict(family="Arial", size=12, color="#333"),
            title=dict(font=dict(size=16, color="#333"), x=0.5, xanchor='center'),
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=40, r=40, t=60, b=40),
            hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
        )
    }
    
    # Crear figura con subplots
    fig = sp.make_subplots(
        rows=rows_grid,
        cols=cols_grid,
        subplot_titles=cols_to_plot,                                       # Pone los títulos a cada histograma
        horizontal_spacing=0.1,
        vertical_spacing=0.15
    )
    
    # Añadir histogramas
    for i, col in enumerate(cols_to_plot, 1):
        row = ((i - 1) // cols_grid) + 1
        col_pos = ((i - 1) % cols_grid) + 1
        
        fig.add_trace(
            go.Histogram(
                x=df[col],
                nbinsx=bins,
                marker=dict(
                    color='rgba(100, 149, 237, 0.7)',
                    line=dict(color='rgba(0, 0, 0, 0.5)', width=1)
                ),
                opacity=0.9,
                hovertemplate=f"{col}: %{{x}}<br>Frecuencia: %{{y}}<extra></extra>",
                name=col
            ),
            row=row, col=col_pos
        )
        
        # Personalizar ejes
        fig.update_xaxes(
            #title_text=col,                                # pone títulos a eje x
            row=row, col=col_pos,
            showgrid=True, gridcolor='rgba(0, 0, 0, 0.05)',
            linecolor='black', linewidth=1
        )
        fig.update_yaxes(
            title_text="Frecuencia",
            row=row, col=col_pos,
            showgrid=True, gridcolor='rgba(0, 0, 0, 0.05)',
            linecolor='black', linewidth=1
        )
    
    # Actualizar layout general
    fig.update_layout(
        height=300 * rows_grid,
        width=400 * min(cols_grid, 3),  # Evitar que sea demasiado ancho
        showlegend=False,
        template=professional_template,
        title_text=title,
        title_x=0.5
    )
    
    return fig

fig = plot_histograms_grid(df, title="Distribuciones de variables numéricas")
fig.show()