import streamlit as st
import pandas as pd
import json
from mplsoccer import VerticalPitch

st.title("Premier League 2024 Shot Map")
st.subheader("Filter to any Team/Player to see all of their shots taken")

# Load and preprocess the data
df = pd.read_csv("euros_2024_shot_map.csv")
df = df[df['type'] == 'Shot'].reset_index(drop=True)
df['location'] = df['location'].apply(json.loads)

team = st.selectbox('Select a team', df['team'].sort_values().unique(), index=None)
player = st.selectbox('Select a player', df[df['team'] == team]['player'].sort_values().unique(), index=None)

# Filter the data
def filter_data(df, team, player):
    if team:
        df = df[df['team'] == team]
    if player:
        df = df[df['player'] == player]
    return df

filter_df = filter_data(df, team, player)

# Plotting function
def plot_shots(df, ax, pitch):
    for x in df.to_dict(orient='records'):
        # Determine the shot color
        color = 'darkgreen' if x['shot_outcome'] == 'Goal' else 'red'
        
        # Plot the shot as a smaller circle
        pitch.scatter(
            x=float(x['location'][0]),
            y=float(x['location'][1]),
            ax=ax,
            s=300,  # Smaller circle size
            color=color,
            edgecolors='black',
            alpha=0.8,
            zorder=2,
        )
        
        # Add a line for shot placement (if placement info exists)
        if 'shot_end_location' in x and x['shot_end_location']:
            end_location = json.loads(x['shot_end_location'])
            pitch.lines(
                xstart=float(x['location'][0]),
                ystart=float(x['location'][1]),
                xend=float(end_location[0]),
                yend=float(end_location[1]),
                ax=ax,
                color=color,
                linewidth=1.5,
                linestyle='dashed',
                alpha=0.7,
                zorder=1,
            )

# Draw the pitch and plot shots
pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2, pitch_color='#f0f0f0', line_color='black', half=True)
fig, ax = pitch.draw(figsize=(10, 10))
plot_shots(filter_df, ax, pitch)
st.pyplot(fig)
st.write("Project Made By Ammar Shahid!")