"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def string(str1, str2):
      if type(str1) != str and type(str2) != str:
        return 0 
      elif str1 == str2:
        return 1 
      elif len(str1) > len(str2):
        return 2
      elif "learn" in str2:
        return 3
      else:
        return "TypeError"
    
    new_string = string("milk", "learn")
    print(new_string)
    new_string = string("juice", "milk")
    print(new_string)
    new_string = string(7, 5)
    print(new_string)
    new_string = string("milk", "milk")
    print(new_string)

if __name__ == "__main__":
  main()

    
      
    

