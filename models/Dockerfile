FROM tp33/django

COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y libmysqlclient-dev
RUN pip install -r /tmp/requirements.txt

