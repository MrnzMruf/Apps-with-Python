import plotly.graph_objects as pgo  # Importing the Plotly graph objects module for data visualization  

# Defining the labels for the nodes in the Sankey diagram  
# Defining the source indices for the links (where the links are coming from) 
# Defining the target indices for the links (where the links are going to)  
# Defining the values associated with each link (the strength of the connections)  
labels = ["Source A", "Source B", "Source C", "Target X", "Target Y", "Target Z"]  
source = [0, 1, 0, 2, 3, 3, 4]  
target = [3, 3, 4, 4, 4, 5, 5]  
values = [8, 4, 2, 8, 4, 2, 3]  

# Creating a Sankey diagram figure  
fig = pgo.Figure(data=[pgo.Sankey(  
    node=dict(  # Configuration for the nodes in the diagram  
        pad=15,  # Padding between the nodes  
        thickness=20,   # Thickness of the nodes  
        line=dict(color="black", width=0.5),  # Border color and width for nodes  
        label=labels  # The labels for each node  
    ),  
    link=dict(  # Configuration for the links between nodes  
        source=source,  # Source node indices  
        target=target,  # Target node indices  
        value=values  # Values for the links indicating the flow size  
    )  
)])  

# Updating the layout of the figure, including the title and font size  
fig.update_layout(title_text="Sankey Diagram", font_size=10)   

# Displaying the figure  
fig.show()
