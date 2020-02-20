Dockerfile

**git pull不用输入密码**

```dockerfile
FROM python:alpine

LABEL maintainer="haowx"

RUN pip install flask

RUN apk add git

RUN echo "[credetial]\
        helper = store" > ~/.gitconfig

RUN echo "https://hw121298%40163.com:hw%21QAZ2wsx@github.com" > ~/.git-credentials

WORKDIR /hook

VOLUME /hook /html

EXPOSE 5000

CMD ["python", "hook.py"]
```

