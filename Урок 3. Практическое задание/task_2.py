"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def user_info(name, surname, date_of_birth, city, email, phone_number):
    print(f"{name} {surname} {date_of_birth} года рождения, "
          f"проживает в городе {city}, адрес электронной почты: {email}, номер телефона: {phone_number}")
user_info(name= 'Семён', surname= 'Сидоров', date_of_birth= '1884', city= 'Липецк',
          email= 'sidorov_s@mail.ru', phone_number= '981-56-17')
