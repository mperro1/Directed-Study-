# Directed Study Rubric: Code Intelligence & Documentation MCP Server

## Course Information
- **Student:** Marcela Perro
- **Course Title:** Independent Study - MCP Server Development
- **Credit Hours:** 4
- **Duration:** Fall Semester
- **Supervising Faculty:** Albert Lionelle

## Study Overview
This directed study explores the local and cloud deployment of MCP servers, focusing on evaluating available MCP server implementations and leveraging AI to develop customized MCP solutions. The study includes hands-on experimentation with Docker-based MCP tools, Google ADK, and other MCP server management platforms. Evaluation centers on performance, scalability, and security trade-offs, with an MCP prototype implemented and tested in both local and cloud environments to assess how infrastructure impacts system efficiency

## Objectives
1. Designing and implementing MCP servers according to industry standards.
2. Hosting servers on both local hardware and in a cloud environment.
3. Testing containerized MCP servers.
4. Utilizing custom prompts / AI-driven tooling to deploy an MCP server.
5. Comparing scalability, latency, and maintenance requirements for each deployment.
6. Measuring the cost, reliability, and security of each hosting approach for representative AI application use cases.

## Project Components & Milestones

### Phase 1: Refinement Period & Technical Foundation (Weeks 1-2)

| Milestone | Deliverable |
|-----------|-------------|
| **Technical Architecture Design** | System architecture document covering MCP server design, API integrations, data flow, and security considerations |
| **Google Cloud Project Setup** | Complete GCP project configuration with Cloud Run deployment, Secret Manager integration, and automated CI/CD pipeline |
| **Development Environment Setup** | Working local and cloud development environment with GitHub integration, basic CLI framework, and initial MCP server structure |
| **Scope Refinement** | Refined project scope with clear security-focused objectives |

**Success Criteria:**
- Clear, security-focused project scope 
- Detailed technical specification with realistic implementation plan
- Fully operational GCP project with deployed "Hello World" MCP server
- Functional development environment with cloud deployment pipeline working

### Phase 2: Implementation of MCP Servers Using Claude Desktop 
1. Install and configure Claude Desktop MCP integrations.
2. Install and test Filesystem MCP
3. Document setup steps, configuration details, and initial evaluations.
4. Establish baseline understanding of MCP communication, capabilities, and limitations.

### Phase 3: Google ADK & Cloud-Hosted MCP Deployment
1. Deploy MCP servers using Google ADK (Application Developer Kit) or relevant cloud tooling.
2. Configure cloud networking, IAM security layers, firewall rules, and service endpoints.
3. Measure cloud-specific metrics (latency, cost, autoscaling behavior, reliability).
4. Compare cloud hosting vs. local hosting in terms of cybersecurity, cost, and maintainability.

### Phase 4: Custom MCP Server Development Using AI-Driven Prompt Engineering
1. Design and implement a custom MCP server using AI as a development assistant.
2. Apply prompt-engineering strategies to generate, refine, and optimize server logic.
3. Integrate additional custom tools, capabilities, or endpoints into the MCP server.
4. Evaluate how AI-assisted development impacts speed, accuracy, and functionality.
5. Document all tooling, prompts, and architectural decisions.

### Phase 5: Final Report, Reflection, and Demonstration
1. Compile all results from local, Docker-based, and cloud-based experiments.
2. Provide a comparative analysis of scalability, performance, cost, reliability, and security.
3. Reflect on challenges, lessons learned, and recommendations for MCP deployments.
4. Prepare and deliver the final demonstration of all MCP implementations.
5. Submit complete documentation, including diagrams, metrics, and code references.

## Required Training & Preparation

### **Pre-Project Learning Requirements**
Before beginning development, the student must complete the following training modules to ensure adequate preparation for the technical requirements.

#### **API Documentation & Integration (Week 0-1)**
| Resource | Focus Area | Estimated Time |
|----------|------------|----------------|
| **GitHub API Documentation** | Repository access, authentication, REST API endpoints | 4-6 hours |
| **Semgrep API Documentation** | Security scanning integration, rule configuration, result parsing | 3-4 hours |
| **Anthropic Claude API Documentation** | LLM integration, prompt engineering, cost management | 3-4 hours |
| **API Integration Best Practices** | Error handling, rate limiting, authentication patterns | 2-3 hours |
| **Docker Documentation** | 

#### **Google Cloud Platform Training (Week 0-1)**
| Course/Resource | Focus Area | Estimated Time |
|-----------------|------------|----------------|
| **Google Cloud Fundamentals** | Core concepts, account setup, billing management | 4-5 hours |
| **Cloud Run Quickstart** | Serverless deployment, container basics, CI/CD setup | 3-4 hours |
| **Secret Manager Tutorial** | API key management, secure configuration | 1-2 hours |
| **Cloud Build Documentation** | Automated deployment, build triggers, Docker integration | 2-3 hours |

#### **MCP Server Development (Week 0-2)**
| Resource | Focus Area | Estimated Time |
|----------|------------|----------------|
| **Anthropic Introduction to MCP Servers** | MCP protocol fundamentals, server architecture, basic implementation | 4-6 hours |
| **Advanced MCP Server Development** | Complex integrations, natural language processing, production deployment | 6-8 hours |
| **MCP Server Best Practices** | Security, scalability, error handling, testing strategies | 3-4 hours |

#### **Supporting Technologies (Ongoing)**
| Resource | Focus Area | Estimated Time |
|----------|------------|----------------|
| **Python AST Module Documentation** | Code parsing, syntax tree manipulation | 2-3 hours |
| **Tree-sitter Documentation** | Advanced code parsing, multi-language support | 2-3 hours |
| **Docker Fundamentals** | Containerization, deployment, best practices | 3-4 hours |

### **Training Schedule Integration**
- Complete API documentation research and Google Cloud fundamentals
- Complete MCP server introduction while setting up development environment
- Advanced MCP server training alongside architecture design
- **Ongoing**: Reference supporting technology documentation as needed during implementation

### **Training Validation**
Students must demonstrate competency by:
- Successfully completing Google Cloud account setup with basic service deployment
- Implementing simple API calls to GitHub, and Claude APIs
- Deploying a basic "Hello World" MCP server to Cloud Run
- Documenting key learnings and architecture decisions from training modules
## Technical Specifications

### **Minimum Viable Product Requirements:**
- **Repository Integration:** GitHub API with authentication
- **Security Analysis:** Vulnerability detection using Semgrep API
- **Documentation Generation:** AI-powered docs for functions, classes, and APIs
- **Infrastructure Analysis:** Docker Compose security and documentation
- **CLI Interface:** Natural language query processing via MCP

## Evaluation Criteria
### **Technical Excellence**
- Code quality, architecture, and documentation
- Proper use of APIs and external services
- Security and performance considerations
- Innovation in combining multiple analysis sources

### **Implementation Success**
- Meeting milestone deadlines and requirements
- Functional demonstration of core features
- User experience and interface design
- Problem-solving and adaptation to challenges


## Final Deliverables

1. **Production MCP Server** - Deployed on locally or on cloud Run with full functionality and monitoring
2. **Technical Report** - Covering architecture, MCP architecture, findings and evaluation
3. **Live Demonstration** - Showcase of key features using production cloud deployment
4. **Source Code Repository** - Clean, documented, and reproducible code with automated deployment pipeline
5. **Reflection** - Written reflection summarizing lessons learned
