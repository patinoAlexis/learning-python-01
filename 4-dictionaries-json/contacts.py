contacts = {
    'number': 4,
    'students': [
        {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
        {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
    ]
}

print('All students available')
for student in contacts['students']:
    print(f"Email: {student.get('email')}")
