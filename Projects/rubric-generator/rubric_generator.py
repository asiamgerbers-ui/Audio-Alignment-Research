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
    # REFINED KEYWORDS - Specific to reduce false positives
    keywords = {
        # FOUNDATIONAL (Keep existing - safe)
        "professional": ["professional", "business", "work", "job", "meeting", "boss", "formal", "corporate"],
        "persuasion": ["persuade", "convince", "justify", "explain", "need", "reason", "argument", "support", "benefit", "value", "advantage", "pull", "draw", "appeal", "why", "important", "keep", "return"],
        "clarity": ["clear", "understand", "explain", "describe", "detail", "specific", "example"],
        "help": ["help", "assist", "create", "build", "put together", "write", "draft", "develop"],
        "concern": ["worry", "worried", "concerned", "anxious", "afraid", "difficult", "challenge"],
        "structure": ["proposal", "plan", "outline", "format", "organize", "structure", "framework"],
        "audience": ["boss", "manager", "director", "stakeholder", "audience", "reader", "recipient"],
        "engagement": ["together", "interaction", "social", "community", "collaborate", "team", "group", "connection", "retain", "return", "keep", "loyal", "clan"],
        "creative": ["story", "character", "dialogue", "narrative", "plot", "setting", "emotional", "engaging", "voice", "talent", "growth", "develop"],
        "emotion": ["emotionally", "feel", "emotional", "touching", "moving", "engaging", "resonate"],
        
        # CODING DOMAINS - More specific
        "backend": ["backend", "api", "server", "database architecture", "infrastructure", "pipeline", "endpoint", "microservice", "scalability"],
        "frontend": ["frontend", "user interface", "ui design", "react", "javascript framework", "responsive design", "css styling"],
        "testing": ["unit test", "integration test", "qa testing", "bug fix", "quality assurance", "debug", "test coverage"],
        "database": ["sql query", "database design", "schema", "data model", "index optimization", "transaction"],
        "fullstack": ["full-stack", "end-to-end", "devops", "ci/cd", "containerization", "docker", "kubernetes"],
        "code_quality": ["code review", "refactor code", "coding standards", "best practices", "maintainability", "efficiency optimization"],
        "systems": ["distributed system", "concurrent programming", "threading", "asynchronous", "consensus algorithm"],
        "ml_ops": ["machine learning", "neural network", "model training", "deep learning", "inference", "algorithm optimization"],
        
        # WRITING & CONTENT - Domain specific
        "writing": ["write article", "blog post", "essay writing", "content creation", "publication"],
        "editing": ["edit text", "proofread", "grammar check", "spelling correction", "revise content"],
        "technical_writing": ["technical documentation", "manual writing", "instruction guide", "api documentation", "specification"],
        "copywriting": ["marketing copy", "headline writing", "call to action", "advertising copy"],
        "storytelling": ["narrative structure", "character development", "plot development", "story arc"],
        "descriptive": ["visual description", "imagery", "scene description", "atmosphere"],
        "image_description": ["image alt text", "describe photo", "visual content", "picture description"],
        "video_description": ["video scene", "cinematography description", "shot description", "video analysis"],
        
        # MEDICAL & HEALTHCARE - Domain specific
        "medical": ["diagnosis", "clinical", "ehr", "patient care", "treatment protocol", "disease"],
        "healthcare_data": ["ehr annotation", "medical coding", "clinical labeling", "chart annotation"],
        "health_policy": ["healthcare policy", "health regulation", "evidence-based", "clinical guideline"],
        "health_informatics": ["healthcare informatics", "clinical workflow", "healthcare system", "medical it"],
        
        # SCIENCE DOMAINS - Domain specific
        "biology": ["biology", "organism", "genetics", "evolution", "ecosystem", "gene", "protein", "dna"],
        "biochemistry": ["biochemistry", "protein folding", "metabolic pathway", "enzyme", "molecular biology"],
        "chemistry": ["chemistry", "molecule", "chemical reaction", "compound", "element", "stoichiometry"],
        "physics": ["physics", "mechanics", "thermodynamics", "electromagnetism", "quantum physics"],
        "math": ["mathematics", "algebra", "calculus", "geometry", "proof", "theorem"],
        "statistics": ["statistics", "probability", "hypothesis test", "regression", "statistical analysis"],
        "data_science": ["data science", "machine learning application", "data analysis", "visualization"],
        "wildlife": ["wildlife conservation", "habitat", "species", "ecosystem", "environmental"],
        
        # ENGINEERING - Domain specific
        "electrical_engineering": ["electrical circuit", "electronics", "power system", "signal processing"],
        "mechanical_engineering": ["mechanical design", "thermodynamics", "fluid dynamics", "structural"],
        "computer_engineering": ["computer architecture", "processor design", "embedded system", "hardware"],
        
        # BUSINESS & FINANCE - Domain specific
        "business": ["business strategy", "operations", "management", "organizational", "corporate"],
        "finance": ["finance", "investment", "trading", "stock market", "portfolio"],
        "accounting": ["accounting", "financial statement", "balance sheet", "audit"],
        "economics": ["economics", "economic theory", "market", "supply demand"],
        "entrepreneurship": ["startup", "business plan", "venture", "founder"],
        "marketing": ["marketing strategy", "consumer behavior", "brand", "campaign"],
        
        # LANGUAGE & LINGUISTICS - Domain specific
        "language_quality": ["language translation", "localization", "fluency", "linguistic accuracy"],
        "spanish": ["spanish language", "castilian", "colombian spanish", "caribbean spanish", "spanish dialect"],
        "asian_languages": ["japanese language", "korean language", "chinese language", "thai language", "asian language"],
        "european_languages": ["french language", "portuguese language", "german language", "italian language"],
        "other_languages": ["arabic language", "hebrew language", "native speaker"],
        
        # SPECIALIZED DOMAINS - Domain specific
        "aviation": ["aviation", "pilot", "atc", "air traffic control", "flight", "aircraft", "phraseology", "tower communications"],
        "transcription": ["transcribe audio", "transcription", "audio transcription", "transcript"],
        "robotics": ["robotics", "robot training", "household tasks", "video data collection"],
        "prediction": ["prediction", "forecast", "probability estimate", "event outcome"],
        "financial_analysis": ["financial analysis", "financial statement", "metric validation"],
        "trading": ["retail trading", "trading behavior", "market signal", "trading data"],
        
        # MEDIA & CREATIVE - Domain specific
        "cinematography": ["cinematography", "camera movement", "shot composition", "visual framing"],
        "film": ["film scene", "narrative beats", "scene description", "cinematographic"],
        "prompt_writing": ["prompt writing", "ai prompt", "test prompt", "challenge prompt"],
        "quality_control": ["quality control", "quality review", "quality assessment", "rating"]
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
    # CODING DOMAINS
    "backend": [
            "The response demonstrates understanding of backend architecture and server-side logic.",
            "The response addresses API design, database interactions, and scalability concerns.",
            "The response considers performance optimization and system reliability.",
            "The response explains infrastructure and deployment considerations."
        ],
        "frontend": [
            "The response demonstrates understanding of user interface design and user experience principles.",
            "The response addresses responsive design, accessibility, and cross-browser compatibility.",
            "The response considers component architecture and state management.",
            "The response includes considerations for performance and load times."
        ],
        "testing": [
            "The response demonstrates understanding of testing methodologies and quality assurance.",
            "The response addresses edge cases, error handling, and validation.",
            "The response explains debugging strategies and error identification.",
            "The response considers test coverage and reliability assessment."
        ],
        "database": [
            "The response demonstrates understanding of database design and optimization.",
            "The response addresses schema design, indexing, and query optimization.",
            "The response considers data integrity and transaction management.",
            "The response explains scalability and performance in data storage."
        ],
        "fullstack": [
            "The response integrates both frontend and backend considerations seamlessly.",
            "The response addresses end-to-end data flow and system integration.",
            "The response considers deployment, DevOps, and CI/CD pipelines.",
            "The response demonstrates understanding of the complete application lifecycle."
        ],
        "code_quality": [
            "The response demonstrates best practices for code readability and maintainability.",
            "The response addresses refactoring, optimization, and efficiency improvements.",
            "The response includes documentation and code comments where appropriate.",
            "The response follows established coding standards and conventions."
        ],
        "systems": [
            "The response demonstrates understanding of distributed systems and concurrent programming.",
            "The response addresses scalability, latency, and throughput considerations.",
            "The response considers thread safety, memory management, and resource allocation.",
            "The response explains trade-offs between consistency, availability, and partition tolerance."
        ],
        "ml_ops": [
            "The response demonstrates understanding of machine learning pipelines and workflows.",
            "The response addresses model training, evaluation, and hyperparameter tuning.",
            "The response considers deployment, monitoring, and model versioning.",
            "The response explains data preprocessing and feature engineering."
        ],
        
        # WRITING & CONTENT
        "writing": [
            "The response demonstrates strong writing skills with clear expression of ideas.",
            "The response maintains consistent voice, tone, and style throughout.",
            "The response engages the reader and sustains interest.",
            "The response is free of grammatical errors and maintains proper syntax."
        ],
        "editing": [
            "The response identifies and corrects grammatical, spelling, and punctuation errors.",
            "The response improves clarity, conciseness, and overall readability.",
            "The response maintains the author's original intent while enhancing quality.",
            "The response suggests improvements for style, tone, and coherence."
        ],
        "technical_writing": [
            "The response provides clear, step-by-step instructions or explanations.",
            "The response includes relevant technical details and specifications.",
            "The response uses appropriate terminology and maintains technical accuracy.",
            "The response is organized logically with clear headings and sections."
        ],
        "copywriting": [
            "The response creates compelling headlines and engaging opening statements.",
            "The response includes a clear call to action that motivates the audience.",
            "The response uses persuasive language and emotional appeals effectively.",
            "The response is concise and memorable while conveying the key message."
        ],
        "storytelling": [
            "The response develops compelling characters with depth and motivation.",
            "The response creates a coherent plot with clear conflict and resolution.",
            "The response uses dialogue effectively to reveal character and advance the story.",
            "The response builds tension and engages the reader emotionally."
        ],
        "descriptive": [
            "The response uses vivid, sensory language to paint a clear picture.",
            "The response creates atmosphere and mood through careful word choice.",
            "The response balances detail with readability and maintains focus.",
            "The response evokes emotion and engages the reader's imagination."
        ],
        "image_description": [
            "The response accurately describes the visual composition and subject matter.",
            "The response includes relevant details about colors, objects, and positioning.",
            "The response is clear and accessible to someone who cannot see the image.",
            "The response captures the mood, context, and significance of the image."
        ],
        "video_description": [
            "The response accurately describes camera movement, framing, and composition.",
            "The response captures mood, pacing, and narrative flow of the scene.",
            "The response includes details about visual elements and cinematographic choices.",
            "The response is organized logically and easy to visualize from the description."
        ],
        
        # MEDICAL & HEALTHCARE
        "medical": [
            "The response demonstrates accurate understanding of medical concepts and terminology.",
            "The response addresses diagnosis, treatment options, and clinical considerations.",
            "The response considers patient safety and evidence-based medical practice.",
            "The response explains medical conditions and procedures clearly and accurately."
        ],
        "healthcare_data": [
            "The response demonstrates understanding of medical coding and classification systems.",
            "The response addresses data quality, accuracy, and completeness in healthcare records.",
            "The response considers patient privacy and data security requirements.",
            "The response explains proper annotation and labeling of healthcare data."
        ],
        "health_policy": [
            "The response demonstrates understanding of healthcare policy and regulations.",
            "The response addresses evidence-based guidelines and best practices.",
            "The response considers ethical implications and patient advocacy.",
            "The response explains healthcare systems and insurance considerations."
        ],
        "health_informatics": [
            "The response demonstrates understanding of healthcare information systems.",
            "The response addresses clinical workflow optimization and system integration.",
            "The response considers data analysis and clinical decision support.",
            "The response explains healthcare IT infrastructure and compliance requirements."
        ],
        
        # SCIENCE DOMAINS
        "biology": [
            "The response demonstrates accurate understanding of biological concepts and processes.",
            "The response addresses genetics, evolution, and ecosystem dynamics.",
            "The response includes relevant examples and applications of biological principles.",
            "The response explains complex biological systems clearly and accurately."
        ],
        "biochemistry": [
            "The response demonstrates understanding of molecular mechanisms and biochemical pathways.",
            "The response addresses protein structure, enzyme kinetics, and metabolic processes.",
            "The response considers molecular interactions and cellular processes.",
            "The response explains biochemical concepts with appropriate detail and accuracy."
        ],
        "chemistry": [
            "The response demonstrates accurate understanding of chemical concepts and reactions.",
            "The response addresses molecular structure, bonding, and stoichiometry.",
            "The response includes relevant examples and real-world applications.",
            "The response explains chemical principles clearly and with proper terminology."
        ],
        "physics": [
            "The response demonstrates understanding of physical laws and principles.",
            "The response addresses forces, energy, motion, and thermodynamics.",
            "The response includes relevant calculations and quantitative analysis.",
            "The response explains physics concepts with clarity and mathematical rigor."
        ],
        "math": [
            "The response demonstrates strong mathematical reasoning and problem-solving.",
            "The response provides clear proofs or derivations with logical steps.",
            "The response includes relevant examples and applications of mathematical concepts.",
            "The response uses proper mathematical notation and terminology throughout."
        ],
        "statistics": [
            "The response demonstrates understanding of statistical methods and concepts.",
            "The response addresses probability, inference, and hypothesis testing.",
            "The response includes appropriate visualizations and quantitative analysis.",
            "The response explains statistical reasoning clearly and accurately."
        ],
        "data_science": [
            "The response demonstrates understanding of data analysis and machine learning.",
            "The response addresses data preprocessing, visualization, and interpretation.",
            "The response includes appropriate statistical or algorithmic approaches.",
            "The response explains data science concepts and methodologies clearly."
        ],
        "wildlife": [
            "The response demonstrates accurate understanding of wildlife and ecology.",
            "The response addresses habitat conservation and species management.",
            "The response considers environmental impacts and sustainability.",
            "The response explains wildlife concepts with scientific accuracy."
        ],
        
        # ENGINEERING
        "electrical_engineering": [
            "The response demonstrates understanding of circuits, power, and electrical systems.",
            "The response addresses signal processing, control systems, and electronics.",
            "The response considers safety, efficiency, and performance optimization.",
            "The response explains electrical engineering concepts with technical accuracy."
        ],
        "mechanical_engineering": [
            "The response demonstrates understanding of mechanics, thermodynamics, and design.",
            "The response addresses fluid dynamics, structural analysis, and material properties.",
            "The response considers stress analysis, safety factors, and manufacturing.",
            "The response explains mechanical concepts with appropriate technical detail."
        ],
        "computer_engineering": [
            "The response demonstrates understanding of computer architecture and hardware design.",
            "The response addresses processors, memory systems, and embedded systems.",
            "The response considers performance, power efficiency, and system integration.",
            "The response explains computer engineering concepts clearly and accurately."
        ],
        
        # BUSINESS & FINANCE
        "business": [
            "The response demonstrates understanding of business strategy and operations.",
            "The response addresses organizational management and business processes.",
            "The response considers market dynamics, competition, and business models.",
            "The response explains business concepts with practical relevance."
        ],
        "finance": [
            "The response demonstrates understanding of financial markets and investment principles.",
            "The response addresses portfolio management, risk assessment, and valuation.",
            "The response includes relevant financial calculations and analysis.",
            "The response explains financial concepts with accuracy and clarity."
        ],
        "accounting": [
            "The response demonstrates understanding of accounting principles and practices.",
            "The response addresses financial statements, auditing, and compliance.",
            "The response includes appropriate accounting treatments and disclosures.",
            "The response explains accounting concepts with technical accuracy."
        ],
        "economics": [
            "The response demonstrates understanding of economic principles and theory.",
            "The response addresses market mechanisms, policy implications, and quantitative analysis.",
            "The response includes relevant economic data and empirical evidence.",
            "The response explains economic concepts with rigor and clarity."
        ],
        "entrepreneurship": [
            "The response demonstrates understanding of startup development and business planning.",
            "The response addresses market validation, funding, and growth strategy.",
            "The response considers risk management and operational execution.",
            "The response explains entrepreneurial concepts with practical insight."
        ],
        "marketing": [
            "The response demonstrates understanding of marketing strategy and consumer behavior.",
            "The response addresses market segmentation, positioning, and brand management.",
            "The response considers customer acquisition and retention strategies.",
            "The response explains marketing concepts with practical application."
        ],
        
        # LANGUAGE & LINGUISTICS
        "language_quality": [
            "The response demonstrates high-quality language use with appropriate fluency.",
            "The response maintains cultural and linguistic accuracy for the target language.",
            "The response considers regional variations, idioms, and natural phrasing.",
            "The response avoids literal translations and captures authentic language use."
        ],
        "spanish": [
            "The response demonstrates accurate Spanish language usage and regional dialect awareness.",
            "The response respects dialectal differences (Castilian, Colombian, Caribbean, etc.).",
            "The response uses appropriate vocabulary and expressions for the dialect.",
            "The response maintains linguistic authenticity and cultural context."
        ],
        "asian_languages": [
            "The response demonstrates accurate language use in Asian languages (Japanese, Korean, Chinese, Thai, Vietnamese, etc.).",
            "The response respects cultural and linguistic nuances specific to each language.",
            "The response uses appropriate formality levels and respectful language conventions.",
            "The response demonstrates native or heritage speaker competency."
        ],
        "european_languages": [
            "The response demonstrates accurate language use in European languages (French, Portuguese, Italian, German, etc.).",
            "The response respects regional and cultural variations within each language.",
            "The response uses appropriate vocabulary, grammar, and idiomatic expressions.",
            "The response demonstrates authentic language proficiency."
        ],
        "other_languages": [
            "The response demonstrates accurate language use in less commonly taught languages (Arabic, Hebrew, etc.).",
            "The response respects cultural context and linguistic conventions.",
            "The response uses appropriate vocabulary and grammatical structures.",
            "The response demonstrates native or heritage speaker competency."
        ],
        
        # SPECIALIZED DOMAINS
        "aviation": [
            "The response demonstrates understanding of aviation procedures and terminology.",
            "The response uses proper phraseology consistent with ATC standards.",
            "The response addresses safety procedures and emergency protocols.",
            "The response explains aviation concepts with technical accuracy and clarity."
        ],
        "transcription": [
            "The response accurately transcribes audio content with correct spelling and punctuation.",
            "The response captures nuances including emphasis, pauses, and tone indicators.",
            "The response maintains accuracy and clarity while following transcription guidelines.",
            "The response is complete and thoroughly reviewed for quality."
        ],
        "robotics": [
            "The response provides high-quality video data for robotics training.",
            "The response captures diverse household tasks and interactions with objects.",
            "The response demonstrates clear, natural movements and realistic scenarios.",
            "The response includes sufficient context and detail for AI training purposes."
        ],
        "prediction": [
            "The response demonstrates strong analytical reasoning and probability assessment.",
            "The response provides well-justified predictions based on available evidence.",
            "The response considers alternative outcomes and uncertainty factors.",
            "The response explains reasoning clearly and acknowledges limitations."
        ],
        "financial_analysis": [
            "The response demonstrates thorough analysis of financial statements and metrics.",
            "The response validates key figures and identifies significant trends.",
            "The response provides actionable insights and comprehensive summaries.",
            "The response maintains accuracy and professional rigor."
        ],
        "trading": [
            "The response demonstrates understanding of retail trading behavior and market dynamics.",
            "The response accurately labels and categorizes trading data.",
            "The response identifies patterns and provides probability estimates.",
            "The response supports AI model training with high-quality analysis."
        ],
        
        # MEDIA & CREATIVE
        "cinematography": [
            "The response accurately describes cinematographic techniques and visual composition.",
            "The response identifies camera movement, framing, and shot types.",
            "The response captures lighting, color, and visual atmosphere.",
            "The response explains visual storytelling choices clearly."
        ],
        "film": [
            "The response accurately describes scenes, beats, and narrative structure.",
            "The response captures mood, pacing, and emotional arc.",
            "The response identifies key visual and narrative elements.",
            "The response provides comprehensive scene analysis."
        ],
        "prompt_writing": [
            "The response creates clear, specific, and challenging prompts for AI evaluation.",
            "The response covers edge cases and diverse scenarios.",
            "The response provides measurable success criteria.",
            "The response stimulates thoughtful AI reasoning and improvement."
        ],
        "quality_control": [
            "The response demonstrates thorough quality assessment and evaluation.",
            "The response identifies errors, inconsistencies, and areas for improvement.",
            "The response provides constructive feedback with specific examples.",
            "The response maintains objectivity and consistency in ratings."
        ],
         
    }
    
    # Generate rubrics based on found concepts
    generated_rubrics = []
    
    # PRIORITY: Add domain-specific rubrics first
    domain_specific = ["aviation", "medical", "healthcare_data", "biology", "chemistry", "physics", 
                      "math", "statistics", "electrical_engineering", "mechanical_engineering",
                      "technical_writing", "coding", "backend", "frontend", "database"]
    
    # Add domain-specific rubrics first
    for concept in concepts:
        if concept in domain_specific and concept in rubric_templates:
            generated_rubrics.extend(rubric_templates[concept])
    
    # Then add general/supporting rubrics
    for concept in concepts:
        if concept not in domain_specific and concept in rubric_templates:
            generated_rubrics.extend(rubric_templates[concept])
    
    # Limit to 6-12 rubrics (prefer 6-8, allow up to 12 for comprehensive coverage)
    if len(generated_rubrics) > 12:
        generated_rubrics = generated_rubrics[:12]
        
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