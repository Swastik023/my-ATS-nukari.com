import spacy

nlp = spacy.load('en_core_web_sm')

def parse_resume(resume_text):
    doc = nlp(resume_text)
    skills = []
    experiences = []
    education = []

        # Example entities extraction (you can customize this based on your needs)
    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            skills.append(ent.text)
        elif ent.label_ == 'ORG' and 'University' in ent.text:
            education.append(ent.text)
        elif ent.label_ == 'WORK_OF_ART':  # Assuming WORK_OF_ART is used to tag experience roles
            experiences.append(ent.text)

    return {
        'skills': skills,
        'experiences': experiences,
        'education': education
    }

# Example usage
if __name__ == "__main__":
    resume_text = """
    John Doe is a software engineer with 5 years of experience in Python, Django, and Flask.
    He graduated from MIT University with a degree in Computer Science. His work experience includes developing
    RESTful APIs, working with AWS, and managing databases using PostgreSQL.
    """
    parsed_data = parse_resume(resume_text)
    print("Skills:", parsed_data['skills'])
    print("Experiences:", parsed_data['experiences'])
    print("Education:", parsed_data['education'])
