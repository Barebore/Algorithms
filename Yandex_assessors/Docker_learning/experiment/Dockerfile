# Использовать Ubuntu 18.04 как базовый образ
FROM ubuntu:18.04

# Обновить пакеты и установить необходимые инструменты
RUN apt-get update -y && apt-get install -y \
    git \
    python3-pip

# Клонировать репозиторий
WORKDIR /app
RUN git clone https://github.com/xionluhnis/neural_inverse_knitting.git

# Установить зависимости Python
WORKDIR /app/neural_inverse_knitting
RUN pip3 install -r requirements.txt

# Настроить входную точку для контейнера
CMD ["python3"]
