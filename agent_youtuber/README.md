# YouTube Content Generation Assistant

A Python-based AI project that helps generate trending YouTube content ideas and teaching materials using CrewAI and LLM technologies.

## 🌟 Features

- Automatically generates trending YouTube video topics
- Creates detailed teaching content for the generated topics
- Uses AI agents to simulate expert YouTube content creators
- Implements a flow-based architecture for sequential content generation

## 🛠️ Technology Stack

- Python 3.13+
- CrewAI
- LiteLLM
- Gemini 1.5 Flash
- UV Package Manager

## 📋 Prerequisites

- Python 3.13 or higher
- UV Package Manager
- Gemini API key (for topic generation)

## 🚀 Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd project
```

2. Create and activate a virtual environment using UV:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Set up your environment variables:
Create a `.env` file in the root directory and add your API key:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 💻 Usage

Run the project using UV:
```bash
uv run panaflow
```

The application will:
1. Generate a trending topic for a YouTube video
2. Create detailed teaching content about the topic
3. Output the results in a structured format

## 🏗️ Project Structure

```
project/
├── src/
│   └── project/
│       ├── crews/
│       │   └── teaching_crew/
│       │       └── teaching_crew.py
│       └── men.py
├── .env
├── pyproject.toml
└── README.md
```

## 🔧 Components

### PanaFlow
- Main flow controller that orchestrates the content generation process
- Handles topic generation using Gemini AI
- Manages state and workflow between different stages

### TeachingCrew
- Implements the AI teaching agent
- Configures and manages the content creation process
- Handles task creation and execution

## 📝 Example Output

```
STEP 1: Generated topic: "The Rise of AI Content Creation"
STEP 2: Generating content
Generated content: [Detailed teaching content about AI Content Creation]
```

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- Make sure to keep your API keys secure and never commit them to version control
- The project requires Python 3.13+ due to specific dependency requirements
- Use UV package manager for best compatibility and performance
