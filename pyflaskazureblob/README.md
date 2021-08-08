
# Repository for Azure Python Libraries and Flask
```
docker run --rm -it -p 5000:5000 --env AZURE_STORAGE_CONNECTION_STRING="passyourstring" --env AZURE_STORAGE_CONTAINER_NAME="passurcontainername" singharunk/pyflaskazureblob:latest
```

## To generate base64 for YAML file

```
echo -n "string" | base64 -w 0
```


- Use of Block in Jinja Templates

url_for - specifiy the name of function rather then hard coded urls.