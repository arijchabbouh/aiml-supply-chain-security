from fastapi import FastAPI

app = FastAPI(title="AI/ML Supply Chain Security Platform")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
