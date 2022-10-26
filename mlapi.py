
from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()


class spacyItem(BaseModel):
  text: str

nlp_ner = spacy.load(".\BestModelCPU\content\model-best")


@app.post('/')
async def spacy_endpoint(item:spacyItem):
  text = item.dict().values()
  doc = nlp_ner(str(text) )

  return { "results" : str(doc.ents)}