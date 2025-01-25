###python - Altersberechnung in Jahren, Tagen, Minuten, Sekunden
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():

   birth_date_str = input("Geburtsdatum (Format: JJJJ-MM-TT): ")
   birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
   age = calculate_age(birth_date)

   print(f"Alter in Jahren: {age}")
   print(f"Alter in Tagen: {age * 365}")
   print(f"Alter in Stunden: {age * 365 * 24}")
   print(f"Alter in Minuten: {age * 365 * 24 * 60}")
   print(f"Alter in Sekunden: {age * 365 * 24 * 60 * 60}")

if __name__ == "__main__":
    main()
