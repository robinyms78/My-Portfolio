# Template with substitution targets
reply = """
        Greetings...
        Hello %(name)s!
        Your age is %(age)s """

# Build up values to substitute
values = {"name": "Bob", "age": 40}
print(reply %values)

