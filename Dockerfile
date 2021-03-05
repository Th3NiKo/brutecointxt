FROM python:3

WORKDIR /usr/src/brutecointxt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./brutecointxt.py", "-t", "test.txt"]