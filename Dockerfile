FROM python
WORKDIR /Docker
COPY . /Docker
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords
CMD ["python", "python.py"]