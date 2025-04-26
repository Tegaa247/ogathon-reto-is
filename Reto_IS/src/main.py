from fastapi import FastAPI
from calculate import calculate_patterns

app = FastAPI(
    title="Ogathon Challenges API",
    description="API para calcular patrones de propagación viral",
    version="1.0.0"
)

@app.get("/challenges/solution-1")
def solution_1(n: int):
    result = calculate_patterns(n)
    return {"distance": n, "patterns": result}


