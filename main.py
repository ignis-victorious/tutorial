
#  __________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI, HTTPException
#  Import FILES
from data import BANDS
from schemas import GenreURLChoices, Band
#  __________________


app = FastAPI()

@app.get('/')
async def index() -> dict[str, str]:
    return {'Index':'Index page'}

@app.get('/bands')
async def bands() -> list[Band]:
# async def bands() -> list[dict[str, Any]]:
    return [Band(**b) for b in BANDS]
    # return BANDS

@app.get('/bands/{band_id}', status_code=206)
async def band(band_id: int) -> Band:
# async def band(band_id: int) -> None | dict[str, Any]:
    band: Band | None = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    # band: dict[str, Any] | None = next((b for b in BANDS if b['id']== band_id), None)
    if band is None:
        # Status code 404
        raise HTTPException(status_code=404, detail='Band not found!')
        # pass
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
# async def bands_for_genre(genre: str) -> list[dict]:
    return [b for b in BANDS if b['genre'].lower() == genre.value]
     


# def main() -> None:
#     print("Hello from tutorial!")
# if __name__ == "__main__":
#     main()





#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________




