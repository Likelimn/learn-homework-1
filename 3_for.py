"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
 [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара sum
* Посчитать и вывести среднее количество продаж для каждого товара 
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sale = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    def count_phones(phone_scores):
      phone_sum = 0
      for score in phone_scores:
        phone_sum += score
      return sum(phone_scores)

    phone_avg = 0
    phone_avg2 = 0
    phone_avg3 = 0
    for one_phone in sale:
      summa =  count_phones(one_phone["items_sold"])
      print(f'{one_phone["product"]} - продано {summa} штук')
      phone_avg += summa
      phones_avg = round(summa / len(one_phone["items_sold"]), 2)  
      print(f'Среднее количество продаж {one_phone["product"]}: {phones_avg}')
      phone_avg2 += summa
      phone_avg3 += summa
      phone_avg3 = phone_avg2  / len(sale)
    print(f'Суммарное количество продаж всех товаров: {phone_avg2}')
    print(f'Среднее количество продаж всех товаров: {phone_avg3}')



  
    #def count_phone_avg(phone_scores_avg):
     # phone_avg = 0
      #for score_avg in phone_scores_avg:
       # phone_avg += score_avg
        #return round(summa / len(phone_scores_avg), 2) 

    #all_avg_sum = 0
    #for one_phone_avg in sale:
    #  avg = count_phone_avg(one_phone_avg["items_sold"])
     # print(f'Среднее количество продаж {one_phone_avg["product"]}: {avg}')
      #all_avg_sum += avg
   # print()


if __name__ == "__main__":
  main()

