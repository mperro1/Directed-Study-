# Study Helper MCP Server - Implementation Guide 
This is the output README from the prompt. 

## Overview
This MCP server helps students study by generating practice questions and suggesting learning resources. It runs entirely offline with hardcoded educational content - no external APIs or keys required.

## Architecture Decisions

### Why Hardcoded Content?
We chose to hardcode questions and resources rather than use external APIs for several reasons:
1. **No API dependencies** - Works offline, no rate limits, no costs
2. **Controlled quality** - Every question is vetted for accuracy
3. **Instant responses** - No network latency
4. **Privacy** - No user data sent to external services
5. **Reliability** - No downtime or API changes

### Knowledge Database Structure
Questions are organized by:
- **Subject** (Math, Science, History, English)
- **Difficulty** (Easy, Medium, Hard)
- **Format** (Multiple choice, True/False)

Each question includes:
- Question text
- Answer choices
- Correct answer index
- Detailed explanation

### Resource Database Structure
Resources are categorized by:
- **Videos** - YouTube channels, Khan Academy
- **Practice** - Interactive websites and problem sets
- **Articles** - Reference materials and guides
- **Tips** - Subject-specific study strategies

## Tool Implementations

### generate_study_questions
**Purpose**: Generate practice questions for self-testing

**Parameters**:
- `topic` - Subject to study (math, science, history, english)
- `difficulty` - Level (easy, medium, hard)
- `count` - Number of questions (1-10)

**Process**:
1. Validates topic and maps to question database
2. Validates difficulty level (defaults to medium)
3. Validates count (defaults to 5, max 10)
4. Randomly selects questions from appropriate database
5. Formats with answers and explanations
6. Adds study tips at the end

**Output Format**:
- Clear section headers
- Numbered questions with lettered choices
- Answers with explanations
- Study tips for effective practice

### find_study_resources
**Purpose**: Suggest learning resources and study strategies

**Parameters**:
- `topic` - Subject to learn
- `resource_type` - Type of resource (videos, articles, practice, all)

**Process**:
1. Validates topic and maps to resource database
2. Validates resource type (defaults to all)
3. Retrieves appropriate resources
4. Formats by category
5. Includes subject-specific and general study tips

**Output Format**:
- Categorized resource lists
- Brief descriptions of each resource
- Study tips specific to the subject
- General study strategies

## Question Quality Guidelines

### Easy Questions
- Test basic recall and recognition
- Simple calculations and definitions
- One-step problems
- Common knowledge
- Example: "What is 7 + 8?"

### Medium Questions
- Require understanding and application
- Multi-step problems
- Connections between concepts
- Less common knowledge
- Example: "Solve: 2x + 5 = 15"

### Hard Questions
- Require analysis and synthesis
- Complex calculations
- Advanced concepts
- Application to new situations
- Example: "What is the derivative of x²?"

## Resource Selection Criteria

All recommended resources must be:
1. **Free** - No paywalls or subscriptions required
2. **Reputable** - From known educational sources
3. **Current** - Active and maintained
4. **Accessible** - Easy to find and use
5. **Quality** - Clear, accurate, well-explained

## Subject Coverage

### Math
- Arithmetic (addition, subtraction, multiplication, division)
- Algebra (equations, variables, functions)
- Geometry (shapes, area, volume)
- Calculus (derivatives, integrals)
- Focus on procedural understanding with explanations

### Science
- Biology (cells, genetics, ecosystems)
- Chemistry (atoms, molecules, reactions)
- Physics (motion, energy, forces)
- Focus on conceptual understanding and real-world applications

### History
- Important dates and events
- Key historical figures
- Causes and effects
- Historical periods and movements
- Focus on context and connections

### English
- Grammar rules and usage
- Vocabulary and spelling
- Literary devices and analysis
- Writing techniques
- Focus on practical application

## Usage Guidelines for Claude

When helping students with this server:

1. **For question generation**:
   - Suggest appropriate difficulty based on student's level
   - Recommend starting with easy and progressing to hard
   - Encourage multiple practice sessions over cramming

2. **For resource finding**:
   - Match resources to learning style (visual → videos, hands-on → practice)
   - Suggest multiple resource types for comprehensive learning
   - Emphasize active learning over passive consumption

3. **Study strategies**:
   - Spaced repetition is more effective than massed practice
   - Active recall (testing) beats passive review (re-reading)
   - Interleaving topics improves long-term retention
   - Sleep is crucial for memory consolidation

## Expansion Opportunities

