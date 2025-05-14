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
