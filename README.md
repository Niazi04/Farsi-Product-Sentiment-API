# Sentiment Analysis API for Product Reviews

## 🎯 Project Overview

A production-ready sentiment analysis API that classifies product reviews as positive, negative, or neutral.

A live demo can  be found here: [Demo](https://product-review-sentiment.vercel.app/)

P.S. I hate front-end. Don't judge

# 🚀 Starting the project

## Clone the app

You have two options to run the app: clone this Github repo or use Docker.

1. Using Github

```bash
mkdir realy-discriptive-name-that-isnt-super-long
cd ./realy-discriptive-name-that-isnt-super-long
# Clone the project
git clone https://github.com/Niazi04/Farsi-Product-Sentiment-API.git .

#Once you've cloned the project, install dependencies:
# Use a virtual environment to avoid version conflicts
pip install -r requirements.txt

# Then run the app:
python app.py
```

2. Using docker

==⚠️ NOTE==: The docker image does **not** include the notebooks for testing or training ML models

If you want to explore the notebooks, clone the repository via GitHub instead.

```bash
docker pull nastyhedgeh0g/farsi-product-sentiment-api:FirstStable

docker run -p 5000:5000 nastyhedgeh0g/sentiment-api:FirstStable
```

To use  a different port:

```bash
docker run -p 8080:5000 nastyhedgeh0g/sentiment-api:FirstStable
```

## 🧪 Test the app

You can simply test the app using `curl` or any http client

### Health Check Endpoint

```bash
curl http://localhost:5000/health
```

Expected response code: **200 OK**

Response body should look like:

```json
{
      "dependencies": {
            "svm":"available",
            "vectorizer":"available"
      },
      "model":"not loaded in memory",
      "timestamp":"2026-02-14T19:50:58.760383+00:00"
}
```

If either 'svm' or 'vectorizer' show `"missing"`, it means they are not found in `./model` directory
Initially 'model' is not loaded in memory. Because I coded it that way. After your first POST request, it will be loaded in memory

### 🔮 Get Your First Prediction

💡 **Tip**: Use Postman, Insomnia, or a similar tool for sending Persian text, as terminals may not handle Unicode properly.

This is how your JSON body should look like:

```json
{
      "review": "گوشی واقعا عالی بود"
}
```

Send a POST request to `http://localhost:5000/predict`

If all the previous steps were successfull, you should get a response like so:

```json
{
    "polarity": "positive",
    "success": true
}
```

After your first request, the model remains loaded in memory for faster subsequent responses.

Send a GET request to `./health` endpoint and verify this.

# Data Source

The dataset used for training this sentiment analysis model is **Pars-ABSA**, a benchmark corpus for Persian aspect-based sentiment analysis.

## 📊 Dataset Information

- **Name**: Pars-ABSA
- **Size**: 10,002 samples (5,114 positive, 3,061 negative, 1,827 neutral)
- **Language**: Farsi (Persian)

## 📥 How to Obtain the Data

Due to licensing and storage constraints, the full dataset is not included in this repository. However for testing purposes, I
have included a sample csv file under 'pipeline/data/processed/sample.csv'

The data is already cleaned and processed and is ready to be fed into the already trained model (look at 'model' dir)

### To download the dataset

1. Visit the original repository: `https://github.com/Titowak/Pars-ABSA`
2. Download 'Pars-ABSA_xml.xml'
3. Place the downloaded file in `pipline/data/raw/` directory

## 🎓 Citation

```
@misc{ataei2019parsabsaaspectbasedsentimentanalysis,
      title={Pars-ABSA: an Aspect-based Sentiment Analysis dataset for Persian}, 
      author={Taha Shangipour Ataei and Kamyar Darvishi and Soroush Javdan and Behrouz Minaei-Bidgoli and Sauleh Eetemadi},
      year={2019},
      eprint={1908.01815},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/1908.01815}
}
```