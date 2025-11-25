# Docker-mcp-setup-guide

## Prerequisites Check (30 seconds)

**Docker Desktop** installed and running  
**Claude Desktop** installed  
Terminal/Command Prompt open  

## Step 1: Enable Docker MCP Toolkit (1 minute)

1. Open Docker Desktop
2. Go to **Settings** → **Beta Features**
3. Enable **"Docker MCP Toolkit"**
4. Click **Apply & Restart**

## Step 2: Select MCP from catalog 

1. Select a server from the list of available servers 


## Step 3: Configure Claude Desktop 

### macOS:
```bash
# Edit Claude config
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Windows (PowerShell):
```powershell
# Edit Claude config
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

Add this configuration (replace `[YOUR_USERNAME]` with your actual username):

```json
{
  "mcpServers": {
    "mcp-toolkit-gateway": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v", "/var/run/docker.sock:/var/run/docker.sock",
        "-v", "/Users/[YOUR_USERNAME]/.docker/mcp:/mcp",
        "docker/mcp-gateway",
        "--catalog=/mcp/catalogs/docker-mcp.yaml",
        "--catalog=/mcp/catalogs/custom.yaml",
        "--config=/mcp/config.yaml",
        "--registry=/mcp/registry.yaml",
        "--tools-config=/mcp/tools.yaml",
        "--transport=stdio"
      ]
    }
  }
}
```

**Note for Windows:** Use `C:\\Users\\[YOUR_USERNAME]` with double backslashes

## Step 4: Test It! 

1. **Restart Claude Desktop** (Quit completely and reopen)
2. Open a new chat
3. Click the tools icon (or press Cmd/Ctrl+I)
4. You should see "mcp-docker" with all the available tools that you can select 

