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
        "social": ["social", "team", "clan", "group", "together", "collaboration", "community"],
        "games": ["game", "gaming", "open-world", "multiplayer", "coop"],
        "retention": ["pull", "back", "return", "keep", "come back", "retention", "why"],
        "interaction": ["interact", "connection", "engage", "discussion"],
        "audio": ["voice", "audio", "speak", "sound", "pronunciation"]
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
    # Rubric templates for each concept
    rubric_templates = {
        "social": [
            "The response acknowledges the importance of social interaction in player retention.",
            "The response provides concrete examples of social gameplay mechanics (teams, clans, collaboration).",
            "The response explains how social bonds and community keep players engaged long-term."
        ],
        "games": [
            "The response demonstrates understanding of open-world game mechanics and structure.",
            "The response uses accurate gaming terminology relevant to the topic.",
            "The response connects social features specifically to open-world gaming context."
        ],
        "retention": [
            "The response directly answers why social interaction pulls players back to games.",
            "The response explains the long-term retention benefits of social gameplay.",
            "The response distinguishes between solo vs. social gaming in terms of player return rates."
        ],
        "interaction": [
            "The response engages the user by acknowledging their perspective on gaming.",
            "The response proactively asks follow-up questions about the user's gaming experience.",
            "The response invites continued conversation about the topic."
        ],
        "audio": [
            "The response uses natural, conversational language appropriate for spoken audio.",
            "The response maintains clear pronunciation of technical terms like 'open-world' and 'multiplayer'.",
            "The response sounds fluent and engaging when delivered as audio."
        ]
    }
    
    # Generate rubrics based on found concepts
    generated_rubrics = []
    
    for concept in concepts:
        if concept in rubric_templates:
            generated_rubrics.extend(rubric_templates[concept])
    
    # Limit to 6-8 rubrics for Phase 1 (prefer 6-7)
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