FROM navikt/deployment:v1

RUN apk add --no-cache python3 jq bash
RUN python3 -m pip install --no-cache-dir naislinter

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]