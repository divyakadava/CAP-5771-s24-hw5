import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5 * math.log((1 - p) / p )"

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.5275
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan's approach using coin flips as an ensemble method for stock market prediction is fundamentally flawed. Coin flips are entirely random and do not correlate with market movements, which are influenced by complex factors like economic indicators and company earnings. While ensemble methods can improve prediction accuracy by aggregating multiple models, these models need to be relevant and based on actual data. Coin flipping lacks any predictive power as it does not incorporate relevant market data, making it unsuitable for financial forecasting. Moreover, relying on random processes can lead to arbitrary decisions, offering no real improvement over random guessing."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "yes"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "yes, C2 is a better classifier than C1 because both classifiers are equivalent to random guessing. This is evidenced by the fact that for both classifiers, the True Positive Rate (TPR) is equal to the False Positive Rate (FPR), which places them on the random guess line in an ROC curve where TPR=FPR."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall' 

    # type: explain_string
    answers['(c) explain'] = "Precision and recall are the appropriate metrics to use in this scenario because they account for the class imbalance present in the dataset. Since C2 has the same precision but a higher recall than C1, it indicates that C2 is better at identifying positive cases without increasing the proportion of negative cases incorrectly identified as positive. Therefore, precision and recall are correctly indicating the relative performance of C2 and C1, with C2 being the better classifier."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 is preferred as it has significantly higher recall and F1-measure than C1, indicating better overall performance in correctly identifying positive cases and maintaining balance between precision and recall."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "The precision, recall, and F1-measure metrics provide a more comprehensive view of how well the classifier performs in terms of balancing the correct identification of positive cases against minimizing incorrect positives, which is critical in practical scenarios."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "Given the balance of high precision, moderate F1-measure, and low FPR, C3 is preferred. It effectively minimizes costly false positives while still identifying a reasonable number of true positives, making it suitable for scenarios where precision is valued over recall."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "0.1"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "(0.2 * p) / (0.1 + p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
            'recall': 0.5333,
            'precision': 0.6153,
            'F-measure': 0.5689,
            'accuracy': 0.88
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "F-measure is the best metric because it balances precision and recall, which are crucial for performance assessment in imbalanced class distributions. Accuracy is the worst metric as it may not reflect the true performance on the minority class; a model might have high accuracy by merely predicting the majority class correctly."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "F-measure is the best metric because it balances precision and recall, which are crucial for performance assessment in imbalanced class distributions. Accuracy is the worst metric as it may not reflect the true performance on the minority class; a model might have high accuracy by merely predicting the majority class correctly."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "F-measure is the best metric because it balances precision and recall, which are crucial for performance assessment in imbalanced class distributions. Accuracy is the worst metric as it may not reflect the true performance on the minority class; a model might have high accuracy by merely predicting the majority class correctly."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
