<p align="center">
  <img src="All_texts_wide2.png" width="800">
</p>
<p align="center">
Word Cloud of top 1000 terms in all texts after removal of stopwords
</p>

# Ancient Texts in Translation

### Purpose
* To discover whether modern NLP tools and predictive algorithms can provide insights into ancient text corpora

### Questions to answer
* Will modern subjectivity and polarity evaluations align with ancient sensibilities
* Will counts and weights either confirm known emphases or provide unexpected patterns
* Will a supervised binary predictive model be able to differentiate between genre of texts, texts featuring different gods, or featuring different persons
* Will an unsupervised clustering model be able to differentiate between genre of texts, texts featuring different gods, or featuring different persons

### Deliverables
This project has five notebooks. Each notebook has an accompanying report

#### *NLP section*
* **Notebook Part I: Extensive EDA**
>Cleaning, wrangling, statistical analyses, and visualizations of data set\
>A description of contents and discussion of why certain transformations were made
  
* **Notebook Part II: Sentiment**
>Used regex extensively to prepare text for analyses\
>Used TextBlob and Vader to acquire scores\
>Aggregated results by genre and featured god; created visuals

* **Notebook Part III: Counts, Frequency, and Weights**
>Tokenized and lemmatized text for analysis using NLTK and regex\
>Calculated feature `word count`\
>Created top five words dictionary by count\
>Created top five weighted bi-grams dictionary\
>Created top five weighted 3>4 gram dictionary\
>Aggregated by genre, god, and person 

#### *Machine Learning Section with Tokenization*
* **Notebook Part IV: Random Forest and XGBoost models**
> Created hstack feature that includes new features: `top_word_freq`, `divine_power_count`, and `divine_power_weighted`\
> Collinearity Assessment, calculating VIF and generating a Pearson correlation coefficient matrix\
> Configured CountVectorizer to produce a feature matrix that captures 2-grams and 3-grams\
> Constructed a Random Forest model using both training and validation datasets\
> Developed an XGBoost model using both training and validation datasets\
> Assessed model performance by creating confusion matrices, plotting ROC curves and calculating AUC scores, and plotting a Precision-Recall Curve\
> Extracted feature importance metrics for both models\
> Evaluated the superior model using test data to assess its performance
     
* **Notebook Part V: K-means clustering model**


#### *Appendices*
* **Appendix a: Word Clouds**
>Used WordCloud to create multiple word clouds by genre, god, and person

* **Appendix b: Hypothesis Testing**
>Performed 3 two-sample hypothesis tests (t-tests) to ascertain if there is a statistically significant difference or a random sampling occurrence in mean by target variable `is_hymn` and the features: `word_count`, `whole_polarity`, and `whole_subjectivity`

### What this is
An experiment using modern NLP tools and predictive algorithms on texts in translation

### What this is not
Foolproof. Each of these notebooks was built and run using translations of ancient texts. Translators may or may not have been consistent in word choice, or, conversely, too consistent in word choice when a different English word would have suited context better. Additionally, some of the texts are extremely fragmentary, thus many texts are missing words, phrases, or large chunks. Many of the texts are composites. In the data set, a single composition is given per observation. However, that single composition may have been pieced together from several exemplars of it. These exemplars are not always exact copies, so where one scribe may have used one term (or sign) to represent, say, "adoration", another may have chosen a different term (or sign). Since the compositions are then compilations, if both original terms are thought to mean generally "adoration," this is the selected English translation. This also means that if there is/was any differing nuance between the exemplars it has been removed.
