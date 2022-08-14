import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run(app, port=2444, host='0.0.0.0')
