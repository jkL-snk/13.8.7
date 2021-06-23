# 13.8.7

Пример запуска:

docker build -t python-favicon:v1 .
docker run --rm -v "$PWD":/app/ python-favicon:v1 http://github.com/

Результатом будет создание изображение с favicon наибольшего из доступных размеров в текущей директории.
