FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY $CONFIG_FILE ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python ./discord-chat-bridge.py $CONFIG_FILE
