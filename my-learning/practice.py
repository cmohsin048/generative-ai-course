"""First exercise: run this without an API key, then change the data."""

projects = [
    {"name": "Portfolio chatbot", "skill": "prompting"},
    {"name": "Document assistant", "skill": "retrieval"},
    {"name": "Tool assistant", "skill": "function calling"},
]

for number, project in enumerate(projects, start=1):
    print(f"{number}. {project['name']} teaches {project['skill']}.")

print("\nYour task: add a project and turn the printing loop into a function.")
