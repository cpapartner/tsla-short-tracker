# TSLA Short Interest Tracker

This app tracks Tesla's (TSLA) stock price against manually updated short interest data.

## Features
- Real-time TSLA price from Yahoo Finance
- Manually updated short interest (from Nasdaq/FINRA)
- Easy hosting via Streamlit Cloud

## Files
- `tsla_tracker_app.py`: Main Streamlit app
- `short_interest.csv`: Bi-weekly short interest input
- `requirements.txt`: Dependencies

## Run Locally
```bash
pip install -r requirements.txt
streamlit run tsla_tracker_app.py
```

## Deploy on Streamlit Cloud
1. Fork or upload this repo to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub
4. Select this repo and run `tsla_tracker_app.py`

Manual short interest updates can be done by editing `short_interest.csv` in your GitHub repo.