# Project: Employee Information Formatter
# Created by: Qazi Azan
# Language: Python
print("===== Employee Information Formatter =====")
email = input("enter your email address:")
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

messy_name = input("enter your name:")
print(f"Original name: '{messy_name}'")

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

messy_email = email
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

phone = input("enter your phone number:")
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

full_address = input("enter your address:")
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

employee_code = input("enter your employee code:")
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

print('Dots in email:',dot_count)
print('Dashes in code:',dash_count)