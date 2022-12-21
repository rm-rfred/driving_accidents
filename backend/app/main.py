from fastapi import FastAPI, File, UploadFile

import pandas as pd

app = FastAPI(title="Driving accidents API", openapi_url="/openapi.json")


@app.get("/", status_code=200)
def root(
) -> dict:
    """
    Root GET
    """
    return (
        {"msg": "Hello World"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")


@app.post("/add_accident", status_code=200)
async def add_accident_file(
        accident_file: UploadFile = File(...)) -> None:
    """
    Upload accidents file into Opensearch
    """
    try:
        df = pd.read_csv(accident_file.file, on_bad_lines="skip")
        return {"msg": "Successfully added"}
    except Exception as e:
        raise e
