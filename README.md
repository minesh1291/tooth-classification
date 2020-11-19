# tooth-classification

- [model training](https://github.com/minesh1291/tooth-classification/blob/main/notebooks/Nov19/keras_binary_classification.ipynb)
- [inference and evaluation](https://github.com/minesh1291/tooth-classification/blob/main/notebooks/Nov19/keras_kfold_inference.ipynb)

# Evaluation Report

```
n_train = 0:52, 1:40
n_test  = 0:13, 1:10

              precision    recall  f1-score   support

           0       0.92      0.92      0.92        13
           1       0.90      0.90      0.90        10

    accuracy                           0.91        23
   macro avg       0.91      0.91      0.91        23
weighted avg       0.91      0.91      0.91        23

Accuracy: 0.91, 21/23
Crossentropy 0.2972

```

# Files
```
notebooks/Nov19
│ 
├── 7_fold_models
│   ├── fold_0_best_model.hdf5
│   ├── fold_1_best_model.hdf5
│   ├── fold_2_best_model.hdf5
│   ├── fold_3_best_model.hdf5
│   ├── fold_4_best_model.hdf5
│   ├── fold_5_best_model.hdf5
│   └── fold_6_best_model.hdf5
├── keras_binary_classification.ipynb
├── keras_kfold_inference.ipynb
└── outputs
    ├── learning_history_df.csv
    ├── oof.csv
    ├── predictions.csv
    ├── test.csv
    └── train.csv

2 directories, 14 files
```
