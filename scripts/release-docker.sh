version=$(<./version)

docker build -t wallachgame/browserwapi:$version -t wallachgame/browserwapi:latest .
docker push wallachgame/browserwapi:$version
docker push wallachgame/browserwapi:latest
