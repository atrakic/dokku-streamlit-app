# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM debian:12-slim AS build
COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -qq --no-install-suggests --no-install-recommends --yes \
    python3-venv gcc libpython3-dev libsqlite3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel pip-tools && \
    /venv/bin/pip install --requirement requirements.txt

FROM build AS build-venv
WORKDIR /app
COPY src/app.py ./

FROM gcr.io/distroless/python3-debian12 AS final
LABEL maintainer="Admir Trakic <atrakic@users.noreply.github.com>"

COPY --from=build-venv --chown=nonroot:nonroot /venv /venv
COPY --from=build-venv --chown=nonroot:nonroot /app /app

WORKDIR /app
VOLUME /var/db

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD [ \
    "/venv/bin/python3", \
    "-c", \
    "import http.client; http.client.HTTPConnection('localhost', 8501).request('GET', '/_stcore/health');"]

EXPOSE 8501
#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
#CMD ["streamlit", "run", "app.py"]
ENTRYPOINT ["/venv/bin/streamlit", "run", "app.py"]
