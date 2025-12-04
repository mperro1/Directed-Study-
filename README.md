# Directed-Study-MCP Servers 

## Introduction 
This directed study explores the local and cloud deployment of Model Context Protocol (MCP) servers, focusing on evaluating available MCP server implementations and leveraging AI to develop customized MCP solutions. The study includes hands-on experimentation with Docker-based MCP tools, Google ADK, and other MCP server management platforms. Evaluation centers on performance, scalability, and security trade-offs, with an MCP prototype implemented and tested in both local and cloud environments to assess how infrastructure impacts system efficiency and cybersecurity. As organizations increasingly migrate from on-premise data centers to cloud infrastructures, this project aims to identify the optimal operational environment for MCP servers. Throughout the report, the configuration steps, AI-driven tool development, and results from testing multiple MCP server frameworks are documented to provide comprehensive insights into deployment practices and recommendations.
Model Context Protocol (MCP) servers are key components in modern AI systems, acting as gateways between large language models (LLMs) and the external context or capabilities they require to deliver meaningful interactions. An MCP server standardizes how data flows, context is maintained, and external resources are queried by connected clients.
The scope of this project includes:

- Designing and implementing MCP servers according to industry standards.​
- Hosting servers on both local hardware and in a cloud environment.
- Testing containerized MCP servers.
- Utilizing custom prompts to deploy an MCP server.
- Comparing scalability, latency, and maintenance requirements for each deployment.
- Measuring the cost, reliability, and security of each hosting approach for representative AI application use cases.​


## Key Functions of an MCP Server 
- Context Management: Maintains a consistent context state for each session, allowing the AI model to track ongoing conversations and relevant data.​
- Data Synchronization: Ensures data consistency by propagating updates between clients and the server, and supports both real-time and batch modes.​
- Request Routing: Directs incoming function requests to appropriate compute resources, APIs, or tools on the server.
- Authentication and Access Control: Employs mechanisms such as OAuth, API keys, and role-based policies to secure access and data exchange.​
- Logging and Monitoring: Captures system metrics, usage events, and health checks for operational oversight and auditing.​
- Error Recovery: Supports strategies for failover, message retries, and context restoration after disruptions.​

## Limitations and Considerations 
- Security Architecture Weakness: MCP initially lacked an authentication/authorization framework, since then these features have been added, but there are still concerns from implementors what the MCP server often plays the authorization and resource server (Example: validating tokens and serving resources) which violates separation-of-concerns. 
- Tool & Context Safety Risks: the protocol allows external “tools” (resources/functions exposed via MCP) to be registered with minimal constraints. A tool can masquerade as a safe operation (e.g., write_secure_file(...)) but actually perform unauthorized or dangerous actions (e.g., data exfiltration).
- LLM / Context Window: reading many documents via multiple tool calls can hit context-window limits, latency problems, and reasoning breakdowns.
- User Experience and Transparency Challenges: For many non-technical users, the sequence of tools and resources invoked through MCP can be difficult to understand. When the system reports something like “Calling Tool X with argument Y,” the user may not realize what data is being accessed, where it is being sent, or who might gain visibility into it. This lack of clarity can undermine trust and raise privacy concerns.

## Parts of MCP Architecture: 
### The Client
The LLM itself. ChatGPT, Claude. 
### The Gateway & Flow 
We can think of the gateway as a middle man that sits between the client and the server. It receives the request, runs the tools, and sends back results in a format the client understands. 
Run the mcp on an end users workstation, needs filesystem access.

How the flow works: 
1. The MCP client, creates a structured JSON payload that includes the tool to invoke, parameters, context, metadata such as authentication tokens, session data. 
2. The MCP client sents this payload to the MCP gateway. Example: 
```json
{
  "type": "call_tool",
  "tool": "list_files",
  "arguments": { "path": "/home/user" }
}
``` 
It doesnt use HTTP routes, no REST endpoints, no URL parameters. Just structured JSON messages 
3. The gateway logs, authorizes, and validates the request.
4. The gateway routes the request to the correct MCP server/servers. The gateway maintains and updates the context state across calls, enabling multi-step and multi-server workflows. The gateway logs this transaction.
5. The MCP server processes the request and creates an MCP-compliant response, adding metadata and updated context.

Often times, the MCP gateway gets confused with the MCP proxy. The MCP proxy is a simpler component that acts like a messenger taking requests from the client and then sending the to the right MCP server. The key difference is that a proxy gives lightweight, fast connectivity and flexible bridging between local and remote environments, while a gateway adds governance, compliance, and visibility on top of that connectivity, making it better suited for enterprise-wide, multi-team deployments.
### Why does MCP doesn't use APIs? 
The API defines what endpoints you can call and how you can call, and then you get a response back. There is a wide variety of ways to do it. Multiple protocols or formats cam be used, you could get resonses back in JSON, or XML. 

MCP is different because it is more dynamic. The documentation for a tool is not something you read in advance; instead, it is sent automatically during the handshake that happens when the connection starts.

Analogy: With MCP, you don’t read documentation and then write code that calls the documented API. That’s how traditional API integrations work: you study the docs, then tailor your code to match them.
MCP solves this differently—its documentation comes through the wire. The AI receives tool descriptions as part of the connection itself, so MCP becomes “documentation + invocation” packaged together.

Here’s what happens during an MCP connection:

The client connects and says:
“I am Claude version X, and I support these capabilities.”

The server responds:
“Hello, I am Puppeteer version X, and here is the list of tools I provide.”

The client then asks for details about those tools.

The server replies with a set of tools and descriptions.

This interaction model is very different from traditional APIs, and that’s where the distinction comes from. MCP tools are self-describing and discovered dynamically, instead of requiring human-written documentation and manual integration work.

![REST APIs vs. MCP](image.png)

### The Server
The piece that processes requests, keeps track of ongoing conversations or tasks, and coordinates with other tools or services as needed routed by the MCP gateway. It coordinates with back-end tools, data sources, and other services, then packages the result in a form the client can use.

## Containeraized MCP Architechture 
MCP servers are packaged as containers. This allows to just run a container rather than spending time installing dependencies and configuring the runtime. Docker MCP allows the selection of an MCP client. For this assignment, I am using Claude desktop to serve as the interface to talk to the MCP servers I’ve installed through Docker Desktop. There are multiple MCP clients to select from. These MCP servers provide capabilities like accessing files, databases, creating custom servers, typically using JSON over either local (stdio) or remote (HTTP) transports. 

![MCP architectue without containers](image-2.png)
![MCP architecture using docker containers ](image-1.png)

How the process works is the client connects to each configured MCP server. When prompting we can specify which tool or server to use. Then the client will query its available tools/capabilities to process, interacts with external systems if needed, and returns the result in natural language. 

Docker MCP architecture allows for strong security and isolation. Every time we run an MCP server with docket its going to run the mcp gateway and then run the specific mcp server. Using standard input and output and JSON RPC is changed through pipes. No need for network overhead. 

Docker MCP gateway differs in the way we dont need to modify out client’s config for each service we run. The gateway comes in as docker, and we can configure multiple servers in docker providing secure, centralized management configuration so instead of having to configure multiple services per client, we only configure one connection that gives us access to a lot of other mcp servers. It is a lot cleaner and easier to keep track and maintain. 

## Remote MCP Architecture 
To-DO 

## Conclusion 
## References 