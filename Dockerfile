FROM python:3.9.0a5-buster
COPY . /app
WORKDIR /app
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
CMD python helper_main.py