docker build -t kawaii .
docker stop klee
docker rm klee
docker run --name klee -p 35022:22 -itd kawaii
docker exec -it --user root klee bash