### Additional Subjects
Potential additions following the same pattern:
- **Languages** (Spanish, French, vocabulary, grammar)
- **Computer Science** (programming, algorithms, data structures)
- **Art** (art history, techniques, famous works)
- **Music** (theory, history, instruments)
- **Geography** (countries, capitals, physical features)

### Additional Question Types
- Fill-in-the-blank
- Matching
- Ordering/sequencing
- Short answer
- Essay prompts

### Additional Features
- Progress tracking (would require storage)
- Adaptive difficulty (adjusts based on performance)
- Timed quizzes
- Study schedules
- Flashcard generation

## Testing Checklist

Before deploying:
- [ ] Test each subject at each difficulty level
- [ ] Verify all answers are correct
- [ ] Check all explanations for clarity
- [ ] Test with invalid inputs
- [ ] Verify resource links are active
- [ ] Confirm no offensive or inappropriate content
- [ ] Test with edge cases (empty strings, invalid counts)

## Educational Best Practices

### Question Design
- Clear, unambiguous wording
- Plausible wrong answers (distractors)
- One clearly correct answer
- Explanations that teach, not just confirm

### Resource Curation
- Mix of different media types
- Appropriate for self-directed learning
- Scaffolded from simple to complex
- Inclusive and accessible

### Study Tips
- Evidence-based learning strategies
- Practical and actionable advice
- Applicable across subjects
- Encourages metacognition

## Support Resources

- Khan Academy: https://www.khanacademy.org/
- Quizlet: https://quizlet.com/
- Purdue OWL: https://owl.purdue.edu/
- CrashCourse: https://www.youtube.com/user/crashcourse

## Future Enhancements

Potential improvements:
1. More questions per subject (currently 5 per difficulty level)
2. More subjects (languages, computer science, etc.)
3. Question analytics (most frequently requested topics)
4. Custom question uploads
5. Exam preparation modes (SAT, ACT, AP)
6. Study group features
7. Integration with calendar for study scheduling
```

# Section 2: Installation Instructions for the User

## Step 1: Save the Files
```bash
# Create project directory
mkdir study-mcp-server
cd study-mcp-server

# Save all 5 files in this directory:
# - Dockerfile
# - requirements.txt
# - study_server.py
# - readme.txt
# - CLAUDE.md
```

## Step 2: Build Docker Image
```bash
docker build -t study-mcp-server .
```

## Step 3: Skip Secrets Setup
This server does not require any API keys or secrets! Skip to Step 4.

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
  study:
    description: "Generate study questions and find learning resources for any subject"
    title: "Study Helper"
    type: server
    dateAdded: "2025-12-06T00:00:00Z"
    image: study-mcp-server:latest
    ref: ""
    readme: ""
    toolsUrl: ""
    source: ""
    upstream: ""
    icon: ""
    tools:
      - name: generate_study_questions
      - name: find_study_resources
    metadata:
      category: productivity
      tags:
        - education
        - study
        - learning
        - questions
        - practice
      license: MIT
      owner: local
```

## Step 5: Update Registry
```bash
# Edit registry file
nano ~/.docker/mcp/registry.yaml
```

Add this entry under the existing `registry:` key:
```yaml
registry:
  study:
    ref: ""
```

**IMPORTANT**: The entry must be under the `registry:` key, not at the root level.

## Step 6: Configure Claude Desktop
Your config should already have the MCP gateway configured. No changes needed if you already have the gateway setup!

If not, find your Claude Desktop config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

Ensure it has the gateway configured with custom.yaml catalog:
```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": [
        "mcp",
        "gateway",
        "run"
      ],
      "env": {
        "LOCALAPPDATA": "C:\\Users\\Marcela\\AppData\\Local",
        "ProgramData": "C:\\ProgramData",
        "ProgramFiles": "C:\\Program Files"
      }
    }
  }
}
```

## Step 7: Restart Claude Desktop

1. Quit Claude Desktop completely
2. Start Claude Desktop again
3. Your new study tools should appear!

## Step 8: Test Your Server
```bash
# Verify it appears in the list
docker mcp server list

# Test directly (optional)
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | python3 study_server.py
```

## Example Usage

Once set up, you can ask Claude things like:

- "Generate 5 easy math questions to practice"
- "Create 10 medium science questions about biology"
- "Give me hard history questions for test prep"
- "Find study resources for learning algebra"
- "Show me practice sites for chemistry"
- "What are good video resources for English?"

The server will generate questions with answers and explanations, or suggest curated learning resources!
