# quay-mcp

MCP server for Quay

## Running with Podman or Docker

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "quay": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "QUAY_TOKEN_<ORG_NAME_1>",
        "-e", "QUAY_TOKEN_<ORG_NAME_2>",
        "quay.io/maorfr/quay-mcp"
      ],
      "env": {
        "QUAY_TOKEN_<ORG_NAME_1>": "REDACTED",
        "QUAY_TOKEN_<ORG_NAME_2>": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with a valid token.

## Available MCP Tools

The following tools are available via the quay-mcp server:

- **get_organization_members(organization_name: str)**
  
  Returns the members of the specified Quay organization.

- **get_team_members(organization_name: str, team_name: str)**
  
  Returns the members of a specific team within a Quay organization.

- **add_team_member(organization_name: str, team_name: str, member_name: str)**
  
  Adds a user as a member to a specific team within a Quay organization.

- **get_repositories(organization_name: str)**
  
  Lists all repositories under the specified Quay organization.

- **create_repository(organization_name: str, repository_name: str, visibility: str = "private", description: str = "")**
  
  Creates a new repository in the specified Quay organization. You can set the repository visibility ("private" or "public") and provide an optional description.

These tools require the appropriate Quay API tokens to be set as environment variables (see above for configuration details).
