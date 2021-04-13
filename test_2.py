from openpyxl import Workbook
user_database = Workbook()
user_database.save(filename='User_data_file.xlsx')
def new_sheet(username):
    user_data_sheet = user_database.create_sheet(username)

new_sheet('darsna19')

def tot_cal_mark1(num_food_items, cuisine):
    for food_num in range(num_food_items):
      globals()["food_" + str(food_num)] = [input("Enter the food item name: "), int(input("Number of servings: "))]
    start = 0
    for i in range(2,len(cuisine['A'])):
      for j in range(num_food_items):
        if globals()["food_" + str(j)][0] == cuisine['A'+str(i+1)].value:
            start += globals()["food_" + str(j)][1]*cuisine['B'+str(i+1)].value
    print('the number of calories consumed is, {}'.format(start) + ' KCal')
    total_calories = start
    return total_calories

print(tot_cal_mark1(4,'South'))