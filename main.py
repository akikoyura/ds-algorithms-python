def smallest_positive(in_list):
    if not in_list:
        return None
    smallest = in_list[0] if in_list[0] >= 0 else 0
    for number in in_list:
        if 0 < number < smallest:
            smallest = number
    return smallest if smallest > 0 else None


courses = {
    'spring2020': {
        'cs101': {'name': 'Building a Search Engine', 'teacher': 'Dave', 'assistant': 'Peter C.'},
        'cs373': {'name': 'Programming a Robotic Car', 'teacher': 'Sebastian', 'assistant': 'Andy'}
    },
    'fall2020': {
        'cs101': {'name': 'Building a Search Engine', 'teacher': 'Dave', 'assistant': 'Sarah'},
        'cs212': {'name': 'The Design of Computer Programs', 'teacher': 'Peter N.', 'assistant': 'Andy',
                  'prereq': 'cs101'},
        'cs253': {'name': 'Web Application Engineering - Building a Blog', 'teacher': 'Steve', 'prereq': 'cs101'},
        'cs262': {'name': 'Programming Languages - Building a Web Browser', 'teacher': 'Wes', 'assistant': 'Peter C.',
                  'prereq': 'cs101'},
        'cs373': {'name': 'Programming a Robotic Car', 'teacher': 'Sebastian'},
        'cs387': {'name': 'Applied Cryptography', 'teacher': 'Dave'}},
    'spring2044': {
        'cs001': {'name': 'Building a Quantum Holodeck', 'teacher': 'Dorina'},
        'cs003': {'name': 'Programming a Robotic Robotics Teacher', 'teacher': 'Jasper'},
    }
}


def when_offered(courses, course):
    results = []
    for key in courses:
        for value in courses[key]:
            if value == course:
                results.append(key)
    return results


if __name__ == '__main__':
    # print(smallest_positive([4, -6, 7, 2, -4, 10]))
    # print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
    # print(smallest_positive([-6, -9, -7]))
    print(smallest_positive([]))
    # print(when_offered(courses, 'cs101'))  # => ['fall2020', 'spring2020']
    # print(when_offered(courses, 'bio893'))  # => []
