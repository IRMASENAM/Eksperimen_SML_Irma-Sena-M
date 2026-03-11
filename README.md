# Eksperimen Supervised Machine Learning – Irma Sena M

## Deskripsi Project

Project ini merupakan eksperimen Supervised Machine Learning untuk memprediksi kemungkinan seseorang memiliki penyakit jantung menggunakan **Heart Disease Dataset**.

Eksperimen dilakukan melalui beberapa tahapan utama:

1. Exploratory Data Analysis (EDA)
2. Data Preprocessing
3. Automasi preprocessing menggunakan Python script
4. Automasi workflow menggunakan GitHub Actions

Dataset yang digunakan berasal dari Kaggle.

---

## Dataset

Dataset: Heart Disease Dataset

Dataset ini berisi atribut medis pasien yang dapat digunakan untuk memprediksi kemungkinan penyakit jantung.

Beberapa fitur penting dalam dataset:

* **age** : usia pasien
* **sex** : jenis kelamin
* **cp** : jenis nyeri dada
* **trestbps** : tekanan darah
* **chol** : kadar kolesterol
* **thalach** : detak jantung maksimum
* **oldpeak** : depresi ST akibat olahraga
* **target** : label penyakit jantung

---

## Struktur Repository

```
Eksperimen_SML_Irma-Sena-M
│
├── .github
│   └── workflows
│       └── preprocessing.yml
│
├── heart_raw
│   └── heart.csv
│
├── preprocessing
│   ├── Eksperimen_Irma-Sena-M.ipynb
│   ├── automate_Irma-Sena-M.py
│   └── heart_clean.csv
│
└── README.md
```

Penjelasan folder:

* **heart_raw**
  Berisi dataset asli sebelum preprocessing.

* **preprocessing**
  Berisi notebook eksperimen, script automasi preprocessing, dan dataset hasil preprocessing.

---

## Automasi Preprocessing

Proses preprocessing dataset diotomatisasi menggunakan script Python:

```
automate_Irma-Sena-M.py
```

Script ini melakukan:

* Menghapus data duplikat
* Memisahkan fitur dan target
* Standarisasi fitur menggunakan StandardScaler
* Menyimpan dataset hasil preprocessing

---

## Workflow Automation

Project ini menggunakan **GitHub Actions** untuk menjalankan preprocessing secara otomatis setiap kali terdapat perubahan pada repository.

Workflow ini terdapat pada:

```
.github/workflows/preprocessing.yml
```

Dengan workflow ini, proses preprocessing akan berjalan otomatis tanpa perlu menjalankan script secara manual.

---

## Tools & Library

Beberapa library yang digunakan dalam eksperimen ini:

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* GitHub Actions
