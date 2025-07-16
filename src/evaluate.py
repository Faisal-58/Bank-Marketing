from sklearn.metrics import classification_report, roc_auc_score

def evaluate_model(y_test,y_pred,y_proba):
    print(f"\n Classificatioin report: ")
    print(classification_report(y_test,y_pred))
    print(f'ROC-AUC curve: {roc_auc_score(y_test,y_proba):.4f}')

