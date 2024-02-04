import spacy


def apply_noun_verb_analysis_spacy(text):
    # Load the spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy
    doc = nlp(text)

    nouns = []
    verbs = []

    # Iterate through tokens to identify nouns and verbs
    for token in doc:
        if token.pos_ == 'NOUN':
            nouns.append(token.text.lower())
        elif token.pos_ == 'VERB':
            verbs.append(token.text.lower())

    return sorted(set(nouns)), sorted(set(verbs))


def get_interpretation():
    return """
    Entities:
        - Benefits
        - Capabilities
        - Deductions
        - Employees
        - HR
        - Managers
        - Payrolls
        - Personnel
        - Reports
        - Salaries
        - Summaries
        - Tax Deductions

    Relationships/Actions:
        - HR manages Salaries
        - HR manages Benefits
        - HR manages Tax Deductions
        - Managers allocate Payrolls
        - The system generates reports on financial summaries
        - The system generates reports on payroll processing
    """


def run():
    # Given text
    text = """
    The payroll management system enables HR personnel to efficiently manage employee payroll information, encompassing salary structures, tax deductions, and benefits. 
    Managers have the capability to allocate payrolls to employees, and the system generates reports on payroll processing and financial summaries.
    """

    # Apply noun-verb analysis using spaCy
    nouns, verbs = apply_noun_verb_analysis_spacy(text)
    interpretation = get_interpretation()

    # Print the results
    print(f"Nouns: {nouns}")
    print(f"Verbs: {verbs}")
    print(f"Interpretation: {interpretation}")


if __name__ == "__main__":
    run()