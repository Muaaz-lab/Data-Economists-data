import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Prepare the data
data = {
    'sender': [
        'Hafiz Zohaib', 'Ahmad Muaz-09 Comsat', 'Arfa-15 Comsat', 'RABIA Tahir-093',
        'Abdul Sami-103 Comsat', 'Eman Anees Comsats', '~Maryam Mohsin~ GR',
        'Aman Khan-104 Comsat', 'Mateen-003', 'Ayesha Iftikhar-19', 'Malika',
        'Umair Abdullah-075 Comsat', 'Abdulmateen-03 Comsat', 'Hadia Ghazali -085 Comsat',
        'Khizar-037 Comsat', 'Areeba Sattar-013 Comsat', 'Mahnoor Jamal-039 Comsat',
        'Zainab Umar-081', 'Zainab Gul Comsat', 'Nimra-061'
    ],
    'messages': [
        1261, 968, 740, 656, 627, 547, 443, 385, 254, 207, 
        174, 165, 139, 127, 80, 74, 73, 62, 44, 39
    ],
    'contribution_percent': [
        17.23, 13.23, 10.11, 8.96, 8.57, 7.47, 6.05, 5.26, 3.47, 2.83,
        2.38, 2.25, 1.90, 1.74, 1.09, 1.01, 1.00, 0.85, 0.60, 0.53
    ]
}

df = pd.DataFrame(data)

# 2. Basic Analysis Printout
print("--- Chat Statistics Summary ---")
print(f"Total Messages: {df['messages'].sum()}")
print(f"Average Messages per User: {df['messages'].mean():.2f}")
print(f"Top Contributor: {df.iloc[0]['sender']} with {df.iloc[0]['messages']} messages.")
print("-" * 31)

# 3. Visualization
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Create horizontal bar chart
barplot = sns.barplot(
    x='messages', 
    y='sender', 
    data=df, 
    palette='viridis'
)

# Add labels and title
plt.title('WhatsApp Group Message Contribution by Sender', fontsize=16, pad=20)
plt.xlabel('Number of Messages', fontsize=12)
plt.ylabel('Sender', fontsize=12)

# Add the message count labels on the bars
for i, v in enumerate(df['messages']):
    barplot.text(v + 5, i + .25, str(v), color='black', fontweight='bold')

plt.tight_layout()
plt.show()
#pie chart
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Data Setup
data = {
    'sender': [
        'Hafiz Zohaib', 'Ahmad Muaz-09 Comsat', 'Arfa-15 Comsat', 'RABIA Tahir-093',
        'Abdul Sami-103 Comsat', 'Eman Anees Comsats', '~Maryam Mohsin~ GR',
        'Aman Khan-104 Comsat', 'Mateen-003', 'Ayesha Iftikhar-19', 'Malika',
        'Umair Abdullah-075 Comsat', 'Abdulmateen-03 Comsat', 'Hadia Ghazali -085 Comsat',
        'Khizar-037 Comsat', 'Areeba Sattar-013 Comsat', 'Mahnoor Jamal-039 Comsat',
        'Zainab Umar-081', 'Zainab Gul Comsat', 'Nimra-061'
    ],
    'messages': [1261, 968, 740, 656, 627, 547, 443, 385, 254, 207, 174, 165, 139, 127, 80, 74, 73, 62, 44, 39]
}

df = pd.DataFrame(data)
total_msgs = df['messages'].sum()
df['percent'] = (df['messages'] / total_msgs) * 100

# 2. Group users with < 5% contribution into 'Others'
threshold = 5.0
major = df[df['percent'] >= threshold].copy()
minor = df[df['percent'] < threshold].copy()

others_row = pd.DataFrame({
    'sender': [f'Others ({len(minor)} members)'],
    'messages': [minor['messages'].sum()],
    'percent': [minor['percent'].sum()]
})
pie_df = pd.concat([major, others_row], ignore_index=True).sort_values(by='messages', ascending=False)

# 3. Create Visualization
fig, ax = plt.subplots(figsize=(10, 7))

# Highlight the top contributor
explode = [0.1 if i == 0 else 0 for i in range(len(pie_df))]

wedges, texts, autotexts = ax.pie(
    pie_df['messages'],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Pastel1(np.linspace(0, 1, len(pie_df))),
    explode=explode,
    pctdistance=0.8,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Style the percentage labels
plt.setp(autotexts, size=10, weight="bold")

# Add Legend to the side
ax.legend(
    wedges, pie_df['sender'],
    title="Senders",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Donut hole
centre_circle = plt.Circle((0,0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Clean Message Distribution (Top Contributors Only)', fontsize=16)
plt.tight_layout()
plt.show()
