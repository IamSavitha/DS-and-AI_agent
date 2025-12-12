# Quick Reference Guide - HW11

## 🎯 Core Concepts

### Chain-of-Debate Pattern
```
Question → [Agent1, Agent2, Agent3] → Synthesis Agent → Recommendation
```

### CAP Theorem (Our System: AP)
- ✅ **Availability**: System always responds
- ✅ **Partition Tolerance**: Agents work independently  
- ⚠️ **Consistency**: Eventual (through synthesis)

## 📁 File Structure

```
Homework11/
├── career_counseling_agent.py  # Main implementation
├── requirements.txt            # Dependencies
├── README.md                   # Quick start guide
├── CONCEPTS_EXPLANATION.md     # Detailed explanations
└── QUICK_REFERENCE.md          # This file
```

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key
export OPENAI_API_KEY='your-key'

# 3. Run
python career_counseling_agent.py
```

## 🔑 Key Classes

| Class | Purpose |
|-------|---------|
| `CareerPerspectiveAgent` | Base class for specialized agents |
| `SynthesisAgent` | Combines multiple perspectives |
| `ChainOfDebateOrchestrator` | Manages the debate process |

## 🎭 Agent Perspectives

1. **Technical Agent**: Skills, technologies, technical paths
2. **Business Agent**: Market demand, salary, ROI
3. **Lifestyle Agent**: Work-life balance, fulfillment
4. **Synthesis Agent**: Combines all perspectives

## 📊 Workflow

```
1. User asks career question
2. Orchestrator distributes to 3 agents (parallel)
3. Each agent provides perspective
4. Synthesis agent combines perspectives
5. Unified recommendation returned
```

## 💡 Key Design Decisions

- **Parallel Processing**: Agents work simultaneously for speed
- **Independent Agents**: No communication ensures diverse perspectives
- **Separate Synthesis**: Objective combination of perspectives
- **AP System**: Prioritize availability and partition tolerance

## 🔍 Code Highlights

### Creating an Agent
```python
agent = CareerPerspectiveAgent(
    agent_id="tech-agent",
    perspective="Technical",
    specialty="Software Engineering"
)
```

### Processing a Question
```python
orchestrator = ChainOfDebateOrchestrator()
result = orchestrator.process_question(
    "Should I learn Python?",
    user_context={"background": "CS student"}
)
```

## 📈 Performance

- **Per Agent**: 2-5 seconds
- **Synthesis**: 3-6 seconds
- **Total**: 8-15 seconds

## 🎓 Learning Outcomes

After completing this homework, you understand:
- ✅ Chain-of-Debate pattern implementation
- ✅ Multi-agent system architecture
- ✅ CAP theorem trade-offs
- ✅ Agent prompt engineering
- ✅ Synthesis and consensus building
