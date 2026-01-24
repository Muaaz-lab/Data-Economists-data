<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WhatsApp Chat Analysis using Python</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 20px;
            line-height: 1.7;
        }
        .container {
            max-width: 1100px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            text-align: center;
        }
        p {
            color: #444;
            font-size: 16px;
        }
        pre {
            background: #0d1117;
            color: #c9d1d9;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 14px;
        }
        code {
            color: #58a6ff;
        }
        .highlight {
            background: #e8f4ff;
            padding: 15px;
            border-left: 5px solid #3498db;
            margin: 20px 0;
            border-radius: 5px;
        }
        ul li {
            margin-bottom: 8px;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #777;
        }
    </style>
</head>

<body>
<div class="container">

<h1>📊 WhatsApp Group Chat Analysis using Python</h1>

<p>
This project analyzes a WhatsApp group chat to understand <b>who contributes the most messages</b>.
We use <b>Pandas</b> for data handling and <b>Matplotlib & Seaborn</b> for beautiful visualizations.
</p>

<hr>

<h2>🧠 Libraries Used</h2>
<ul>
    <li><b>Pandas</b> – for data storage and calculations</li>
    <li><b>Matplotlib</b> – for plotting graphs</li>
    <li><b>Seaborn</b> – for attractive statistical charts</li>
    <li><b>NumPy</b> – for numerical operations</li>
</ul>

<hr>

<h2>📌 Step 1: Import Libraries</h2>
<p>
We start by importing the required Python libraries.
</p>

<pre><code>import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns</code></pre>

<hr>

<h2>📌 Step 2: Prepare the Data</h2>
<p>
Here we manually create a dataset that contains:
</p>
<ul>
    <li><b>Sender name</b></li>
    <li><b>Number of messages sent</b></li>
    <li><b>Percentage contribution</b></li>
</ul>

<pre><code>data = {
    'sender': [
        'Hafiz Zohaib', 'Ahmad Muaz-09 Comsat', 'Arfa-15 Comsat', 'RABIA Tahir-093',
        'Abdul Sami-103 Comsat', 'Eman Anees Comsats', '~Maryam Mohsin~ GR',
        'Aman Khan-104 Comsat', 'Mateen-003', 'Ayesha Iftikhar-19', 'Malika Tousif-41',
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

df = pd.DataFrame(data)</code></pre>

<div class="highlight">
💡 <b>Why Pandas DataFrame?</b><br>
It makes data easy to analyze, filter, and visualize.
</div>

<hr>

<h2>📌 Step 3: Basic Statistical Analysis</h2>

<p>
We calculate:
</p>
<ul>
    <li>Total messages</li>
    <li>Average messages per user</li>
    <li>Top contributor</li>
</ul>

<pre><code>print("--- Chat Statistics Summary ---")
print(f"Total Messages: {df['messages'].sum()}")
print(f"Average Messages per User: {df['messages'].mean():.2f}")
print(f"Top Contributor: {df.iloc[0]['sender']} with {df.iloc[0]['messages']} messages.")
print("-" * 31)</code></pre>

<hr>

<h2>📊 Step 4: Horizontal Bar Chart (Seaborn)</h2>

<p>
This graph shows <b>message count per sender</b>.
The highest contributor appears at the top.
</p>

<pre><code>plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

barplot = sns.barplot(
    x='messages', 
    y='sender', 
    data=df, 
    palette='viridis'
)

plt.title('WhatsApp Group Message Contribution by Sender', fontsize=16)
plt.xlabel('Number of Messages')
plt.ylabel('Sender')

for i, v in enumerate(df['messages']):
    barplot.text(v + 5, i + .25, str(v), fontweight='bold')

plt.tight_layout()
plt.show()</code></pre>

<div class="highlight">
🎯 <b>Why Horizontal Bar Chart?</b><br>
It is easier to read long names and compare contributors clearly.
</div>

<hr>

<h2>🥧 Step 5: Pie Chart with “Others” Grouping</h2>

<p>
Users contributing less than <b>5%</b> are grouped into <b>"Others"</b> to keep the chart clean.
</p>

<pre><code>threshold = 5.0
major = df[df['percent'] >= threshold]
minor = df[df['percent'] < threshold]</code></pre>

<p>
The top contributor is highlighted using an <b>explode effect</b>, and the pie is converted into a <b>donut chart</b>.
</p>

<pre><code>centre_circle = plt.Circle((0,0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)</code></pre>

<div class="highlight">
✨ <b>Why Donut Chart?</b><br>
It looks modern and focuses attention on percentage contribution.
</div>

<hr>

<h2>✅ Final Outcome</h2>
<ul>
    <li>Clear understanding of group activity</li>
    <li>Top contributors identified easily</li>
    <li>Clean and professional visualization</li>
    <li>Beginner-friendly Python project</li>
</ul>

<hr>

<footer>
    📌 Created by <b>Ahmad Muaaz</b><br>
    📊 Python | Data Analysis | Visualization
</footer>

</div>
</body>
</html>
