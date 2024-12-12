# Программа-экспортер для Prometheus
## 1. Настройка Prometheus

### 1.1 Настройка онфигурации в prometheus.yml-файле
  ```yml
  scrape_configs:
  - job_name: 'custom_exporter'
    static_configs:
      - targets: ['localhost:8000'] # Убедитесь, что указали правильный адрес и порт
  ```
### 1.2 Запуск prometheus-сервера
  ```cmd
  # Переход к директории prometheus
  cd ./prometheus_3.0.1 & prometheus.exe
  ```
##  2. Настройка программы
### 2.1 Копируем все файлы и устанавливаем зависимости
  ```python
  pip install -r requirements.txt
  ```
### 2.2 Записываем свои значения в переменные файла .env
    #Пример
    EXPORTER_PORT=8000
    EXPORTER_HOST='127.0.0.1'
### 2.3 Запуск скрипта 
```cmd
python main.py
```
## 3. Запросы на PromQL
### 3.1 Использование процессоров
```

cpu_usage
avg(cpu_usage{instance="127.0.0.1:8000"})

# Пиковая нагрузка за промежуток времени
max_over_time(cpu_usage{instance=""}[1h])
```
### 3.2 Памяти всего
```
memory_total

```
### 3.3 Используемая память(вывод в процентах)
```
(memory_used{instance=""} / memory_total{instance=""}) * 100

```
### 3.4 Объем дисков
```
disk_total

```
### 3.5 Используемый объем дисков
```
(disk_used{instance=""} / disk_total{instance=""}) * 100


```

