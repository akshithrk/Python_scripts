import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        # 
        # your code here
        # for example, assuming that passengers who are male
        # and older than 18 surived:
        #     if passenger['Sex'] == 'male' or passenger['Age'] < 18:
        #         predictions[passenger_id] = 1
        #
        if (passenger['Sex']=='female' or passenger['Pclass']==1 and passenger['Age']<18):
            predictions[passenger['PassengerId']] = 1
        else:
            predictions[passenger['PassengerId']] = 0
    
    return predictions
