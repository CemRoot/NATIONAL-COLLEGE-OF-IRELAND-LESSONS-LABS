
# MongoDB with Python (Jupyter Notebook)

[Go to English Version](#readme-english-version) | [Türkçe Versiyon için tıklayın](#readme-türkçe-versiyonu)

---

### **README (English Version)**

# MongoDB with Python (Jupyter Notebook)

## Project Overview

This project demonstrates how to work with **MongoDB** using **Python** through a Jupyter Notebook. The code covers the key functionalities of connecting to a MongoDB database, performing basic CRUD operations (Create, Read, Update, Delete), and integrating these operations with a recommendation system using collaborative filtering. The project is intended to help you understand how to leverage MongoDB as a database to store and manipulate data, as well as perform recommendation tasks in Python.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Function Documentation](#function-documentation)
- [Usage](#usage)

---

## Requirements

To run this project, you'll need the following libraries installed:

- **Python 3.x**
- **PyMongo**: To interact with MongoDB.
- **Pandas**: For data manipulation and analysis.
- **Sklearn**: To perform collaborative filtering and cosine similarity.
- **Flask**: To create a web API for song recommendations (optional).

You can install the required libraries using:

```bash
pip install pymongo pandas scikit-learn flask
```

---

## Installation

### MongoDB Setup
1. **Download and Install MongoDB**:
   - MongoDB can be downloaded from its [official website](https://www.mongodb.com/try/download/community).
   - Follow the installation instructions specific to your operating system.
2. **Run MongoDB**: Start MongoDB by running the following command in your terminal:
   ```bash
   mongod
   ```

### Python and Jupyter Notebook Setup
1. **Clone or Download the Project**:
   Download this project from the repository or open it directly in your Jupyter Notebook environment.
   
2. **Start Jupyter Notebook**:
   Run the following command in your terminal to start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. **Run the `mongodb.ipynb` File**:
   Open the notebook file (`mongodb.ipynb`) and execute the cells step by step.

---

## Project Structure

```bash
mongodb_project/
│
├── mongodb.ipynb        # Main Jupyter Notebook containing code and explanations
├── README.md            # This file explaining the project
├── requirements.txt     # List of required packages (optional)
└── data/                # Data used in the project (optional if loading from MongoDB)
```

---

## Function Documentation

### 1. **Connecting to MongoDB**
   - **`from pymongo import MongoClient`**: This is the main MongoDB client used to establish a connection with the database.
   - **`client = MongoClient('mongodb://localhost:27017/')`**: Creates a connection to the local MongoDB instance.

   **Documentation**: [PyMongo MongoClient](https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html)

### 2. **CRUD Operations**

   #### a. **Inserting Data**:
   - **`collection.insert_many(data.to_dict('records'))`**: Inserts multiple records into the MongoDB collection.
   
   #### b. **Retrieving Data**:
   - **`collection.find()`**: Retrieves all documents from the collection.

   #### c. **Updating Data**:
   - **`collection.update_one({filter}, {"$set": {updated_values}})`**: Updates a document in the MongoDB collection.

   #### d. **Deleting Data**:
   - **`collection.delete_one({filter})`**: Deletes a single document from the collection.

   **Documentation**: [PyMongo CRUD Documentation](https://pymongo.readthedocs.io/en/stable/tutorial.html)

### 3. **Collaborative Filtering and Recommendation**

   #### a. **Cosine Similarity**:
   - **`from sklearn.metrics.pairwise import cosine_similarity`**: This function computes the cosine similarity between users to perform collaborative filtering for recommendations.
   
   #### b. **Prediction Function**:
   - **`predict_ratings(user_item_matrix, user_similarity)`**: Predicts ratings for items the user hasn't interacted with based on the similarity with other users.

   **Documentation**: [Scikit-learn Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)

### 4. **Flask API for Song Recommendations**
   - **`from flask import Flask, jsonify, request`**: Used to create an API endpoint for serving recommendations.

   - **API Endpoint**: `/recommend/<int:user_id>` is a route that provides recommendations for a given user ID.

   **Documentation**: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

---

## Usage

1. **Step 1**: Load data into MongoDB.
2. **Step 2**: Execute the Jupyter Notebook to interact with the data.
3. **Step 3**: Test the recommendation system by providing a `user_id`.
4. **Step 4** (Optional): Use the Flask API to serve recommendations over HTTP.

---

---

### **README (Türkçe Versiyonu)**

# MongoDB ile Python (Jupyter Notebook)

[İngilizce Versiyon için tıklayın](#readme-english-version) | [En Üste Dön](#mongodb-ile-python-jupyter-notebook)

---

## Proje Özeti

Bu proje, **Python** kullanarak **MongoDB** ile nasıl çalışılacağını bir Jupyter Notebook üzerinden göstermektedir. Kodlar, MongoDB'ye bağlanma, temel CRUD işlemleri (Oluşturma, Okuma, Güncelleme, Silme) gerçekleştirme ve bu işlemleri işbirlikçi filtreleme kullanarak öneri sistemiyle entegre etme adımlarını içermektedir. Proje, MongoDB'yi veri saklama ve işleme için nasıl kullanabileceğinizi ve Python'da öneri görevlerini nasıl gerçekleştirebileceğinizi anlamanıza yardımcı olmayı amaçlamaktadır.

---

## İçindekiler
- [Proje Özeti](#proje-özeti)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Proje Yapısı](#proje-yapısı)
- [Fonksiyon Dokümantasyonu](#fonksiyon-dokümantasyonu)
- [Kullanım](#kullanım)

---

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- **Python 3.x**
- **PyMongo**: MongoDB ile etkileşim için.
- **Pandas**: Veri manipülasyonu ve analizi için.
- **Sklearn**: İşbirlikçi filtreleme ve cosine benzerliği için.
- **Flask**: Şarkı öneri sistemi için web API oluşturma (isteğe bağlı).

Gerekli kütüphaneleri şu komutla yükleyebilirsiniz:

```bash
pip install pymongo pandas scikit-learn flask
```

---

## Kurulum

### MongoDB Kurulumu
1. **MongoDB'yi İndirin ve Kurun**:
   - MongoDB'yi [resmi web sitesinden](https://www.mongodb.com/try/download/community) indirebilirsiniz.
   - İşletim sisteminize özel kurulum talimatlarını takip edin.
   
2. **MongoDB'yi Başlatın**: Terminalde şu komutu çalıştırarak MongoDB'yi başlatın:
   ```bash
   mongod
   ```

### Python ve Jupyter Notebook Kurulumu
1. **Projeyi Klonlayın veya İndirin**:
   Projeyi indirin ve Jupyter Notebook ortamınızda açın.

2. **Jupyter Notebook'u Başlatın**:
   Terminalde şu komutu çalıştırın:
   ```bash
   jupyter notebook
   ```

3. **`mongodb.ipynb` Dosyasını Çalıştırın**:
   Notebook dosyasını açın ve adım adım hücreleri çalıştırın.

---

## Proje Yapısı

```bash
mongodb_projesi/
│
├── mongodb.ipynb        # Ana Jupyter Notebook dosyası
├── README.md            # Bu dosya
├── requirements.txt     # Gerekli paketlerin listesi (isteğe bağlı)
└── data/                # Projede kullanılan veri dosyaları (isteğe bağlı)
```

---

## Fonksiyon Dokümantasyonu

### 1. **MongoDB'ye Bağlanma**
   - **`from pymongo import MongoClient`**: MongoDB'ye bağlanmak için kullanılan ana istemci.
   - **`client = MongoClient('mongodb://localhost:27017/')`**: Yerel MongoDB instance'ına bağlantı oluşturur.

   **Dokümantasyon**: [PyMongo MongoClient](https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html)

### 2. **CRUD İşlemleri**

   #### a. **Veri Ekleme**:
   - **`collection.insert_many(data.to_dict('records'))`**: Birden fazla kaydı MongoDB koleksiyonuna ekler.
   
   #### b. **Veri Okuma**:
   - **`collection.find()`**: Koleksiyondaki tüm belgeleri getirir.

   #### c. **Veri Güncelleme**:
   - **`collection.update_one({filter}, {"$set": {updated_values}})`**: Koleksiyondaki bir belgeyi günceller.

   #### d. **Veri Silme**:
   - **`collection.delete_one({filter})`**: Koleksiyondan bir belgeyi siler.

   **Dokümantasyon**: [PyMongo CRUD Dokümantasyonu](https://pymongo.readthedocs.io/en/stable/tutorial.html)

### 3. **İşbirlikçi Filtreleme ve Öneri**

   #### a. **Cosine Benzerliği**:
   - **`from sklearn.metrics.pairwise import cosine_similarity`**: Kullanıcılar arasındaki cosine benzerliğini hesaplar.

   #### b. **Tahmin Fonksiyonu**:
   - **`predict_ratings(user_item_matrix, user_similarity)`**: Kullanıcıların etkileşimde bulunmadığı öğeler için tahmini puanları hesaplar.

   **Dokümantasyon**: [Scikit-learn Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)

### 4. **Şarkı Önerileri için Flask API**
   - **`from flask import Flask, jsonify, request`**: Önerileri sunmak için API endpoint oluşturur.

   - **API Endpoint**: `/recommend/<int:user_id>` belirli bir kullanıcı ID'si için öneriler sağlar.

   **Dokümantasyon**: [Flask Dokümantasyonu](https://flask.palletsprojects.com/en/2.0.x/)

---

## Kullanım

1. **Adım 1**: Verileri MongoDB'ye yükleyin.
2. **Adım 2**: Jupyter Notebook'u çalıştırarak verilerle etkileşime geçin.
3. **Adım 3**: Öneri sistemini bir `user_id` sağlayarak test edin.
4. **Adım 4** (İsteğe Bağlı): Flask API'yi kullanarak önerileri HTTP üzerinden sunun.

---

