# HW11: Career Counseling Agent with Chain-of-Debate Pattern

## Overview

This homework implements a **Career Counseling Agent** using the **Chain-of-Debate** pattern, demonstrating advanced multi-agent AI concepts and distributed systems principles.

## Concepts Covered

### 1. Chain-of-Debate Pattern
- **Definition**: A multi-agent pattern where multiple agents with different perspectives independently analyze a question, then a synthesis agent combines their viewpoints into a unified recommendation.
- **Benefits**: 
  - Comprehensive analysis from multiple angles
  - Reduced bias from single-agent systems
  - Better decision-making through diverse perspectives

### 2. Multi-Agent Architecture
- **Specialized Agents**: Each agent has a distinct perspective (Technical, Business, Lifestyle)
- **Parallel Processing**: Agents work independently and concurrently
- **Synthesis**: Final agent combines all perspectives

### 3. CAP Theorem
- **Consistency**: Agents may have slightly different information (eventual consistency)
- **Availability**: System remains operational even if one agent fails
- **Partition Tolerance**: Agents can work in isolation
- **Our Choice**: AP system (Availability + Partition Tolerance)

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

```bash
python career_counseling_agent.py
```

## Architecture

```
User Question
    │
    ▼
Chain-of-Debate Orchestrator
    │
    ├──► Technical Agent (Perspective 1)
    ├──► Business Agent (Perspective 2)
    └──► Lifestyle Agent (Perspective 3)
    │
    ▼
Synthesis Agent (Combines all perspectives)
    │
    ▼
Unified Recommendation
```

## Key Components

1. **CareerPerspectiveAgent**: Base class for specialized agents
2. **SynthesisAgent**: Combines multiple perspectives
3. **ChainOfDebateOrchestrator**: Manages the debate process

## Example Output

The system processes career questions through multiple agents and provides:
- Individual perspectives from each agent
- Synthesized recommendation
- Timing metrics
- Structured JSON output
