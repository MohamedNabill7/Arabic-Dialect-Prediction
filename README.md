# Arabic-Dialect-Prediction
Many countries speak Arabic. 
However, each country has its own dialect, the aim of this repo is to build a model that predicts the dialect given the text.

## App

![sc](https://user-images.githubusercontent.com/67477345/158219878-585f1e91-9842-4701-ad5e-4a8da48857b3.png)



## Introduction

The process of computationally identifying the language of a given text is considered the cornerstone of many important NLP applications such as machine translation, social media analysis, etc. 

Dataset collected of tweets belonging to a wide range of country level Arabic dialects covering 18 different countries in the Middle East and North Africa region, which initially consists of 2 columns id and dialect.

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
    - In ML : (Linear SVC & Multinomial naive bayes) models trained using CountVectorizer features and transform using TfidfTransformer.
    - In DL :  Using LSTM as it deal very well with Text data which have long sequences. It tooks hours just to finish one epoch.

- Deployment
    - Deploying the LinearSVC model using Flask as a back end and HTML as front end.
    
    
## Result 

 The macro-averaged F1 score (or macro F1 score) is computed by taking the arithmetic mean (aka unweighted mean) of all the per-class F1 scores. This method treats all classes equally regardless of their support values. working with an imbalanced dataset where all classes are equally important, using the macro average would be a good choice as it treats all classes equally. 
 
            ------------------------------------------------------------
           |     Model                      |   5-fold cv   |  F1 Score |
           |------------------------------------------------|-----------|
           | LinearSVC     (dialect)        |    with       |    0.513  |
           |------------------------------------------------|-----------|
           | MultinomialNB (dialect)        |    with       |    0.365  |
           |------------------------------------------------|-----------|
           | LinearSVC     (dialect)        |    without    |    0.541  |
           |------------------------------------------------|-----------|          
           | MultinomialNB (dialect)        |    without    |    0.364  |
           |------------------------------------------------|-----------|    
           | LinearSVC (region_dialect)     |    with       |    0.788  |
           |------------------------------------------------|-----------|    
           | MultinomialNB (region_dialect) |    with       |    0.701  |
           |------------------------------------------------|-----------|
           | LinearSVC (region_dialect)     |    without    |    0.802  |
           |------------------------------------------------|-----------|    
           | MultinomialNB (region_dialect) |    without    |    0.665  |
           |------------------------------------------------|-----------|    
           | LSTM                           |    ------     |    0.505  |
            ------------------------------------------------------------ 
            
            
## How to Run
    
    - Clone this repo to your local machine.
    - Due to github maximum file size i couldn't upload model to the repo but you can download  
    - Run the following command "pip install requirements.txt".
    - Run the following command "python predictor_app.py".
Download Model from <a href="https://drive.google.com/file/d/1rCj2Z2IDwWKHhmWwkCCfAFR8ZF-HtieD/view?usp=sharing"> Here </a>

## Tools Used

- Python 3.7 
- Jupyter-lab or Google Colab 

  
## Conclusions

 - Our model suffered from class imbalance. Dialectical classification needs more data to work better.
  
  ## Next Steps

- Finetuning of Arabert
