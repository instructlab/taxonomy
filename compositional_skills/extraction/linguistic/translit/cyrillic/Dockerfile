FROM python

RUN apt-get update
RUN apt-get install -y aspell-ru aspell-uk

RUN pip install pyyaml
RUN pip install cyrtranslit

COPY . /app

CMD ["/app/run"]
