# docker-logs-localtime
replace all UTC dates to local dates in pipe
by ieaster1 https://github.com/ieaster1

usage: docker logs -t container_name | local-docker-logs

### Install

`wget -O /usr/local/bin/docker-logs-localtime https://raw.githubusercontent.com/ieaster1/docker-logs-localtime/master/docker-logs-localtime && chmod +x /usr/local/bin/docker-logs-localtime`

*or*

`git clone https://github.com/ieaster1/docker-logs-localtime.git /usr/local/docker-logs-localtime && ln -s /usr/local/docker-logs-localtime/docker-logs-localtime /usr/local/bin/docker-logs-localtime && chmod +x /usr/local/docker-logs-localtime/docker-logs-localtime /usr/local/bin/docker-logs-localtime`