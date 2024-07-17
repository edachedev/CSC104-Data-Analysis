import numpy as np
import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sb
df = pd.read_csv("all_recs.csv", encoding='unicode_escape')
df.head
df.info
df.describe
year_order = df['Year'].value_counts().index
location_order = df['Location'].value_counts().index
motive_order = df['Motive'].value_counts().index
industry_order = df['Industry'].value_counts().index
base_color = sb.color_palette()[2]
pit.figure(figsize=(20,8))
pit.title("Attack Frequency by year")
sb.countplot(data=df,y='Year',color=base_color,order=year_order)
pit.xticks(rotation=45);
pit.figure(figsize=(20,8))
pit.title("Attack Frequency by Industry")
sb.countplot(data=df,y='Year',color=base_color,order=industry_order)
pit.xticks(rotation=45);