import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Assuming you have a DataFrame 'nodes' and a list of 'connections'
# nodes = pd.DataFrame(...)
# connections = [...]

# Create a Dash application
app = dash.Dash(__name__)
app = app.server



data = pd.read_csv('https://raw.githubusercontent.com/Himanshu484/UF-UNF/main/assets/nodes_final.csv')
df_UF_UNF = pd.read_csv("https://raw.githubusercontent.com/Himanshu484/UF-UNF/main/assets/node_list.csv")
df_UF_UNF_Network = pd.read_csv("https://raw.githubusercontent.com/Himanshu484/UF-UNF/main/assets/edge_list.csv")

connections = []
for i in range(len(data)):
    target_list = df_UF_UNF_Network[df_UF_UNF_Network["source"] == data["researcher_id"][i]]["target"].to_list()
    index = data[data["researcher_id"].isin(target_list)].index.to_list()
    for j in index:
        connections.append((i,j))

# Define your scatter plot
fig = px.scatter(data, x='x', y='y', color="affiliation", size="size",
                 color_discrete_map={'Area1': 'red', 'Area2': 'blue', 'Area3': 'green', 'Area4': 'purple'},
                 labels={'color': 'Legend'},
                 hover_data={
                     "x": False,
                     "y": False,
                     "affiliation": True,
                     "name": True,
                     "area": True,
                     "size": False
                 })

# Add connections as lines and remove the legend for lines
line_traces = []
line_data = []  # List to store custom line data

for connection in connections:
    idx1, idx2 = connection
    line_trace = go.Scatter(x=[data['x'][idx1], data['x'][idx2]],
                            y=[data['y'][idx1], data['y'][idx2]],
                            mode='lines',
                            line=dict(color='gray'),
                            showlegend=False)  # Set showlegend to False for lines
    line_traces.append(line_trace)
fig.add_traces(line_traces)

fig.update_layout(
    xaxis_title='',
    yaxis_title='',
    xaxis_showticklabels=False,  # Remove x-axis tick labels
    yaxis_showticklabels=False,  # Remove y-axis tick labels
    paper_bgcolor='white',  # Set background color to transparent
    plot_bgcolor='white',   # Set plot area background color to transparent
)

# Remove the legend for all traces
for trace in fig.data:
    trace.showlegend = False


# Define the layout of your Dash app with the title and placement of lasso selection text
app.layout = html.Div(style={'backgroundColor': 'white'}, children=[
    html.H1("UNF-UF Collaboration Network", style={'backgroundColor': 'white'}),
    dcc.Graph(id='scatter-plot', figure=fig),
    html.Div(id='hover-info-point'),
    html.Div(id='lasso-selected-info', style={'backgroundColor': 'white'})
])


# # Callback function for handling hover events on points
# @app.callback(
#     Output('hover-info-point', 'children'),
#     [Input('scatter-plot', 'hoverData')]
# )
# def display_hover_point_data(hoverData):
#     if hoverData is not None:
#         point_index = hoverData['points'][0]['pointIndex']
#         x = hoverData["points"][0]["x"]
#         y = hoverData["points"][0]["y"]
#         x_value = data['name'][(data["x"]==x) & (data["y"]==y)].to_list()[0]
#         y_value = data['area'][(data["x"]==x) & (data["y"]==y)].to_list()[0]
#         area_value = data['affiliation'][(data["x"]==x) & (data["y"]==y)].to_list()[0]
        
#         hover_info = html.Div([
#             html.Strong("Point Info:"),
#             html.Br(),
#             f"Name: {x_value}",
#             html.Br(),
#             f"Research Area: {y_value}",
#             html.Br(),
#             f"Affiliation: {area_value}"
#         ])
#         return hover_info

# Callback function for handling lasso selections and returning selected point information
@app.callback(
    Output('lasso-selected-info', 'children'),
    [Input('scatter-plot', 'selectedData')]
)

def update_lasso_info(selectedData):
    if selectedData is None:
        return html.Div(
            "Use lasso to select researchers to find the common publications between them.",
            style={'width': '100%', 'height': '100%', 'backgroundColor': 'white'}
        )
    else:
        # Handle lasso-selected content as before
        selected_indices = []
        for point in selectedData['points']:
            x_value = point['x']
            y_value = point['y']
            index = data[(data['x'] == x_value) & (data['y'] == y_value)].index[0]
            selected_indices.append(index)

        all_authors = data["researcher_id"][selected_indices].unique()
        all_authors_name = data["name"][selected_indices].unique()
        all_publications = df_UF_UNF["xid"][df_UF_UNF["researcher_id"].isin(data.researcher_id[selected_indices].to_list())].to_list()
        joint_publications = []

        for paper_xid in all_publications:
            if paper_xid not in joint_publications:
                if all(author in df_UF_UNF["researcher_id"][df_UF_UNF["xid"]==paper_xid].to_list() for author in all_authors):
                    joint_publications.append(paper_xid)

        authors_info = html.Div([
            html.Strong("Selected Authors:"),
            html.Br(),
            ", ".join(all_authors_name)
        ])

        publications_info = html.Div([
            html.Strong("Joint Publications:"),
            html.Br(),
            html.Ul([
                html.Li([
                    html.Div([
                        html.Strong("Title:"),
                        html.Br(),
                        df_UF_UNF["title"][df_UF_UNF["xid"] == xid].values[0]
                    ]),
                    html.Div([
                        html.Strong("Abstract:"),
                        html.Br(),
                        df_UF_UNF["abstract"][df_UF_UNF["xid"] == xid].values[0]
                    ])
                ])
                for xid in joint_publications
            ])
        ])

        return html.Div([authors_info, publications_info])

        

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
