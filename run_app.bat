@echo off
CALL C:\Users\USERNAME\anaconda3\Scripts\activate.bat
CALL conda activate streamlit-env
streamlit run gold_tracker_app.py
pause
