# Sentiment Analysis API for Product Reviews

## 🎯 Project Overview
A production-ready sentiment analysis API that classifies product reviews as positive, negative, or neutral.
A live demo can  be found here

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

### To download the dataset:
1. Visit the original repository: https://github.com/Titowak/Pars-ABSA
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
      url={https://arxiv.org/abs/1908.01815}, 
```