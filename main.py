from fastapi import FastAPI

app = FastAPI(title="Vegas Pro Engine")

@app.get("/health")
def health():
    return {"ok": True, "service": "vegas-pro-engine"}
