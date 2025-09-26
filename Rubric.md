# Directed Study Rubric: Code Intelligence & Documentation MCP Server

## Course Information
- **Student:** Marcela Perro
- **Course Title:** Independent Study - MCP Server Development
- **Credit Hours:** 4
- **Duration:** Fall Semester
- **Supervising Faculty:** Albert Lionelle

## Study Overview
This directed study focuses on researching, implementing, and evaluating a comprehensive Secure Code Review MCP Server that combines automated security analysis, code quality assessment, and vulnerability detection for software repositories and infrastructure configurations.

## Learning Objectives
Upon completion, the student will be able to:
1. Demonstrate comprehensive understanding of MCP server architecture and integration patterns
2. Design and implement AI-powered code analysis systems using existing security and analysis APIs
3. Integrate multiple data sources (repositories, YAML configs, documentation) into unified intelligence systems
4. Evaluate and optimize system performance, security, and developer experience

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

### Phase 2: Core Intelligence Engine (Weeks 3-6)  

| Component | Description |
|-----------|-------------|
| **Repository Analysis Engine** | GitHub integration with code parsing, basic security vulnerability detection using Semgrep API, and code quality metrics |
| **Natural Language CLI Interface** | MCP server with natural language query processing: "What security issues exist?", "Generate docs for this module" |

**Technical Requirements:**
- Support for 1 programming languages (Python)
- Integration with GitHub REST API with proper authentication
- Security analysis using existing APIs (Semgrep free tier)

### Phase 3: Advanced Code Review (Weeks 7-8)

| Component | Description |
|-----------|-------------|
| **Enhaned Security Analysis** | Implement deeper code review capabilities to detect complex vulnerabilities and patterns |
| **Advanced Query Capabilities** | Enhanced CLI supporting complex queries: "List all high-severity vulnerabilities across the repository |

**Success Criteria:**
- Identify and classify advanced security vulnerabilities
- Provide detailed remediation suggestions for code issues 

### Phase 4: Polish & Testing (Weeks 9-10)

| Deliverable | Description | 
|-------------|-------------|
| **System Performance & Security Testing** | Load testing, security audit of API integrations, cost analysis of external service usage |
| **Final Demonstration & Report** | Working demo presentation, comprehensive technical documentation, user guide, report |
| **Reflection** | Week 10 written reflection on project progress, lessons learned, and future directions |

## Weekly Milestone Checkpoints

| Week | Key Milestone | Success Metric |
|------|---------------|----------------|
| **Week 1** | Scope Refinement and GCP Project setup | Can deploy and access MCP server on Cloud Run with "Hello World" functionality | Refined Scope Document |
| **Week 2** | Architecture finalized and GitHub integration | Clear technical specification and successful GitHub API connection through deployed server |
| **Week 3** | Basic code analysis working | Can identify functions/classes in repository and detect simple security issues via cloud-deployed server |
| **Week 4** | Security integration complete | Semgrep API integration working with meaningful vulnerability detection |
| **Week 5** | Extended vulnerability analysis | Ability to classify vulnerabilities by severity and suggest remediation strategies |
| **Week 6** | CLI interface polished | Natural language queries working reliably through Cloud Run endpoint |
| **Week 7** | Advanced security analysis implemented | Enhanced vulnerability detection with detailed remediation suggestions and risk scoring |
| **Week 8** | Performance optimization complete | Production-ready system with caching, cost monitoring, and scalability improvements |
| **Week 9** | System testing complete | Performance benchmarks, cost analysis, and security validation done on production GCP deployment |
| **Week 10** | Final presentation, report, and reflection | Live cloud demonstration, written report, and reflection |

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
- Implementing simple API calls to GitHub, Semgrep, and Claude APIs
- Deploying a basic "Hello World" MCP server to Cloud Run
- Documenting key learnings and architecture decisions from training modules
## Technical Specifications

### **Minimum Viable Product Requirements:**
- **Repository Integration:** GitHub API with authentication
- **Security Analysis:** Vulnerability detection using Semgrep API
- **Documentation Generation:** AI-powered docs for functions, classes, and APIs
- **Infrastructure Analysis:** Docker Compose security and documentation
- **CLI Interface:** Natural language query processing via MCP

### **Advanced Features (if ahead of schedule):**
- Multiple programming language support (beyond initial)
- Mermaid diagram analysis and documentation generation
- GitLab/Bitbucket integration
- Custom security rule configuration
- Docker compose parsing 
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

## Resources & Budget

### **Cloud Infrastructure Budget:** 
**Google Cloud Platform:**
- Cloud Run hosting
- Cloud Storage
- Secret Manager
- Cloud Build CI/CD
- **Total GCP**: Covered entirely by $300 GCP credit 

**External API Usage:**
- GitHub API: Free tier
- Semgrep API: Free tier (100k lines/month)
- Docker Hub API: Free tier

### **Development Tools:**
- Google Cloud SDK and CLI tools
- Python for MCP server implementation
- GitHub for version control and CI/CD integration
- Postman or similar for API testing

## Final Deliverables

1. **Production MCP Server** - Deployed on Google Cloud Run with full functionality and monitoring
2. **Technical Report** - Covering architecture, API integrations, findings and evaluation
3. **Live Demonstration** - Showcase of key features using production cloud deployment
4. **Source Code Repository** - Clean, documented, and reproducible code with automated deployment pipeline
5. **Reflection** - Written reflection in Week 10 summarizing lessons learned
