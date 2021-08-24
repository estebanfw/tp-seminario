FROM ubuntu

RUN  apt-get update &&  apt-get install -y python3 && \
     apt-get install -y cron && \
     apt-get install -y vim  && \
     apt-get install -y pip && \
     pip install pandas numpy requests datetime psycopg2-binary && \
     (crontab -l; echo "* * * * * /usr/bin/python3 /home/scripts/load_data_to_db.py") | sort -u | crontab - 

COPY ./scripts /home/scripts/

CMD service cron start && tail -f /dev/null