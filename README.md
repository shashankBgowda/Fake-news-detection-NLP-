# Fake News Detection using NLP and Machine Learning

## Overview
This project aims to classify news articles as real or fake using Natural Language Processing (NLP) techniques and machine learning algorithms. The model is trained using a dataset of labeled news articles and employs TF-IDF for feature extraction and a Naive Bayes classifier for prediction.

## Features
- **Text Preprocessing**: Cleans and processes text data by removing noise and stopwords.
- **Feature Extraction**: Uses TF-IDF vectorization to convert text into numerical features.
- **Model Training**: Utilizes a Naive Bayes classifier for text classification.
- **Performance Evaluation**: Provides accuracy and classification reports.

## Dataset
The dataset used should contain two columns:
- `text`: The content of the news article.
- `label`: Classification of the article as `real` or `fake`.

Ensure your dataset is in CSV format and placed in the project directory as `news.csv`.

## Installation & Usage
1. Install dependencies:
   ```bash
   pip install pandas numpy nltk scikit-learn
   ```

2. Download necessary NLTK resources:
   ```python
   import nltk
   nltk.download('stopwords')
   ```

3. Run the script:
   ```bash
   python fake_news_detection.py
   ```

## Results
The model provides an accuracy score along with a classification report for performance evaluation.

## Future Improvements
- Implement deep learning-based classification.
- Use additional feature engineering techniques.
- Train on a larger dataset for better generalization.

## License
This project is open-source and free to use under the MIT License.

