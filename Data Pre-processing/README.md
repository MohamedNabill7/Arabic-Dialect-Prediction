## In this section, we will discuss what are the steps of Data Pre-processing:

### Data cleaning
Arabic text preprocessing is an essential step in any ANLP application. Preprocessing Arabic text on social media, which is usually informal (not standard), is more complicated owing to several reasons such as the presence of dialect text, common spelling mistakes, extra characters, diacritical marks, and elongations. Consequently, to preprocess such Arabic text, we must perform additional processing such as stripping the elongations, diacritical marks, and extra characters. Additionally, we must convert the text into its normal Arabic form. To this end, this approach provides two preprocessing modules:

#### a- Text cleaning
  The cleaning function reads the text, character by character, and then checks whether the character belongs to the Arabic alphabet or the required character; if yes, the function selects it, otherwise, replaces it with a space.
  
  This function of cleaning eliminates all noises, such as additional characters, samples, non-Arabic characters, URLs, and any shapes, and provides clean Arabic text without affecting its meaning or content.
  
#### b- Text normalization
  Used a different approach while cleaning the noises. Our proposed normalization replaces a non-normal word by a normal one by removing the repeated characters and using a set of common non-normal words.
  

### Tokenization
  Based on the cleaning and normalization results, the tokenization can be implemented easily and in a straightforward manner.
  The tokenization uses the spaces between words and punctuation, such as stop marks, commas, and semicolons to fragment text into words. 



### Relabelling

To start i want to train a model that will identify broader areas of dialectical similarity:

   I have put together these groups of dialects. 

Nile Basin: Egypt & Sudan

Gulf: Saudi Arabia & Oman & Arab Emirates & Bahrain & Qatar & Kuwait & Iraq & Yemen

Levantine: Syria & Jordan & Palestine & Lebanon

Maghrebi: Algeria & Morocco & Tunisia & Libya


**Clean Dataset** <a href='https://drive.google.com/file/d/1enbmBUeS8djGdoyCR-Z4YlLrCbdBVzRM/view?usp=sharing'> Here </a>
