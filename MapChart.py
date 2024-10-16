import plotly.express as px

data = {
    'Country': ['United Kingdom', 'United States', 'Canada', 'Russia', 'India', 'France'],
    'Values': [100, 50, 80, 90, 70, 60]
}

fig = px.choropleth(
    data,
    locations = 'Country',
    locationmode = 'country names',
    color = 'Values',
    color_continuous_scale = 'Blues',
    title = 'Choropleth Map of Values by country'
)

fig.show()
