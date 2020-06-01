# Tweet Sentiment Analysis

## Aim:
 - To analyse the sentiments from a movie review data collected from twitter. 
 
## Data description:
 Dataset has only one column "comments" which has the reviews of moview on twitter. 

Columns : Comments
Rows : 1957

## Library Used:
We used [Textblob](https://textblob.readthedocs.io/en/dev/) library. Working of TextBlob library is explained through below snippet of code.
- It takes sentence as input and output it's polarity. 
- Polarity ranges from -1 to +1 where -1 denotes strong negative statement and +1 denotes strong positive statement. 
- Example
![](https://github.com/Noopuragr/Project/blob/master/Tweet%20Sentiment%20Analysis/textblob.PNG)

## Implementation:
For implementation in python please refer this notebook : [Click here](https://github.com/Noopuragr/Project/blob/master/Tweet%20Sentiment%20Analysis/sentiment_analysis.ipynb) 

## Analysis on proportion of comments : 
![](https://github.com/Noopuragr/Project/blob/master/Tweet%20Sentiment%20Analysis/proportion.PNG)

## Wordcloud of positive comments :
![](https://github.com/Noopuragr/Project/blob/master/Tweet%20Sentiment%20Analysis/positive.png)

## Wordcloud for negative comments : 
![](https://github.com/Noopuragr/Project/blob/master/Tweet%20Sentiment%20Analysis/negative.png)
