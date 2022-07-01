import numpy as np

def days_month(month, leap_year):
    """
    Tar inn en mnd. gitt i tallverdi 1-12 og
    gir tilbake antall dager i den gitte mnd.
    """
    if month == 2:      # Checking month for february
        if leap_year is True:
            return 29
        else:
            return 28

    if month >= 1 and month < 8:
        if month % 2 == 0: return 30
        else: return 31

    if month >= 8 and month <= 12:
        if month % 2 == 0: return 31
        else: return 30

def is_leapyear_and_first_day(year):
    """
    2023 er et skuddår vi vet om. Dersom et år er et multiplum
    av 4 i differansen mellom skuddårene er gitt år også et skuddår.
    Året midt mellom to skuddår hopper over to dager, dvs. at
      2018: 1
      2019: 2
    * 2020: 3 (skuddår)
      2021: 5       bruker 2021 som referanseår for dette. For hvert 4 år
      2022: 6
      2023: 7 (skuddår)
      2024: 1
    og mønsteret gjentar seg

    * Funker ikke enda for år tidligere enn 2018 (kommentar - ble misforstått at 2023 er skuddår
    2024 er skuddår, blir feil å matematikken) *
    """
    ref_year = 2018
    ref_day = 1
    # Formel som jeg har loket meg frem til på ipad, aner ikke hvorfor de funker (og funker ikke før 2019)
    K = abs(year - ref_year) + (abs(year - ref_year) + ref_day) // 4
    # print(K)
    day_num = K - 7 * ((K + ref_day)//7) + ref_day
    # print(day_num)
    if abs(year - 2024) % 4 == 0:
        return True
    else: return False


def number_of_days(day, date, year_start_day, leap_year=False, year=2018):
    """
    Kode som finner antall datoer på spesifikke dager i et år.
    Første argument: Dagen med dato du ser etter
    Andre argument: Dato du ser etter
    Tredje argument: Første dagen i året (dagen som er på 1. Januar)
    """
    # Lager to dicts som inneholder tall for dagene. Mest for formatteringens skyld.
    days_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4,
                  'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'Novembre ', 12: 'December'}

    # leap_year = is_leapyear_and_first_day(year)
    day = days_dict[day]
    start_day_next_month = days_dict[year_start_day]
    super_count = 0         # Teller totalt antall dager med søkt dato
    month_list = []         # Liste som lagrer hvilke mnder som har søkte datoer
    for month in range(1, 13):          # Looper gjennom alle mnd
        G = day - start_day_next_month + 1      # G er datoen dagen man ser etter starter på i gitt mnd.
        if G < 1: G += 7
        # print(G)
        day_dates = [G]
        N_days_month = days_month(month, leap_year)     # Antall dager i en mnd
        # print(N_days_month)

        count = 0
        for days in range(0, N_days_month):
            """
            Denne loopen går gjennom datoene dagen du søker etter har i gitt mnd.
            og lagrer det i en liste.
            """
            if day_dates[days] > N_days_month:
                day_dates.remove(day_dates[days])
                # print(day_dates)
                break
            day_dates.append(day_dates[days] + 7)

        # Loop som sjekker om datoen du søker ligger i listen som inneholder alle datoene dagen har i gitt mnd.
        for k in day_dates:
            if date == k:
                count += 1
                month_list.append(month)
        # print(start_day_next_month)
        # Formel som finner hvilken dag neste mnd. starter på
        start_day_next_month = N_days_month % 7 + start_day_next_month      # Hvilken dag neste mnd. starter på (mandag, tirsdag etc.)
        if start_day_next_month > 7: start_day_next_month -= 7              # Om det går over søndag trekker vi fra 7 for å komme tilbake til (1-7)
        super_count += count

    M = [months_dict[i] for i in month_list]        # Formatterer penere
    return super_count, M, leap_year


# print(number_of_days('Friday', 13, 'Monday'))

def find_all_dates(day, date):
    days_list = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for days in days_list:
        print(number_of_days(day, date, days))
        print(number_of_days(day, date, days, True))    # Skuddår
        print()

find_all_dates('Friday', 13)

# 2026 starter på en torsdag og er ikke et skuddår, som medfører 3 fredag den 13. 
