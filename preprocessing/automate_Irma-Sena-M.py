
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocessing():

    # Load dataset
    df = pd.read_csv("heart_raw/heart.csv")

    # Hapus duplikasi
    df = df.drop_duplicates()

    # Pisahkan fitur dan target
    X = df.drop("target", axis=1)
    y = df["target"]

    # Standarisasi data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Gabungkan kembali fitur dan target
    processed_df = pd.DataFrame(X_scaled, columns=X.columns)
    processed_df["target"] = y.values

    # Simpan dataset preprocessing
    processed_df.to_csv("heart_clean.csv", index=False)

    print("Preprocessing selesai")

if __name__ == "__main__":
    preprocessing()
