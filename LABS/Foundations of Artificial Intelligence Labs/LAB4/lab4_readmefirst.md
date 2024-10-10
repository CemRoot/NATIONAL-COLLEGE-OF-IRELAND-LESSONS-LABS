# Wine Quality Prediction with Decision Tree and Naive Bayes

## Project Overview

This project aims to classify wine quality based on various chemical properties using two machine learning models:
1. **Decision Tree Classifier**
2. **Naive Bayes Classifier**

The dataset used for this project is the **Wine Quality Dataset**, which contains several chemical features such as acidity, sugar, pH, and alcohol percentage. The goal is to predict the quality of the wine based on these features.

## Dataset

The dataset used in this project is `WineQT.csv`. It includes the following attributes:
- **Fixed Acidity**
- **Volatile Acidity**
- **Citric Acid**
- **Residual Sugar**
- **Chlorides**
- **Free Sulfur Dioxide**
- **Total Sulfur Dioxide**
- **Density**
- **pH**
- **Sulphates**
- **Alcohol**
- **Quality** (target variable)

### Dataset Source
The dataset is available on Kaggle or can be provided in your working environment as `WineQT.csv`.

## Project Workflow

1. **Data Loading**: The dataset is loaded using `pandas` from the file `WineQT.csv`.
2. **Data Exploration**: Basic statistical summaries and class distributions are examined to understand the dataset.
3. **Data Preparation**: The dataset is split into features (X) and target labels (y). The data is further split into training and test sets using an 80/20 ratio.
4. **Model Training**:
   - **Decision Tree Classifier**: A decision tree model is trained on the training data.
   - **Naive Bayes Classifier**: A Naive Bayes model is also trained on the same data.
5. **Model Evaluation**:
   - Both models are evaluated using metrics such as Accuracy, F1 Score, Precision, and Recall.
   - Confusion matrices are generated to visualize the model's performance.
6. **Comparison**: The performance of both models is compared to determine which model performs better on the given dataset.

## Installation

To run this project, you need to have Python installed along with the following libraries:
- `pandas`
- `scikit-learn`
- `matplotlib`

You can install the required libraries using the following command:


```bash
pip install pandas scikit-learn matplotlib
```

### README.md İçeriği Açıklaması:
1. **Proje Genel Bilgisi**: Projenin amacı ve kullanılan modeller açıklanmıştır.
2. **Veriseti**: Wine Quality veri setinin temel özellikleri ve verisetindeki sütunlar listelenmiştir.
3. **Kurulum**: Gerekli kütüphanelerin nasıl yükleneceği ve projenin nasıl çalıştırılacağı açıklanmıştır.
4. **Proje Akışı**: Projede hangi adımların gerçekleştirildiği detaylandırılmıştır.
5. **Model Değerlendirme**: Hangi metriklerin kullanıldığı ve sonuçların nasıl yorumlandığı belirtilmiştir.
6. **Sonuç**: Projenin sonucunda elde edilen bulgular özetlenmiştir.
7. **Lisans**: Proje için bir MIT lisansı eklenmiştir.

Bu README dosyası, projenizi başkalarına tanıtmak veya kendi referansınız olarak kullanmak için hazır hale gelmiştir. Başka bir yardıma ihtiyacınız olursa lütfen bana bildirin!
