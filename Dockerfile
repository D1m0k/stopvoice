FROM python:3
RUN pip3 install --no-cache-dir --upgrade pip \
&& pip3 install --no-cache-dir telethon

WORKDIR /app

COPY . .


CMD [ "python", "./stopvoice.py" ]