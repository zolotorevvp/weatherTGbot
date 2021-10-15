FROM python:3.9

WORKDIR /home/app

ENV OPEN_WEATHER_TOKEN="91fe395159be930cd4d91179c794c957"
ENV TELEGRAM_API_TOKEN="2017714130:AAH7tGE_0UK6MiqCgNF-BanNHg9JoV6BdUs"

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip && pip install requirements.txt
COPY *.py ./

ENTRYPOINT ["python", "main.py"]