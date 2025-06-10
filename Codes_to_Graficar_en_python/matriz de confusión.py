# matriz de confusión
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import plotly.figure_factory as ff
cm = confusion_matrix(y_test, y_pred, labels=[1, 0])  # 1 = positivo, 0 = negativo
# Extraer valores
VP, FN = cm[0][0], cm[0][1]
FP, VN = cm[1][0], cm[1][1]

# Texto con etiquetas + valores
annotations = [
    [f'VP = {VP}', f'FN = {FN}'],
    [f'FP = {FP}', f'VN = {VN}']
]

# Crear el heatmap
fig = ff.create_annotated_heatmap(
    z=cm,
    x=['Predicho: Positivo', 'Predicho: Negativo'],
    y=['Real: Positivo', 'Real: Negativo'],
    annotation_text=annotations,
    colorscale='Blues',
    showscale=True
)

fig.update_layout(
    title='Matriz de Confusión con Etiquetas y Valores',
    xaxis_title='Predicción del Modelo',
    yaxis_title='Estado Real',
    autosize=True
)

fig.show()