# MCP Prompt Engineering Steps + Build 

### MCP Server Builder Prompt 
Before generating the MCP server, please provide:

Service/Tool Name: What service or functionality will this MCP server provide?

API Documentation: If this integrates with an API, please provide the documentation URL

Required Features: List the specific features/tools you want implemented

Authentication: Does this require API keys, OAuth, or other authentication?

Data Sources: Will this access files, databases, APIs, or other data sources?

## Example Prompt for a study aid mcp server:

Build an MCP server in Python that helps students generate study questions and find learning resources for any topic. The server should expose 2 simple, well-documented tools:
Tools to Implement:
generate_study_questions - Generate practice questions for a given topic with answers

Input: topic (subject/concept to study), difficulty (easy/medium/hard), count (number of questions)
Output: Formatted list of questions with answers for self-testing
Should generate multiple question types: multiple choice, true/false, short answer
Include explanations with answers for learning

find_study_resources - Suggest learning resources and study strategies for a topic

Input: topic (subject to learn), resource_type (videos/articles/practice/books)
Output: Formatted suggestions of where/how to learn the topic
Should recommend: Khan Academy, YouTube channels, Wikipedia sections, practice websites
Include study tips specific to the topic type (math vs history vs language)

# Requirements 

## Give the LLM a role 

You are an expert MCP (Model Context Protocol) server developer. You will create a complete, working MCP server based on the user's requirements.

## YOUR OUTPUT STRUCTURE

You must organize your response in TWO distinct sections:

### Section 1: Files to Create 

Generate EXACTLY these 5 files with complete content that the user can copy and save.

**DO NOT** create duplicate files or variations. Each file should appear ONCE with its complete content.

### Section 2: Installation Instructions for the user

Provide step-by-step commands the user needs to run on their computer.

Present these as a clean, numbered list without creating duplicate instruction sets.

# Files to Create. Indicate if the server will be installed locally or utilizing Docker 

## File 1: Dockerfile

```dockerfile

# Use Python slim image

FROM python:3.11-slim


# Set working directory

WORKDIR /app


# Set Python unbuffered mode

ENV PYTHONUNBUFFERED=1


# Copy requirements first for better caching

COPY requirements.txt .


# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt


# Copy the server code

COPY [SERVER_NAME]_server.py .


# Create non-root user

RUN useradd -m -u 1000 mcpuser && \

&nbsp;&nbsp;&nbsp;&nbsp;chown -R mcpuser:mcpuser /app

  
# Switch to non-root user

USER mcpuser

  
# Run the server

CMD ["python", "[SERVER_NAME]_server.py"]

```

## File 2: requirements.txt

```

mcp[cli]>=1.2.0

httpx

# Add any other required libraries based on the user's needs

```

## File 3: [SERVER_NAME]_server.py
```python
#!/usr/bin/env python3

"""
Simple [SERVICE_NAME] MCP Server - [DESCRIPTION]
"""

import os
import sys
import logging
from datetime import datetime, timezone
import httpx

from mcp.server.fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("[SERVER_NAME]-server")

# Initialize MCP server - NO PROMPT PARAMETER!
mcp = FastMCP("[SERVER_NAME]")

# Configuration
# Add any API keys, URLs, or configuration here
# API_TOKEN = os.environ.get("[SERVER_NAME_UPPER]_API_TOKEN", "")

# === UTILITY FUNCTIONS ===
# Add utility functions as needed

# === MCP TOOLS ===
# Create tools based on user requirements
# Each tool must:
# - Use @mcp.tool() decorator
# - Have SINGLE-LINE docstrings only
# - Use empty string defaults (param: str = "") NOT None
# - Have simple parameter types
# - Return a formatted string
# - Include proper error handling
# WARNING: Multi-line docstrings will cause gateway panic errors!

@mcp.tool()
async def example_tool(param: str = "") -> str:
    """Single-line description of what this tool does - MUST BE ONE LINE."""
    logger.info(f"Executing example_tool with {param}")

    try:
        # Implementation here
        result = "example"
        return f"✅ Success: {result}"
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"❌ Error: {str(e)}"

# === SERVER STARTUP ===
if __name__ == "__main__":
    logger.info("Starting [SERVICE_NAME] MCP server...")

    # Add any startup checks
    # if not API_TOKEN:
    #     logger.warning("[SERVER_NAME_UPPER]_API_TOKEN not set")

    try:
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)
```
## File 4: README.md
Create a comprehensive readme with all sections filled in based on the implementation.

## File 5: claude.md
Create a CLAUDE.md file with implementation details and guidelines.

# Section 2: Installation Instructions for the user 
After creating the files above, provide these instructions for the user to run:

## Step 1: Save the Files
```bash

# Create project directory

mkdir [SERVER_NAME]-mcp-server

cd [SERVER_NAME]-mcp-server

  

# Save all 5 files in this directory

```

## Step 2: Build Docker Image
```bash

docker build -t [SERVER_NAME]-mcp-server .

```

## Step 3: Set Up Secrets (if needed)
```bash

# Only include if the server needs API keys or secrets

docker mcp secret set [SECRET_NAME]="your-secret-value"

  

# Verify secrets

docker mcp secret list

```

## Step 4: Create Custom Catalog
```bash

# Create catalogs directory if it doesn't exist

mkdir -p ~/.docker/mcp/catalogs

  

# Create or edit custom.yaml

nano ~/.docker/mcp/catalogs/custom.yaml

```

Add this entry to custom.yaml:

```yaml
version: 2

name: custom
displayName: Custom MCP Servers

registry:
  [SERVER_NAME]:
    description: "[DESCRIPTION]"
    title: "[SERVICE_NAME]"
    type: server
    dateAdded: "[CURRENT_DATE]" # Format: 2025-01-01T00:00:00Z
    image: [SERVER_NAME]-mcp-server:latest

```

## Step 5: Update Registry
```bash

# Edit registry file

nano ~/.docker/mcp/registry.yaml

```

Add this entry under the existing `registry:` key:

```yaml

registry:
  # ... existing servers ...

  [SERVER_NAME]:
    ref: ""


```

**IMPORTANT**: The entry must be under the `registry:` key, not at the root level.

## Step 6: Configure Claude Desktop
Find your Claude Desktop config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

- **Linux**: `~/.config/Claude/claude_desktop_config.json`

Edit the file and add your custom catalog to the args array:


## Step 7: Restart Claude Desktop

1. Quit Claude Desktop completely

2. Start Claude Desktop again

3. Your new tools should appear!

## Step 8: Test Your Server

```bash

# Verify it appears in the list

docker mcp server list

  

# If you don't see your server, check logs:

docker logs [container_name]

```

## Development

### Local Testing

```bash

# Set environment variables for testing

export [SECRET_NAME]="test-value"

# Run directly

python [SERVER_NAME]_server.py

# Test MCP protocol

echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | python [SERVER_NAME]_server.py

```
### Adding New Tools

1. Add the function to `[SERVER_NAME]_server.py`

2. Decorate with `@mcp.tool()`

3. Update the catalog entry with the new tool name

4. Rebuild the Docker image

## Troubleshooting

### Tools Not Appearing

- Verify Docker image built successfully

- Check catalog and registry files

- Ensure Claude Desktop config includes custom catalog

- Restart Claude Desktop

### Authentication Errors

- Verify secrets with `docker mcp secret list`

- Ensure secret names match in code and catalog

## Security Considerations

- All secrets stored in Docker Desktop secrets

- Never hardcode credentials

- Running as non-root user

- Sensitive data never logged
