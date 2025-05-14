import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("quay")

QUAY_API_BASE = os.environ["QUAY_URL"] + "/api/v1"


async def make_request(url: str, organization_name: str) -> dict[str, Any] | None:
    token = os.environ[f"QUAY_TOKEN_{organization_name.upper()}"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            return None


@mcp.tool()
async def get_organization_members(organization_name: str) -> str:
    url = f"{QUAY_API_BASE}/organization/{organization_name}/members"
    data = await make_request(url, organization_name)
    print(data)
    return data


@mcp.tool()
async def get_team_members(organization_name: str, team_name: str) -> str:
    url = f"{QUAY_API_BASE}/organization/{organization_name}/teams/{team_name}/members"
    data = await make_request(url, organization_name)
    print(data)
    return data


if __name__ == "__main__":
    mcp.run(transport="stdio")
