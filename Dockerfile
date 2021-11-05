FROM python:3.9

WORKDIR /home/app

ENV OPEN_WEATHER_TOKEN=""
ENV TELEGRAM_API_TOKEN=""

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt ./
COPY *.py ./

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
