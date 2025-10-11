import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def model_results(model_name: str, model_object, metric: str): 

    """
    model_results extracts and summarizes model performance metrics from a fitted GridSearchCV object

    Parameters:
    model_name (str): name of model being trained
    model_object: a fitted GridSearchCV object containing cross-validation results
    metric (str): metric to evaluate ('precision', 'recall', 'f1', 'accuracy')

    Returns:
    pd.DataFrame: a DataFrame containing the model name and its corresponding performance metrics
    """    
    
    # Create dictionary
    metric_dict = {
        'precision': 'mean_test_precision',
        'recall': 'mean_test_recall',
        'f1': 'mean_test_f1',
        'accuracy': 'mean_test_accuracy',
    }
                   
    # Create DataFrame for all results
    TT_cv_results = pd.DataFrame(model_object.cv_results_)  # Create DataFrame for all results
    
    # Get the best results based on the specified metric
    best_estimator_results = TT_cv_results.iloc[    # iloc, select rows based on indexing (idmax())
    
    # Retrieve col from TT_cv_results that corresponds to specified metric
           TT_cv_results[metric_dict[metric]].idxmax(),  # .idxmax(), return index of first occurrence of max value
           :
    ]  

    # Get best accuracy of model
    accuracy = best_estimator_results.mean_test_accuracy
    
    # Get best precision of model
    precision = best_estimator_results.mean_test_precision
    
    # Get best recall of model
    recall = best_estimator_results.mean_test_recall
    
    # Get best F1 score of model
    f1 = best_estimator_results.mean_test_f1

    table = pd.DataFrame({
        'Model': [model_name],
        'Precision': [precision],
        'Recall': [recall],
        'Accuracy': [accuracy],
        'F1': [f1]
    })
    
    return table



def get_val_scores(model_name: str, preds, y_val_data): 

    """
    get_val_scores calculates validation scores for a model and returns them in a DataFrame

    Parameters:
    model_name (str): name of model being evaluated
    preds: predictions made by model
    y_val_data: true labels for validation dataset

    Returns:
    pd.DataFrame: A DataFrame containing the model name and its corresponding validation scores
    """
    
    # Calculate accuracy of model
    accuracy = accuracy_score(y_val_data, preds)
    
    # Calculate precision of model
    precision = precision_score(y_val_data, preds)
    
    # Calculate recall of model
    recall = recall_score(y_val_data, preds)
    
    # Calculate F1 score of model
    f1 = f1_score(y_val_data, preds)
    
    # Create DataFrame to summarize model's performance
    table = pd.DataFrame({'Model': [model_name],
                          'Precision': [precision],
                          'Recall': [recall],
                          'Accuracy': [accuracy],
                          'F1': [f1]
                          })

    return table
    
    

def get_test_scores(model_name:str, preds, y_test_data):

    """
    get_test_scores calculates test scores for a model and returns them in a DataFrame.

    Parameters:
    model_name (str): name of model being tested
    preds: predictions made by model
    y_test_data: true labels for test dataset

    Returns:
    pd.DataFrame: A DataFrame containing the model name and its corresponding test scores.
    
    """
    # Calculate accuracy of model
    accuracy = accuracy_score(y_test_data, preds)
    
    # Calculate precision of model
    precision = precision_score(y_test_data, preds)
    
    # Calculate recall of model
    recall = recall_score(y_test_data, preds)
    
    # Calculate F1 score of  model
    f1 = f1_score(y_test_data, preds)

    
    # Create DataFrame to summarize model's performance
    table = pd.DataFrame({'Model': [model_name],
                          'Precision': [precision],
                          'Recall': [recall],
                          'Accuracy': [accuracy],
                          'F1': [f1]
                          },)
    return table
    
    
