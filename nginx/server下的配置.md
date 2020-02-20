## server 下的配置

```
server {
listen 80;
location /{
root /var/www/html;
autoindex on;
index index.php index.html index.htm;
}

location /automation/log {
if ( $request_uri ~ (/automation/log([\S\s]*)) ){

set $needuri $2;

}

proxy_pass http://10.239.147.17$needuri;
}

“”# location /dsecp/workflow {
“”# if ( $request_uri ~ (/dsecp/workflow([\S\s]*)) ){
“”#
“”# set $needuri $2;

"# }
"#
"# proxy_pass http://192.168.2.231:9060$needuri;
"# }
}

nginx.conf 下的配置
worker_processes 2;

events {
worker_connections 1024;
}

http {
include mime.types;
default_type application/octet-stream;

sendfile on;
client_body_timeout 300s;
client_header_timeout 300s;
proxy_read_timeout 300s;
fastcgi_connect_timeout 300s;
fastcgi_send_timeout 300s;
fastcgi_read_timeout 300s;
fastcgi_buffers 8 256000k;
fastcgi_buffer_size 256000k;
fastcgi_intercept_errors on;
fastcgi_busy_buffers_size 256000k;
fastcgi_temp_file_write_size 256000k;
client_max_body_size 200m;

keepalive_timeout 300s;

include servers/*;
server_names_hash_bucket_size 128;
client_header_buffer_size 32k;
large_client_header_buffers 4 32k;
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.0;
gzip_comp_level 2;
gzip_types text/plain application/x-javascript text/css application/xml;
gzip_vary on;

}
```

