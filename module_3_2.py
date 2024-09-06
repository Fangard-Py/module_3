
def send_email(message, recipient, sender='university.help@gmail.com'):

    print(input(f'Введите адрес электронной почты: '))
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    elif not recipient.endswith(('.ru', '.com', '.net')):
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    elif not sender.endswith(('.ru', '.com', '.net')):
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',sender, 'на адрес', recipient)
    return message


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
