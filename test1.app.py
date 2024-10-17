import streamlit as st
import pandas as pd

# Load the CSV file
data = pd.read_csv('carrying_capacity_scenarios.csv')

# Title and description
st.title("Habitat-Based Carrying Capacity Calculator")
st.write("""
Explore how habitat area, area loss, and habitat quality affect the carrying capacity for the herd.
You can interact with the sliders below to change these inputs and see the resulting carrying capacity.
""")

# Sliders for user input
habitat_area = st.slider('Habitat Area (sq km)', 100, 1000, int(data['Habitat_Area (sq km)'].mean()))
habitat_quality = st.slider('Habitat Quality (0-1)', 0.1, 1.0, float(data['Habitat_Quality'].mean()))
area_loss = st.slider('Area Loss (%)', 0, 100, int(data['Area_Loss (%)'].mean()))
quality_reduction = st.slider('Quality Reduction (%)', 0, 100, int(data['Quality_Reduction (%)'].mean()))

# Calculate carrying capacity based on user input
carrying_capacity = (habitat_area * (1 - area_loss / 100)) * (habitat_quality * (1 - quality_reduction / 100))

# Display the calculated carrying capacity
st.write(f"Estimated Carrying Capacity: {carrying_capacity:.2f} animals")

# Show the original dataset for reference
if st.checkbox('Show scenario dataset'):
    st.write(data)

# Basic line chart with habitat area vs. carrying capacity
st.write("### Carrying Capacity vs. Habitat Area")
st.write("The graph below shows how the carrying capacity changes based on habitat area.")
st.line_chart(data[['Habitat_Area (sq km)', 'Carrying_Capacity']])

# Rename columns for map visualization
data = data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

# Show map with scenario locations
st.write("### Map of Scenarios in Northern Alberta")
st.map(data[['latitude', 'longitude']])
