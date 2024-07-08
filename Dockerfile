FROM  python:3.12.4-bookworm

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/seambr/micro-center-stock-checker .

RUN pip3 install --no-cache-dir -r requirments.txt

CMD python main.py $LINK --store $STORE
# CMD ["bash"]