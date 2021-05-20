FROM rcarmo/ubuntu-python:onbuild
# FROM akhmetov/python-telegram
# RUN apk update && \
#     apk upgrade && \
#     apk add git
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./main.py", ""]