def collect_contact_info(name, email, interest):
    """
    Simulates storing user contact info.
    For demo purposes, we just print it.
    """
    # You could also write to a CSV for demo/admin view
    with open("contacts.csv", "a", encoding="utf-8") as f:
        f.write(f"{name},{email},{interest}\n")
    return "Thank you! Your contact details have been recorded. We will get back to you soon."
