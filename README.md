# Web Scraping and Sentiment Analysis Tool

This Python script uses web scraping techniques and sentiment analysis to extract and analyze the content of articles from specified URLs. It uses the requests library to fetch HTML content, BeautifulSoup for parsing, and various Natural Language Processing (NLP) techniques to analyze sentiment.
- Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
- Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
- Polarity score: Lies between [-1,1], where -1 refers to negative sentiment and +1 refers to positive sentiment. 
- Subjectivity score: Lies between [0,1]. It quantifies the amount of personal opinion and factual information contained in the text. Higher subjectivity score means that the text contains personal opinion rather than factual information.

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