import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

grafico_map_estado = px.scatter_geo(
    df_rec_estado, 
    lat = 'lat',
    lon = 'lon',
    scope = 'south america', # Limita o mapa para América do Sul
    size = 'Preço',
    template = 'seaborn', # Usa um tema de plotly express
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False}, # Não exibe as coordenadas
    title = 'Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers = True, # Adiciona marcadores
    range_y = (0, df_rec_mensal.max()), # Limita o eixo Y
    color = 'Ano', # Define a cor do gráfico por ano
    line_dash = 'Ano',
    title = 'Receita Mensal'   
)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.head(7),
    x = 'Local da compra',
    y = 'Preço',
    text_auto= True, # Exibe o valor no topo dos barras
    title = 'Top receita por estado' 
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto= True, # Exibe o valor no topo dos barras
    title='Top 7 categorias com maior receita', 
)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x= 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto= True,
    title= 'Top 7 vendedores por receita'
)