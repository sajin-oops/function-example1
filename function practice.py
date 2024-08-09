def display_invoice(username, amount , due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount:.2f} is due:{due_date}")

display_invoice("Sajin",100.3333, "21/01/2003")

#O/P

'''
Hello Sajin
Your bill of $100.33 is due:21/01/2003

'''