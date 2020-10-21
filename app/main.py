import uvicorn
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse


from . import settings


app = Starlette(debug=settings.DEBUG)




@app.route("/run")
class SparringView(HTTPEndpoint):

    async def get(self, request):
        response = {
            "status": "OK",
        }
        return UJSONResponse(response)


if __name__ == '__main__':  # pragma: no cover
    uvicorn.run(app, host='0.0.0.0', port=settings.PORT)

