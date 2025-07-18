import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def evaluate_model(y_test,y_pred,y_proba):
    print(f"\n Classificatioin report: ")
    print(classification_report(y_test,y_pred))
    print(f'ROC-AUC curve: {roc_auc_score(y_test,y_proba):.4f}')


    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.savefig("images/confusion_matrix.png")
    plt.close()