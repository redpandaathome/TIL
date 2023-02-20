# Freetier time up.
Log of considering new mms-api server setup for 2022 🤔

----
## Alternative - Oracle Cloud Free tier
### step1.
Q. How to replace Elastic beanstalk and AWS Code pipeline for CI/CD ??<br>
A. Let's try Jenkins<br><br>

Q2. Jenkins install issue on linux...<br> 
A. Firewall problem and fixed after changing to Ubuntu<br><br>

Q3. Jenkins Plugin install timeout errors... on port 8080<br>
A. Firewall setting trouble shooting... -> partially installed.<br><br>

## step2.
Q.How to set git repository?<br>
A.added new server's newly generated ssh key to github setting. Fixed.<br><br>
Q2.RDS... options are too limited - Just oracle.<br> Worth of refactoring all the codes from mysql-sequelize to oracle-something?<br>
A.There's alternative of using sequelize-oracle. But is it really good idea to go for? 💭<br>

A.Making another oci instance and install mysql to use as a RDS instance.<br><br>

## step3.
- adding .env for prod server and run node<br>

Q. Connection from mysql workbench via ssh was successful. But what about as a RDS using a connection string?<br>

A. After giving correct privileges to mysql user, I could connect without ssh connection on work bench.

Q. What about connecting on that information? Should test with local server first. 🤔 [✅]

- Setting nginx config with jenkins going on.<br>
## collapsible markdown?

<details><summary>nginx config with jenkins</summary>
<p>

#### sudo vim /etc/nginx/sites-available/mymoviestory.ml.conf

```bash
# configure upstream
upstream jenkins {
    server localhost:8080;
    # limit the number of idle connections to this upstream
    keepalive 16;
}

server {
    # standard "redirect-all-to-https" configuration
    listen 80;
    listen [::]:80;
    server_name mywebsitedomain.com;
    # return 301 http://$host$request_uri;
    if ($scheme = "http") {
	return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name  mywebsitedomain.com;

    ssl_certificate /etc/letsencrypt/live/mywebsitedomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mywebsitedomain.com/privkey.pem;

    # root directive is not needed here,
    # since all traffic is redirected to Jenkins and
    # it will be serving static files
    # standard long block of SSL configuration is omitted,
    # check the full file for details

    # Jenkins will use custom headers for CSRF protection
    # whithout this directive NGINX will drop those headers
    ignore_invalid_headers off;

    location / {
        # proxy_pass http://jenkins;
        proxy_pass http://jenkins;


        # we want to connect to Jenkins via HTTP 1.1 with keep-alive connections
        proxy_http_version 1.1;

        # has to be copied from server block,
        # since we are defining per-location headers, and in
        # this case server headers are ignored
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # no Connection header means keep-alive
        proxy_set_header Connection "";

        # Jenkins will use this header to tell if the connection
        # was made via http or https
        proxy_set_header X-Forwarded-Proto $scheme;

        # increase body size (default is 1mb)
        client_max_body_size       10m;

        # increase buffer size, not sure how this impacts Jenkins, but it is recommended
        # by official guide
        client_body_buffer_size    128k;

        # block below is for HTTP CLI commands in Jenkins
        # increase timeouts for long-running CLI commands (default is 60s)
        proxy_connect_timeout      90;
        proxy_send_timeout         90;
        proxy_read_timeout         90;

        # disable buffering
        proxy_buffering            off;
        proxy_request_buffering    off;
    }

    error_page 404 /404.html;
        location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }
}
```

</p>
</details>
## step4.
- When I reach my domain, there's jenkins admin page.<br><br>

Q.How to map deployed project to targeted domain...?<br>
Q.git push -> project deployed...?<br>