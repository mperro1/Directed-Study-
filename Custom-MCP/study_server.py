#!/usr/bin/env python3
"""
Simple Study Helper MCP Server - Generate study questions and find learning resources
"""
import sys
import logging
import random
from mcp.server.fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("study-server")

# Initialize MCP server
mcp = FastMCP("study")

# === KNOWLEDGE DATABASE ===

MATH_QUESTIONS = {
    "easy": [
        ("What is 7 + 8?", ["15", "16", "14", "17"], 0, "Add the two numbers: 7 + 8 = 15"),
        ("What is 12 - 5?", ["7", "8", "6", "9"], 0, "Subtract: 12 - 5 = 7"),
        ("What is 3 x 4?", ["12", "7", "15", "10"], 0, "Multiply: 3 x 4 = 12"),
        ("What is 20 / 4?", ["5", "4", "6", "8"], 0, "Divide: 20 / 4 = 5"),
        ("What is 50% of 100?", ["50", "25", "75", "100"], 0, "50% means half, so 100 / 2 = 50"),
    ],
    "medium": [
        ("What is 15 x 12?", ["180", "170", "190", "200"], 0, "15 x 12 = (15 x 10) + (15 x 2) = 150 + 30 = 180"),
        ("What is 144 / 12?", ["12", "10", "14", "11"], 0, "144 / 12 = 12 (think: 12 x 12 = 144)"),
        ("What is 3^3 (3 cubed)?", ["27", "9", "18", "36"], 0, "3^3 = 3 x 3 x 3 = 27"),
        ("Solve: 2x + 5 = 15. What is x?", ["5", "10", "7", "8"], 0, "2x + 5 = 15, subtract 5: 2x = 10, divide by 2: x = 5"),
        ("What is the area of a rectangle 8cm x 5cm?", ["40 cm²", "13 cm²", "20 cm²", "25 cm²"], 0, "Area = length x width = 8 x 5 = 40 cm²"),
    ],
    "hard": [
        ("What is the quadratic formula?", ["x = (-b ± √(b²-4ac)) / 2a", "x = b² - 4ac", "x = -b / 2a", "x = √(b²-4ac)"], 0, "The quadratic formula solves ax² + bx + c = 0"),
        ("Solve: 3x² - 12x = 0", ["x = 0 or x = 4", "x = 4", "x = 0", "x = 12"], 0, "Factor: 3x(x - 4) = 0, so x = 0 or x = 4"),
        ("What is sin(30°)?", ["0.5 or 1/2", "0.707", "0.866", "1"], 0, "sin(30°) = 1/2 or 0.5 (common angle to memorize)"),
        ("If f(x) = 2x + 3, what is f(5)?", ["13", "10", "8", "15"], 0, "Substitute: f(5) = 2(5) + 3 = 10 + 3 = 13"),
        ("What is the derivative of x²?", ["2x", "x²", "x", "2x²"], 0, "Power rule: d/dx(x^n) = nx^(n-1), so d/dx(x²) = 2x"),
    ]
}

