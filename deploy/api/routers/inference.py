from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from apiinference import Inference
import dotenv
import os

router = APIRouter()

@router.get("/inference")
async def inference_route(address: str):
    try:
        inf = Inference()
        results = inf.combined_inference(str(address))
        return str(results)
    except Exception as e:
        HTTPException(502, detail="Could not run inference")