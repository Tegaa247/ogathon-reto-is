import requests
import time

url = "http://localhost:8080/challenges/solution-1?n=91"

# Medir tiempo con alta precisión
start = time.perf_counter()
response = requests.get(url)
end = time.perf_counter()

# Mostrar resultados
print("Tiempo:", round((end - start) * 1000, 3), "ms")
print("Respuesta:", response.json())