SCIENCE_QUESTIONS = {
    "easy": [
        ("What is H2O commonly known as?", ["Water", "Oxygen", "Hydrogen", "Carbon"], 0, "H2O is the chemical formula for water (2 hydrogen + 1 oxygen)"),
        ("What planet is closest to the Sun?", ["Mercury", "Venus", "Earth", "Mars"], 0, "Mercury is the first and closest planet to the Sun"),
        ("True or False: Plants make their own food through photosynthesis.", ["True", "False"], 0, "Plants use sunlight, water, and CO2 to create glucose (sugar) through photosynthesis"),
        ("What gas do humans breathe in?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], 0, "Humans breathe in oxygen (O2) and breathe out carbon dioxide (CO2)"),
        ("What is the center of an atom called?", ["Nucleus", "Electron", "Proton", "Neutron"], 0, "The nucleus is the dense center of an atom, containing protons and neutrons"),
    ],
    "medium": [
        ("What is the speed of light?", ["299,792 km/s", "150,000 km/s", "500,000 km/s", "100,000 km/s"], 0, "Speed of light is approximately 300,000 km/s or 186,000 miles/s"),
        ("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"], 0, "Mitochondria produce ATP (energy) for the cell through cellular respiration"),
        ("What is Newton's Second Law?", ["F = ma", "E = mc²", "F = G(m1m2)/r²", "V = IR"], 0, "Force equals mass times acceleration (F = ma)"),
        ("What is the pH of pure water?", ["7", "0", "14", "10"], 0, "Pure water is neutral with a pH of 7 (neither acidic nor basic)"),
        ("What are the three states of matter?", ["Solid, Liquid, Gas", "Hot, Cold, Warm", "Big, Medium, Small", "Fast, Slow, Still"], 0, "The three common states are solid, liquid, and gas (plasma is the 4th)"),
    ],
    "hard": [
        ("What is the first law of thermodynamics?", ["Energy cannot be created or destroyed", "Entropy always increases", "For every action there's a reaction", "Objects in motion stay in motion"], 0, "Energy conservation: energy can only be transferred or transformed, not created/destroyed"),
        ("What is DNA composed of?", ["Nucleotides", "Amino acids", "Lipids", "Carbohydrates"], 0, "DNA is made of nucleotides, each with a sugar, phosphate, and nitrogenous base"),
        ("What is Avogadro's number?", ["6.022 x 10²³", "3.14", "9.8", "1.6 x 10⁻¹⁹"], 0, "Avogadro's number is the number of particles in one mole of a substance"),
        ("What is the process of cell division called?", ["Mitosis and Meiosis", "Photosynthesis", "Respiration", "Diffusion"], 0, "Mitosis creates identical cells; meiosis creates sex cells with half the chromosomes"),
        ("What is Ohm's Law?", ["V = IR", "F = ma", "E = mc²", "P = IV"], 0, "Voltage equals current times resistance (V = IR)"),
    ]
}

