# Rubric Generator - Phase 1

## Overview
An interactive Python rubric generation system that creates dynamic, atomic rubrics for ANY user prompt or task. Extracts key concepts from user input and generates 6-8 relevant, verifiable evaluation criteria specific to the task at hand.

## Features
- **Domain-Agnostic:** Works across business, academic, creative, technical, medical, scientific, and conversational prompts
- **Concept Extraction:** Analyzes user input to identify key themes:
  - Professional requirements
  - Persuasion/justification needs
  - Clarity and structure expectations
  - Help/assistance requests
  - User concerns
  - Engagement/interaction
  - Audience-specific considerations
  - Creative/emotional elements
- **Dynamic Rubric Generation:** Creates 6-8 atomic rubrics tailored to the specific prompt (not generic templates)
- **Verifiable Criteria:** Each rubric is concrete, measurable, and independently verifiable
- **File Output:** Saves generated rubrics to a formatted text file for review and editing

## How to Run
```bash
python rubric_generator.py
```

Then follow the prompts to:
1. Enter your question, task description, or user request
2. Program extracts key concepts automatically
3. Program generates 6-8 atomic rubrics specific to your input
4. Review generated rubrics (note: partially atomic rubrics will need editing for full atomicity)
5. View saved output in `generated_rubrics.txt`

## Example Usage

### Example 1: Academic Essay Request
**User Input:** "I'm taking an online course and need to write an essay about climate change. The teacher wants it to be well-researched, with multiple sources, and argue a specific position."

**Extracted Concepts:** persuasion, clarity, help, structure

**Generated Rubrics:**
- The response clearly explains the need or reason for the request.
- The response provides logical justification and compelling arguments.
- The response addresses potential concerns or objections from the audience.
- The response is well-organized and easy to follow.
- The response uses specific details and concrete examples to support claims.
- The response avoids vague language and clearly defines key terms.
- The response directly addresses the user's request and provides actionable assistance.
- The response is complete and thorough without unnecessary information.

### Example 2: Creative Writing Request
**User Input:** "I want to write a short story about a character who discovers a hidden talent late in life. The story should be emotionally engaging, have realistic dialogue, and show character growth."

**Extracted Concepts:** help, creative, emotion

**Generated Rubrics:**
- The response directly addresses the user's request and provides actionable assistance.
- The response is complete and thorough without unnecessary information.
- The response provides practical next steps or recommendations.
- The response provides creative ideas and suggestions that inspire the user.
- The response demonstrates understanding of storytelling techniques and narrative structure.
- The response offers specific guidance on character development and dialogue.
- The response creates or acknowledges emotional resonance and engagement.
- The response helps the user connect with themes of growth and personal transformation.

### Example 3: Business/Technical Request
**User Input:** "Our team's website keeps crashing during peak hours. I need to explain to management why we need to upgrade our servers and database infrastructure. It needs to be clear, include specific technical details, but also be understandable to non-technical stakeholders."

**Extracted Concepts:** persuasion, clarity, structure, audience, engagement

**Generated Rubrics:**
- The response clearly explains the need or reason for the request.
- The response provides logical justification and compelling arguments.
- The response addresses potential concerns or objections from the audience.
- The response is well-organized and easy to follow.
- The response uses specific details and concrete examples to support claims.
- The response avoids vague language and clearly defines key terms.
- The response follows a logical structure (e.g., introduction, body, conclusion).
- The response includes clear sections or headings that guide the reader.

## Technical Details
- **Language:** Python
- **Architecture:** Modular functions for extensibility
- **Concept Extraction:** Keyword-based matching across 8+ concept categories
- **Rubric Generation:** Template-based system with domain-aware keywords
- **Output:** Plain text file with formatted rubrics for easy review and editing

## Phase 1 Status
✅ Concept extraction working across 5+ domains
✅ Rubric generation producing 6-8 criteria per prompt
✅ Tested on: gaming, business, academic, creative, technical domains
✅ Ready for Phase 2: Bias detection and clarity checking

## Next Phases
**Phase 2 (In Development):** Add bias detection, clarity checking, and rubric refinement
**Phase 3 (Planned):** JSON storage, learning from edits, improved rubric atomicity

## Important Notes
- Generated rubrics are typically **partially atomic** and will require user editing to achieve full atomicity
- This is expected behavior and reflects real-world rubric development
- User expertise is essential for final quality and domain-specific accuracy