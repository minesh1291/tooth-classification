# tooth-classification

- [model training](https://github.com/minesh1291/tooth-classification/blob/main/notebooks/Nov19-1/classification-19-1.ipynb)
- [inference and evaluation](https://github.com/minesh1291/tooth-classification/blob/main/notebooks/Nov19-1/kfold_inference-19-1.ipynb)

# Evaluation Report

```
n_train = 0:52, 1:40
n_test  = 0:13, 1:10

precision    recall  f1-score   support

      1 root       1.00      0.92      0.96        13
  multi-root       0.91      1.00      0.95        10

    accuracy                           0.96        23
   macro avg       0.95      0.96      0.96        23
weighted avg       0.96      0.96      0.96        23

Accuracy: 0.96, 22/23
Crossentropy 0.1343
```
Confusion Matrix
|                 |	(pred, 1 root)  |	(pred, multi-root) |
|-----------------|----------------:|-------------------:|
| **(ture, 1 root)**     |        12	  |   1                |
| **(ture, multi-root)** |	       0    |   10               |



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