HISTORY_QUESTIONS = {
    "easy": [
        ("In what year did World War II end?", ["1945", "1918", "1939", "1950"], 0, "WWII ended in 1945 with Germany's surrender in May and Japan's in September"),
        ("Who was the first President of the United States?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], 0, "George Washington served 1789-1797 as the first U.S. President"),
        ("What year did Columbus reach the Americas?", ["1492", "1776", "1620", "1500"], 0, "Columbus reached the Americas in 1492 (remember: In 1492, Columbus sailed the ocean blue)"),
        ("What ancient civilization built the pyramids?", ["Egyptians", "Romans", "Greeks", "Aztecs"], 0, "Ancient Egyptians built the pyramids as tombs for pharaohs around 2500 BCE"),
        ("True or False: The Great Wall of China was built to keep out invaders.", ["True", "False"], 0, "The Great Wall was built primarily for defense against northern invasions"),
    ],
    "medium": [
        ("What year did the American Civil War start?", ["1861", "1776", "1812", "1865"], 0, "The Civil War began in 1861 and ended in 1865"),
        ("Who wrote the Declaration of Independence?", ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams"], 0, "Thomas Jefferson was the primary author of the Declaration in 1776"),
        ("What was the Renaissance?", ["Cultural rebirth in Europe", "A war", "A plague", "A religion"], 0, "The Renaissance (14th-17th century) was a period of cultural and artistic revival"),
        ("What empire did Julius Caesar lead?", ["Roman Empire", "Greek Empire", "Persian Empire", "Ottoman Empire"], 0, "Julius Caesar was a Roman general and statesman in the 1st century BCE"),
        ("What was the Cold War?", ["Political tension between US and USSR", "A literal cold war", "WWI", "WWII"], 0, "The Cold War (1947-1991) was ideological tension without direct military conflict"),
    ],
    "hard": [
        ("What year did the French Revolution begin?", ["1789", "1776", "1815", "1804"], 0, "The French Revolution started in 1789 with the storming of the Bastille"),
        ("Who was the first person to circumnavigate the globe?", ["Ferdinand Magellan's crew", "Christopher Columbus", "Vasco da Gama", "Marco Polo"], 0, "Magellan's expedition (1519-1522) first circumnavigated; Magellan died during the journey"),
        ("What was the Magna Carta?", ["Document limiting king's power", "A trade agreement", "A religious text", "A war treaty"], 0, "The Magna Carta (1215) established that the king was subject to law"),
        ("What caused the fall of the Roman Empire?", ["Multiple factors (economic, military, political)", "One battle", "Natural disaster", "Disease only"], 0, "The fall was gradual due to economic troubles, invasions, and internal decay"),
        ("What was the Treaty of Versailles?", ["Peace treaty ending WWI", "Treaty ending WWII", "Trade agreement", "Military alliance"], 0, "The Treaty of Versailles (1919) officially ended WWI and imposed harsh terms on Germany"),
    ]
}

ENGLISH_QUESTIONS = {
    "easy": [
        ("What is a noun?", ["A person, place, or thing", "An action word", "A describing word", "A connecting word"], 0, "Nouns name people (teacher), places (school), or things (book)"),
        ("What is a verb?", ["An action word", "A person, place, or thing", "A describing word", "A connecting word"], 0, "Verbs show action (run, jump) or state of being (is, are)"),
        ("Which is the correct spelling?", ["Definitely", "Definately", "Definetly", "Definitly"], 0, "Definitely is spelled with 'finite' in the middle (de-finite-ly)"),
        ("What is an adjective?", ["A describing word", "An action word", "A person, place, or thing", "A connecting word"], 0, "Adjectives describe nouns (big dog, happy child, red car)"),
        ("Complete: She _____ to the store yesterday.", ["went", "go", "goes", "going"], 0, "Past tense of 'go' is 'went' (yesterday indicates past tense)"),
    ],
    "medium": [
        ("What is a metaphor?", ["Comparison without like/as", "Comparison with like/as", "Exaggeration", "Sound words"], 0, "Metaphor: direct comparison (He is a lion). Simile uses like/as (He is like a lion)"),
        ("Which sentence is correct?", ["Their going to the park", "They're going to the park", "There going to the park"], 1, "They're = they are. Their = possession. There = location"),
        ("What is alliteration?", ["Repetition of initial sounds", "Repetition of vowels", "Rhyming words", "Exaggeration"], 0, "Alliteration: repeated consonant sounds at word beginnings (Peter Piper picked)"),
        ("What is the subject in: 'The cat chased the mouse'?", ["The cat", "chased", "the mouse", "The cat chased"], 0, "The subject is who/what does the action (the cat is doing the chasing)"),
        ("What is irony?", ["Opposite of expectation", "A comparison", "Repetition", "Rhyming"], 0, "Irony is when the opposite of what's expected happens or is said"),
    ],
    "hard": [
        ("What is a dangling modifier?", ["Modifier not clearly related to subject", "A comma error", "A spelling error", "A verb tense error"], 0, "Example: 'Walking to school, the bus passed me' - who was walking is unclear"),
        ("What is parallelism?", ["Similar grammatical structure", "Similar meaning", "Similar sound", "Similar length"], 0, "Parallelism uses similar structures (I like reading, writing, and hiking)"),
        ("What is the subjunctive mood?", ["Expressing wishes/hypotheticals", "Past tense", "Future tense", "Commands"], 0, "Subjunctive: 'If I were rich' (not 'was'), 'I suggest he go' (not 'goes')"),
        ("What is a gerund?", ["Verb ending in -ing used as noun", "Past tense verb", "Adjective", "Adverb"], 0, "Gerund: verb as noun (Swimming is fun, I enjoy reading)"),
        ("What is the Oxford comma?", ["Comma before 'and' in lists", "Comma after introduction", "Comma in dates", "Comma in addresses"], 0, "Oxford comma: 'red, white, and blue' (comma before 'and')"),
    ]
}

# ✨ NEW: Computer Science Questions
CS_QUESTIONS = {
    "easy": [
        ("What is a variable in programming?", ["A container for storing data", "A type of loop", "A function", "An error"], 0, "Variables store values that can be used and changed throughout your program (e.g., x = 5)"),
        ("What does HTML stand for?", ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"], 0, "HTML is the standard markup language for creating web pages"),
        ("What is a loop used for?", ["Repeating code multiple times", "Storing data", "Creating functions", "Fixing errors"], 0, "Loops execute code repeatedly, like a for loop or while loop"),
        ("True or False: Python uses indentation to define code blocks.", ["True", "False"], 0, "Python uses whitespace/indentation instead of braces {} to structure code"),
        ("What is binary?", ["Base-2 number system (0s and 1s)", "A programming language", "A type of variable", "Computer hardware"], 0, "Binary uses only 0 and 1 to represent all data in computers"),
    ],
    "medium": [
        ("What is the output of: print(5 == 5)?", ["True", "False", "5", "Error"], 0, "The == operator checks equality, 5 equals 5, so it returns True"),
        ("What is an array/list?", ["Collection of items in order", "A single value", "A function", "A loop"], 0, "Arrays/lists store multiple values in a single variable (e.g., [1, 2, 3, 4])"),
        ("What does API stand for?", ["Application Programming Interface", "Advanced Programming Integration", "Automated Program Instruction", "Applied Program Interface"], 0, "APIs allow different software applications to communicate with each other"),
        ("What is the purpose of a function?", ["Reusable block of code", "Store data", "Create loops", "Define variables"], 0, "Functions group code into reusable blocks that can be called multiple times"),
        ("What is Git used for?", ["Version control", "Writing code", "Running programs", "Designing websites"], 0, "Git tracks changes in code and enables collaboration among developers"),
    ],
    "hard": [
        ("What is Big O notation?", ["Describes algorithm efficiency", "A programming language", "A data structure", "A debugging tool"], 0, "Big O describes time/space complexity (e.g., O(n), O(log n), O(n²))"),
        ("What is recursion?", ["Function that calls itself", "A type of loop", "An error handling method", "A variable type"], 0, "Recursion is when a function calls itself to solve problems (e.g., calculating factorials)"),
        ("What is the difference between stack and heap memory?", ["Stack is for local variables, heap for dynamic allocation", "Stack is slower than heap", "They are the same", "Stack is for objects only"], 0, "Stack: automatic, local scope, fast. Heap: manual, global scope, slower but flexible"),
        ("What is object-oriented programming (OOP)?", ["Programming using objects and classes", "Programming without functions", "Low-level programming", "Web development only"], 0, "OOP organizes code into objects with properties and methods (encapsulation, inheritance, polymorphism)"),
        ("What is time complexity of binary search?", ["O(log n)", "O(n)", "O(n²)", "O(1)"], 0, "Binary search divides the search space in half each time, resulting in logarithmic time complexity"),
    ]
}

RESOURCES_DATABASE = {
    "math": {
        "videos": [
            "Khan Academy Math - Comprehensive free video courses for all levels",
            "3Blue1Brown (YouTube) - Visual, intuitive math explanations",
            "PatrickJMT (YouTube) - Clear step-by-step math tutorials",
            "Professor Leonard (YouTube) - Full college-level math lectures",
        ],
        "practice": [
            "Khan Academy Practice - Adaptive practice problems with hints",
            "Paul's Online Math Notes - Practice problems with solutions",
            "IXL Math - Comprehensive practice (free with limits)",
            "Mathway - Problem solver showing step-by-step work",
        ],
        "articles": [
            "BetterExplained - Intuitive math explanations",
            "Math is Fun - Clear explanations with diagrams",
            "Purplemath - Practical algebra help",
            "Wikipedia Math Portal - In-depth mathematical concepts",
        ],
        "tips": "Practice daily, show your work step-by-step, understand WHY formulas work (not just memorizing), draw diagrams for word problems, check answers by working backwards"
    },
    "science": {
        "videos": [
            "Khan Academy Science - Biology, Chemistry, Physics courses",
            "CrashCourse (YouTube) - Fast-paced, engaging science videos",
            "Bozeman Science (YouTube) - AP Biology and Chemistry",
            "MIT OpenCourseWare - Free college-level lectures",
        ],
        "practice": [
            "Khan Academy Science Practice - Interactive problems",
            "PhET Simulations - Interactive science simulations",
            "Quizlet - Flashcards for science terms and concepts",
            "Biology Corner - Worksheets and activities",
        ],
        "articles": [
            "Wikipedia Science Portal - Comprehensive articles",
            "HyperPhysics - Physics concepts with diagrams",
            "Biology Online - Life science articles",
            "Science Daily - Current science news and research",
        ],
        "tips": "Connect concepts to real life, draw diagrams and label them, use mnemonic devices for memorization, do lab experiments if possible, explain concepts out loud to test understanding"
    },
    "history": {
        "videos": [
            "CrashCourse History (YouTube) - Engaging historical overviews",
            "History.com Videos - Documentary clips and series",
            "Extra History (YouTube) - Animated history stories",
            "Epic History TV (YouTube) - Detailed historical documentaries",
        ],
        "practice": [
            "Quizlet History Sets - Flashcards for dates and events",
            "Khan Academy History - Practice questions and quizzes",
            "Sporcle History Quizzes - Fun trivia-style practice",
            "History.com Quizzes - Test your knowledge",
        ],
        "articles": [
            "Wikipedia History Portal - Detailed historical articles",
            "History.com Articles - Well-researched topics",
            "Britannica Online - Encyclopedia entries",
            "National Geographic History - Historical articles with photos",
        ],
        "tips": "Create timelines to visualize chronology, connect events to their causes and effects, make flashcards for important dates, relate history to current events, use memory palaces for complex information"
    },
    "english": {
        "videos": [
            "Khan Academy Grammar - Comprehensive grammar lessons",
            "CrashCourse Literature (YouTube) - Book analysis and themes",
            "The Great Courses - Literature and writing lectures",
            "TED-Ed English Lessons - Animated grammar and literature",
        ],
        "practice": [
            "Grammarly - Writing feedback and corrections",
            "Purdue OWL - Writing exercises and examples",
            "Grammar Monster - Interactive grammar quizzes",
            "NoRedInk - Adaptive grammar practice",
        ],
        "articles": [
            "Purdue Online Writing Lab (OWL) - Comprehensive writing guide",
            "Grammar Girl - Quick grammar tips",
            "SparkNotes - Literature guides and analysis",
            "Literary Devices - Explanations with examples",
        ],
        "tips": "Read daily for vocabulary and style, practice writing regularly, read your work aloud to catch errors, keep a vocabulary journal, analyze how authors structure their writing"
    },
    # ✨ NEW: Computer Science Resources
    "cs": {
        "videos": [
            "freeCodeCamp (YouTube) - Full courses on web dev, Python, algorithms",
            "CS50 by Harvard - Introduction to Computer Science (free)",
            "Traversy Media (YouTube) - Modern web development tutorials",
            "The Net Ninja (YouTube) - JavaScript, React, and more",
            "Programming with Mosh (YouTube) - Clean, professional tutorials",
        ],
        "practice": [
            "LeetCode - Algorithm and data structure problems",
            "HackerRank - Coding challenges and competitions",
            "Codewars - Gamified coding practice",
            "Exercism - Practice with mentor feedback",
            "CodeSignal - Interview prep and assessments",
        ],
        "articles": [
            "MDN Web Docs - Comprehensive web development documentation",
            "GeeksforGeeks - Algorithms, data structures, interview prep",
            "Real Python - Python tutorials and guides",
            "Dev.to - Community articles on all CS topics",
            "Stack Overflow - Q&A for specific coding problems",
        ],
        "tips": "Code every day (consistency over quantity), build projects to apply knowledge, read and understand others' code, debug systematically using print statements or debuggers, comment your code to explain your thinking, break problems into smaller pieces"
    },
    "general": {
        "videos": [
            "Khan Academy - Free courses in all subjects",
            "CrashCourse (YouTube) - Fast-paced educational content",
            "TED-Ed - Animated educational videos",
            "MIT OpenCourseWare - Free college-level courses",
        ],
        "practice": [
            "Quizlet - Flashcards for any subject",
            "Khan Academy - Practice in all subjects",
            "Coursera - Free online courses (audit option)",
            "Anki - Spaced repetition flashcard app",
        ],
        "articles": [
            "Wikipedia - Comprehensive encyclopedia",
            "Simple Wikipedia - Easier-to-understand articles",
            "BBC Bitesize - Educational content for all ages",
            "Britannica Online - Reliable encyclopedia",
        ],
        "tips": "Space out study sessions (don't cram), teach concepts to others to reinforce learning, take breaks every 25-30 minutes, practice active recall instead of passive reading, get enough sleep for memory consolidation"
    }
}

# === UTILITY FUNCTIONS ===

def get_questions_for_subject(subject, difficulty, count):
    """Get questions based on subject and difficulty"""
    subject_lower = subject.lower()
    
    # Map subject to question database
    if "math" in subject_lower or "algebra" in subject_lower or "geometry" in subject_lower or "calculus" in subject_lower:
        question_bank = MATH_QUESTIONS
    elif "science" in subject_lower or "biology" in subject_lower or "chemistry" in subject_lower or "physics" in subject_lower:
        question_bank = SCIENCE_QUESTIONS
    elif "history" in subject_lower or "social" in subject_lower:
        question_bank = HISTORY_QUESTIONS
    elif "english" in subject_lower or "grammar" in subject_lower or "writing" in subject_lower or "literature" in subject_lower:
        question_bank = ENGLISH_QUESTIONS
    # ✨ NEW: Computer Science topic detection
    elif ("computer" in subject_lower or "programming" in subject_lower or "coding" in subject_lower or 
          "cs" in subject_lower or "algorithm" in subject_lower or "data structure" in subject_lower or
          "python" in subject_lower or "javascript" in subject_lower or "java" in subject_lower or
          "software" in subject_lower or "web dev" in subject_lower):
        question_bank = CS_QUESTIONS
    else:
        return None
    
    # Get questions for difficulty level
    if difficulty in question_bank:
        available_questions = question_bank[difficulty]
        selected = random.sample(available_questions, min(count, len(available_questions)))
        return selected
    
    return None

def format_question(index, q_data, show_answer=True):
    """Format a single question nicely"""
    question, choices, correct_idx, explanation = q_data
    
    result = f"\nQuestion {index}:\n{question}\n"
    
    if len(choices) == 2:
        # True/False question
        result += f"A) {choices[0]}\nB) {choices[1]}\n"
    else:
        # Multiple choice
        for i, choice in enumerate(choices):
            result += f"{chr(65+i)}) {choice}\n"
    
    if show_answer:
        correct_letter = chr(65 + correct_idx)
        result += f"\nAnswer: {correct_letter}) {choices[correct_idx]}\n"
        result += f"Explanation: {explanation}\n"
    
    return result

def get_resources_for_subject(subject, resource_type):
    """Get learning resources for a subject"""
    subject_lower = subject.lower()
    
    # Map subject to resource database
    if "math" in subject_lower or "algebra" in subject_lower or "geometry" in subject_lower or "calculus" in subject_lower:
        resources = RESOURCES_DATABASE["math"]
    elif "science" in subject_lower or "biology" in subject_lower or "chemistry" in subject_lower or "physics" in subject_lower:
        resources = RESOURCES_DATABASE["science"]
    elif "history" in subject_lower or "social" in subject_lower:
        resources = RESOURCES_DATABASE["history"]
    elif "english" in subject_lower or "grammar" in subject_lower or "writing" in subject_lower or "literature" in subject_lower:
        resources = RESOURCES_DATABASE["english"]
    # ✨ NEW: Computer Science resource mapping
    elif ("computer" in subject_lower or "programming" in subject_lower or "coding" in subject_lower or 
          "cs" in subject_lower or "algorithm" in subject_lower or "data structure" in subject_lower or
          "python" in subject_lower or "javascript" in subject_lower or "java" in subject_lower or
          "software" in subject_lower or "web dev" in subject_lower):
        resources = RESOURCES_DATABASE["cs"]
    else:
        resources = RESOURCES_DATABASE["general"]
    
    return resources

# === MCP TOOLS ===

@mcp.tool()
async def generate_study_questions(topic: str = "", difficulty: str = "medium", count: str = "5") -> str:
    """Generate practice questions for a topic with answers and explanations to help you study."""
    logger.info(f"Generating questions for {topic} at {difficulty} level")
    
    if not topic.strip():
        return "Error: Please specify a topic (e.g., math, science, history, english, computer science)"
    
    # Validate difficulty
    difficulty_lower = difficulty.strip().lower()
    if difficulty_lower not in ["easy", "medium", "hard"]:
        difficulty_lower = "medium"
    
    # Validate count
    try:
        num_questions = int(count) if count.strip() else 5
        if num_questions < 1 or num_questions > 10:
            num_questions = 5
    except ValueError:
        num_questions = 5
    
    try:
        # Get questions
        questions = get_questions_for_subject(topic, difficulty_lower, num_questions)
        
        if not questions:
            return f"Error: Could not generate questions for '{topic}'. Try: math, science, history, english, or computer science"
        
        # Format output
        result = f"STUDY QUESTIONS - {topic.upper()}\n"
        result += f"Difficulty: {difficulty_lower.capitalize()}\n"
        result += f"{'='*60}\n"
        
        for i, q_data in enumerate(questions, 1):
            result += format_question(i, q_data, show_answer=True)
        
        result += f"\n{'='*60}\n"
        result += f"Study Tips:\n"
        result += "- Cover the answers and try to solve each question first\n"
        result += "- Review the explanations carefully\n"
        result += "- Practice similar problems to reinforce learning\n"
        result += "- If you get one wrong, understand why before moving on\n"
        
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

@mcp.tool()
async def find_study_resources(topic: str = "", resource_type: str = "all") -> str:
    """Find learning resources and study strategies for any topic including videos, articles, and practice sites."""
    logger.info(f"Finding resources for {topic}, type: {resource_type}")
    
    if not topic.strip():
        return "Error: Please specify a topic (e.g., math, science, history, english, computer science)"
    
    # Validate resource type
    resource_type_lower = resource_type.strip().lower()
    valid_types = ["videos", "articles", "practice", "books", "all"]
    if resource_type_lower not in valid_types:
        resource_type_lower = "all"
    
    try:
        # Get resources
        resources = get_resources_for_subject(topic, resource_type_lower)
        
        # Format output
        result = f"LEARNING RESOURCES - {topic.upper()}\n"
        result += f"{'='*60}\n\n"
        
        if resource_type_lower == "all" or resource_type_lower == "videos":
            result += "VIDEO RESOURCES:\n"
            for video in resources["videos"]:
                result += f"  - {video}\n"
            result += "\n"
        
        if resource_type_lower == "all" or resource_type_lower == "practice":
            result += "PRACTICE SITES:\n"
            for practice in resources["practice"]:
                result += f"  - {practice}\n"
            result += "\n"
        
        if resource_type_lower == "all" or resource_type_lower == "articles":
            result += "ARTICLES & REFERENCES:\n"
            for article in resources["articles"]:
                result += f"  - {article}\n"
            result += "\n"
        
        if resource_type_lower == "all":
            result += f"STUDY TIPS FOR {topic.upper()}:\n"
            result += f"{resources['tips']}\n\n"
        
        result += f"{'='*60}\n"
        result += "GENERAL STUDY STRATEGIES:\n"
        result += "1. Set specific goals for each study session\n"
        result += "2. Eliminate distractions (phone, TV, etc.)\n"
        result += "3. Use active learning (practice, not just reading)\n"
        result += "4. Take regular breaks (Pomodoro technique: 25 min work, 5 min break)\n"
        result += "5. Review material multiple times over several days\n"
        result += "6. Test yourself frequently to reinforce memory\n"
        result += "7. Study in a dedicated, comfortable space\n"
        result += "8. Get enough sleep - it helps memory consolidation\n"
        
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

# === SERVER STARTUP ===
if __name__ == "__main__":
    logger.info("Starting Study Helper MCP server...")
    
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)