from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):

    today_data = date.today()
    today_data_week = today_data.strftime('%A')
    one_day_before_today = today_data - timedelta(days=1)
    two_days_before_today = today_data - timedelta(days=2)
    inteval_week = today_data + timedelta(days=7)

    # створюємо словник на тиждень за ключем "день"
    congratulations_dict = {current_date.strftime('%A'):[] for current_date in (today_data + timedelta(days=i) for i in range(7))}
    
    for user in users:
        user_name = user['name']
        user_birthday = user['birthday'].replace(year=today_data.year)
        user_birthday_weekday = user_birthday.strftime('%A')

        # якщо сьогодні ПН, а ДР були в минулі вихідні - треба привітати сьогодні (в ПН)
        if today_data_week == 'Monday':
            if user_birthday == one_day_before_today or user_birthday == two_days_before_today:
                congratulations_dict[today_data_week] = congratulations_dict.get(today_data_week, []) + [user_name] 
                
        # беремо інтервал 7 днів від сьогодні
        if  today_data <= user_birthday < inteval_week:
            congratulations_dict[user_birthday_weekday] = congratulations_dict.get(user_birthday_weekday, []) + [user_name]
        
        # враховуємо кінець року
        if today_data.month > user_birthday.month:
            user_birthday_next_year = user['birthday'].replace(year=today_data.year+1)
            if (user_birthday_next_year - today_data).days <= 7:
                congratulations_dict[user_birthday_weekday] = congratulations_dict.get(user_birthday_weekday, []) + [user_name]

    # переносимо "вітання" з Сб та Нд на Пн
    if congratulations_dict['Sunday'] != 0:   
        congratulations_dict['Monday'] = congratulations_dict.get('Sunday', []) + congratulations_dict.get('Monday', [])
        del congratulations_dict['Sunday']
    if congratulations_dict['Saturday'] != 0:   
        congratulations_dict['Monday'] = congratulations_dict.get('Saturday', []) + congratulations_dict.get('Monday', [])
        del congratulations_dict['Saturday']

    # робимо словник без пустих значень    
    congratulations_dict_short = {key: value for key, value in congratulations_dict.items() if value}
  
    print(congratulations_dict_short)
    return congratulations_dict_short

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 17).date()},
        {"name": "Bo Bo", "birthday": datetime(1990, 1, 14).date()},
        {"name": "Tim Tim", "birthday": datetime(1956, 2, 19).date()},
        {"name": "Poll", "birthday": datetime(2022, 5, 15).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
   
