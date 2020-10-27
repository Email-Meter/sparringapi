import asyncio
import random
import uvicorn
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse

from . import settings

app = Starlette(debug=settings.DEBUG)


@app.route("/")
class SparringView(HTTPEndpoint):

    def get_latency(self, request):
        """
        Simulates request latency:

        By default the latency will vary from 0 to 1 secs. You can customize this value
        passing the `latency` GET param.

        There is a max value for the latency specified in settings.MAX_LATENCY
        """
        return min(float(request.query_params.get("latency", random.random())), settings.MAX_LATENCY)

    def get_status_code(self, request):
        """
        Gets the response status code

        By default this returns 200 OK (specified in settings.DEFAULT_STATUS_CODE).
        You can customize this status code by passing the `status_code` GET param.

        If you use status_code=random, SparringAPI will simulate a weighted random choice
        between the most common kinds of HTTP status codes.
        """

        custom_status_code = request.query_params.get("status_code", 0)
        if custom_status_code == 'random':
            return random.choices([200, 201, 400, 401, 404, 500, 429], weights=[15, 8, 2, 2, 2, 1, 1])[0]
        else:
            return int(custom_status_code) or settings.DEFAULT_STATUS_CODE

    async def get(self, request):
        latency = self.get_latency(request)
        await asyncio.sleep(latency)
        response = {
            "status": "OK",
        }
        return UJSONResponse(response, status_code=self.get_status_code(request))


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
