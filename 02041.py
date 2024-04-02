
# Домашнее задание:
# 2. Написать тест по математике.
#    генерить примеры на +, -, *
#    проверки хранить в виде функций
#    к функции проверки обращаться по ключу-действию, собрав их в словарь!
#    внешний цикл предлагает решить ещё один пример, либо завершить тест.
#    выводится статистика.
import random
def math_test():
    correct_answers = 0
    total_questions = 0
    continue_test = True
    
    while continue_test:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
        
        print(f" {number1} {operation} {number2}?")
        
        user_answer = input("Напишите ваш ответ: ")
        
        if user_answer.isdigit(): #Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.

            user_answer = int(user_answer)
            if (operation == '+' and number1 + number2 == user_answer) or (operation == '-' and number1 - number2 == user_answer):
                print("Правильно!")
                correct_answers += 1
            else:
                print("Неправильно!")
            total_questions += 1
        else:
            print("Не верно. Попробуйте еще раз")
        
        choice = input("Хотите попробовать решить еще один пример? (да/нет): ")
        continue_test = 'да' in choice 

    print(f"Вы ответили {correct_answers} из {total_questions} вопросов правильно.")
math_test() #обращаюсь к функции

