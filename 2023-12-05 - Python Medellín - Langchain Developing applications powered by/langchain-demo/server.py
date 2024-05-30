#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# 1. Import chains
from meals_chain.chain import chain as meals_chain
from translation_chain.chain import chain as  translation_chain
from agent_coupon_code.chain import agent_executor as agent_coupon_code

# 2. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 3. Adding chain route
add_routes(app,meals_chain,path="/meals_chain")
#add_routes(app, translation_chain, path="/translation_chain")
add_routes(app, agent_coupon_code, path="/agent_coupon_code")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)