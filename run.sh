#!/bin/bash
source jamshidenv/bin/activate 
uvicorn main:app --host 0.0.0.0 --port 3455