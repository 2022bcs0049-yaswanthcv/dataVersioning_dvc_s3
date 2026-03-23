# MLOps Pipeline with DVC, S3, GitHub Actions & Docker

## 🚀 Overview

This project demonstrates an end-to-end MLOps pipeline with data versioning, automated model training, and containerized deployment.

The system uses **DVC for dataset versioning**, **AWS S3 for storage**, **GitHub Actions for CI/CD**, and **Docker for containerization**.

---

## 🧠 Key Features

* Data versioning using **DVC**
* Remote dataset storage using **AWS S3**
* Automated pipeline using **GitHub Actions**
* Model training with evaluation metrics (RMSE, R²)
* Containerized pipeline using **Docker**
* Reproducibility of experiments

---

## ⚙️ Tech Stack

* Python
* DVC (Data Version Control)
* AWS S3
* GitHub Actions (CI/CD)
* Docker
* scikit-learn
* pandas

---

## 📂 Project Structure

```
├── app/
├── data/
│   └── housing.csv.dvc
├── src/
│   └── train.py
├── .github/workflows/
│   └── pipeline.yml
├── Dockerfile
├── .dvc/
├── .gitignore
└── README.md
```

---

## 🔄 Workflow

1. Push code to GitHub
2. GitHub Actions triggers pipeline
3. DVC pulls dataset from S3
4. Model is trained
5. Metrics (RMSE, R²) are generated
6. Docker image is built
7. Image is pushed to DockerHub

---

## 📊 Results

| Version   | Dataset Size | RMSE     | R²     |
| --------- | ------------ | -------- | ------ |
| Version 1 | 5000         | 60985.58 | 0.6858 |
| Version 2 | 20640        | 70031.42 | 0.6257 |

---

## 🔁 Reproducibility

To reproduce Version 1:

```
git checkout <version1_commit>
dvc pull
python src/train.py
```

---

## 📦 Docker

The project is containerized using Docker.

Image available at:
https://hub.docker.com/r/<your-username>/housing-mlops

---

## 💡 Why DVC?

DVC enables version control of large datasets by storing metadata in Git and actual data in remote storage like S3. This ensures reproducibility and efficient collaboration in ML workflows.

---

## 👨‍💻 Author

C.V.Yaswanth
