# Gregors Lasenbergs (s1075747)


from UI import UI
from datetime import date

TODAY = str(date.today()).split("-")
today_year = int(TODAY[0])

if __name__ == '__main__':

    # Starts user interface
    new_ui = UI(today_year)
    new_ui.start_ui()
