# Используем официальный образ Nginx
FROM nginx:alpine

# Добавляем метаданные для образа
LABEL maintainer="kuptsova_nika@mail.ru"
LABEL version="1.1"
LABEL description="Custom Nginx web server with static HTML pages"

# Устанавливаем рабочую директорию
WORKDIR /usr/share/nginx/html

# Копируем HTML файлы в контейнер
COPY index.html about.html style.css ./

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Устанавливаем curl для healthcheck (в alpine нет curl по умолчанию)
RUN apk add --no-cache curl

# Создаем healthcheck для проверки работоспособности
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Открываем порт 80
EXPOSE 80

# Команда запуска 
CMD ["nginx", "-g", "daemon off;"]