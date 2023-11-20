# Web Scraping and Sentiment Analysis Tool

This Python script uses web scraping techniques and sentiment analysis to extract and analyze the content of articles from specified URLs. It uses the requests library to fetch HTML content, BeautifulSoup for parsing, and various Natural Language Processing (NLP) techniques to analyze sentiment.

Features:
1. Input Data: Reads input data from an Excel file (Input.xlsx) containing URLs to articles.
2. Web Scraping: Retrieves the HTML content of each article from the provided URLs using the requests library.
3. Text Extraction: Extracts the title and content of each article using BeautifulSoup's HTML parsing capabilities.
4. Stop Words Removal: Utilizes a stop words directory to exclude common words from the article text, enhancing sentiment analysis accuracy.
5. Sentiment Analysis: Calculates negative, positive, polarity, and subjectivity scores for each article.
6. Output: Outputs results, including excluded stop words and sentiment scores, to the console.

Dependencies:
1. requests: For making HTTP requests to fetch HTML content.
2. BeautifulSoup: For parsing HTML content.
3. pandas: For reading input data from an Excel file.
4. nltk: For Natural Language Processing tasks, including tokenization.