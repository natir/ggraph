# GGraph

web service for generate svg with graphviz information

## Requirement

* python >= 3.4

## Instalation

```
git clone http://gogs.pierre.marjon.fr/natir/ggraph.git

pip install -r requirement.txt

# For test only
make run [port number]
```

## Usage

Service is provide at this adresse : http://ggraph.pierre.marijon.fr/

You can try some url :
* [node a to b](http://ggraph.pierre.marijon.fr/?digraph{a->b;})
* [node a to b png version](http://ggraph.pierre.marijon.fr/png/?digraph{a->b;})
* [some complex graph](http://ggraph.pierre.marijon.fr/?digraph{
    fontname = "Bitstream Vera Sans";
    fontsize = 8;
    node [fontname = "Bitstream Vera Sans";fontsize = 8;shape = "record";];
    edge [fontname = "Bitstream Vera Sans";fontsize = 8;];
    Sequence [label = "{Sequence|+data:string\\l+comment:string\\l|+gc\(\):float}"];
    Genome [label = "{Genome|+seqs:Sequence[]\\l+annotation:Annotation\\l}"];
    Sequence -> Genome;
})

## Production setup

For run ggraph in production you can use this configuration file.

### Systemd

```
[Unit]
Description=SVG graph generator
After=network.target
Requires=network.target

[Service]
User=youruser
Group=yourgroup
Environement="PATH=/path/to/ggraph/env/bin"
ExecStart=/path/to/ggraph/env/bin/gunicorn --workers 3 -bind unix:ggraph.sock -m 007 wsgi
Restart=always

[Install]
WantedBy=multi-user.target
```

### nginx

```
server
{
	listen 80;
	listen 443 ssl;

	server_name ggraph.hostname;

	location /
	{
		proxy_set_header Host $http_host;
		proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/path/to/ggraph/ggraph.sock;
	}
}
```
