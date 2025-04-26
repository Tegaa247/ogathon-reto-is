from calculate import calculate_patterns

# Pruebas básicas
print("Distancia 3:", calculate_patterns(3))      # → 3
print("Distancia 10:", calculate_patterns(10))    # → 89
print("Distancia 20:", calculate_patterns(20))    # → 10946
print("Distancia 50:", calculate_patterns(50))    # → 20365011074

# Resultado final
n = 91
result = calculate_patterns(n)
print(f"Distancia {n}: {result}")
