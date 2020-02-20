### docker部署gitbook

###### Run container:

$ docker run -p 80:4000 -v /srv/gitbook fellah/gitbook
4000 – GitBook default service port.

35729 – Live reload server port.

/srv/gitbook – Default working directory for GitBook container.

###### Build Static Website

$ docker run -v /srv/gitbook -v /srv/html fellah/gitbook gitbook build . /srv/html

```
args=$*

function init(){
    bookID=$(docker ps -aqf name=gitbook)
    if [[ ! $bookID ]];then
        echo $args
        docker run --name gitbook -itd -v $HOME/gitbook/booklog:/srv/gitbook -v $HOME/gitbook/html:/srv/html --restart=always -p 80:4000 fellah/gitbook /bin/bash
        exec docker exec -it gitbook gitbook $args
    else
        docker start $bookID
        exec docker exec -it gitbook gitbook $args
    fi
}

function start(){
    bookID=$(docker ps -qf name=gitbook)
    if [[ ! $bookID ]];then
        # bookID=$(docker ps -aqf name=gitbook)
        # docker start $bookID
        init
    else
        exec docker exec -it gitbook gitbook $args
    fi
}

start
```

