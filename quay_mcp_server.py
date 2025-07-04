import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("quay")

QUAY_API_BASE = os.environ["QUAY_URL"] + "/api/v1"


async def make_request(
    url: str, organization_name: str, method: str = "GET", params: dict[str, Any] = None
) -> dict[str, Any] | None:
    token = os.environ[f"QUAY_TOKEN_{organization_name.upper()}"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method, url, headers=headers, json=params, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            return None


@mcp.tool()
async def get_organization_members(organization_name: str) -> str:
    """
    Retrieve the members of a specified Quay organization.

    Args:
        organization_name (str): The name of the Quay organization.

    Returns:
        str: JSON string containing the list of organization members.
    """
    url = f"{QUAY_API_BASE}/organization/{organization_name}/members"
    data = await make_request(url, organization_name)
    print(data)
    return data


@mcp.tool()
async def get_team_members(organization_name: str, team_name: str) -> str:
    """
    Retrieve the members of a specific team within a Quay organization.

    Args:
        organization_name (str): The name of the Quay organization.
        team_name (str): The name of the team within the organization.

    Returns:
        str: JSON string containing the list of team members.
    """
    url = f"{QUAY_API_BASE}/organization/{organization_name}/team/{team_name}/members"
    data = await make_request(url, organization_name)
    print(data)
    return data


@mcp.tool()
async def add_team_member(organization_name: str, team_name: str, member_name: str) -> str:
    """
    Add a user as a member to a specific team within a Quay organization.

    Args:
        organization_name (str): The name of the Quay organization.
        team_name (str): The name of the team within the organization.
        member_name (str): The username of the member to add.

    Returns:
        str: JSON string with the result of the operation.
    """
    url = f"{QUAY_API_BASE}/organization/{organization_name}/team/{team_name}/members/{member_name}"
    data = await make_request(url, organization_name, method="PUT")
    print(data)
    return data


@mcp.tool()
async def get_repositories(organization_name: str) -> str:
    """
    List all repositories under the specified Quay organization.

    Args:
        organization_name (str): The name of the Quay organization.

    Returns:
        str: JSON string containing the list of repositories.
    """
    url = f"{QUAY_API_BASE}/repository"
    params = {
        "namespace": organization_name,
    }
    data = await make_request(url, organization_name, params=params)
    print(data)
    return data


@mcp.tool()
async def create_repository(
    organization_name: str,
    repository_name: str,
    visibility: str = "private",
    description: str = "",
) -> str:
    """
    Create a new repository in the specified Quay organization.

    Args:
        organization_name (str): The name of the Quay organization.
        repository_name (str): The name of the new repository.
        visibility (str, optional): Repository visibility, either "private" or "public". Defaults to "private".
        description (str, optional): Description for the repository. Defaults to an empty string.

    Returns:
        str: JSON string with the result of the repository creation.
    """
    url = f"{QUAY_API_BASE}/repository"
    params = {
        "repository": repository_name,
        "visibility": visibility,
        "namespace": organization_name,
        "description": description,
        "repo_kind": "image",
    }
    data = await make_request(url, organization_name, method="POST", params=params)
    print(data)
    return data


if __name__ == "__main__":
    mcp.run(transport="stdio")
