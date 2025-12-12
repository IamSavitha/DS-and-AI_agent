"""
HW11: Career Counseling Agent with Chain-of-Debate Pattern
==========================================================

This implementation demonstrates:
1. Chain-of-Debate Pattern: Multiple agents with different perspectives debate a career question
2. CAP Theorem Concepts: How distributed systems handle Consistency, Availability, and Partition tolerance
3. Multi-Agent Collaboration: Agents work together to provide comprehensive career advice

CONCEPTS COVERED:
- Chain-of-Debate: Multiple perspectives → Debate → Synthesis
- Agent-based Architecture: Specialized agents with distinct viewpoints
- Consensus Building: Combining different opinions into actionable advice
- CAP Theorem Trade-offs: Consistency vs Availability in distributed agent systems
"""

import os
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# ============================================================================
# CONCEPT 1: AGENT DEFINITIONS - Specialized Career Counseling Agents
# ============================================================================

class CareerPerspectiveAgent:
    """
    Base class for career counseling agents with different perspectives.
    
    CONCEPT: Each agent represents a different viewpoint in the debate:
    - Technical Agent: Focuses on skills, technologies, and technical career paths
    - Business Agent: Focuses on market demand, salary, and business value
    - Lifestyle Agent: Focuses on work-life balance, personal fulfillment, and well-being
    
    This follows the Chain-of-Debate pattern where multiple agents provide
    different perspectives before synthesis.
    """
    
    def __init__(self, agent_id: str, perspective: str, specialty: str):
        """
        Initialize a career perspective agent.
        
        Args:
            agent_id: Unique identifier for the agent
            perspective: The perspective this agent represents (e.g., "Technical", "Business")
            specialty: Specific area of expertise
        """
        self.agent_id = agent_id
        self.perspective = perspective
        self.specialty = specialty
        
        # Initialize LLM for this agent
        # CONCEPT: Each agent uses the same LLM but with different system prompts
        # This creates distinct "personalities" and perspectives
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",  # Using gpt-4o-mini for cost efficiency
            temperature=0.8,  # Higher temperature for more diverse perspectives
            api_key=api_key
        )
        
        # System prompt defines the agent's perspective and expertise
        # CONCEPT: The system prompt shapes how the agent interprets and responds
        # Different prompts = different perspectives in the debate
        self.system_prompt = self._create_system_prompt()
    
    def _create_system_prompt(self) -> str:
        """
        Create a system prompt that defines this agent's perspective.
        
        CONCEPT: System prompts are crucial in agent design - they define:
        - The agent's role and expertise
        - The agent's perspective and priorities
        - How the agent should structure responses
        
        This is where we encode the "personality" of each agent.
        """
        if self.perspective == "Technical":
            return f"""You are a Technical Career Counselor specializing in {self.specialty}.
Your perspective focuses on:
- Technical skills and competencies required
- Emerging technologies and trends
- Career progression in technical roles
- Certifications and learning paths
- Technical challenges and problem-solving

Provide detailed, technical advice with specific technologies, tools, and skills.
Be practical and focus on what's technically feasible and valuable."""
        
        elif self.perspective == "Business":
            return f"""You are a Business Career Counselor specializing in {self.specialty}.
Your perspective focuses on:
- Market demand and job opportunities
- Salary ranges and compensation trends
- Business value and ROI of career choices
- Industry trends and market dynamics
- Career growth potential and advancement paths

Provide business-focused advice with market data, salary insights, and career ROI.
Be realistic about market conditions and opportunities."""
        
        elif self.perspective == "Lifestyle":
            return f"""You are a Lifestyle Career Counselor specializing in {self.specialty}.
Your perspective focuses on:
- Work-life balance and personal well-being
- Job satisfaction and personal fulfillment
- Remote work opportunities and flexibility
- Stress levels and work environment
- Long-term happiness and career sustainability

Provide advice that considers personal happiness, work-life balance, and long-term well-being.
Be empathetic and consider the human side of career decisions."""
        
        else:
            return f"You are a Career Counselor with expertise in {self.specialty}."
    
    def provide_perspective(self, question: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Provide a perspective on a career question.
        
        CONCEPT: This method implements one "turn" in the chain-of-debate.
        Each agent independently analyzes the question from their perspective.
        
        Args:
            question: The career question to analyze
            context: Optional context (e.g., user background, previous responses)
        
        Returns:
            Dictionary containing the agent's perspective and reasoning
        """
        print(f"\n[{self.agent_id}] Analyzing from {self.perspective} perspective...")
        
        # Build the prompt with context if available
        # CONCEPT: Context allows agents to build on previous discussions
        # This enables iterative refinement in the debate
        prompt = question
        if context:
            prompt += f"\n\nContext: {json.dumps(context, indent=2)}"
        
        try:
            # Call the LLM with the agent's system prompt
            # CONCEPT: The system prompt ensures consistent perspective
            # Each agent will interpret the same question differently
            messages = [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=prompt)
            ]
            
            start_time = time.time()
            response = self.llm.invoke(messages)
            elapsed_time = time.time() - start_time
            
            # Structure the response
            # CONCEPT: Structured responses enable better synthesis later
            result = {
                'agent_id': self.agent_id,
                'perspective': self.perspective,
                'specialty': self.specialty,
                'question': question,
                'response': response.content,
                'timestamp': datetime.now().isoformat(),
                'processing_time': round(elapsed_time, 2),
                'status': 'success'
            }
            
            print(f"[{self.agent_id}] ✓ Completed analysis ({elapsed_time:.2f}s)")
            return result
            
        except Exception as e:
            print(f"[{self.agent_id}] ✗ Error: {e}")
            return {
                'agent_id': self.agent_id,
                'perspective': self.perspective,
                'question': question,
                'response': f"Error: {str(e)}",
                'timestamp': datetime.now().isoformat(),
                'status': 'error'
            }


# ============================================================================
# CONCEPT 2: SYNTHESIS AGENT - Combines Multiple Perspectives
# ============================================================================

class SynthesisAgent:
    """
    Synthesis agent that combines multiple perspectives into a unified recommendation.
    
    CONCEPT: In Chain-of-Debate, synthesis is crucial:
    1. Multiple agents provide different perspectives (debate phase)
    2. Synthesis agent analyzes all perspectives
    3. Creates a balanced, actionable recommendation
    
    This mirrors real-world decision-making where we consider multiple viewpoints.
    """
    
    def __init__(self):
        """Initialize the synthesis agent."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.5,  # Lower temperature for more consistent synthesis
            api_key=api_key
        )
        
        # System prompt for synthesis
        # CONCEPT: Synthesis requires different skills than perspective-taking
        # The agent must be objective, balanced, and action-oriented
        self.system_prompt = """You are a Career Counseling Synthesis Expert.
Your role is to analyze multiple perspectives on a career question and create a unified, actionable recommendation.

When synthesizing:
1. Identify key insights from each perspective
2. Find common ground and areas of agreement
3. Acknowledge trade-offs and conflicts
4. Provide a balanced recommendation that considers all viewpoints
5. Be specific and actionable

Structure your synthesis as:
- Summary of Perspectives
- Key Insights
- Trade-offs and Considerations
- Recommended Action Plan
- Next Steps"""
    
    def synthesize(self, question: str, perspectives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Synthesize multiple perspectives into a unified recommendation.
        
        CONCEPT: This is the core of Chain-of-Debate:
        - Input: Multiple independent perspectives (debate results)
        - Process: Analyze, compare, find consensus
        - Output: Unified recommendation
        
        Args:
            question: Original career question
            perspectives: List of perspective responses from different agents
        
        Returns:
            Synthesized recommendation combining all perspectives
        """
        print("\n[Synthesis Agent] Combining perspectives...")
        
        # Build context from all perspectives
        # CONCEPT: The synthesis agent needs to see all perspectives to make informed decisions
        # This is similar to how a judge considers all arguments before making a ruling
        perspectives_text = "\n\n".join([
            f"=== {p['perspective']} Perspective ({p['agent_id']}) ===\n{p['response']}"
            for p in perspectives
        ])
        
        synthesis_prompt = f"""Original Question: {question}

Perspectives from Different Agents:
{perspectives_text}

Please synthesize these perspectives into a unified career counseling recommendation.
Consider all viewpoints, identify common themes, acknowledge trade-offs, and provide actionable advice."""
        
        try:
            messages = [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=synthesis_prompt)
            ]
            
            start_time = time.time()
            response = self.llm.invoke(messages)
            elapsed_time = time.time() - start_time
            
            result = {
                'question': question,
                'synthesis': response.content,
                'perspectives_count': len(perspectives),
                'perspectives': [p['perspective'] for p in perspectives],
                'timestamp': datetime.now().isoformat(),
                'processing_time': round(elapsed_time, 2),
                'status': 'success'
            }
            
            print(f"[Synthesis Agent] ✓ Completed synthesis ({elapsed_time:.2f}s)")
            return result
            
        except Exception as e:
            print(f"[Synthesis Agent] ✗ Error: {e}")
            return {
                'question': question,
                'synthesis': f"Error during synthesis: {str(e)}",
                'timestamp': datetime.now().isoformat(),
                'status': 'error'
            }


# ============================================================================
# CONCEPT 3: CHAIN-OF-DEBATE ORCHESTRATOR
# ============================================================================

class ChainOfDebateOrchestrator:
    """
    Orchestrator that manages the Chain-of-Debate process.
    
    CONCEPT: Chain-of-Debate Pattern Flow:
    1. Question Input → Multiple Perspective Agents
    2. Each agent provides independent perspective (parallel processing)
    3. All perspectives collected
    4. Synthesis agent combines perspectives
    5. Final recommendation returned
    
    This pattern ensures comprehensive analysis by considering multiple viewpoints.
    """
    
    def __init__(self):
        """Initialize the orchestrator with multiple perspective agents."""
        print("Initializing Chain-of-Debate Orchestrator...")
        
        # Create multiple perspective agents
        # CONCEPT: Diversity in perspectives leads to better decisions
        # Each agent brings a different lens to the same question
        self.agents = [
            CareerPerspectiveAgent("tech-agent", "Technical", "Software Engineering & Technology"),
            CareerPerspectiveAgent("business-agent", "Business", "Career Market Analysis"),
            CareerPerspectiveAgent("lifestyle-agent", "Lifestyle", "Work-Life Balance & Well-being")
        ]
        
        # Create synthesis agent
        self.synthesis_agent = SynthesisAgent()
        
        print(f"✓ Initialized {len(self.agents)} perspective agents + 1 synthesis agent")
    
    def process_question(self, question: str, user_context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Process a career question through the Chain-of-Debate pattern.
        
        CONCEPT: This method implements the full Chain-of-Debate workflow:
        
        Phase 1: Parallel Perspective Gathering
        - Each agent independently analyzes the question
        - No communication between agents (ensures diverse perspectives)
        - All agents work in parallel for efficiency
        
        Phase 2: Synthesis
        - Synthesis agent receives all perspectives
        - Analyzes, compares, and combines them
        - Produces unified recommendation
        
        Args:
            question: Career question to analyze
            user_context: Optional user background information
        
        Returns:
            Complete Chain-of-Debate result with all perspectives and synthesis
        """
        print("\n" + "="*70)
        print("CHAIN-OF-DEBATE PROCESS STARTED")
        print("="*70)
        print(f"\nQuestion: {question}")
        
        if user_context:
            print(f"User Context: {json.dumps(user_context, indent=2)}")
        
        start_time = time.time()
        
        # PHASE 1: Gather perspectives from all agents (parallel)
        # CONCEPT: Parallel processing improves efficiency
        # Each agent works independently, allowing concurrent execution
        print("\n" + "-"*70)
        print("PHASE 1: Gathering Multiple Perspectives")
        print("-"*70)
        
        perspectives = []
        for agent in self.agents:
            perspective = agent.provide_perspective(question, user_context)
            perspectives.append(perspective)
        
        perspective_time = time.time() - start_time
        
        # PHASE 2: Synthesize perspectives
        # CONCEPT: Synthesis happens after all perspectives are gathered
        # This sequential dependency ensures synthesis has complete information
        print("\n" + "-"*70)
        print("PHASE 2: Synthesizing Perspectives")
        print("-"*70)
        
        synthesis = self.synthesis_agent.synthesize(question, perspectives)
        
        total_time = time.time() - start_time
        
        # Compile final result
        # CONCEPT: Structured output enables downstream processing
        # This format allows for further analysis, storage, or presentation
        result = {
            'question': question,
            'user_context': user_context,
            'perspectives': perspectives,
            'synthesis': synthesis,
            'timing': {
                'perspective_gathering': round(perspective_time, 2),
                'synthesis': round(synthesis['processing_time'], 2),
                'total': round(total_time, 2)
            },
            'timestamp': datetime.now().isoformat()
        }
        
        print("\n" + "="*70)
        print("CHAIN-OF-DEBATE PROCESS COMPLETED")
        print("="*70)
        print(f"Total time: {total_time:.2f}s")
        
        return result
    
    def display_results(self, result: Dict[str, Any]):
        """
        Display the Chain-of-Debate results in a readable format.
        
        CONCEPT: Clear presentation is crucial for understanding multi-agent outputs
        This method formats the complex multi-perspective analysis for human consumption
        """
        print("\n" + "="*70)
        print("CAREER COUNSELING RECOMMENDATION")
        print("="*70)
        
        print(f"\n📋 Question: {result['question']}")
        
        print("\n" + "-"*70)
        print("PERSPECTIVES FROM DIFFERENT AGENTS")
        print("-"*70)
        
        for i, perspective in enumerate(result['perspectives'], 1):
            print(f"\n{i}. {perspective['perspective']} Perspective ({perspective['agent_id']})")
            print(f"   Processing time: {perspective['processing_time']}s")
            print(f"   Response:\n   {perspective['response'][:200]}...")
        
        print("\n" + "-"*70)
        print("SYNTHESIZED RECOMMENDATION")
        print("-"*70)
        print(f"\n{result['synthesis']['synthesis']}")
        
        print("\n" + "-"*70)
        print("TIMING SUMMARY")
        print("-"*70)
        timing = result['timing']
        print(f"Perspective gathering: {timing['perspective_gathering']}s")
        print(f"Synthesis: {timing['synthesis']}s")
        print(f"Total: {timing['total']}s")


# ============================================================================
# CONCEPT 4: CAP THEOREM EXPLANATION
# ============================================================================

def explain_cap_theorem():
    """
    Explain CAP Theorem in the context of this Chain-of-Debate system.
    
    CONCEPT: CAP Theorem states that in a distributed system, you can only
    guarantee 2 out of 3 properties:
    - Consistency: All nodes see the same data simultaneously
    - Availability: System remains operational
    - Partition tolerance: System continues despite network failures
    
    In our Chain-of-Debate system:
    - We prioritize Availability and Partition tolerance
    - We sacrifice strong Consistency (agents work independently)
    - Final consistency achieved through synthesis
    """
    print("\n" + "="*70)
    print("CAP THEOREM IN CHAIN-OF-DEBATE SYSTEMS")
    print("="*70)
    
    explanation = """
    CAP THEOREM TRADE-OFFS IN THIS SYSTEM:
    
    1. CONSISTENCY (C):
       - Agents work independently without shared state
       - Each agent may have slightly different information
       - Final consistency achieved through synthesis
       - Trade-off: We accept eventual consistency for better availability
    
    2. AVAILABILITY (A):
       - System remains operational even if one agent fails
       - Other agents can continue processing
       - Synthesis can work with partial perspectives
       - Priority: High availability ensures system responsiveness
    
    3. PARTITION TOLERANCE (P):
       - Agents can work in isolation (network partitions)
       - System continues even if communication fails
       - Each agent is self-contained
       - Priority: Essential for distributed agent systems
    
    OUR CHOICE: AP System (Availability + Partition Tolerance)
    - We prioritize availability and partition tolerance
    - We accept eventual consistency (synthesis provides final consistency)
    - This allows agents to work independently and in parallel
    - Better performance and fault tolerance
    
    ALTERNATIVE: CP System (Consistency + Partition Tolerance)
    - Would require agents to coordinate before responding
    - Slower but ensures all agents have same information
    - Better for systems requiring strong consistency
    
    ALTERNATIVE: CA System (Consistency + Availability)
    - Not possible in distributed systems (network partitions always possible)
    - Only works in single-node systems
    """
    
    print(explanation)


# ============================================================================
# MAIN DEMO FUNCTION
# ============================================================================

def run_demo():
    """
    Run the Career Counseling Agent demo.
    
    This demonstrates the complete Chain-of-Debate workflow with
    multiple perspective agents and synthesis.
    """
    print("\n" + "="*70)
    print("HW11: CAREER COUNSELING AGENT - CHAIN-OF-DEBATE PATTERN")
    print("="*70)
    
    # Explain CAP Theorem
    explain_cap_theorem()
    
    # Initialize orchestrator
    orchestrator = ChainOfDebateOrchestrator()
    
    # Example career questions
    questions = [
        {
            'question': "Should I transition from software engineering to data science?",
            'context': {
                'current_role': 'Software Engineer',
                'years_experience': 5,
                'interests': ['Machine Learning', 'Data Analysis'],
                'concerns': ['Job market stability', 'Learning curve']
            }
        },
        {
            'question': "Is it worth pursuing a career in AI/ML given the current market?",
            'context': {
                'background': 'Computer Science graduate',
                'skills': ['Python', 'Basic ML'],
                'goals': ['High salary', 'Cutting-edge work']
            }
        }
    ]
    
    # Process each question
    for i, q_data in enumerate(questions, 1):
        print(f"\n\n{'#'*70}")
        print(f"EXAMPLE {i}: {q_data['question']}")
        print(f"{'#'*70}")
        
        result = orchestrator.process_question(
            q_data['question'],
            q_data.get('context')
        )
        
        orchestrator.display_results(result)
        
        # Save result to file
        output_file = f"career_counseling_result_{i}.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n✓ Results saved to {output_file}")
    
    print("\n" + "="*70)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("="*70)


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
    except Exception as e:
        print(f"\n\nError running demo: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure OPENAI_API_KEY is set: export OPENAI_API_KEY='your-key'")
        print("2. Check internet connectivity")
        print("3. Verify OpenAI API quota")
