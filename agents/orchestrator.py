from agents.retrieval_agent import retrieve_answer
from agents.form_agent import collect_contact_info

def orchestrate(user_input):
    """
    Simple rules:
    - If input contains 'register' or 'contact', use form agent
    - Else, use RAG retrieval agent
    """
    user_input_lower = user_input.lower()

    if any(word in user_input_lower for word in ["register", "contact", "sign up", "follow up"]):
        # For demo, ask user info
        name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        interest = input("Which program are you interested in? ")
        return collect_contact_info(name, email, interest)
    else:
        return retrieve_answer(user_input)
