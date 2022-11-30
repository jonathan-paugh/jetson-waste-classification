import matplotlib.pyplot as plt
import numpy as np
from utils.plot import save_plot
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix




def plot_history(history):
    fig, ax = plt.subplots()
    ax.plot(history['accuracy'], label='Training accuracy')
    ax.plot(history['val_accuracy'], label='Validation accuracy')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Accuracy')
    ax.legend()
    save_plot(fig, 'history.png')
    plt.close(fig)


def evaluate_model(model, test_data, verbose=2):
    _, test_acc = model.evaluate(test_data, verbose=verbose)
    print(f'Accuracy on test set:'
          f' {test_acc * 100:.2f}%')

def plot_confusion_matrix(y_actual, y_pred, test_data):
    cm = confusion_matrix(y_actual, y_pred)
    fig, ax = plt.subplots()
    ax.imshow(cm, cmap=plt.cm.Blues)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_xticks(np.arange(len(test_data.class_names)))
    ax.set_yticks(np.arange(len(test_data.class_names)))
    ax.set_xticklabels(test_data.class_names)
    ax.set_yticklabels(test_data.class_names)
    ax.set_title('Confusion Matrix')
    for i in range(len(test_data.class_names)):
        for j in range(len(test_data.class_names)):
            ax.text(j, i, cm[i, j], ha='center', va='center', color='blue')
    save_plot(fig, 'confusion_matrix.png')
    plt.close(fig)

def get_predicted_vs_actual(model, test_data):
    y_actual = []
    y_pred = []
    for x, y in test_data:
        y_actual.extend(y.numpy())
        y_pred.extend(np.argmax(model.predict(x), axis=-1))
    return y_actual, y_pred

def get_evaluation_metrics(history, model, test_data):
   
    plot_history(history)

    evaluate_model(model, test_data)

    y_actual, y_pred = get_predicted_vs_actual(model, test_data)
    plot_confusion_matrix(y_actual, y_pred, test_data)

    print("Classification Report")
    print(classification_report(y_actual, y_pred, target_names=test_data.class_names))
   