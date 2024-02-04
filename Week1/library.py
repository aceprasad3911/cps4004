library_database = {
    "library": {
        "name": "ABC Library",
        "sections": {
            "Fiction": {
                "books": {
                    "F101": {
                        "title": "The Great Gatsby",
                        "author": "F. Scott Fitzgerald",
                        "copies_available": 5
                    },
                    "F102": {
                        "title": "To Kill a Mockingbird",
                        "author": "Harper Lee",
                        "copies_available": 3
                    },
                    "F103": {
                        "title": "1984",
                        "author": "George Orwell",
                        "copies_available": 6
                    }
                },
                "periodicals": {
                    "P101": {
                        "title": "Fiction Monthly",
                        "copies_available": 10
                    },
                    "P102": {
                        "title": "Storyteller's Digest",
                        "copies_available": 8
                    }
                }
            },
            "Non-Fiction": {
                "books": {
                    "NF201": {
                        "title": "Sapiens: A Brief History of Humankind",
                        "author": "Yuval Noah Harari",
                        "copies_available": 8
                    },
                    "NF202": {
                        "title": "The Immortal Life of Henrietta Lacks",
                        "author": "Rebecca Skloot",
                        "copies_available": 4
                    }
                },
                "periodicals": {
                    "P201": {
                        "title": "Science Today",
                        "copies_available": 12
                    },
                    "P202": {
                        "title": "National Geographic",
                        "copies_available": 7
                    }
                }
            }
        },
        "users": {
            "U001": {
                "name": "Alice",
                "borrowed_books": ["F101", "NF201"],
                "borrowed_equipment": ["Laptop"]
            },
            "U002": {
                "name": "Bob",
                "borrowed_books": ["F102", "NF202"],
                "borrowed_equipment": ["Headphones"]
            }
        },
        "facilities": {
            "study_areas": 3,
            "meeting_rooms": 1,
            "workstations": 20
        }
    }
}

# CRUD functions for Books
def create_book(section, book_id, title, author, copies_available):
    library_database["library"]["sections"][section]["books"][book_id] = {
        "title": title,
        "author": author,
        "copies_available": copies_available
    }

def read_book(section, book_id):
    return library_database["library"]["sections"].get(section, {}).get("books", {}).get(book_id, None)

def update_book(section, book_id, updates):
    book = library_database["library"]["sections"].get(section, {}).get("books", {}).get(book_id, None)
    if book:
        book.update(updates)

def delete_book(section, book_id):
    if book_id in library_database["library"]["sections"].get(section, {}).get("books", {}):
        del library_database["library"]["sections"][section]["books"][book_id]

# CRUD functions for Periodicals
def create_periodical(section, periodical_id, title, copies_available):
    library_database["library"]["sections"][section]["periodicals"][periodical_id] = {
        "title": title,
        "copies_available": copies_available
    }

def read_periodical(section, periodical_id):
    return library_database["library"]["sections"].get(section, {}).get("periodicals", {}).get(periodical_id, None)

def update_periodical(section, periodical_id, updates):
    periodical = library_database["library"]["sections"].get(section, {}).get("periodicals", {}).get(periodical_id, None)
    if periodical:
        periodical.update(updates)

def delete_periodical(section, periodical_id):
    if periodical_id in library_database["library"]["sections"].get(section, {}).get("periodicals", {}):
        del library_database["library"]["sections"][section]["periodicals"][periodical_id]

# CRUD functions for Users
def create_user(user_id, name, borrowed_books, borrowed_equipment):
    library_database["library"]["users"][user_id] = {
        "name": name,
        "borrowed_books": borrowed_books,
        "borrowed_equipment": borrowed_equipment
    }

def read_user(user_id):
    return library_database["library"]["users"].get(user_id, None)

def update_user(user_id, updates):
    user = library_database["library"]["users"].get(user_id, None)
    if user:
        user.update(updates)

def delete_user(user_id):
    if user_id in library_database["library"]["users"]:
        del library_database["library"]["users"][user_id]

# CRUD functions for Facilities
def update_facilities(study_areas=None, meeting_rooms=None, workstations=None):
    facilities = library_database["library"]["facilities"]
    if study_areas is not None:
        facilities["study_areas"] = study_areas
    if meeting_rooms is not None:
        facilities["meeting_rooms"] = meeting_rooms
    if workstations is not None:
        facilities["workstations"] = workstations


# Example Usage:
if __name__ == "__main__":
    create_book("Fiction", "F103", "1984", "George Orwell", 6)
    print("Added Book:", read_book("Fiction", "F103"))

    update_user("U001", {"name": "Alicia"})
    print("Updated User:", read_user("U001"))

    delete_periodical("Non-Fiction", "P201")
    print("Deleted Periodical:", read_periodical("Non-Fiction", "P201"))

    update_facilities(study_areas=5, workstations=25)
    print("Updated Facilities:", library_database["library"]["facilities"])