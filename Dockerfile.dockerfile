FROM python 3.10.7
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /app
COPY TGbotGaraj TGbotGaraj
ENTRYPOINT ["python3", "bot.py"]



