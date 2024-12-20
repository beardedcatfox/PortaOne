
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openmpi-bin \
    openmpi-common \
    libopenmpi-dev \
    && apt-get clean

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
COPY mpi.py /app/mpi.py
COPY main.py /app/main.py
COPY source.txt /app/source.txt

CMD ["bash"]
