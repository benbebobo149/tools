## create environment command
```

#remove the old image
docker rmi image-pdf-download-img

# build the new image
docker image build -t image-pdf-download-img .

# run the container
docker run -it --name image-pdf-download -v ./:/app -d image-pdf-download-img
```