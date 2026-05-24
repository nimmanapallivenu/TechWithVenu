#!/usr/bin/env python3
"""
Content Generator for Software Solution Engineer Learning Path
Generates README.md files for all topics across all phases
"""

import os
from pathlib import Path

# Define the content structure
CONTENT_STRUCTURE = {
    "01-full-stack-development": {
        "01-frontend": {
            "css": {
                "title": "CSS - Cascading Style Sheets",
                "description": "Master styling, layouts, and responsive design",
                "topics": ["Selectors", "Box Model", "Flexbox", "Grid", "Responsive Design", "Animations", "CSS Variables", "Preprocessors"]
            },
            "javascript": {
                "title": "JavaScript",
                "description": "Learn modern JavaScript programming",
                "topics": ["Variables & Data Types", "Functions", "Objects & Arrays", "DOM Manipulation", "Events", "Async/Await", "ES6+ Features", "Error Handling"]
            },
            "react": {
                "title": "React.js",
                "description": "Build modern user interfaces with React",
                "topics": ["Components", "Props & State", "Hooks", "Context API", "React Router", "Forms", "Performance", "Testing"]
            },
            "tailwind": {
                "title": "Tailwind CSS",
                "description": "Utility-first CSS framework",
                "topics": ["Utility Classes", "Responsive Design", "Customization", "Components", "Dark Mode", "Plugins", "Best Practices"]
            }
        },
        "02-backend": {
            "nodejs": {
                "title": "Node.js",
                "description": "JavaScript runtime for server-side development",
                "topics": ["Event Loop", "Modules", "File System", "Streams", "HTTP Server", "NPM", "Debugging", "Performance"]
            },
            "apis": {
                "title": "RESTful APIs",
                "description": "Design and build robust APIs",
                "topics": ["REST Principles", "HTTP Methods", "Status Codes", "API Design", "Versioning", "Documentation", "Error Handling", "Rate Limiting"]
            },
            "databases": {
                "title": "Databases",
                "description": "Work with SQL and NoSQL databases",
                "topics": ["PostgreSQL", "Redis", "SQL Queries", "Indexes", "Transactions", "Migrations", "ORMs", "Query Optimization"]
            },
            "authentication": {
                "title": "Authentication & Authorization",
                "description": "Secure your applications",
                "topics": ["JWT", "OAuth 2.0", "Sessions", "Password Hashing", "RBAC", "Security Best Practices", "2FA", "API Keys"]
            }
        },
        "03-devops": {
            "git-github": {
                "title": "Git & GitHub",
                "description": "Version control and collaboration",
                "topics": ["Git Basics", "Branching", "Merging", "Pull Requests", "GitHub Actions", "Git Workflows", "Conflict Resolution"]
            },
            "linux": {
                "title": "Linux Basics",
                "description": "Command line essentials",
                "topics": ["File System", "Commands", "Permissions", "Process Management", "Shell Scripting", "Package Management", "SSH"]
            },
            "aws": {
                "title": "AWS Services",
                "description": "Cloud infrastructure basics",
                "topics": ["EC2", "S3", "VPC", "Route53", "RDS", "Lambda", "CloudWatch", "IAM"]
            },
            "ci-cd": {
                "title": "CI/CD",
                "description": "Continuous Integration and Deployment",
                "topics": ["GitHub Actions", "Pipelines", "Testing", "Deployment Strategies", "Rollbacks", "Monitoring", "Automation"]
            },
            "monitoring": {
                "title": "Monitoring & Logging",
                "description": "Application observability",
                "topics": ["Logging", "Metrics", "Alerts", "APM", "Error Tracking", "Performance Monitoring", "Log Aggregation"]
            }
        }
    },
    "02-ai-engineering": {
        "01-fundamentals": {
            "ai-basics": {
                "title": "AI Fundamentals",
                "description": "Introduction to Artificial Intelligence",
                "topics": ["What is AI", "AI vs ML vs DL", "AI Applications", "AI Ethics", "AI Limitations", "Future of AI"]
            },
            "ml-basics": {
                "title": "Machine Learning Basics",
                "description": "Core ML concepts and algorithms",
                "topics": ["Supervised Learning", "Unsupervised Learning", "Model Training", "Feature Engineering", "Model Evaluation", "Overfitting"]
            },
            "terminology": {
                "title": "AI Terminology",
                "description": "Essential AI/ML vocabulary",
                "topics": ["Common Terms", "Algorithms", "Metrics", "Frameworks", "Tools", "Industry Jargon"]
            }
        },
        "02-llms": {
            "inference": {
                "title": "LLM Inference",
                "description": "Running Large Language Models",
                "topics": ["Model Loading", "Tokenization", "Generation", "Sampling", "Temperature", "Top-k/Top-p", "Batching", "Optimization"]
            },
            "training": {
                "title": "LLM Training",
                "description": "Fine-tuning and training LLMs",
                "topics": ["Pre-training", "Fine-tuning", "LoRA", "QLoRA", "PEFT", "Dataset Preparation", "Training Strategies"]
            },
            "embeddings": {
                "title": "Embeddings",
                "description": "Vector representations of text",
                "topics": ["Word Embeddings", "Sentence Embeddings", "Similarity", "Dimensionality", "Use Cases", "Best Practices"]
            }
        },
        "03-tools": {
            "vector-databases": {
                "title": "Vector Databases",
                "description": "Store and query embeddings",
                "topics": ["Pinecone", "Weaviate", "Qdrant", "ChromaDB", "Similarity Search", "Indexing", "Performance"]
            },
            "rag": {
                "title": "RAG - Retrieval Augmented Generation",
                "description": "Enhance LLMs with external knowledge",
                "topics": ["RAG Architecture", "Document Processing", "Chunking", "Retrieval", "Context Injection", "Optimization"]
            },
            "prompt-engineering": {
                "title": "Prompt Engineering",
                "description": "Craft effective prompts for LLMs",
                "topics": ["Prompt Patterns", "Few-shot Learning", "Chain of Thought", "System Prompts", "Best Practices", "Testing"]
            }
        },
        "04-agents": {
            "README": {
                "title": "AI Agents",
                "description": "Build autonomous AI systems",
                "topics": ["Agent Architecture", "Tools & Functions", "Memory", "Planning", "Multi-agent Systems", "LangChain", "AutoGPT"]
            }
        }
    },
    "03-software-architecture": {
        "01-basics": {
            "what-is-architecture": {
                "title": "What is Software Architecture",
                "description": "Understanding software architecture fundamentals",
                "topics": ["Definition", "Importance", "Architecture vs Design", "Stakeholders", "Quality Attributes", "Trade-offs"]
            },
            "architect-role": {
                "title": "Software Architect Role",
                "description": "Responsibilities and skills of an architect",
                "topics": ["Responsibilities", "Skills Required", "Decision Making", "Communication", "Leadership", "Career Path"]
            },
            "levels": {
                "title": "Architecture Levels",
                "description": "Different levels of architecture",
                "topics": ["Application Architecture", "Solution Architecture", "Enterprise Architecture", "Technical Architecture"]
            }
        },
        "02-design-patterns": {
            "README": {
                "title": "Design Patterns",
                "description": "Common software design patterns",
                "topics": ["Creational Patterns", "Structural Patterns", "Behavioral Patterns", "Architectural Patterns", "Anti-patterns"]
            }
        },
        "03-system-design": {
            "README": {
                "title": "System Design",
                "description": "Design scalable distributed systems",
                "topics": ["Requirements Analysis", "High-level Design", "Low-level Design", "Trade-offs", "Case Studies", "Interview Prep"]
            }
        },
        "04-scalability": {
            "README": {
                "title": "Scalability",
                "description": "Build systems that scale",
                "topics": ["Horizontal vs Vertical Scaling", "Load Balancing", "Caching", "Database Scaling", "Microservices", "Performance"]
            }
        },
        "05-security": {
            "README": {
                "title": "Security Architecture",
                "description": "Secure system design",
                "topics": ["Security Principles", "Authentication", "Authorization", "Encryption", "OWASP Top 10", "Compliance", "Threat Modeling"]
            }
        },
        "06-cloud-architecture": {
            "README": {
                "title": "Cloud Architecture",
                "description": "Design cloud-native applications",
                "topics": ["Cloud Patterns", "Serverless", "Containers", "Kubernetes", "Multi-cloud", "Cost Optimization", "Best Practices"]
            }
        }
    }
}

