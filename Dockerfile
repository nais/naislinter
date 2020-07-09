FROM python:3.7

# RUN pip install --no-cache-dir naislinter
COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]