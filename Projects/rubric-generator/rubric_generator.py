# Rubric Generator - Phase 1
# Generates dynamic rubrics based on user input

def get_user_input():
    """Get the user's question/prompt"""
    print("\n" + "="*60)
    print("RUBRIC GENERATOR - PHASE 1")
    print("="*60)
    print("\nPlease enter your question or task description:")
    print("(This will be used to generate atomic rubrics)\n")
    
    user_input = input("Your prompt: ").strip()
    
    if not user_input:
        print("Error: You must enter a prompt. Please try again.")
        return get_user_input()  # Ask again if empty
    
    return user_input 

def extract_concepts(user_input):
    """Extract key concepts from the user's input"""
    # Keywords to look for (organized by category)
    keywords = {
     "professional": ["professional", "business", "work", "job", "meeting", "boss", "formal", "corporate"],
        "persuasion": ["persuade", "convince", "justify", "explain", "need", "reason", "argument", "support", "benefit", "value", "advantage", "pull", "draw", "appeal", "why", "important", "keep", "return"],
        "clarity": ["clear", "understand", "explain", "describe", "detail", "specific", "example", "game", "concept", "term"],
        "help": ["help", "assist", "create", "build", "put together", "write", "draft", "develop", "think", "question", "ask", "do you"],
        "concern": ["worry", "worried", "concerned", "anxious", "afraid", "difficult", "challenge"],
        "structure": ["proposal", "plan", "outline", "format", "organize", "structure", "framework"],
        "audience": ["boss", "manager", "director", "stakeholder", "audience", "reader", "recipient"],
        "engagement": ["together", "interaction", "social", "community", "collaborate", "team", "group", "connection", "retain", "return", "keep", "loyal", "clan"],
        "creative": ["story", "character", "dialogue", "narrative", "plot", "setting", "emotional", "engaging", "voice", "talent", "growth", "develop"],
        "emotion": ["emotionally", "feel", "emotional", "touching", "moving", "engaging", "resonate"],
    }    
    
    # Convert input to lowercase for matching
    user_input_lower = user_input.lower()
    
    # Find which keywords appear in the input
    found_concepts = []
    for category, words in keywords.items():
        for word in words:
            if word in user_input_lower and category not in found_concepts:
                found_concepts.append(category)
                break  # Only add each category once
    
    # If no concepts found, use generic ones
    if not found_concepts:
        found_concepts = ["content", "quality", "accuracy"]
    
    print(f"\nExtracted concepts: {', '.join(found_concepts)}")
    return found_concepts

def generate_rubrics(concepts):
    """Generate atomic rubrics based on extracted concepts"""
  # GENERIC rubric templates that work across ANY domain
    rubric_templates = {
        "professional": [
            "The response maintains a professional tone and formal language appropriate for the context.",
            "The response uses proper grammar, spelling, and punctuation throughout.",
            "The response demonstrates respect for the audience and the situation."
        ],
        "persuasion": [
            "The response clearly explains the need or reason for the request.",
            "The response provides logical justification and compelling arguments.",
            "The response addresses potential concerns or objections from the audience."
        ],
        "clarity": [
            "The response is well-organized and easy to follow.",
            "The response uses specific details and concrete examples to support claims.",
            "The response avoids vague language and clearly defines key terms."
        ],
        "help": [
            "The response directly addresses the user's request and provides actionable assistance.",
            "The response is complete and thorough without unnecessary information.",
            "The response provides practical next steps or recommendations."
        ],
        "concern": [
            "The response acknowledges the user's concerns and shows empathy.",
            "The response provides reassurance through confidence and clarity.",
            "The response offers strategies to address the user's worries."
        ],
        "structure": [
            "The response follows a logical structure (e.g., introduction, body, conclusion).",
            "The response includes clear sections or headings that guide the reader.",
            "The response presents information in a coherent, hierarchical format."
        ],
        "audience": [
            "The response is tailored to the specific audience (e.g., boss, manager, stakeholder).",
            "The response anticipates what the audience cares about and prioritizes accordingly.",
            "The response uses language and examples relevant to the audience's context."
        ],
"engagement": [
    "The response acknowledges the value and benefits of collaboration and community.",
    "The response uses relatable examples that resonate with the user's interests.",
    "The response demonstrates understanding of what keeps people engaged and committed.",
    "The response encourages continued participation or involvement from the user."
],
"creative": [  
    "The response provides creative ideas and suggestions that inspire the user.",
    "The response demonstrates understanding of storytelling techniques and narrative structure.",
    "The response offers specific guidance on character development and dialogue."
],
"emotion": [
    "The response creates or acknowledges emotional resonance and engagement.",
    "The response helps the user connect with themes of growth and personal transformation.",
    "The response suggests ways to make content emotionally compelling and relatable."
],
         
    }
    
    # Generate rubrics based on found concepts
    generated_rubrics = []
    
    for concept in concepts:
        if concept in rubric_templates:
            generated_rubrics.extend(rubric_templates[concept])
    
    # Limit to 6-8 rubrics (prefer 6-8 for Phase 1)
    if len(generated_rubrics) > 8:
        generated_rubrics = generated_rubrics[:8]
    elif len(generated_rubrics) < 4:
        # Add generic rubrics if we have fewer than 4
        generated_rubrics.extend([
            "The response provides accurate, helpful information.",
            "The response is clear and well-organized."
        ])
    
    return generated_rubrics

def display_rubrics(rubrics):
    """Display rubrics to user"""
    print("\n" + "="*60)
    print("GENERATED ATOMIC RUBRICS")
    print("="*60)
    print("\nReview these rubrics. Edit any that don't meet expectations:")
    print("(Specific, Verifiable, Atomic, Appropriately Difficult)\n")
    
    for i, rubric in enumerate(rubrics, 1):
        print(f"{i}. {rubric}")
    
    print("\n" + "="*60)

def save_rubrics(rubrics, filename="generated_rubrics.txt"):
    """Save rubrics to a file"""
    try:
        with open(filename, 'w') as f:
            f.write("GENERATED ATOMIC RUBRICS\n")
            f.write("="*60 + "\n\n")
            for i, rubric in enumerate(rubrics, 1):
                f.write(f"{i}. {rubric}\n")
        print(f"\n✓ Rubrics saved to: {filename}")
        return True
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")
        return False

def main():
    """Main program flow"""
    # Step 1: Get user input
    user_input = get_user_input()
    
    # Step 2: Extract concepts
    concepts = extract_concepts(user_input)
    
    # Step 3: Generate rubrics
    rubrics = generate_rubrics(concepts)
            
    # Step 4: Display rubrics
    display_rubrics(rubrics)
    
    # Step 5: Save rubrics
    save_rubrics(rubrics)  

if __name__ == "__main__":
    main()