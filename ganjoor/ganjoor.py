from typing import Literal
from ganjoor.types import Poet, PoetsTypeAdapter
import httpx


class Ganjoor:
    """the ganjoor base class"""

    BASE_API_URL = "https://api.ganjoor.net/api"

    def __init__(self) -> None:
        # get user's authentication vars here
        self.httpx_client = httpx.AsyncClient(base_url=self.BASE_API_URL)

    async def _send_request(
        self,
        request_method: Literal["get", "post", "delete", "put"],
        api_path: str,
        params: httpx.QueryParams | None = None,
    ) -> httpx.Response:
        response = await self.httpx_client.request(
            method=request_method, url=api_path, params=params
        )
        return response

    async def get_poets(self) -> list[Poet]:
        """get list of all poets in ganjoor api"""
        response = await self._send_request(
            request_method="get", api_path="/ganjoor/poets"
        )

        return PoetsTypeAdapter.validate_json(response.text)