def create_readme_content(phase, section, topic, data):
    """Generate README content for a topic"""
    title = data["title"]
    description = data["description"]
    topics = data["topics"]
    
    content = f"""# {title}

> {description}

## 📚 Table of Contents

- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
- [Key Topics](#key-topics)
- [Hands-On Practice](#hands-on-practice)
- [Projects](#projects)
- [Resources](#resources)
- [Next Steps](#next-steps)

## 🎯 Introduction

{description}

### What You'll Learn

"""
    
    for t in topics:
        content += f"- ✅ {t}\n"
    
    content += f"""
### Prerequisites

- Basic understanding of previous topics
- Development environment setup
- Willingness to practice

### Time to Complete

**Estimated:** 1-2 weeks

## 🧠 Core Concepts

### Overview

This section covers the fundamental concepts you need to master {title.lower()}.

"""
    
    for i, topic_item in enumerate(topics[:3], 1):
        content += f"""### {i}. {topic_item}

**Description:** Key concepts and principles of {topic_item.lower()}.

**Why It Matters:** Understanding {topic_item.lower()} is crucial for building robust applications.

**Example:**
```
// Code example will be added here
```

"""
    
    content += f"""## 📖 Key Topics

"""
    
    for topic_item in topics:
        content += f"- [ ] {topic_item}\n"
    
    content += f"""
## 💻 Hands-On Practice

### Exercise 1: Basic Implementation
Practice the fundamentals with a simple exercise.

### Exercise 2: Intermediate Challenge
Apply concepts to a real-world scenario.

### Exercise 3: Advanced Application
Combine multiple concepts in a complex project.

## 🚀 Projects

### Project 1: Beginner
**Goal:** Build a simple application demonstrating core concepts

**Requirements:**
- Implement basic functionality
- Follow best practices
- Document your code

**Time:** 3-5 hours

### Project 2: Intermediate
**Goal:** Create a more complex application

**Requirements:**
- Multiple features
- Error handling
- Testing

**Time:** 8-12 hours

## 📚 Resources

### Documentation
- Official documentation links
- API references
- Tutorials

### Courses
- Online course recommendations
- Video tutorials
- Interactive platforms

### Books
- Recommended reading
- Reference materials

### Tools
- Development tools
- Testing frameworks
- Debugging utilities

## ✅ Checkpoint

Before moving forward, ensure you can:

"""
    
    for topic_item in topics:
        content += f"- [ ] Understand and apply {topic_item.lower()}\n"
    
    content += f"""
## 🎯 Next Steps

1. Complete all exercises
2. Build at least one project
3. Review and refactor your code
4. Move to the next topic

---

[← Back](./../README.md) | [Next Topic →](../README.md)
"""
    
    return content

def generate_all_readmes():
    """Generate README files for all topics"""
    base_path = Path(".")
    
    for phase, sections in CONTENT_STRUCTURE.items():
        print(f"\n📁 Processing {phase}...")
        
        for section, topics in sections.items():
            print(f"  📂 {section}")
            
            for topic, data in topics.items():
                topic_path = base_path / phase / section / topic
                readme_path = topic_path / "README.md"
                
                # Skip if README already exists
                if readme_path.exists():
                    print(f"    ⏭️  Skipping {topic} (already exists)")
                    continue
                
                # Create directory if it doesn't exist
                topic_path.mkdir(parents=True, exist_ok=True)
                
                # Generate content
                content = create_readme_content(phase, section, topic, data)
                
                # Write README
                with open(readme_path, 'w') as f:
                    f.write(content)
                
                print(f"    ✅ Created {topic}/README.md")
    
    print("\n✨ All README files generated successfully!")

if __name__ == "__main__":
    print("=" * 70)
    print("Software Solution Engineer Learning Path - Content Generator")
    print("=" * 70)
    generate_all_readmes()

# Made with Bob
