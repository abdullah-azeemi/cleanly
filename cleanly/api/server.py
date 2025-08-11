from fastapi import FastAPI, UploadFile, Form
import pandas as pd
import numpy as np
from cleanly.core import DataCleaner
from cleanly.llm.parser import parse_cleaning_instructions
from cleanly.io import load_csv
import io

app = FastAPI(title="Cleanly API", version="0.1.0")

@app.post('/clean')
async def clean_data(file: UploadFile, instruction: str = Form(...)):
  contents = await file.read()
  df = pd.read_csv(io.BytesIO(contents))
  
  steps = parse_cleaning_instructions(instruction)
  cleaner = DataCleaner(df)
  
  for step in steps: 
    action = step.pop("action")
    getattr(cleaner, action)(**step)
    
  preview_df = cleaner.preview()
  safe_preview_df = preview_df.replace([np.inf, -np.inf], None)
  safe_preview_df = safe_preview_df.astype(object).where(pd.notna(safe_preview_df), None)
  
  return {
    "preview": safe_preview_df.to_dict(orient="records"),
    "steps": steps
  }
  