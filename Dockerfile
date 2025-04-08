FROM python:3.13.1

RUN pip install poetry

COPY pyproject.toml poetry.lock /src/  

WORKDIR /src

RUN poetry config virtualenvs.create false && poetry install --no-root 

COPY . /src 

EXPOSE 8501

CMD ["streamlit", "run", "/src/main.py", "--server.address=0.0.0.0", "--server.port=8501"]