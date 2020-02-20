gitbook sh脚本编写

```sh
#/bin/bash
# gitbook运行脚本
#

args=$*

function init(){
    bookID=$(docker ps -aqf name=gitbook)
    if [[ ! $bookID ]];then
        echo $args
        docker run --name gitbook -d -v $HOME/gitbook/booklog:/srv/gitbook -v $HOME/gitbook/html:/srv/html --restart=always -p 80:4000 fellah/gitbook
    else
        docker start $bookID
    fi
}

function start(){
    bookID=$(docker ps -qf name=gitbook)
    if [[ ! $bookID ]];then
        init
    fi
    if [[ ! $args ]];then
        args="serve"
    fi
    exec docker exec -it gitbook gitbook $args
    
}

start
```



