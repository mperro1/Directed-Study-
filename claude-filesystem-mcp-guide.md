# Filesystem MCP 

## Prerequisites Check (30 seconds)

**Claude Desktop** installed  
Terminal/Command Prompt open  

## Step 1: Installing te MCP Server 
```bash

uvx mcp-server-git

pip install mcp-server-git
python -m mcp_server_git
```
## Step 2: Configuring the Server for Claude
To use an MCP server with Claude, add your server definitions to the Claude configuration file 
(usually claude_desktop_config.json).

Replace /path/to/allowed/files with the directory you want Claude to access.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/files"
      ]
    },
  }
}
```

Example run for this project: 
![alt text](image-3.png)
For other example servers see: https://modelcontextprotocol.io/examples