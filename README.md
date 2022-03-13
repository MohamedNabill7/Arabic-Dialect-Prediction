# Arabic-Dialect-Prediction
Many countries speak Arabic. 
However, each country has its own dialect, the aim of this repo is to build a model that predicts the dialect given the text.

## Introduction

The process of computationally identifying the language of a given text is considered the cornerstone of many important NLP applications such as machine translation, social media analysis, etc. Since the dialects could be considered as a closely related languages, dialect identification could be referred to as a special (more diﬀicult) case of language identification problem.

Dataset collected of tweets belonging to a wide range of country level Arabic dialects covering 18 different countries in the Middle East and North Africa region. The dataset used is the QADI dataset, which initially consists of 2 columns id and dialect.

**Dataset** <a href='https://drive.google.com/file/d/1Rf-pPGle3HVZzovTghKRwWThqFBlj84k/view?usp=sharing'> Here </a>

## Abstractly, the Project is divided into 4 steps.

- Data Fetching:
    - Fetches the tweets from an API using the given ids.
    
-  Data Pre-processing:
    - Cleaning
    - Normalization
    - Tokenization
    - Labelling
    
- Modeling
    - 
    - 
- Deployment
    - Deploying the LinearSVC model using Flask as a back end and HTML as front end.

## Technologies and Tools Used

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Requests
- RegEx
- Sklearn
- Nltk 
- Keras
- Flask
  
  
  
  
## Conclusions

 - The geographical variation in dialect lends itself readily to geographical classification.
 - Our model suffered from class imbalance. Dialectical classification needs more data to work better.
 - Oversampling does not solve class imbalance in this case.
 - Due to the extreme dimensionality of my model we were unable to run some of the more complex models/ GridSearches.  
  
  ## Next Steps

- Clustering to attempt to test the hypothesis: geographical proximity correlates with language similarity.
- Experiment with Vector Embedding in Arabic.
- Model using AraBert and AraElectra
