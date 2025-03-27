def calculate_net_salary(gross, children):
    try:
        # inputs are valid
        gross = float(gross)
        children = int(children)

        # base tax rates
        if gross < 1000:
            tax_rate = 0.10
        elif gross < 2000:
            tax_rate = 0.12
        elif gross < 4000:
            tax_rate = 0.14
        else:
            tax_rate = 0.18

        # child tax deduction
        if gross < 2000:
            tax_rate -= children * 0.01  # 1% per child
        else:
            tax_rate -= children * 0.005  # 0.5% per child

        # Calculate net salary
        net_salary = gross * (1 - tax_rate)

        return f"Net Salary: {net_salary:.2f}"

    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage:
gross_salary = 2500  # Example gross salary
num_children = 2  # Example number of children
print(calculate_net_salary(gross_salary, num_children))
