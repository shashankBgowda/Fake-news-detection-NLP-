import pandas as pd

fake = pd.read_csv(r'D:\NLP-fakenews_detectionproj\Fake.csv')
true = pd.read_csv(r'D:\NLP-fakenews_detectionproj\True.csv')

fake['label'] = 'fake'
true['label'] = 'real'

df = pd.concat([fake, true], axis=0)
df = df[['text', 'label']]  # Keep only the required columns
df.to_csv('news.csv', index=False)
