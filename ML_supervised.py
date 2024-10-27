import pandas
from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

if __name__ == "__main__":
    #step 1: caricare il dataset tramite la libreria pandas
    my_dataset = pandas.read_csv('dataset_labeled.csv')
    my_labels = my_dataset["label"]
    my_data = my_dataset.drop(columns=['label'])

    #step 2: fare lo spit dei dati per l'addestramento e per il test
    x_train, x_test, y_train, y_test = train_test_split(my_data, my_labels,test_size = 0.5)


    # step 3: addestramento sulla base del training set
    model = RandomForestClassifier(n_estimators=100)
    model.fit(x_train, y_train)

    # step 4: eseguo una previsione sul test set
    y_pred = model.predict(x_test)

    # step 5: valuto il modello
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

    cm = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = cm.ravel()
    # Visualizzazione dei risultati
    print(f"Veri Positivi (TP): {TP}")
    print(f"Veri Negativi (TN): {TN}")
    print(f"Falsi Positivi (FP): {FP}")
    print(f"Falsi Negativi (FN): {FN}")
#    print(classification_report(y_test, y_pred))
