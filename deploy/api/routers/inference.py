from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from apiinferencev2 import nn_prediction, combined_prediction
import dotenv
import os

router = APIRouter()

@router.get("/inference")
async def inference_route(address: str):
    try:
        results = nn_prediction(str(address))
        return str(results)
    except Exception as e:
        HTTPException(502, detail="Could not run inference")

# @router.get("/combined_inference")
# async def inference_route(address: str):
#     try:
#         results = combined_prediction(str(address))
#         return str(results)
#     except Exception as e:
#         HTTPException(502, detail="Could not run inference")
