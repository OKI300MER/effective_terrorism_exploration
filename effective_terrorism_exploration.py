import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mutual_info_score
from matplotlib.patches import Rectangle
import folium
from folium.plugins import HeatMap
from matplotlib.patches import Rectangle
from scipy.stats import chi2_contingency
# Load the dataset
terrorism_df = pd.read_csv(r"C:\Users\shric\Desktop\Dai\assignments\midterm\effective_terrorism_tactics_exploration\data\globalterrorismdb_0522dist.csv")

# Clean the dataset
columns_to_remove = [
    "imonth", "iday", "approxdate", "extended", "specificity", "property", "resolution", 
    "claimmode", "claimmode_txt", "claim2", "claimmode2", "claimmode2_txt", "claim3", 
    "claimmode3", "claimmode3_txt", "compclaim", "propextent", "propextent_txt", "propvalue", 
    "propcomment", "nhours", "ndays", "addnotes", "scite1", "scite2", "scite3", "dbsource", 
    "INT_LOG", "INT_IDEO", "INT_MISC", "INT_ANY", "location", "alternative", "alternative_txt", 
    "provstate", "city"
]
cleaned_terrorism_df = terrorism_df.drop(columns=columns_to_remove)

# Filter out specific attack types
drop_attacks = cleaned_terrorism_df[~cleaned_terrorism_df['attacktype1_txt'].isin(['Unknown', 'Hostage Taking (Barricade Incident)', 'Unarmed Assault', 'Hostage Taking (Kidnapping)'])]

# Visualize top countries by number of attacks
top_countries = drop_attacks['country_txt'].value_counts().head(15)
plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='skyblue')
plt.xlabel('Country')
plt.ylabel('Number Of Attacks')
plt.title('Top Countries by Number of Attacks')
plt.xticks(rotation=70)
plt.show()

# Visualize number of attacks by attack type and country
country_attack_counts = drop_attacks.groupby(['country_txt', 'attacktype1_txt']).size().unstack(fill_value=0).loc[top_countries.index].reset_index().melt(id_vars='country_txt', var_name='Type of Attack', value_name='Number of Attacks')
plt.figure(figsize=(12, 8))
sns.barplot(data=country_attack_counts, x='country_txt', y='Number of Attacks', hue='Type of Attack', palette='muted')
plt.xlabel('Country')
plt.ylabel('Number of Attacks')
plt.title('Top Countries by Number of Attacks and Top Types of Attack')
plt.legend(title='Type of Attack', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()

# Visualize number of attacks by target type and region
plt.figure(figsize=(12, 8))
sns.countplot(data=drop_attacks, x='targtype1_txt', hue='region_txt', palette='tab20')
plt.xlabel('Target Type')
plt.ylabel('Number of Attacks')
plt.title('Number of Attacks by Target Type and Region')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualize number of attacks over time
plt.figure(figsize=(12, 6))
sns.scatterplot(x=drop_attacks['iyear'].dt.year, y=drop_attacks['iyear'].dt.year.value_counts().sort_index(), color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.title('Number of Attacks Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualize attacks on map
drop_attacks.dropna(subset=['latitude', 'longitude'], inplace=True)
mymap = folium.Map(location=[drop_attacks['latitude'].mean(), drop_attacks['longitude'].mean()], zoom_start=2)
HeatMap([[row['latitude'], row['longitude']] for _, row in drop_attacks.iterrows()], radius=5, blur=2, gradient={0.4: 'blue', 0.65: 'yellow', 1: 'red'}).add_to(mymap)
mymap

# Visualize correlation analysis
plt.figure(figsize=(12, 8))
sns.countplot(data=drop_attacks, x='attacktype1_txt', hue='success', palette='Set1')
plt.xlabel('Type of Attack')
plt.ylabel('Succsessful or Failed Attacks')
plt.title('Count of Attack Types by Success')
plt.legend(title='Success', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualize number of attacks over time by country
attacks_over_time_by_country = drop_attacks.groupby(['iyear', 'country_txt']).size().reset_index(name='num_attacks')
top_countries = drop_attacks['country_txt'].value_counts().head(15).index
attacks_over_time_by_country = attacks_over_time_by_country[attacks_over_time_by_country['country_txt'].isin(top_countries) & (attacks_over_time_by_country['iyear'] % 5 == 0)]
plt.figure(figsize=(12, 8))
sns.barplot(data=attacks_over_time_by_country, x='iyear', y='num_attacks', hue='country_txt', palette='tab10')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.title('Number of Attacks Over Time by Country')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Visualize most attacks by region and attack type
attacks_by_region_type = drop_attacks.groupby(['region_txt', 'attacktype1_txt']).size().reset_index(name='attack_count')
plt.figure(figsize=(12, 8))
sns.barplot(data=attacks_by_region_type, x='region_txt', y='attack_count', hue='attacktype1_txt', palette='tab10')
plt.xlabel('Region')
plt.ylabel('Number of Attacks')
plt.title('Most Attacks by Region and Attack Type')
plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.gca().add_patch(Rectangle((7.4, 0), 0.8, 25000, edgecolor='red', facecolor='none', linewidth=2))  # Middle East & North Africa
plt.gca().add_patch(Rectangle((4.5, 0), 1, 35500, edgecolor='red', facecolor='none', linewidth=2))  # South Asia
plt.show()

# Visualize association between attack type and target type
plt.figure(figsize=(14, 8))
sns.heatmap(pd.crosstab(drop_attacks['attacktype1_txt'], drop_attacks['targtype1_txt']), cmap='Reds', annot=True, fmt='d')
plt.xlabel('Target Type')
plt.ylabel('Attack Type')
plt.title('Association between Attack Type and Target Type')
plt.tight_layout()
plt.show()

# Visualize cross-tabulation of region and attack type
cross_tab = pd.crosstab(drop_attacks['region_txt'], drop_attacks['attacktype1_txt'])
plt.figure(figsize=(10, 8))
sns.heatmap(cross_tab, annot=True, cmap='Blues', fmt="d")
plt.title('Cross-Tabulation of Region and Attack Type')
plt.xlabel('Type of Attack')
plt.ylabel('Region')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualize attacks lethality over time
attacks_fatalities_by_year = drop_attacks.groupby('iyear').agg({'eventid': 'count', 'nkill': 'sum'}).reset_index()
attacks_fatalities_by_year['lethality'] = attacks_fatalities_by_year['nkill'] / attacks_fatalities_by_year['eventid']
plt.figure(figsize=(10, 6))
plt.plot(attacks_fatalities_by_year['iyear'], attacks_fatalities_by_year['lethality'], color='skyblue', marker='o')
plt.xlabel('Year')
plt.ylabel('Lethality (Fatalities per Attack)')
plt.title('Lethality of Attacks Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# Identify the year with the most attacks
most_attacks_year = drop_attacks['iyear'].value_counts().idxmax()
num_attacks_most_year = drop_attacks['iyear'].value_counts().max()
print("Year with the most attacks:", most_attacks_year)
print("Number of attacks in the most attacked year:", num_attacks_most_year)

# Create a violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(data=attacks_fatalities_by_year[['eventid', 'nkill']], palette=['blue', 'red'])
plt.xlabel('Event')
plt.ylabel('Count')
plt.title('Violin Plot of Number of Attacks and Fatalities Over Time')
plt.xticks(ticks=[0, 1], labels=['Number of Attacks', 'Number of Fatalities'])
plt.grid(True)
plt.tight_layout()
plt.show()