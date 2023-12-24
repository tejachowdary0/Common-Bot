FROM python:3.10
WORKDIR /Common-Bot
COPY . /Common-Bot
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
