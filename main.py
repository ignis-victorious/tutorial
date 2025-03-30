
#  __________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  __________________


app = FastAPI()

@app.get('/')
async def index() -> dict[str, str]:
    return {'hello':'woirld'}

@app.get('/about')
async def about() -> str:
    return 'An exceptional product!'


# def main() -> None:
#     print("Hello from tutorial!")
# if __name__ == "__main__":
#     main()





#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________




