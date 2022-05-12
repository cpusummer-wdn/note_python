from base64 import b16decode
from doctest import TestResults
from gettext import npgettext
from ntpath import join
from optparse import Values
from os import popen
from platform import java_ver
from random import shuffle
from socket import SO_VM_SOCKETS_BUFFER_MAX_SIZE
from tarfile import PAX_NAME_FIELDS
from tkinter import Y
from turtle import pd

关于 python 第三方库的安装最好少使用 easy_install，因为 easy_install 只能安装不能卸载，如果要卸载需要进入到 python 的安装目录下面的 lib 的文件夹下手动删除对应的模块内容。所以建议多用 pip 的方式安装，安装时，用 pip install + 模块名称 命令来安装，卸载时，用 pip uninstall +模块名称 命令来删除。
******基础教程*******
https://docs.python.org/zh-cn/3/tutorial/index.html

方法调用 实参变量名.方法名
函数调用 函数名(实参变量名)


字符串
拼接字符串
first_name = "ada" 
last_name = "lovelace" 
full_name = first_name + " " + last_name 
print("Hello, " + full_name.title() + "!")
Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip()


数字
数字转字符串
age = 23 
message = "Happy " + str(age) + "rd Birthday!" 
print(message)

列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
如果你让Python将列表打印出来，Python将打印列表的内部表示，包括方括号
访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
message = "My first bicycle was a " + bicycles[0].title() + "." 
print(message)


append函数
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles.append('ducati') 
print(motorcycles)

insert函数
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') 
print(motorcycles)

删除元素 del pop
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[0] 
print(motorcycles)
方法pop() 可删除列表末尾的元素
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
popped_motorcycle = motorcycles.pop()  
print(motorcycles) 
print(popped_motorcycle)
用pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可
motorcycles = ['honda', 'yamaha', 'suzuki'] 
first_owned = motorcycles.pop(0) 
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
根据值删除元素 remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] print(motorcycles) 
motorcycles.remove('ducati') print(motorcycles)

sort 永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru'] ❶ cars.sort() print(cars)
sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru'] ❶ print("Here is the original list:") print(cars) ❷ print("\nHere is the sorted list:") print(sorted(cars)) ❸ print("\nHere is the original list again:") print(cars)

反转列表元素的排列顺序，可使用方法reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru'] print(cars) cars.reverse() print(cars)
函数len() 可快速获悉列表的长度
 cars = ['bmw', 'audi', 'toyota', 'subaru'] 
len(cars)

访问最后一个列表元素时使用索引-1 
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[-1])
'suzuki'
仅当列表为空时，-1访问才会导致错误

遍历整个列表
❶ magicians = ['alice', 'david', 'carolina'] ❷ for magician in magicians: ❸ print(magician)

Python根据缩进来判断代码行与前一个代码行的关系。在前面的示例中，向各位魔术师显示消息的代码行是for 循环的一部分，因为它们缩进了。

for value in range(1,5): 
    print(value)

创建数字列表 使用函数list() 将range() 的结果直接转换为列表
numbers = list(range(1,6)) print(numbers)
指定步长为2
even_numbers = list(range(2,11,2)) print(even_numbers)
[2, 4, 6, 8, 10]

在Python中，两个星号（** ）表示乘方运算
❶ squares = [] ❷ for value in range(1,11): ❸ square = value**2 ❹ squares.append(square) ❺ print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
简写上面的代码
squares = []
for value in range(1,11): 
     squares.append(value**2) 
print(squares)

对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits) 
max(digits) 
sum(digits)

列表解析 
将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value**2 for value in range(1,11)] 
print(squares)

切片
要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
如果你没有指定第一个索引，Python将自动从列表开头开始： 
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[:4])
切片终止于列表末尾
players = ['charles', 'martina', 'michael', 'florence', 'eli'] print(players[2:])
遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli'] print("Here are the first three players on my team:") 
for player in players[:3]: 
    print(player.title())

复制列表 复制列表必须使用切片 friend_foods = my_foods[:]
❶ my_foods = ['pizza', 'falafel', 'carrot cake'] ❷ friend_foods = my_foods[:] print("My favorite foods are:") print(my_foods) print("\nMy friend's favorite foods are:") print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake'] ❶ friend_foods = my_foods[:] ❷ my_foods.append('cannoli') ❸ friend_foods.append('ice cream') print("My favorite foods are:") print(my_foods) print("\nMy friend's favorite foods are:") print(friend_foods)

元组
Python将不能修改的值称为不可变的 不 ，而不可变的列表被称为元组 使用圆括号定义
❶ dimensions = (200, 50) ❷ print(dimensions[0]) print(dimensions[1])
元组不可修改
dimensions = (200, 50) ❶ dimensions[0] = 250 报错
遍历元组中的所有值
dimensions = (200, 50) for dimension in dimensions: print(dimension)

修改元组变量 修 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组： 
dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions: 
    print(dimension)  
dimensions = (400, 100) #定义了一个新元组
    print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)

PEP 8建议每级缩进都使用四个空格

要将程序的不同部分分开，可使用空行

cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars: 
    if car == 'bmw': 
        print(car.upper()) 
    else:
        print(car.title())

if 检查是否相等时不考虑大小写

使用使 and 检查多个条件
age_0 >= 21 and age_1 >= 21 
为改善可读性，可将每个测试都分别放在一对括号内
(age_0 >= 21) and (age_1 >= 21)
使用使 or 检查多个条件

检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
'mushrooms' in requested_toppings

检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie' 
if user not in banned_users: 
    print(user.title() + ", you can post a response if you wish.")

if-elif-else 结构
if age < 4: 
    print("Your admission cost is $0.") 
elif age < 18: 
    print("Your admission cost is $5.")
else:print("Your admission cost is $10.")

使用使 if 语句处理列表
检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers': 
        print("Sorry, we are out of green peppers right now.") 
    else:print("Adding " + requested_topping + ".") 
        print("\nFinished making your pizza!")
确定列表不是空的
requested_toppings = []  
if requested_toppings: 
    for requested_topping in requested_toppings: 
        print("Adding " + requested_topping + ".") 
        print("\nFinished making your pizza!") 
    else:print("Are you sure you want a plain pizza?")

字典
字典是一系列键—值对值 。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的 值可以是数字、字符串、列表乃至字典
字典用放在花括号{} 中的一系列键—值对表示
alien_0 = {'color': 'green', 'points': 5}
访问字典中的值
alien_0 = {'color': 'green'} 
print(alien_0['color']) 这将返回字典alien_0 中与键'color' 相关联的值
添加键—值对
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0) 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 
创建空字典再添加元素
alien_0 = {} 
alien_0['color'] = 'green' 
alien_0['points'] = 5 
print(alien_0)
修改字典中的值
alien_0 = {'color': 'green'} 
print("The alien is " + alien_0['color'] + ".") 
alien_0['color'] = 'yellow' 
print("The alien is now " + alien_0['color'] + ".")
删除键值对
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0) 
del alien_0['points'] 
print(alien_0)
遍历所有的键值对 可声明两个变量key value，用于存储键—值对中的键和值
user_0 = { 
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi', } 
for key, value in user_0.items(): 
    print("\nKey: " + key)
    print("Value: " + value)
遍历字典中的所有键
favorite_languages = { 
    'jen': 'python', 
    'sarah':'c', 
    'edward':'ruby', 
    'phil': 'python', }  
for name in favorite_languages.keys(): 
    print(name.title())
按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
遍历字典中的所有值
for language in favorite_languages.values():

set集合 类似列表 但是每个元素必须独一无二 
for language in set(favorite_languages.values()): 
    print(language.title()) 结果是一个不重复的列表

嵌套
将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
字典列表
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens: 
    print(alien)


# 创建一个用于存储外星人的空列表 
aliens = [] 
# 创建30个绿色的外星人
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) 
# 显示前五个外星人 
for alien in aliens[:5]: 
    print(alien) print("...")
# 显示创建了多少个外星人  
print("Total number of aliens: " + str(len(aliens)))


在字典中存储列表
# 存储所点比萨的信息 
pizza = { 'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], } 
# 概述所点的比萨 
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']: 
    print("\t" + topping)

input()函数默认输入为字符串 用int() 将这个字符串转换成了数值表示
age = input("How old are you? ")
age = int(age)

求模运算符（%）

while 循环

使用标志 用于判断整个程序是否处于活动状态
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 

active = True 把这个标志命名为active （可给它指定任何名称），它将用于判断程序是否应继续运行
while active: 
    message = input(prompt) 
if message == 'quit': 
    active = False 
else:print(message)

函数
def greet_user(username):
    print("Hello, " + username.title() + "!") 
greet_user('jesse')
定义函数
def describe_pet(animal_type, pet_name): 
    print("\nI have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".") 
传递实参
describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
给形参animal_type指定了默认值
def describe_pet(pet_name, animal_type='dog'): 
    print("\nI have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".") 
describe_pet(pet_name='willie')

结合实例来学习
def get_formatted_name(first_name, last_name): 
    full_name = first_name + ' ' + last_name 
    return full_name.title() 
while True: 
    print("\nPlease tell me your name:") 
    print("(enter 'q' at any time to quit)") 
    f_name = input("First name: ") 
    if f_name == 'q': 
        break 
    l_name = input("Last name: ") 
    if l_name == 'q': 
        break 
    formatted_name = get_formatted_name(f_name, l_name) 
    print("\nHello, " + formatted_name + "!")

传入列表
def greet_users(names):
    for name in names: 
        msg = "Hello, " + name.title() + "!" print(msg) 
usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)

将函数存储在模块中
将函数存储在被称为模块的独立文件中， 再将模块导入到主程序中。
import 语句允许在当前运行的程序文件中使用模块中的代码。
模块是扩展名为.py的文件，包含要导入到程序中的代码

创建模块
def make_pizza(size, *toppings): 
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:") 
for topping in toppings: 
    print("- " + topping)
导入模块
import pizza
pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
导入模块中的函数
from module_name import function_name
用 as 给函数指定别名
from pizza import make_pizza as mp

类
class Dog():
    def __init__(self, name, age):
        self.name = name self.age = age 
    def sit(self):
        print(self.name.title() + " is now sitting.") 
    def roll_over(self): 
        print(self.name.title() + " rolled over!")
根据类创建实例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")

Python标准库

使用模块json 来存储数据
使用 json.dump() 和json.load()
使用json.dump() 来存储数字列表
import json numbers = [2, 3, 5, 7, 11, 13] ❶ filename = 'numbers.json' ❷ with open(filename, 'w') as f_obj: ❸ json.dump(numbers, f_obj)
使用json.load() 将这个列表读取到内存中
import json ❶ filename = 'numbers.json' ❷ with open(filename) as f_obj: ❸ numbers = json.load(f_obj) print(numbers)

重构函数


项目** 数据可视化
import matplotlib
import matplotlib.pyplot as plt 
squares = [1, 4, 9, 16, 25] 
plt.plot(squares) 
plt.show()
import matplotlib.pyplot as plt 
squares = [1, 4, 9, 16, 25] 
plt.plot(squares, linewidth=5) 
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
plt.tick_params(axis='both', labelsize=14) 
plt.show()

import matplotlib.pyplot as plt 
x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values] 
plt.scatter(x_values, y_values, s=40) 
# 设置图表标题并给坐标轴加上标签 
#  # 设置每个坐标轴的取值范围 
plt.axis([0, 1100, 0, 1100000]) 
plt.show()

使用Pygal来创建直方图

读取数据
import csv filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader) 
    print(header_row)
导入模块csv 后，我们将要使用的文件的名称存储在filename 中。接下来，我们打开这个文件，并将结果文件对象存储在f 中（见❶）。然后，我们调用csv.reader() ， 并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader ）对象（见❷）。我们将这个阅读器对象存储在reader 中。 模块csv 包含函数next() ，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。在前面的代码中，我们只调用了next() 一次，因此得到的是文件的第一行，其中 包含文件头（见❸）。我们将返回的数据存储在header_row 中。
打印文件头
for index, column_header in enumerate(header_row): 
    print(index, column_header
创建了一个名为highs 的空列表（见❶），再遍历文件中余下的各行（见❷）。阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一 行。由于我们已经读取了文件头行，这个循环将从第二行开始——从这行开始包含的是实际数据。每次执行该循环时，我们都将索引1处（第2列）的数据附加到highs 末尾
提取了每天的最高气温，并将它们作为字符串整洁地存储在一个列表中。
highs = [] 
for row in reader: 
    highs.append(row[1]) 
    print(highs)
使用int() 将这些字符串转换为数字，让matplotlib能够读取它们
highs = [] 
for row in reader:
    high = int(row[1]) 
    highs.append(high) 
    print(highs)
将最高气温列表传给plot() ，并传递c='red' 以便将数据点绘制为红色（红色显示最高气温，蓝色显示最低气温）。
import csv from matplotlib import pyplot as plt
fig = plt.figure(dpi=128, figsize=(10, 6)) 
plt.plot(highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24) 
plt.xlabel('', fontsize=16) 
plt.ylabel("Temperature (F)", fontsize=16) 
plt.tick_params(axis='both', which='major', labelsize=16) 
plt.show()
读取该数据时，获得的是一个字符串，使用模块datetime中的方法strptime()将字符串'2014-7-1' 转换为一个表示相应日期的对象
from datetime import datetime 
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
在❶处，我们添加了空列表lows ，用于存储最低气温。接下来，我们从每行的第4列（row[3] ）提取每天的最低气温，并存储它们（见❷）。在❸处，我们添加了一个 对plot() 的调用，以使用蓝色绘制最低气温。最后，我们修改了标题（见❹）
# 从文件中获取日期、最高气温和最低气温 
filename = 'sitka_weather_2014.csv' 
with open(filename) as f: 
    reader = csv.reader(f) 
    header_row = next(reader) 
    
    dates, highs, lows = [], [], [] 
    for row in reader: 
        current_date = datetime.strptime(row[0], "%Y-%m-%d") 
        dates.append(current_date) 

        high = int(row[1]) 
        highs.append(high)  

        low = int(row[3]) 
        lows.append(low) 
# 根据数据绘制图形 
fig = plt.figure(dpi=128, figsize=(10, 6)) 
plt.plot(dates, highs, c='red') 
plt.plot(dates, lows, c='blue') 
# 设置图形的格式 
plt.title("Daily high and low temperatures - 2014", fontsize=24)


*制作世界人口地图： 制 JSON格式格
我们首先导入了模块json ，以便能够正确地加载文件中的数据，然后，我们将数据存储在pop_data 中（见❶）。函数json.load() 将数据转换为Python能够处理的格式， 这里是一个列表。在❷处，我们遍历pop_data 中的每个元素。每个元素都是一个字典，包含四个键—值对，我们将每个字典依次存储在pop_dict 中。 在❸处，我们检查字典的'Year' 键对应的值是否是2010（由于population_data.json中的值都是用引号括起的，因此我们执行的是字符串比较）。如果年份为2010，我们就将 与'Country Name' 相关联的值存储到country_name 中，并将与'Value' 相关联的值存储在population 中（见❹）。
import json 
# 将数据加载到一个列表中 
filename = 'population_data.json' 
with open(filename) as f: 
    pop_data = json.load(f) 
# 打印每个国家2010年的人口数量 
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name'] 
        population = pop_dict['Value'] 
        print(country_name + ": " + population)
Python不能直接将包含小数点的字符串'1127437398.85751' 转换为整数（这个小数值可能是人 口数据缺失时通过插值得到的）。为消除这种错误，我们先将字符串转换为浮点数，再将浮点数转换为整数
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010': 
        country = pop_dict['Country Name'] 
        population = int(float(pop_dict['Value'])) 
        print(country + ": " + str(population))
获取两个字母的国别码
Pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，以及用数字表示人口数量。处理地理政治数据时，经常需要用到几个标准化国别码集。population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。我们需要想办法根据国家名获取两个字母的国别码。 Pygal使用的国别码存储在模块i18n （internationalization的缩写）中。字典COUNTRIES 包含的键和值分别为两个字母的国别码和国家名。要查看这些国别码，可从模块i18n 中导 入这个字典，并打印其键和值：
for 循环中，Python将键按字母顺序排序
from pygal.i18n import COUNTRIES 
for country_code in sorted(COUNTRIES.keys()): 
    print(country_code, COUNTRIES[country_code])
编写一个函数，它在COUNTRIES 中查找并返回国别码
from pygal.i18n import COUNTRIES 
def get_country_code(country_name): 
    for code, name in COUNTRIES.items(): 
        if name == country_name: 
            return code 
    return None print(get_country_code('Andorra')) 
print(get_country_code('United Arab Emirates')) 
print(get_country_code('Afghanistan'))
接下来 导入函数get_country_code 在world_population.py中导入get_country_code
import json from country_codes 
import get_country_code
# 打印每个国家2010年的人口数量 
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010': 
        country_name = pop_dict['Country Name'] 
        population = int(float(pop_dict['Value'])) 
        code = get_country_code(country_name) 
        if code: 
            print(code + ": "+ str(population)) 
        else:
            print('ERROR - ' + country_name)
制作世界地图
Pygal提供了图表类型Worldmap ，可帮助你制作呈现各国数据的世界地图
在❶处，我们创建了一个Worldmap 实例，并设置了该地图的的title 属性。在❷处，我们使用了方法add() ，它接受一个标签和一个列表，其中后者包含我们要突出的国家 的国别码。每次调用add() 都将为指定的国家选择一种新颜色，并在图表左边显示该颜色和指定的标签。我们要以同一种颜色显示整个北美地区，因此第一次调用add() 时， 在传递给它的列表中包含'ca' 、'mx' 和'us' ，以同时突出加拿大、墨西哥和美国。接下来，对中美和南美国家做同样的处理。 ❸处的方法render_to_file() 创建一个包含该图表的.svg文件，你可以在浏览器中打开它。输出是一幅以不同颜色突出北美、中美和南美的地图
import pygal
wm = pygal.Worldmap() 
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us']) 
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv']) 
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've']) 
wm.render_to_file('americas.svg')
在世界地图上呈现数字数据
首先，创建了一个Worldmap 实例并设置了标题。接下来，使用了方法add() ，但这次通过第二个实参传递了一个字典而不是列表（见❶）。这个字典将两个字母的Pygal国别 码作为键，将人口数量作为值。Pygal根据这些数字自动给不同国家着以深浅不一的颜色（人口最少的国家颜色最浅，人口最多的国家颜色最深），
import pygal wm = pygal.Worldmap() 
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000}) 
wm.render_to_file('na_populations.svg')
首先导入了pygal 。在❶处，我们创建了一个空字典，用于以Pygal要求的格式存储国别码和人口数量。在❷处，如果返回了国别码，就将国别码和人口数量分别作为键和值 填充字典cc_populations 。我们还删除了所有的print 语句。 在❸处，我们创建了一个Worldmap 实例，并设置其title 属性。在❹处，我们调用了add() ，并向它传递由国别码和人口数量组成的字典。
import json 
import pygal 
from country_codes import get_country_code 
cc_populations = {} 
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010': 
        country = pop_dict['Country Name'] 
        population = int(float(pop_dict['Value'])) 
        code = get_country_code(country) 
        if code: 
            cc_populations[code] = population 
wm = pygal.Worldmap() 
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations) 
wm.render_to_file('world_population.svg')
根据人口数量将国家分组
创建了三个空字典（见❶）。接下来，遍历cc_populations ，检查每个国家的人口数量（见❷）。if-elif-else 代码块将每个国别码-人口数量对加 入到合适的字典（cc_pops_1 、cc_pops_2 或cc_pops_3 ）中。 在❸处，我们打印这些字典的长度，以获悉每个分组的规模。绘制地图时，我们将全部三个分组都添加到Worldmap 中
cc_populations = {} 
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010': 
        country = pop_dict['Country Name'] 
        population = int(float(pop_dict['Value'])) 
        code = get_country_code(country)
        if code: 
            cc_populations[code] = population 
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {} 
for cc, pop in cc_populations.items(): 
    if pop < 10000000: 
        cc_pops_1[cc] = pop 
    elif pop < 1000000000: 
        cc_pops_2[cc] = pop 
    else:
        cc_pops_3[cc] = pop 
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3)) 
wm = pygal.Worldmap() 
wm.title = 'World Population in 2010, by Country' 
wm.add('0-10m', cc_pops_1) 
wm.add('10m-1bn', cc_pops_2) 
wm.add('>1bn', cc_pops_3) 
wm.render_to_file('world_population.svg')
Pygal样式存储在模块style 中，我们从这个模块中导入了样式RotateStyle
import json 
import pygal 
from pygal.style import RotateStyle
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {} 
for cc, pop in cc_populations.items(): 
    if pop < 10000000: 
        --snip-- 
wm_style = RotateStyle('#336699') 
wm = pygal.Worldmap(style=wm_style) 
wm.title = 'World Population in 2010, by Country' 
加亮颜色主题
用LightColorizedStyle类加亮地图的颜色
先导入然后就可以使用LightColorizedStyle
from pygal.style import LightColorizedStyle
wm_style = LightColorizedStyle
然而使用这个类时，你不能直接控制使用的颜色，Pygal将选择默认的基色。要设置颜色，可使用RotateStyle ，并将LightColorizedStyle 作为基本样式。为此，导 入LightColorizedStyle 和RotateStyle,再使用RotateStyle 创建一种样式，并传入另一个实参base_style 同时根据通过实参传递的颜色给各个国家着色
#from pygal.style import LightColorizedStyle, RotateStyle
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
wm_style = RS('#336699', base_style=LCS)

使用API:网络爬虫
Web API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。请求的数据将以易于处理的格式（如JSON或CSV）返回。依赖于外部数据源的大多数应用程序都依赖于API调用，如集成社交媒体网站的应用程序。
我们将编写一个程序，它自动下载GitHub上星级最高的Python项目的 信息，并对这些信息进行可视化。
repositories 后面的问号指出我们要传递一个实参。q 表示查询，而等号让我们能够开始指定查询（q= ）。通过使用language:python ，我们指出只想获取主要语言为 Python的仓库的信息。最后一部分（&sort=stars ）指定将项目按其获得的星级进行排序。
https://api.github.com/search/repositories?q=language:python&sort=stars
requests包让Python程序能够轻松地向网站请求信息以及检查返回的响应。
$ pip install --user requests
编写一个程序，它执行API调用并处理结果，找出GitHub上星级最高的Python项目
存储API调用的URL，然后使用requests 来执行调用（见❸）。我们调用get() 并将URL传递给它，再将响应对象存储在 变量r 中。响应对象包含一个名为status_code 的属性，它让我们知道请求是否成功了（状态码200表示请求成功）。在❹处，我们打印status_code ，核实调用是否成功 了。这个API返回JSON格式的信息，因此我们使用方法json() 将这些信息转换为一个Python字典（见❺）。我们将转换得到的字典存储在response_dict 中。 最后，我们打印response_dict 中的键。
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
r = requests.get(url)
print("Status code:", r.status_code) 
response_dict = r.json() 使用方法json() 将这些信息转换为一个Python字典
print(response_dict.keys())
将API调用返回的信息存储到字典中后，就可以处理这个字典中的数据了
在❶处，我们打印了与'total_count' 相关联的值，它指出了GitHub总共包含多少个Python仓库。 与'items' 相关联的值是一个列表，其中包含很多字典，而每个字典都包含有关一个Python仓库的信息。在❷处，我们将这个字典列表存储在repo_dicts 中。接下来，我们 打印repo_dicts 的长度，以获悉我们获得了多少个仓库的信息。 为更深入地了解返回的有关每个仓库的信息，我们提取了repo_dicts 中的第一个字典，并将其存储在repo_dict 中（见❸）。接下来，我们打印这个字典包含的键数，看看 其中有多少信息（见❹）。在❺处，我们打印这个字典的所有键，看看其中包含哪些信息。
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
r = requests.get(url) 
print("Status code:", r.status_code) 
response_dict = r.json()  
print("Total repositories:", response_dict['total_count']) 

repo_dicts = response_dict['items'] 
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0] 
print("\nKeys:", len(repo_dict)) 
for key in sorted(repo_dict.keys()): 
    print(key)

打印表示第一个仓库的字典中与很多键相关联的值。
在❶处，我们打印了项目的名称。项目所有者是用一个字典表示的，因此在❷处，我们使用键owner 来访问 表示所有者的字典，再使用键key 来获取所有者的登录名。在❸处，我们打印项目获得了多少个星的评级，以及项目在GitHub仓库的URL。接下来，我们显示项目的创建时间 （见❹）和最后一次更新的时间（见❺）。
print("\nSelected information about first repository:") 
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count']) 
print('Repository:', repo_dict['html_url']) 
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at']) 
print('Description:', repo_dict['description'])
编写一个循环，打印API调用返回的每个仓库的特定信息,遍历repo_dicts 中的所有字典。
print("\nSelected information about each repository:")
for repo_dict in repo_dicts: 
    print('\nName:', repo_dict['name']) 
    print('Owner:', repo_dict['owner']['login']) 
    print('Stars:', repo_dict['stargazers_count'])
     print('Repository:', repo_dict['html_url']) 
     print('Description:', repo_dict['description'])
使用Pygal可视化仓库
我们首先导入了pygal 以及要应用于图表的Pygal样式。接下来，打印API调用响应的状态以及找到的仓库总数，以便获悉API调用是否出现了问题。我们不再打印返回的有关项目 的信息，因为将通过可视化来呈现这些信息。 在❶处，我们创建了两个空列表，用于存储将包含在图表中的信息。我们需要每个项目的名称，用于给条形加上标签，我们还需要知道项目获得了多少个星，用于确定条形的高 度。在循环中，我们将项目的名称和获得的星数附加到这些列表的末尾❷。 接下来，我们使用LightenStyle 类（别名LS ）定义了一种样式，并将其基色设置为深蓝色（见❸）。我们还传递了实参base_style ，以使用LightColorizedStyle 类（别名LCS ）。然后，我们使用Bar() 创建一个简单的条形图，并向它传递了my_style （见❹）。我们还传递了另外两个样式实参：让标签绕x 轴旋转45度 （x_label_rotation=45 ），并隐藏了图例（show_legend=False ），因为我们只在图表中绘制一个数据系列。接下来，我们给图表指定了标题，并将属性x_labels 设置为列表names 。 由于我们不需要给这个数据系列添加标签，因此在❺处添加数据时，将标签设置成了空字符串。
import requests 
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS  
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star' 
r = requests.get(URL) 
print("Status code:", r.status_code) 
response_dict = r.json() 
print("Total repositories:", response_dict['total_count']) 
repo_dicts = response_dict['items'] 
names, stars = [], [] 
for repo_dict in repo_dicts:
    names.append(repo_dict['name']) 
    stars.append(repo_dict['stargazers_count']) 
# 可视化 
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) 
chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names
chart.add('', stars) 
chart.render_to_file('python_repos.svg')
我们创建了一个Pygal类Config 的实例，并将其命名为my_config 。通过修改my_config 的属性，可定制图表的外观。在❷处，我们设置了两个属性 ——x_label_rotation 和show_legend ，它们原来是在创建Bar 实例时以关键字实参的方式传递的。在❸处，我们设置了图表标题、副标签和主标签的字体大小。在这个 图表中，副标签是 x 轴上的项目名以及 y 轴上的大部分数字。主标签是 y 轴上为5000整数倍的刻度 这些标签应更大，以与副标签区分开来。在❹处，我们使 用truncate_label 将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）。接下来，我们将show_y_guides 设置为False ，以隐藏图表中的水平线（见❺）。最后，在❻处设置了自定义宽度，让图表更充分地利用浏览器中的可用空间。 在❼处创建Bar 实例时，我们将my_config 作为第一个实参，从而通过一个实参传递了所有的配置设置。我们可以通过my_config 做任意数量的样式和配置修改，而❼处的 代码行将保持不变。
my_style = LS('#333366', base_style=LCS) 
my_config = pygal.Config() 
my_config.x_label_rotation = 45 
my_config.show_legend = False 
my_config.title_font_size = 24 
my_config.label_font_size = 14 
my_config.major_label_font_size = 18 
my_config.truncate_label = 15 
my_config.show_y_guides = False 
my_config.width = 1000 
chart = pygal.Bar(my_config, style=my_style) 
chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names 
chart.add('', stars) 
chart.render_to_file('python_repos.svg')
添加自定义工具提示
在Pygal中，将鼠标指向条形将显示它表示的信息，这通常称为工具提示
在❶处，我们定义了一个名为plot_dicts 的列表，其中包含三个字典，分别针对项目HTTPie、Django和Flask。每个字典都包含两个键：'value' 和'label' 。Pygal根据与 键'value' 相关联的数字来确定条形的高度，并使用与'label' 相关联的字符串给条形创建工具提示。例如，❷处的第一个字典将创建一个条形，用于表示一个获得了16101 颗星、工具提示为Description of httpie的项目。 方法add() 接受一个字符串和一个列表。这里调用add() 时，我们传入了一个由表示条形的字典组成的列表（plot_dicts ）（见❸）。图17-3显示了一个工具提示：除默认 工具提示（获得的星数）外，Pygal还显示了我们传入的自定义提示。
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 
my_style = LS('#333366', base_style=LCS) 
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) 
chart.title = 'Python Projects' 
chart.x_labels = ['httpie', 'django', 'flask'] 
plot_dicts = [ 
    {'value': 16101, 'label': 'Description of httpie.'}, {'value': 15028, 'label': 'Description of django.'}, {'value': 14798, 'label': 'Description of flask.'}, ] 
chart.add('', plot_dicts) 
chart.render_to_file('bar_descriptions.svg')
为根据数据绘图，我们将自动生成plot_dicts ，其中包含API调用返回的30个项目的信息。创建了两个空列表names 和plot_dicts 。为生成x 轴上的标签，我们依然需要列表names 。 在循环内部，对于每个项目，我们都创建了字典plot_dict （见❷）。在这个字典中，我们使用键'value' 存储了星数，并使用键'label' 存储了项目描述。接下来，我们 将字典plot_dict 附加到plot_dicts 末尾（见❸）。在❹处，我们将列表plot_dicts 传递给了add() 。
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts)) 
names, plot_dicts = [], [] 
for repo_dict in repo_dicts: 
    names.append(repo_dict['name']) 
    plot_dict = { 
        'value': repo_dict['stargazers_count'], 
        'label': repo_dict['description'], 
        } 
    plot_dicts.append(plot_dict)  
my_style = LS('#333366', base_style=LCS) 
--snip--
chart.add('', plot_dicts) chart.render_to_file('python_repos.svg')
在图表中添加可单击的链接 
Pygal根据与键'xlink' 相关联的URL将每个条形都转换为活跃的链接。单击图表中的任何条形时，都将在浏览器中打开一个新的标签页，并在其中显示相应项目的GitHub页面。 至此，你对API获取的数据进行了可视化，它是交互性的，包含丰富的信息！
names, plot_dicts = [], [] 
for repo_dict in repo_dicts: 
    names.append(repo_dict['name']) 
    plot_dict = { 
        'value': repo_dict['stargazers_count'], 
        'label': repo_dict['description'], 
        'xlink': repo_dict['html_url'], 
        } 
    plot_dicts.append(plot_dict)
为探索如何使用其他网站的API调用，我们来看看Hacker News（http://news.ycombinator.com/ ）。在Hacker News网站，用户分享编程和技术方面的文章，并就这些文章展开积极的讨 论。Hacker News的API让你能够访问有关该网站所有文章和评论的信息，且不要求你通过注册获得密钥。
下面的调用返回本书编写时最热门的文章的信息：
https://hacker-news.firebaseio.com/v0/item/9884165.json
下面来执行一个API调用，返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章
首先，我们执行了一个API调用，并打印了响应的状态（见❶）。这个API调用返回一个列表，其中包含Hacker News上当前最热门的500篇文章的ID。接下来，我们将响应文本转 换为一个Python列表（见❷），并将其存储在submission_ids 中。我们将使用这些ID来创建一系列字典，其中每个字典都存储了一篇文章的信息。 在❸处，我们创建了一个名为submission_dicts 的空列表，用于存储前面所说的字典。接下来，我们遍历前30篇文章的ID。对于每篇文章，我们都执行一个API调用，其中 的URL包含submission_id 的当前值（见❹）。我们打印每次请求的状态，以便知道请求是否成功了。 在❺处，我们为当前处理的文章创建一个字典，并在其中存储文章的标题以及到其讨论页面的链接。在❻处，我们在这个字典中存储了评论数。如果文章还没有评论，响应字典 中将没有键'descendants' 。不确定某个键是否包含在字典中时，可使用方法dict.get() ，它在指定的键存在时返回与之相关联的值，并在指定的键不存在时返回你指定 的值（这里是0）。最后，我们将submission_dict 附加到submission_dicts 末尾。 Hacker News上的文章是根据总体得分排名的，而总体得分取决于很多因素，其中包含被推荐的次数、评论数以及发表的时间。我们要根据评论数对字典列 表submission_dicts 进行排序，为此，使用了模块operator 中的函数itemgetter() （见❼）。我们向这个函数传递了键'comments' ，因此它将从这个列表的每个 字典中提取与键'comments' 相关联的值。这样，函数sorted() 将根据这种值对列表进行排序。我们将列表按降序排列，即评论最多的文章位于最前面。 使用任何API来访问和分析信息时，流程都与此类似。有了这些数据后，你就可以进行可视化，指出最近哪些文章引发了最激烈的讨论。
import requests 
from operator import itemgetter 
# 执行API调用并存储响应 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
r = requests.get(url) 
print("Status code:", r.status_code) 
# 处理有关每篇文章的信息 
submission_ids = r.json() 
submission_dicts = [] 
for submission_id in submission_ids[:30]: 
    # 对于每篇文章，都执行一个API调用 
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json') 
    submission_r = requests.get(url) 
    print(submission_r.status_code) 
    response_dict = submission_r.json()

    submission_dict = { 
        'title': response_dict['title'], 
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id), 
        'comments': response_dict.get('descendants', 0) 
        } 
    submission_dicts.append(submission_dict) 
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
 for submission_dict in submission_dicts: 
     print("\nTitle:", submission_dict['title']) 
     print("Discussion link:", submission_dict['link']) 
     print("Comments:", submission_dict['comments'])

Django入门
学习如何使用 Django（http://djangoproject.com/ ）来开发一个名为“学习笔记”（LearningLog）的项目，这是一个在线日志系统，让你能够记录所学习的有关特定主题的知识。
我们将为这个项目制定规范，然后为应用程序使用的数据定义模型。我们将使用Django的管理系统来输入一些初始数据，再学习编写视图和模板，让Django能够为我们 的网站创建网页。 Django是一个Web框架框 ——一套用于帮助开发交互式网站的工具。Django能够响应网页请求，还能让你更轻松地读写数据库、管理用户等。在第19章和第20章，我们 将改进“学习笔记”项目，再将其部署到活动的服务器，让你和你的朋友能够使用它。
建立虚拟环境
虚拟环境是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。将项目的库与其他项目分离是有益的，且为 了在第20章将“学习笔记”部署到服务器，这也是必须的。
创建虚拟环境 运行了模块venv ，并使用它来创建一个名为ll_env的虚拟环境
learning_log$ python -m venv ll_env 
这里书中的例子麻烦 跟着y总吧

Python 虽然简单易用，但它可是真正的编程语言，提供了大量的数据结构，也支持开发大型程序，远超 shell 脚本或批处理文件，Python 提供的错误检查比 C 还多，作为一种“非常高级的语言”，它内置了灵活的数组与字典等高级数据类型。正因为配备了更通用的数据类型，Python 比 Awk，甚至 Perl 能解决更多问题，而且，很多时候，Python 比这些语言更简单。
Python 程序简洁、易读，通常比实现同种功能的 C、C++、Java 代码短很多，原因如下：
高级数据类型允许在单一语句中表述复杂操作，
使用缩进，而不是括号实现代码块分组，
无需预声明变量或参数。

Python 全面支持浮点数，混合类型运算数的运算会把整数转换为浮点数：
>>> 4 * 3.75 - 1
14.0
除了数字，Python 还可以操作字符串。字符串有多种表现形式，用单引号（'……'）或双引号（"……"）标注的结果相同 2。反斜杠 \ 用于转义

pass 还可以用作函数或条件子句的占位符，让开发者聚焦更抽象的层次。此时，程序直接忽略 pass：
>>> def initlog(*args):
...     pass   # Remember to implement this!

python接受一个match表达式并将其值与作为一个或多个 case 块给出的连续模式进行比较。这表面上类似于 C、Java 或 JavaScript（以及许多其他语言）中的 switch 语句，但它也可以将组件（序列元素或对象属性）从值中提取到变量中。
最简单的形式是将一个目标值与一个或多个字面值进行比较：

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
注意最后一个代码块：“变量名” _ 被作为 通配符 并必定会匹配成功。 如果没有 case 语句匹配成功，则不会执行任何分支。

使用 | （“ or ”）在一个模式中可以组合多个字面值：

case 401 | 403 | 404:
    return "Not allowed"

模式的形式类似解包赋值，并可被用于绑定变量：

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
请仔细研究此代码！ 第一个模式有两个字面值，可以看作是上面所示字面值模式的扩展。但接下来的两个模式结合了一个字面值和一个变量，而变量 绑定 了一个来自目标的值（point）。第四个模式捕获了两个值，这使得它在概念上类似于解包赋值 (x, y) = point。

如果使用类实现数据结构，可在类名后加一个类似于构造器的参数列表，这样做可以把属性放到变量里：

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point") 


"
可在 dataclass 等支持属性排序的内置类中使用位置参数。还可在类中设置 __match_args__ 特殊属性为模式的属性定义指定位置。如果它被设为 ("x", "y")，则以下模式均为等价的，并且都把 y 属性绑定到 var 变量：

Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
读取模式的推荐方式是将它们看做是你会在赋值操作左侧放置的内容的扩展形式，以便理解各个变量将会被设置的值。 只有单独的名称（例如上面的 var）会被 match 语句所赋值。 带点号的名称 (例如 foo.bar)、属性名称（例如上面的 x= 和 y=）或类名称（通过其后的 "(...)" 来识别，例如上面的 Point）都绝不会被赋值。

模式可以任意地嵌套。例如，如果有一个由点组成的短列表，则可使用如下方式进行匹配：

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
为模式添加成为守护项的 if 子句。如果守护项的值为假，则 match 继续匹配下一个 case 语句块。注意，值的捕获发生在守护项被求值之前：

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
match 语句的其他特性：

与解包赋值类似，元组和列表模式具有完全相同的含义，并且实际上能匹配任意序列。 但它们不能匹配迭代器或字符串。

序列模式支持扩展解包操作：[x, y, *rest] 和 (x, y, *rest) 的作用类似于解包赋值。 在 * 之后的名称也可以为 _，因此，(x, y, *_) 可以匹配包含至少两个条目的序列，而不必绑定其余的条目。

映射模式：从字典中捕获 和值。与序列模式不同，额外的键被忽略。还支持解包。（但会是多余的，所以是不允许的。）{"bandwidth": b, "latency": l}"bandwidth""latency"**rest**_

使用 as 关键字可以捕获子模式：

case (Point(x1, y1), Point(x2, y2) as p2): ...
将把输入的第二个元素捕获为 p2 (只要输入是包含两个点的序列)

大多数字面值是按相等性比较的，但是单例对象 True, False 和 None 则是按标识号比较的。

模式可以使用命名常量。 这些命名常量必须为带点号的名称以防止它们被解读为捕获变量:

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

定义函数
下列代码创建一个可以输出限定数值内的斐波那契数列函数：



定义 函数使用关键字 def，后跟函数名与括号内的形参列表。函数语句从下一行开始，并且必须缩进。
return 语句返回函数的值。return 语句不带表达式参数时，返回 None。函数执行完毕退出也返回 None。


result.append(a) 语句调用了列表对象 result 的 方法。
方法是“从属于”对象的函数，命名为 obj.methodname，obj 是对象（也可以是表达式），methodname 是对象类型定义的方法名。
不同类型定义不同的方法，不同类型的方法名可以相同，且不会引起歧义。（用 类 可以自定义对象类型和方法，详见 类 ）
示例中的方法 append() 是为列表对象定义的，用于在列表末尾添加新元素。本例中，该方法相当于 result = result + [a] ，但更有效。

 def fib2(n):   
   result = []
   a, b = 0, 1
   while a < n:
    result.append(a)   
     a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

>>>
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

关键字
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

当通过从类或实例获取一个类方法对象的方式创建一个实例对象时，实例对象的 __self__ 属性为该类本身，其 __func__ 属性为类方法对应的下层函数对象。

当一个实例方法对象被调用时，会调用对应的下层函数 (__func__)，并将类实例 (__self__) 插入参数列表的开头。例如，当 C 是一个包含了 f() 函数定义的类，而 x 是 C 的一个实例，则调用 x.f(1) 就等同于调用 C.f(x, 1)。
当一个实例方法对象是衍生自一个类方法对象时，保存在 __self__ 中的 "类实例" 实际上会是该类本身，因此无论是调用 x.f(1) 还是 C.f(1) 都等同于调用 f(C,1)，其中 f 为对应的下层函数。

请注意从函数对象到实例方法对象的变换会在每一次从实例获取属性时发生。在某些情况下，一种高效的优化方式是将属性赋值给一个本地变量并调用该本地变量。还要注意这样的变换只发生于用户定义函数，其他可调用对象 (以及所有不可调用对象) 在被获取时都不会发生变换。还有一个需要关注的要点是作为一个类实例属性的用户定义函数不会被转换为绑定方法，这样的变换 仅当 函数是类属性时才会发生。

生成器函数
使用该yield语句的函数或方法（参见 yield 语句部分）称为生成器函数。这样的函数在调用时总是返回一个迭代器对象，该对象可用于执行函数体：调用迭代器的 iterator.__next__()方法将导致函数执行，直到它使用yield语句提供值。当函数执行return语句或结束时， StopIteration会引发异常并且迭代器将到达要返回的值集的末尾。

importlib 模块提供了一个丰富的 API 用来与导入系统进行交互。 例如 importlib.import_module() 提供了相比内置的 __import__() 更推荐、更简单的 API 用来发起调用导入机制。 更多细节请参看 importlib 库文档。

Python 只有一种模块对象类型，所有模块都属于该类型，无论模块是用 Python、C 还是别的语言实现。 为了帮助组织模块并提供名称层次结构，Python 还引入了 包 的概念。

6.3. 原型
原型代表编程语言中最紧密绑定的操作。 它们的句法如下:

primary ::=  atom | attributeref | subscription | slicing | call

6.3.3. 切片
切片就是在序列对象（字符串、元组或列表）中选择某个范围内的项。 切片可被用作表达式以及赋值或 del 语句的目标。 切片的句法如下:

内置函数
Python 解释器内置了很多函数和类型，任何时候都能使用。

@classmethod
把一个方法封装成类方法。

类方法隐含的第一个参数就是类，就像实例方法接收实例作为参数一样。要声明一个类方法，按惯例请使用以下方案：

class C:
    @classmethod
    def f(cls, arg1, arg2): ...

dir([object])
如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。

如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象能够自定义 dir() 来报告它们的属性。

返回的列表按字母表排序。例如：
import struct
dir()   # show the names in the module namespace  
['__builtins__', '__name__', 'struct']
dir(struct)   # show the names in the struct module 
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
s = Shape()
dir(s)
['area', 'location', 'perimeter']

hash(object)
返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。

len(s)
返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。

class list([iterable])
虽然被称为函数，list 实际上是一种可变序列类型

map(function, iterable, ...)
返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。 如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。 当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。

内置类型
以下部分描述了解释器中内置的标准类型。

主要内置类型有数字、序列、映射、类、实例和异常。

有些多项集类是可变的。 它们用于添加、移除或重排其成员的方法将原地执行，并不返回特定的项，绝对不会返回多项集实例自身而是返回 None。

有些操作受多种对象类型的支持；特别地，实际上所有对象都可以比较是否相等、检测逻辑值，以及转换为字符串（使用 repr() 函数或略有差异的 str() 函数）。 后一个函数是在对象由 print() 函数输出时被隐式地调用的。


******数字类型的哈希运算
如果 x = m / n 是一个非负的有理数且 n 不可被 P 整除，则定义 hash(x) 为 m * invmod(n, P) % P，其中 invmod(n, P) 是对 n 模 P 取反。

如果 x = m / n 是一个非负的有理数且 n 可被 P 整除（但 m 不能）则 n 不能对 P 降模，以上规则不适用；在此情况下则定义 hash(x) 为常数值 sys.hash_info.inf。

如果 x = m / n 是一个负的有理数则定义 hash(x) 为 -hash(-x)。 如果结果哈希值为 -1 则将其替换为 -2。

特殊值 sys.hash_info.inf 和 -sys.hash_info.inf 分别用于正无穷或负无穷的哈希值。

对于一个 complex 值 z，会通过计算 hash(z.real) + sys.hash_info.imag * hash(z.imag) 将实部和虚部的哈希值结合起来，并进行降模 2**sys.hash_info.width 以使其处于 range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1)) 范围之内。 同样地，如果结果为 -1 则将其替换为 -2。
import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value

迭代器类型
Python 支持在容器中进行迭代的概念。 这是通过使用两个单独方法来实现的；它们被用于允许用户自定义类对迭代的支持。 将在下文中详细描述的序列总是支持迭代方法。

需要为容器对象定义一种方法以提供可迭代 支持：

container.__iter__()
返回一个迭代器对象。该对象需要支持下面描述的迭代器协议。如果容器支持不同类型的迭代，则可以提供额外的方法来专门为这些迭代类型请求迭代器。（支持多种迭代形式的对象的一个​​示例是支持广度优先和深度优先遍历的树结构。）此方法对应于 tp_iterPython/C API 中 Python 对象的类型结构的槽。

迭代器对象自身需要支持以下两个方法，它们共同组成了 迭代器协议:

iterator.__iter__()
返回迭代器对象本身。这是允许容器和迭代器与forand in语句一起使用所必需的。该方法对应于 tp_iterPython/C API 中 Python 对象的类型结构的 slot。

iterator.__next__()
从迭代器返回下一项。如果没有其他项目，请引发StopIteration异常。该方法对应于tp_iternextPython/C API 中 Python 对象的类型结构的 slot。

生成器类型
Python 的 generator 提供了一种实现迭代器协议的便捷方式。 如果容器对象 __iter__() 方法被实现为一个生成器，它将自动返回一个迭代器对象（从技术上说是一个生成器对象），该对象提供 __iter__() 和 __next__() 方法。 有关生成器的更多信息可以参阅 yield 表达式的文档。


序列类型 --- list, tuple, range
有三种基本序列类型：list, tuple 和 range 对象。 为处理 二进制数据 和 文本字符串 而特别定制的附加序列类型会在专门的小节中描述。



列表
列表是可变序列，通常用于存放同类项目的集合（其中精确的相似程度将根据应用而变化）。
list（[可迭代] ）
可以用多种方式构建列表：
使用一对方括号来表示空列表: []
使用方括号，其中的项以逗号分隔: [a], [a, b, c]
使用列表推导式: [x for x in iterable]
使用类型的构造器: list() 或 list(iterable）


元组
元组是不可变序列，通常用于储存异构数据的多项集（例如由 enumerate() 内置函数所产生的二元组）。 元组也被用于需要同构数据的不可变序列的情况（例如允许存储到 set 或 dict 的实例）tuple（[可迭代] ）
可以用多种方式构建元组：

使用一对圆括号来表示空元组: ()

使用一个后缀的逗号来表示单元组: a, 或 (a,)

使用以逗号分隔的多个项: a, b, c or (a, b, c)

使用内置的 tuple(): tuple() 或 tuple(iterable)

range 对象
range 类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。
类range（停止）
类range（开始，停止[，步骤] ）
范围构造函数的参数必须是整数（内置 int或任何实现__index__()特殊方法的对象）。如果省略step参数，则默认为1. 如果省略start参数，则默认为0. 如果步长为零，ValueError则升高。
如果 step 为正值，确定 range r 内容的公式为 r[i] = start + step*i 其中 i >= 0 且 r[i] < stop。
如果 step 为负值，确定 range 内容的公式仍然为 r[i] = start + step*i，但限制条件改为 i >= 0 且 r[i] > stop.
如果 r[0] 不符合值的限制条件，则该 range 对象为空。 range 对象确实支持负索引，但是会将其解读为从正索引所确定的序列的末尾开始索引。
元素绝对值大于 sys.maxsize 的 range 对象是被允许的，但某些特性 (例如 len()) 可能引发 OverflowError。
range 对象实现了 collections.abc.Sequence ABC，提供如包含检测、元素索引查找、切片等特性，并支持负索引 (参见 序列类型 --- list, tuple, range)


集合类型 --- set, frozenset
set 对象是由具有唯一性的 hashable 对象所组成的无序多项集。 常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算，例如交集、并集、差集与对称差集等等。 （关于其他容器对象请参看 dict, list 与 tuple 等内置类，以及 collections 模块。）

与其他多项集一样，集合也支持 x in set, len(set) 和 for x in set。 作为一种无序的多项集，集合并不记录元素位置或插入顺序。 相应地，集合不支持索引、切片或其他序列类的操作。

目前有两种内置集合类型，set 和 frozenset。 set 类型是可变的 --- 其内容可以使用 add() 和 remove() 这样的方法来改变。 由于是可变类型，它没有哈希值，且不能被用作字典的键或其他集合的元素。 frozenset 类型是不可变并且为 hashable --- 其内容在被创建后不能再改变；因此它可以被用作字典的键或其他集合的元素。

类set（[可迭代] ）
类frozenset（[可迭代] ）
返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 集合的元素必须为 hashable。 要表示由集合对象构成的集合，所有的内层集合必须为 frozenset 对象。 如果未指定 iterable，则将返回一个新的空集合。

集合可用多种方式来创建:

使用花括号内以逗号分隔元素的方式: {'jack', 'sjoerd'}

使用集合推导式: {c for c in 'abracadabra' if c not in 'abc'}

使用类型构造器: set(), set('foobar'), set(['a', 'b', 'foo'])

映射类型 --- dict
mapping 对象会将 hashable 值映射到任意对象。 映射属于可变对象。 目前仅有一种标准映射类型 字典。 （关于其他容器对象请参看 list, set 与 tuple 等内置类，以及 collections 模块。）

字典的键 几乎 可以是任何值。 非 hashable 的值，即包含列表、字典或其他可变类型的值（此类对象基于值而非对象标识进行比较）不可用作键。 数字类型用作键时遵循数字比较的一般规则：如果两个数值相等 (例如 1 和 1.0) 则两者可以被用来索引同一字典条目。 （但是请注意，由于计算机对于浮点数存储的只是近似值，因此将其用作字典键是不明智的。）

类型注解的类型 --- Generic Alias 、 Union
type annotations 的内置类型为 Generic Alias 和 Union。

GenericAlias 类型
GenericAlias对象通常是通过 下标类来创建的。它们最常与 容器类一起使用，例如list或 dict。例如，list[int]是通过使用参数GenericAlias为类下标而创建的对象。 对象主要用于 类型注释。listintGenericAlias

注解 如果类实现了特殊方法，通常只能为类下标__class_getitem__()。
GenericAlias对象充当泛型类型的代理，实现参数化泛型。

对于容器类，提供给类订阅的参数可以指示对象包含的元素的类型。例如， set[bytes]可以在类型注释中使用，以表示set所有元素都是 type 的a bytes。

函数
函数对象是通过函数定义创建的。 对函数对象的唯一操作是调用它: func(argument-list)。

实际上存在两种不同的函数对象：内置函数和用户自定义函数。 两者支持同样的操作（调用函数），但实现方式不同，因此对象类型也不同。

更多信息请参阅 函数定义。

方法
方法是使用属性表示法来调用的函数。 存在两种形式：内置方法（例如列表的 append() 方法）和类实例方法。 内置方法由支持它们的类型来描述。

如果你通过一个实例来访问方法（即定义在类命名空间内的函数），你会得到一个特殊对象: 绑定方法 (或称 实例方法) 对象。 当被调用时，它会将 self 参数添加到参数列表。 绑定方法具有两个特殊的只读属性: m.__self__ 操作该方法的对象，而 m.__func__ 是实现该方法的函数。 调用 m(arg-1, arg-2, ..., arg-n) 完全等价于调用 m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)。

与函数对象类似，绑定方法对象也支持获取任意属性。 但是，由于方法属性实际上保存于下层的函数对象中 (meth.__func__)，因此不允许设置绑定方法的方法属性。 尝试设置方法的属性将会导致引发 AttributeError。 想要设置方法属性，你必须在下层的函数对象中显式地对其进行设置:


>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'


re --- 正则表达式操作

本模块提供了与 Perl 语言类似的正则表达式匹配操作。

模式和被搜索的字符串既可以是 Unicode 字符串 (str) ，也可以是8位字节串 (bytes)。 但是，Unicode 字符串与 8 位字节串不能混用：也就是说，不能用字节串模式匹配 Unicode 字符串，反之亦然；同理，替换操作时，替换字符串的类型也必须与所用的模式和搜索字符串的类型一致。

正则表达式用反斜杠字符 ('\') 表示特殊形式，或是允许在使用特殊字符时，不引发它们的特殊含义。 这与 Python 的字符串字面值中对相同字符出于相同目的的用法产生冲突；例如，要匹配一个反斜杠字面值，用户可能必须写成 '\\\\' 来作为模式字符串，因为正则表达式必须为 \\，而每个反斜杠在普通 Python 字符串字面值中又必须表示为 \\。 而且还要注意，在 Python 的字符串字面值中使用的反斜杠如果有任何无效的转义序列，现在会触发 DeprecationWarning，但以后会改为 SyntaxError。 此行为即使对于正则表达式来说有效的转义字符同样会发生。

解决办法是对于正则表达式样式使用 Python 的原始字符串表示法；在带有 'r' 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 因此 r"\n" 表示包含 '\' 和 'n' 两个字符的字符串，而 "\n" 则表示只包含一个换行符的字符串。 样式在 Python 代码中通常都使用原始字符串表示法。

绝大多数正则表达式操作都提供为模块函数和方法，在 编译正则表达式. 这些函数是一个捷径，不需要先编译正则对象，但是损失了一些优化参数。


模块内容
模块定义了几个函数、常量，和一个异常。有些函数是编译后的正则表达式方法的简化版本（少了一些特性）。重要的应用程序大多会在使用前先编译正则表达式。

在 3.6 版更改: 标志常量现在是 RegexFlag 类的实例，这个类是 enum.IntFlag 的子类。

re.compile(pattern, flags=0)
将正则表达式的样式编译为一个 正则表达式对象 （正则对象），可以用于匹配，通过这个对象的方法 match(), search() 以及其他如下描述。

这个表达式的行为可以通过指定 标记 的值来改变。值可以是以下任意变量，可以通过位的OR操作来结合（ | 操作符）。

序列

difflib --- 计算差异的辅助工

readline --- GNU readline 接口
readline 模块定义了许多方便从 Python 解释器完成和读取/写入历史文件的函数。 此模块可以直接使用，或通过支持在交互提示符下完成 Python 标识符的 rlcompleter 模块使用。 使用此模块进行的设置会同时影响解释器的交互提示符以及内置 input() 函数提供的提示符。

collections --- 容器数据类型
collections.abc --- 容器的抽象基类
heapq --- 堆队列算法  
bisect --- 数组二分查找算法
array --- 高效的数值数组
weakref --- 弱引用
types --- 动态类型创建和内置类型名称
copy --- 浅层 (shallow) 和深层 (deep) 复制
copy.copy(x)
返回 x 的浅层复制。
copy.deepcopy(x[, memo])
返回 x 的深层复制。
pprint --- 数据美化输出
enum --- 对枚举的支持

函数式编程模块
itertools --- 为高效循环而创建迭代器的函数
Itertool函数
itertools 配方
functools --- 高阶函数和可调用对象上的操作
partial 对象
operator --- 标准运算符替代函数
将运算符映射到函数
原地运算符


切片 https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856
取前3个元素，用一行代码就可以完成切片：
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']




******机器学习day*******
  ROC曲线（Receiver Operator Characteristic）即受试者工作特征曲线反映的是真阳性占总的实际阳性的比例。将它与在各种阈值设置情况下假阳性占总的实际阴性的比例进行对比。对角连线表示50%预测的准确性，并可作为评价的基准以便后续提高。曲线位于左边高出对角线的部分表示模型的精准度高，当然您也会希望实验的结果曲线出现在此区域。
    准确率和召回率是衡量信息检索系统性能的重要指标。准确率是指检索到相关文档数占检索到的文档总数的比例，而召回率是指检索到相关文档数占所有相关文档总数的比例。
    lift曲线是数据挖掘分类器最常用的方式之一，与ROC曲线不同的是lift考虑分类器的准确性，也就是使用分类器获得的正类数量和不使用分类器随机获取正类数量的比例。
day1 

1.机器学习概述
1.1 人工智能概述
    1.人工智能起源
        图灵测试
        达特茅斯会议
    2.人工智能三个阶段
        1980年代是正式成形期
        1990-2010年代是蓬勃发展期
        2012年之后是深度学习期
    3.人工智能、机器学习和深度学习
        机器学习是人工智能的一个实现途径
        深度学习是机器学习的一个方法发展而来
    4.主要分支介绍
        1.计算机视觉
            eg:人脸识别
        2.自然语言处理
            语音识别
            语义识别
        3.机器人
    5.人工智能必备三要素【***】
        数据
        算法
        计算力
    6.gpu,cpu【**】
        gpu -- 计算密集型
        cpu -- IO密集型
1.2.机器学习工作流程
    1.定义【***】
        数据
        自动分析获得模型
        预测
        从数据中自动分析获得模型，并利用模型对未知数据进行预测
    2.工作流程【****】
        1.获取数据
        2.数据基本处理
        3.特征工程
        4.机器学习（模型训练）
        5.模型评估
    3.获取到的数据集介绍【*****】
        1.专有名词
            样本
            特征
            目标值（标签值）
            特征值
        2.数据类型构成
            类型一：特征值+目标值
                目标值分为是离散还是连续
            类型二： 只有特征值，没有目标值
        3.数据划分
            训练数据（训练集） -- 构建模型
                0.7--0.8
            测试数据（测试集） -- 模型评估
                0.2--0.3
    4.数据基本处理
        对数进行缺失值、去除异常值等处理
    5.特征工程
        1.定义
            把数据转换成为机器更容易识别的数据
        2.为什么需要特征工程
            数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已
        3.包含内容
            特征提取
            特征预处理
            特征降维
    6.机器学习
        选择合适的算法对模型进行训练
    7.模型评估
        对训练好的模型进行评估
1.3 机器学习算法分类【***】
    1.监督学习 -- 有特征值，有目标值
        目标值连续-- 回归
        目标值离散-- 分类
    2.无监督学习 -- 仅有特征值
    3.半监督学习
        有特征值，但是一部分数据有目标值，一部分没有
    4.强化学习
        动态过程，上一步数据的输出是下一步数据的输入
        四要素：agent, action, environment,Reward,
1.4 模型评估
    1.分类模型评估
        准确率
        精确率
        召回率
        F1-score
        AUC指标
    2 回归模型评估
        均方根误差
        相对平方误差
        平均绝对误差
        相对绝对误差
        决定系数
    3.拟合
        欠拟合
        过拟合

2.机器学习基础环境安装与使用
2.1 库的安装
    pip install -r requirements.txt
2.2 Jupyter Notebook使用【**】json
    1.jupyter定义
        开源的科学计算平台
        类比ipython
        可以运行代码，可以做笔记
        文件后缀： .ipynb
    2.jupyter和pycharm对比
        jupyter -- 探索性数据，一边分析，一边运行
        pycharm -- 适合逻辑性强的操作（web）
    3.如何使用
        jupyter notebook
        使用方式和ipython一样，但是要比ipython强大（可以画图）
    4.cell
        一对In Out会话被视作一个代码单元，称为cell
    5.jupyter两种模式
        编辑模式
            直接点击进去，可以进行编写代码，做笔记
        命令模式
            通过快捷键，操作，eg:添加一行
    6.快捷键
        通用：
            Shift+Enter，执行本单元代码，并跳转到下一单元
            Ctrl+Enter，执行本单元代码，留在本单元
        命令模式
            Y，cell切换到Code模式
            M，cell切换到Markdown模式
            A，在当前cell的上面添加cell
            B，在当前cell的下面添加cell
            双击D：删除当前cell
        编辑模式：
            和常规方式一样
    7.markdown语法
        # -- *级标题
        - -- 缩进

3. Matplotlib
3.1 Matplotlib之HelloWorld
    1.定义
        主要用于开发2D图表（3D）
        数据分析，基于分析，进行展示
    2.绘图流程【***】
        1.创建画布
        2.绘制图像
        3.显示图像
    3.matplotlib三层结构
        容器层
            canvas
            figure
            axes
        辅助显示层
            添加x轴，y轴描述，标题。。。
        图像层
            绘制什么图像的声明
3.2 折线图(plot)与基础绘图功能【****】
    1.图像保存
        plt.savefig()
        注意：图像保存一定要放到show前面
    2.添加x轴,y轴刻度
        plt.xticks
        plt.yticks
        注意:第一个参数必须是数字,如果不是数字,需要进行值替换
    3.添加网格
        plt.grid()
            参数:
            linestyle -- 绘制网格的方式
            alpha -- 透明度
    4.添加描述信息
        plt.xlabel("时间")
        plt.ylabel("温度")
        plt.title("一小时温度变化图", fontsize=20)
    5.多次plot
        直接进行绘制
    6.显示图例
        plt.legend()
        注意:需要在显示之前,声明plot里面的具体值
    7.多个坐标系图像显示【###】
        fig, axes = plt.subplots()
            nrows -- 几行
            ncols -- 几列
            注意:有些方法需要添加set_*
    8.折线图应用场景
        1.表示数据变化
        2.绘制一些数学图像



1
from array import array
from binascii import a2b_base64
from cgi import test
from email.errors import NoBoundaryInMultipartDefect
from lib2to3.pgen2.pgen import DFAState
from locale import ABDAY_1, DAY_3, DAY_6, DAY_7
from msilib.schema import ServiceInstall
from re import A
from socket import NI_DGRAM
from turtle import shape
import matplotlib.pyplot as plt

# 1. 创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.图像绘制
x = [1,2,3,4,5,6]
y = [3,6,3,5,3,10]
plt.plot(x, y)

# 2.1 图像保存
plt.savefig("./data/test.png")

# 3.图像展示
plt.show()

# 图像保存一定要放到show前面
# # 2.1 图像保存
# plt.savefig("./data/test.png")

2 图像基本绘制功能演示

# 0.生成数据
x = range(60)
y_beijing = [random.uniform(10, 15) for i in x]
y_shanghai = [random.uniform(15, 25) for i in x]

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.图形绘制
plt.plot(x, y_beijing, label="北京", color="g", linestyle="-.")
plt.plot(x, y_shanghai, label="上海")

# 2.1 添加x,y轴刻度
y_ticks = range(40)
x_ticks_labels = ["11点{}分".format(i) for i in x]

plt.yticks(y_ticks[::5])
plt.xticks(x[::5], x_ticks_labels[::5])
# plt.xticks(x_ticks_labels[::5])  # 必须最开始传递进去的是数字

# 2.2 添加网格
plt.grid(True, linestyle="--", alpha=0.7)

# 2.3 添加描述
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("一小时温度变化图", fontsize=20)

# 2.4 显示图例
plt.legend(loc=0)

# 3.图像展示
plt.show()


3  多个坐标系显示图像

# 0.生成数据
x = range(60)
y_beijing = [random.uniform(10, 15) for i in x]
y_shanghai = [random.uniform(15, 25) for i in x]

# 1.创建画布
# plt.figure(figsize=(20, 8), dpi=100)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 2.图形绘制
# plt.plot(x, y_beijing, label="北京", color="g", linestyle="-.")
# plt.plot(x, y_shanghai, label="上海")
axes[0].plot(x, y_beijing, label="北京", color="g", linestyle="-.")
axes[1].plot(x, y_shanghai, label="上海")


# # 2.1 添加x,y轴刻度
y_ticks = range(40)
x_ticks_labels = ["11点{}分".format(i) for i in x]

# plt.yticks(y_ticks[::5])
# plt.xticks(x[::5], x_ticks_labels[::5])
# # plt.xticks(x_ticks_labels[::5])  # 必须最开始传递进去的是数字

axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_labels[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_labels[::5])

# # 2.2 添加网格
# plt.grid(True, linestyle="--", alpha=0.7)
axes[0].grid(True, linestyle="--", alpha=0.7)
axes[1].grid(True, linestyle="--", alpha=0.7)

# # 2.3 添加描述
# plt.xlabel("时间")
# plt.ylabel("温度")
# plt.title("一小时温度变化图", fontsize=20)

axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].set_title("北京一小时温度变化图", fontsize=20)
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].set_title("上海一小时温度变化图", fontsize=20)

# 2.4 显示图例
# plt.legend(loc=0)
axes[0].legend(loc=0)
axes[1].legend(loc=0)

# 3.图像展示
plt.show()


4  plot绘制数学图像
import matplotlib.pyplot as plt
import numpy as np
# 0.生成数据
x = np.linspace(-10, 10, 1000)
y = x*x*x

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制
plt.plot(x, y)

plt.grid()

# 3.显示
plt.show()

day2

3.3 常见图形绘制[*]
    1.折线图 -- plt.plot
        变化
    2.散点图 -- plt.scatter()
        分布规律
    3.柱状图 -- plt.bar
        统计、对比
    4.直方图 -- plt.hist()
        统计，分布
    5.饼图 -- plt.pie()
        占比
4 Numpy
4.1 Numpy优势
    1.定义
        开源的Python科学计算库，
        用于快速处理任意维度的数组
        Numpy中，存储对象是ndarray
    2.创建
        np.array([])
    3.numpy的优势
        内存块风格 -- 一体式存储
        支持并行化运算
        效率高于纯Python代码 -- 底层使用了C，内部释放了GIL
4.2 N维数组-ndarray[**]
    1.ndarray的属性
        属性名字    属性解释
        ndarray.shape   数组维度的元组
        ndarray.ndim    数组维数
        ndarray.size    数组中的元素数量
        ndarray.itemsize    一个数组元素的长度（字节）
        ndarray.dtype   数组元素的类型
    2.ndarray的形状
        np.array()
            三维数组不好理解 -- excel中有多个sheet
    3.ndarray的类型
        bool
        int
        float
        str
        ...
        注意：若不指定，整数默认int64，小数默认float64
4.3 基本操作
    1 生成数组的方法[**]
        1.生成0和1的数组
            np.ones()
            np.ones_like()
        2.从现有数组中生成
            np.array -- 深拷贝
            np.asarray -- 浅拷贝
        3.生成固定范围数组
            np.linspace()
                nun -- 生成等间隔的多少个
            np.arange()
                step -- 每间隔多少生成数据
            np.logspace()
                生成以10的N次幂的数据
        4 生成随机数组
            1.均匀分布生成
                np.random.uniform()
                    low
                    high
                    size
            2.正态分布[****]
                均值，方差
                均值 -- 图形的左右位置
                方差 -- 图像是瘦，还是胖
                    值越小，图形越瘦高，数据越集中
                    值越大，图形越矮胖，数据越分散
            3.正态分布api[***]
                np.random.normal()
                    low
                    high
                    size
    2.数组的索引、切片[***]
        直接索引
        先对行进行索引，再进行列索引 -- [*, #]
        高维数组索引，从宏观到微观
    3.形状修改[**]
        1.对象.reshape
            不进行行列互换，产生新变量
        2.对象.resize
            不进行行列互换,对原值进行更改
        3.对象.T
            进行行列互换
    4.类型修改[*]
        对象.astype()
    5.数组去重[*]
        np.unique()
4.4 ndarray运算[**]
    1.逻辑运算
        大于，小于直接进行判断
        赋值：满足要求，直接进行赋值
    2.通用判断函数
        np.all()
            所有满足要求，才返回True
        np.any()
            只要有一个满足要求，就返回True
    3.三元运算符
        np.where()
            满足要求，赋值第一个值，否则赋值第二个值
        np.logical_and()
            并
        np.logical_or()
            或
    4.统计运算
        min
        max
        midian
        mean
        std -- 标准差
        var -- 方差
        argmax -- 最大值下标
        argmin -- 最小值下标
4.5 矩阵[*]
    1.矩阵和向量
        矩阵：理解-二维数组
        向量：理解-一维数组
    2.加法和标量乘法
        加法： 对应位置相加
        乘法： 标量和每个位置的元素相乘
    3.矩阵向量（矩阵）乘法[*****]
        [M行, N列]*[N行, L列] = [M行, L列]
    4.矩阵乘法性质
        1.满足结合律，不满足交换律
    5.单位矩阵
        对角线为1，其他位置为0的矩阵
    6.逆
        矩阵A*矩阵B=单位矩阵I
        那么A和B就互为逆矩阵
    7.转置
        行列互换
4.6 数组间运算[*]
    1.数组和数字是直接可以进行运算
    2.数组和数组
        需要满足广播机制
            维度相同
            shape对应位置为1
    3.矩阵乘法api
        np.dot --点乘
        np.matmul -- 矩阵相乘
        注意：两者之间在进行矩阵相乘时候，没有区别
        但是，dot支持矩阵和数字相乘

5.Pandas
5.1Pandas介绍
    1.pandas概念
        开源的数据挖掘库
        用于数据探索
        封装了matplotlib,numpy
    2.案例知识点
        1.创建DataFrame
            pd.DataFrame(ndarray)
        2.创建日期
            pd.date_range()
                start -- 开始日期
                end -- 结束日期
                periods -- 时间跨度
                freq -- 统计时间方式
    3.DataFrame介绍 -- 类比二维数组[***]
        1.dataframe属性
            对象.shape
            对象.index
            对象.columns
            对象.values
            对象.T
            对象.head()
            对象.tail()
        2.dataframe设置索引
            1.修改行列索引
                必须整行或者整列去进行修改
            2.重设索引
                对象.reset_index()
            3.设置新索引
                对象.set_index()
                如果设置索引是两个的时候就是multiIndex
    4.MultiIndex和panel -- 类比三维数组[**]
        1.MultiIndex
            对象.index
            对象.index.names
        2.panel -- 已经弃用,了解
            直接没法进行查看里面的值,需要通过索引获取
            对象[:, :, ""]
    5.Series  -- 一维数组[**]
        1.创建
            通过ndarray创建
            指定索引创建
            通过字典创建
        2.属性
            对象.index
            对象.values


import matplotlib.pyplot as plt

1 散点图
# 0.数据准备
x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01,  20.67, 288.64,
       163.56, 120.06, 207.83, 342.75, 147.9 ,  53.06, 224.72,  29.51,
        21.61, 483.21, 245.25, 399.25, 343.35]
y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61,  24.9 , 239.34,
       140.32, 104.15, 176.84, 288.23, 128.79,  49.64, 191.74,  33.1 ,
        30.74, 400.02, 205.35, 330.64, 283.45]

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.图像绘制（散点图）
plt.scatter(x, y)

# 3.图像展示
plt.show()

2 柱状图
# 0.获取数据
# 电影名字
x = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']
# 横坐标
# x = range(len(movie_name))
# # 票房数据
# y = [73853,57767,22354,15969,14839,8725,8716,8318,7916,6764,52222]

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制
plt.bar(x, y)

# # 2.1 x轴
# plt.xticks(x, movie_name, fontsize=15)

# # 2.2 网格
# plt.grid()

# # 2.3 标题
# plt.title("某月电影票房统计")


# 3.显示
plt.show()

 
3 
import numpy as np

score = np.array([[80, 89, 86, 67, 79],
          [78, 97, 89, 67, 81],
          [90, 94, 78, 67, 74],
          [91, 91, 90, 67, 69],
          [76, 87, 75, 67, 86],
          [70, 79, 84, 67, 84],
          [94, 92, 93, 67, 64],
          [86, 85, 83, 67, 80]])
score

4 效率对比
import random
import time
import numpy as np
a = []
for i in range(100000000):
    a.append(random.random())

# 通过%time魔法方法, 查看当前行的代码运行一次所花费的时间
%time sum1=sum(a)

b=np.array(a)

%time sum2=np.sum(b)


5 ndarray的属性
score.shape
score.ndim
score.size
score.itemsize
score.dtype


6 ndarray的形状
a = np.array([1,2,3])
a 
b = np.array([[1,2,3],[2,3,4]])
b 
c = np.array([[[1,2,3],[2,3,4]],[[3,4,5],[4,5,6]]])
c 
a.shape
b.shape
c.shape
a.ndim 
a.dtype 

7 ndarray的类型
d.dtype
e = np.array(["I", "love", "python"], dtype = np.string_)
e 


import numpy as np
import matplotlib.pyplot as plt

8 生成数组
ones = np.ones([4,8])
ones

np.zeros_like(ones)

a = np.array([[1, 2, 3], [4, 5, 6]])

a1 = np.array(a)  # 深拷贝
a1 

a2 = np.asarray(a)  # 浅拷贝
a2 

a[0,0] = 100
a 


np.linspace(0, 100, 11)

np.arange(10, 50, 2)

np.logspace(0, 2, 3)

np.random.rand(2,3)

np.random.uniform(low=1, high=10, size=(3,5))

np.random.randint(1, 10, (3, 5))

# 生成均匀分布小案例
# 0.准备数据
x = np.random.uniform(0, 1, 100000000)

# 1.画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制
plt.hist(x, bins=1000)

# 3.显示
plt.show()


# 生成正态分布数据
np.random.normal(1.75, 1, 100000000)

# 生成正态分布小案例
# 0.准备数据
x = np.random.normal(1.75, 1, 100000000)

# 1.画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制
plt.hist(x, bins=1000)

# 3.显示
plt.show()

9 数组索引，切片
stock_change = np.random.normal(0, 1, (8, 10))
stock_change

stock_change[0:2, 0:3]

a1 = np.array([ [[1,2,3],[4,5,6]], [[12,3,34],[5,6,7]]])
a1 

a1[1,0,0]

a1[1, 0, 2]

10 形状修改
stock_change = np.random.normal(0, 1, (4, 5))
stock_change

stock_change.reshape([5,4])
stock_change.reshape([-1, 2])
stock_change

stock_change.resize([5,4])
stock_change
stock_change.T


11 类型修改
stock_change

stock_change.astype(np.int32)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[12, 3, 34], [5, 6, 7]]])

arr.tostring()

12 数据去重
arr = np.array([[1,2,3,4,5], [3,4,5,6,7]])

np.unique(arr)

test = np.array([[1,2,3],[2,4,6]])
test 

test.dtype


import numpy as np
13 逻辑运算
stock_change = np.random.normal(0, 1, (8, 10))
stock_change

stock_c = stock_change[0:5, 0:5]
stock_c

stock_c > 1

stock_c[stock_c >1] = 2
stock_c
# ? 这句逻辑判断的含义

test_a = [1,2,3]
# test_a > 2

stock_d = stock_change[0:2, 0:5]
stock_d

np.all(stock_d > 0)
np.any(stock_d>0)

np.where(stock_d>0, 1, 0)
np.where(np.logical_and(stock_d>-0.5, stock_d<0.5), 1, 0)
np.where(np.logical_or(stock_d>0, stock_d<-1), 2, 0)

stock_change

stock_change.max(axis=0)
stock_c

stock_c.argmax(axis=1)
stock_c.argmax(axis=0)
stock_c.argmin(axis=1)

14 数组运算
arr = np.array([1,2,3,4])
arr

arr+1

arr/2

arr*10

arr1 = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr2 = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
# arr1+arr2 不可以运算

arr1 = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr2 = np.array([[1], [3]])
arr1+arr2

a = np.array([[80, 86],
              [82, 80],
              [85, 78],
              [90, 90],
              [86, 82],
              [82, 90],
              [78, 80],
              [92, 94]])

b = np.array([[0.7], [0.3]])

np.matmul(a, b)
np.dot(a,b)

# np.matmul(a, 10) 
# matmul不支持矩阵和数字的相乘
np.dot(a, 10)

import pandas as pd
import numpy as np

15 pandas案例导入
stock_change = np.random.normal(0, 1, (10, 5))
stock_change

stock_rise = pd.DataFrame(stock_change)
stock_rise

stock_rise.shape[0]

stock_code = ["股票{}".format(i+1) for i in range(stock_rise.shape[0])]
stock_code


pd.DataFrame(stock_change, index=stock_code)
date = pd.date_range(start="20190403", periods=stock_rise.shape[1], freq="B")
date

stock_c = pd.DataFrame(stock_change, index=stock_code, columns=date)

16 dataframe
stock_c

stock_c.shape

stock_c.index

stock_c.columns

stock_c.values

stock_c.T

stock_c.head()

stock_c.tail(3)

17 设置索引
stock_code = ["股票__{}".format(i+1) for i in range(stock_rise.shape[0])]
stock_c.index = stock_code
stock_c
# stock_c.index[3] = "hahaha"


18 重设索引
stock_c.reset_index()
stock_c.reset_index(drop=True)

19 以某列设置新的索引
df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})
df 

df.set_index(keys=["year"])

df = df.set_index(keys=["year", "month"])

20 MultiIndex和panel
MultiIndex

df.index
df.index.names
df.index.levels

panel

np.arange(24).reshape(4,3,2)

p = pd.Panel(np.arange(24).reshape(4,3,2),
                 items=list('ABCD'),
                 major_axis=pd.date_range('20130101', periods=3),
                 minor_axis=['first', 'second'])
p


p[:,:,"first"]

p["A", :, :]

21 series 
type(stock_c["2019-04-03"])

stock_c

stock_c["2019-04-03"]["股票__1"]


pd.Series(np.arange(10))

pd.Series([6.7,5.6,3,10,2], index=[1,2,3,4,5])
series_demo = pd.Series({"red":10, "green":20})
series_demo.index
series_demo.values

day3 
5.2 基本数据操作
    1.索引操作
        1.直接 -- 先列后行
        2.loc -- 先行后列，索引值
        3.iloc -- 先行后列，索引值的下标
        4.ix -- 先行后列，混合索引
    2.赋值操作
        1.对象[""]
        2.对象.close
    3.排序
        1.dataframe
            对象.sort_values()
                by -- 按照什么排序
                ascending -- 升降序
            对象.sort_index()
            注意:by这个参数可以接受多个值,优先按照第一个索引排序,如果相同,按照后面的
        2.series
            对象.sort_values()
            对象.sort_index()
5.3 DataFrame运算
    1.算术运算
        直接使用方法, add, sub ...
        也可以用符号
    2.逻辑运算
        2.1 逻辑运算符号<、 >、|、 &
            直接判断
        2.2 逻辑运算函数
            对象.query("")
            对象.isin([])
    3.统计函数
        对象.describe()
        统计函数
            sum
            mean
            ...
            mode -- 众数
            idxmax -- 最大值的索引
            idxmin -- 最小值的索引
    4.累计统计函数
        函数      作用
        cumsum  计算前1/2/3/…/n个数的和
        cummax  计算前1/2/3/…/n个数的最大值
        cummin  计算前1/2/3/…/n个数的最小值
        cumprod 计算前1/2/3/…/n个数的积
    5.自定义运算[***]
        apply(func, axis=)
            func -- 自己定义的函数
5.4 Pandas画图
    对象.plot()
        kind --
            line -- 折线图
            bar
            barh -- 条形图旋转
            hist
            pie
            scatter
5.5 文件读取与存储
    1.csv
        1.读取-- pd.read_csv
            参数:
            usecols -- 需要哪列
        2.存储 -- 对象.to_csv
            参数:
            columns -- 保存哪列
    2.hdf
        1.读取 -- pd.read_hdf()
        2.写入 -- 对象.to_hdf()
            注意:保存文件是****.h5
    3.json
        1.读取 -- pd.read_json()
        2.写入 -- 对象.to_josn()
            参数:
            orient -- 按照什么方式进行读取或者写入
            lines -- 是否按照行读取和写入
    4.推荐使用hdf
        1.压缩方式,读取效率快
        2.压缩后,节省空间
        3.支持跨平台

5.6 高级处理-缺失值处理[*****]
    判断数据是否为NaN：
        np.any(pd.isnull(movie))  # 里面如果有一个缺失值,就返回True
        np.all(pd.notnull(movie))  # 里面如果有一个缺失值,就返回False
    处理方式：
        存在缺失值nan,并且是np.nan:
        1、删除存在缺失值的:dropna(axis='rows')
            注：不会修改原数据，需要接受返回值
        2、替换缺失值:fillna(value, inplace=True)
            value:替换成的值
            inplace:True:会修改原数据，False:不替换修改原数据，生成新的对象
    不是缺失值nan，有默认标记的
        对象.replace()
            to_replace -- 替换前的值
            value -- 替换后的值
5.7 高级处理-数据离散化
    1.什么是数据离散化
        把一些数据分到某个区间,最后用不同的符号或者数字表达
    2.数据离散化api
        pd.qcut() -- 把数据大致分为数量相等的几类
        pd.cut()  -- 指定分组间隔
        数量统计:
            对象.value_counts()
    3.one-hot编码
        就是把数据转换成为0,1统计类型
        别名:哑变量,热独编码
        api:
            pd.get_dummies()
5.8 高级处理-合并
    pd.concat()
        axis=
    pd.merge()
        left -- 左表
        right -- 右表
        on -- 指定键
        how -- 按照什么方式进行拼接
5.9 高级处理-交叉表与透视表
    1.什么交叉表,透视表
        就是探索两列数据之间的关系
    2.pd.crosstab()
        返回具体数量
    3.对象.pivot_table()
        返回占比情况
5.10 高级处理-分组与聚合
    1.api
        对象.groupby()
            参数:as_index -- 是否进行索引
        注意:可以对数据进行对此分组,需要里面传递一个列表进行完成.


day4 
1.K-近邻算法
1.1 K-近邻算法简介
    1.定义:
        就是通过你的"邻居"来判断你属于哪个类别
    2.如何计算你到你的"邻居"的距离
        一般时候,都是使用欧氏距离
1.2 k近邻算法api初步使用
    1.sklearn
        优势:
        1.文档多,且规范,
        2.包含的算法多
        3.实现起来容易
    2.sklearn中包含内容
        分类、聚类、回归
        特征工程
        模型选择、调优
    3.knn中的api
        sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
            参数:
            n_neighbors -- 选定参考几个邻居
    4.机器学习中实现的过程
        1.实例化一个估计器
        2.使用fit方法进行训练
1.3 距离度量[###]
    1.欧式距离
        通过距离平方值进行计算
    2.曼哈顿距离(Manhattan Distance)：
        通过举例的绝对值进行计算
    3.切比雪夫距离 (Chebyshev Distance)：
        维度的最大值进行计算
    4.闵可夫斯基距离(Minkowski Distance)：
        当p=1时，就是曼哈顿距离
        当p=2时，就是欧氏距离
        当p→∞时，就是切比雪夫距离
    小结:前面四个距离公式都是把单位相同看待了,所以计算过程不是很科学

    5.标准化欧氏距离 (Standardized EuclideanDistance)：
        在计算过程中添加了标准差,对量纲数据进行处理
    6.余弦距离(Cosine Distance)
        通过cos思想完成
    7.汉明距离(Hamming Distance)【了解】：
        一个字符串到另一个字符串需要变换几个字母,进行统计
    8.杰卡德距离(Jaccard Distance)【了解】：
        通过交并集进行统计
    9.马氏距离(Mahalanobis Distance)【了解】
        通过样本分布进行计算

1.4 k值选择[***]
    K值过小：
       容易受到异常点的影响
        过拟合
    k值过大：
        受到样本均衡的问题
        欠拟合
    拓展:
    近似误差 -- 过拟合 --在训练集上表现好,测试集表现不好 过拟合 以假为真 第一类错误
    估计误差好才是真的好!
1.5 kd树[###]
    1.构建树
    2.最近领域搜索
    案例:
    一,构建树
        第一次:
        x轴-- 2,5,9,4,8,7 --> 2,4,5,7,8,9
        y轴-- 3,4,6,7,1,2 --> 1,2,3,4,6,7

        首先选择x轴, 找中间点,发现是(7,2)

        第二次:
        左面: (2,3), [4,7], [5,4] --> 3,4,7
        右面: (8,1), (9,6) --> 1,6

        从y轴开始选择, 左边选择点是(5,4),右边选择点(9,6)

        第三次:
        从x轴开始选择

    二,搜索
        1.在本域内,没有进行跨域搜索
        2.要跨到其他域搜索
1.6 案例：鸢尾花种类预测--数据集介绍[****]
    1.获取数据集
        sklearn.datasets.
        小数据:
            sklearn.datasets.load_*
            注意:
            该数据从本地获取
        大数据集:
            sklearn.datasets.fetch_*
            注意:
            该数据从网上下载
            subset--表示获取到的数据集类型
    2.数据集返回值介绍
        返回值类型是bunch--是一个字典类型
        返回值的属性:
            data：特征数据数组
            target：标签(目标)数组
            DESCR：数据描述
            feature_names：特征名,
            target_names：标签(目标值)名
    3.数据可视化
        import seaborn
        seaborn.lmplot()
            参数
            x,y -- 具体x轴,y轴数据的索引值
            data -- 具体数据
            hue -- 目标值是什么
            fit_reg -- 是否进行线性拟合
    4.数据集的划分
        api:
        sklearn.model_selection.train_test_split(arrays, *options)
            参数:
            x -- 特征值
            y -- 目标值
            test_size -- 测试集大小
            ramdom_state -- 随机数种子
            返回值:
            x_train, x_test, y_train, y_test
1.7 特征工程-特征预处理[****]
    1.定义
        通过一些转换函数将特征数据转换成更加适合算法模型的特征数据过程
    2.包含内容:
        归一化
        标准化
    3.api
        sklearn.preprocessing
    4.归一化
        定义:
            对原始数据进行变换把数据映射到(默认为[0,1])之间
        api:
            sklearn.preprocessing.MinMaxScaler (feature_range=(0,1)… )
            参数:
            feature_range -- 自己指定范围,默认0-1
        总结:
            鲁棒性比较差(容易受到异常点的影响)
            只适合传统精确小数据场景(以后不会用你了)
    5.标准化
        定义:
            对原始数据进行变换把数据变换到均值为0,标准差为1范围内
        api:
            sklearn.preprocessing.StandardScaler( )
        总结:
            异常值对我影响小
            适合现代嘈杂大数据场景(以后就是用你了)
1.8 案例：鸢尾花种类预测—流程实现[***]
    1.api
    sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,algorithm='auto')
        algorithm -- 选择什么样的算法进行计算
            auto,ball_tree, kd_tree, brute
    2.案例流程
        1.获取数据集
        2.数据基本处理
        3.特征工程
        4.机器学习(模型训练)
        5.模型评估





1 KNN
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# coding:utf-8

from sklearn.neighbors import KNeighborsClassifier

# 获取数据
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]

# 机器学习
# 1.实例化一个训练模型
estimator = KNeighborsClassifier(n_neighbors=2)
# 2.调用fit方法进行训练
estimator.fit(x, y)

# 预测其他值
ret = estimator.predict([[-1]])
print(ret)


2 数据集介绍
# coding:utf-8

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split

# 1.数据集获取
# 1.1 小数据集获取
iris = load_iris()
# print(iris)

# 1.2 大数据集获取
news = fetch_20newsgroups()
# print(news)

# 2.数据集属性描述
# print("数据集中特征值是:\n", iris.data)
# print("数据集中目标值是:\n", iris["target"])
# print("数据集中特征值名字是:\n", iris.feature_names)
# print("数据集中目标值名字是:\n", iris.target_names)
# print("数据集的描述:\n", iris.DESCR)

# 3.数据可视化
# 3.1 数据类型转换,把数据用DataFrame存储
iris_data = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_data["target"] = iris.target


# print(iris_data)


def iris_plot(data, col1, col2):
    sns.lmplot(x=col1, y=col2, data=data, hue="target", fit_reg=False)
    plt.title("鸢尾花数据展示")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


# iris_plot(iris_data, "Sepal_Length", 'Petal_Width')
# iris_plot(iris_data, 'Sepal_Width', 'Petal_Length')


# 4.数据集的划分
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)
# print("训练集的特征值是:\n", x_train)
# print("测试集的特征值是:\n", x_test)
# print("训练集的目标值是:\n", y_train)
print("测试集的目标值是:\n", y_test)


# print("训练集的目标值形状:\n", y_train.shape)
# print("测试集的目标值形状:\n", y_test.shape)


x_train1, x_test1, y_train1, y_test1 = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
x_train2, x_test2, y_train2, y_test2 = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
print("测试集的目标值是:\n", y_test1)
print("测试集的目标值是:\n", y_test2)


4 特征预处理
# coding:utf-8

from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

data = pd.read_csv("./data/dating.txt")
print(data)

# # 1.归一化
# # 1.1 实例化一个转换器
# transfer = MinMaxScaler(feature_range=(0, 10))
# # 1.2 调用fit_transfrom方法
# minmax_data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
# print("经过归一化处理之后的数据为:\n", minmax_data)


# 2.标准化
# 2.1 实例化一个转换器
transfer = StandardScaler()
# 2.2 调用fit_transfrom方法
minmax_data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
print("经过标准化处理之后的数据为:\n", minmax_data)

5 knn_example
# coding:utf-8
"""
1.获取数据集
2.数据基本处理
3.特征工程
4.机器学习(模型训练)
5.模型评估
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
# 2.1 数据分割
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.2)

# 3.特征工程
# 3.1 实例化一个转换器
transfer = StandardScaler()
# 3.2 调用fit_transform方法
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 4.机器学习(模型训练)
# 4.1 实例化一个估计器
estimator = KNeighborsClassifier(n_neighbors=5)
# 4.2 模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是:\n", y_pre)
print("预测值和真实值对比:\n", y_pre == y_test)

# 5.2 输出准确率
ret = estimator.score(x_test, y_test)
print("准确率是:\n", ret)


day5 
1.9 k近邻算法总结[**]
    优点：
        1.简单有效
        2.重新训练代价底
        3.适合类域交叉样本
        4.适合大样本自动分类
    缺点：
        1.惰性学习
        2.类别评分不是规格化
        3.输出可解释性不强
        4.对不均衡的样本不擅长
            样本不均衡：收集到的数据每个类别占比严重失衡
        5.计算量较大
1.10 交叉验证和网格搜索[****]
    1.交叉验证
        1.定义：
            将拿到的训练数据，分为训练和验证集
            *折交叉验证
        2.分割方式：
            训练集：训练集+验证集
            测试集：测试集
        3.为什么需要交叉验证
            为了让被评估的模型更加准确可信
            注意：交叉验证不能提高模型的准确率
    2.网格搜索
        超参数:
            sklearn中,需要手动指定的参数,叫做超参数
        网格搜索就是把这些超参数的值,通过字典的形式传递进去,然后进行选择最优值
    3.api:
        sklearn.model_selection.GridSearchCV(estimator, param_grid=None,cv=None)
            estimator -- 选择了哪个训练模型
            param_grid -- 需要传递的超参数
            cv -- 几折交叉验证
1.11 案例2：预测facebook签到位置[***]
    # 1、获取数据集
    # 2.基本数据处理
    # 2.1 缩小数据范围
    # 2.2 选择时间特征
    # 2.3 去掉签到较少的地方
    # 2.4 确定特征值和目标值
    # 2.5 分割数据集
    # 3.特征工程--特征预处理(标准化)
    # 4.机器学习--knn+cv
    # 5.模型评估
2. 线性回归
2.1 线性回归简介
    1.定义
        利用回归方程(函数)对一个或多个自变量(特征值)和因变量(目标值)之间关系进行建模的一种分析方式
    2.表示方式:
        h(w) = w1x1 + w2x2 + w3x3 + ... + b
            = W转置x + b
    3.分类
        线性关系
        非线性关系
2.2 线性回归api初步使用
    1.api
        sklearn.linear_model.LinearRegression()
            属性:
            LinearRegression.coef_：回归系数

2.4 线性回归的损失和优化[****]
    1.损失
        最小二乘法
    2.优化
        正规方程
        梯度下降法
    3.正规方程 -- 一蹴而就
        利用矩阵的逆,转置进行一步求解
        只是适合样本和特征比较少的情况
    4.梯度下降法 -- 循序渐进
        举例:
            山  -- 可微分的函数
            山底 -- 函数的最小值
        梯度的概念
            单变量 -- 切线
            多变量 -- 向量
        梯度下降法中关注的两个参数
            α  -- 就是步长
                步长太小 -- 下山太慢
                步长太大 -- 容易跳过极小值点(*****)
            为什么梯度要加一个负号
                梯度方向是上升最快方向,负号就是下降最快方向
    5.梯度下降法和正规方程对比:
        梯度下降                 正规方程
        需要选择学习率          不需要
        需要迭代求解            一次运算得出
        特征数量较大可以使用     需要计算方程，时间复杂度高O(n3)
    6.选择：
        小规模数据：
            LinearRegression(不能解决拟合问题)
            岭回归
        大规模数据：
            SGDRegressor
2.5 梯度下降法介绍[###]
    1 全梯度下降算法（FG）
        在进行计算的时候,计算所有样本的误差平均值,作为我的目标函数
    2 随机梯度下降算法（SG）
        每次只选择一个样本进行考核
    3 小批量梯度下降算法（mini-bantch）
        选择一部分样本进行考核
    4 随机平均梯度下降算法（SAG）
        会给每个样本都维持一个平均值,后期计算的时候,参考这个平均值
2.6 api
    正规方程
        sklearn.linear_model.LinearRegression(fit_intercept=True)
    梯度下降法


2.7 案例[**]
    # 1.获取数据
    # 2.数据基本处理
    # 2.1 数据集划分
    # 3.特征工程 --标准化
    # 4.机器学习(线性回归)
    # 5.模型评估

1 cv_example
# coding:utf-8
"""
1.获取数据集
2.数据基本处理
3.特征工程
4.机器学习(模型训练)
5.模型评估
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
# 2.1 数据分割
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# 3.特征工程
# 3.1 实例化一个转换器
transfer = StandardScaler()
# 3.2 调用fit_transform方法
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)


# 4.机器学习(模型训练)
# 4.1 实例化一个估计器
estimator = KNeighborsClassifier()

# 4.2 调用交叉验证网格搜索模型
param_grid = {"n_neighbors": [1, 3, 5, 7, 9]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=10, n_jobs=-1)

# 4.3 模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是:\n", y_pre)
print("预测值和真实值对比:\n", y_pre == y_test)

# 5.2 输出准确率
ret = estimator.score(x_test, y_test)
print("准确率是:\n", ret)

# 5.3 其他评价指标
print("最好的模型：\n", estimator.best_estimator_)
print("最好的结果:\n", estimator.best_score_)
print("整体模型结果:\n", estimator.cv_results_)

2 FBlocation_example
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1、获取数据集
# 2.基本数据处理
# 2.1 缩小数据范围
# 2.2 选择时间特征
# 2.3 去掉签到较少的地方
# 2.4 确定特征值和目标值
# 2.5 分割数据集
# 3.特征工程--特征预处理(标准化)
# 4.机器学习--knn+cv
# 5.模型评估b

# 1、获取数据集
data = pd.read_csv("./data/FBlocation/train.csv")
data.head()
data.describe()
data.shape

# 2.基本数据处理
# 2.1 缩小数据范围
facebook_data = data.query("x>2.0 & x<2.5 & y>2.0 & y<2.5")
facebook_data.head()
facebook_data.shape
# 2.2 选择时间特征
facebook_data["time"].head()

time = pd.to_datetime(facebook_data["time"], unit="s")
# 脱敏
time.head()

time = pd.DatetimeIndex(time)
time

facebook_data["hour"] = time.hour
time.hour

facebook_data["day"] = time.day
time.day

facebook_data["weekday"] = time.weekday
time.weekday

facebook_data.head()

# 2.3 去掉签到较少的地方
place_count = facebook_data.groupby("place_id").count()
place_count.head()

place_count = place_count[place_count["row_id"] > 3]
place_count.head()

place_count.index

facebook_data = facebook_data[facebook_data["place_id"].isin(place_count.index)]
facebook_data.head()

facebook_data.shape

# 2.4 确定特征值和目标值
x = facebook_data[["x", "y", "accuracy", "day", "hour", "weekday"]]
y = facebook_data["place_id"]

# 2.5 分割数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.2)

# 3.特征工程--特征预处理(标准化)
# 3.1 实例化一个转换器
transfer = StandardScaler()

# 3.2 调用fit_transform
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.机器学习--knn+cv
# 4.1 实例化一个估计器
estimator = KNeighborsClassifier()

# 4.2 调用交叉验证,网格搜索
param_grid = {"n_neighbors" : [3,5,7]}
estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=9, n_jobs=14)

# 4.3 训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 预测值输出
y_pre = estimator.predict(x_test)
print("预测值为:\n", y_pre)

# 5.2 score
score = estimator.score(x_test, y_test)
print("准确率为:\n", score)

# 5.3 其他评价指标
print("最好的模型：\n", estimator.best_estimator_)
print("最好的结果:\n", estimator.best_score_)
print("整体模型结果:\n", estimator.cv_results_)


3 hello_linear_model
# coding:utf-8
"""
1.获取数据集
2.数据基本处理（该案例中省略）
3.特征工程（该案例中省略）
4.机器学习
5.模型评估（该案例中省略）
"""

from sklearn.linear_model import LinearRegression

# 获取数据
x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

# 模型训练
# 1.实例化一个估计器
estimator = LinearRegression()

# 2.调用fit方法,进行模型训练
estimator.fit(x, y)

# 查看一下系数值
coef = estimator.coef_
print("系数是:\n", coef)

# 预测:
print("预测值是:\n", estimator.predict([[80, 100]]))

4 linear_model_demo
# coding:utf-8

"""
1.获取数据
2.数据基本处理
2.1 数据集划分
3.特征工程 --标准化
4.机器学习(线性回归)
5.模型评估
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def linear_model1():
    """
    正规方程
    :return: None
    """
    # 1.获取数据
    boston = load_boston()

    # 2.数据基本处理
    # 2.1 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习(线性回归)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    print("这个模型的偏置是:\n", estimator.intercept_)

    # 5.模型评估
    # 5.1 预测值和准确率
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)

    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)

    # 5.2 均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


if __name__ == '__main__':
    linear_model1()

day6 
2.6 api介绍【**】
    1.梯度下降法
        sklearn.linear_model.SGDRegressor(loss="squared_loss", fit_intercept=True, learning_rate ='invscaling', eta0=0.01)
            参数：
                1.loss -- 损失 （最小二乘）
                2.learning_rate -- 学习率
                    一般时都是进行动态的更新，也可以指定成为一个常数，但是不推荐。
2.8 欠拟合和过拟合【****】
    欠拟合
        在训练集上表现不好，在测试集上表现不好
        解决方法：
            继续学习
            1.添加其他特征项
            2.添加多项式特征
    过拟合
        在训练集上表现好，在测试集上表现不好
        解决方法：
            1.重新清洗数据集
            2.增大数据的训练量
            3.正则化
            4.减少特征维度
    正则化
        通过限制高次项的系数进行防止过拟合
            L1正则化
                理解：直接把高次项前面的系数变为0
                Lasso回归
            L2正则化
                理解：把高次项前面的系数变成特别小的值
                岭回归
2.9  正则化线性模型【***】
    1.Ridge Regression 岭回归
        就是把系数添加平方项
        然后限制系数值的大小
        α值越小，系数值越大，α越大，系数值越小
    2.Lasso 回归
        对系数值进行绝对值处理
        由于绝对值在顶点处不可导，所以进行计算的过程中产生很多0，最后得到结果为：稀疏矩阵
    3.Elastic Net 弹性网络
        是前两个内容的综合
        设置了一个r,如果r=0--岭回归，r=1--Lasso回归
    4.Early stopping
        通过限制错误率的阈值，进行停止
2.10 线性回归的改进-岭回归【**】
    1.api
    sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True,solver="auto", normalize=False)
        具有l2正则化的线性回归
        alpha -- 正则化
            正则化力度越大，权重系数会越小
            正则化力度越小，权重系数会越大
        normalize
            默认封装了，对数据进行标准化处理
2.11 模型的保存和加载【*】
    api:
    sklearn.externals import joblib
        保存：joblib.dump(estimator, 'test.pkl')
        加载：estimator = joblib.load('test.pkl')
    注意：
    1.保存文件，后缀名是**.pkl
    2.加载模型是需要通过一个变量进行承接

3.逻辑回归
3.1 逻辑回归介绍【****】
    1.逻辑回归概念
        解决的是一个二分类问题
        逻辑回归的输入是线性回归的输出
    2.原理
        1.输入：
            线性回归的输出
        2.激活函数
            sigmoid函数
                把整体的值映射到[0,1]
                再设置一个阈值，进行分类判断
        3.损失
            对数似然损失
                借助了log思想，进行完成
                真实值等于0，等于1两种情况进行划分
        4.优化
            提升原本属于1类别的概率，降低原本是0类别的概率。
3.2 逻辑回归api介绍【*】
    sklearn.linear_model.LogisticRegression()
    注意：回归，分类api有时候是可以混合使用的
3.3 案例：癌症分类预测-良／恶性乳腺癌肿瘤预测【**】
    1.获取数据
    2.基本数据处理
    2.1 缺失值处理
    2.2 确定特征值,目标值
    2.3 分割数据
    3.特征工程(标准化)
    4.机器学习(逻辑回归)
    5.模型评估
3.4 分类评估方法【***】
    1.混淆矩阵
        真正例（TP）
        伪反例（FN）
        伪正例（FP）
        真反例（TN）
    2. 精确率(Precision)与召回率(Recall)
        准确率：（对不对）
            （TP+TN）/(TP+TN+FN+FP)
        精确率 -- 查的准不准
            TP/(TP+FP)
        召回率 -- 查的全不全
            TP/(TP+FN)
        F1-score
            反映模型的稳健性
    3.api
        sklearn.metrics.classification_report(y_true, y_pred)
    4.roc曲线和auc指标
        roc曲线
            通过tpr和fpr来进行图形绘制，然后绘制之后，行成一个指标auc
        auc
            越接近1，效果越好
            越接近0，效果越差
            越接近0.5，效果就是胡说
        注意：
            这个指标主要用于评价不平衡的二分类问题
    5.api
        sklearn.metrics.roc_auc_score(y_true, y_score)
            y_true -- 要把正例转换为1，反例转换为0
3.5 ROC曲线的绘制【###】
    1.构建模型，把模型的概率值从大到小进行排序
    2.从概率最大的点开始取值，一直进行tpr和fpr的计算，然后构建整体模型，得到结果
    3.其实就是在求解积分（面积）

4.决策树算法
4.1 决策树算法简介【**】
    1.简介
        定义：
        是一种树形结构，其中每个内部节点表示一个属性上的判断，每个分支代表一个判断结果的输出，最后每个叶节点代表一种分类结果，本质是一颗由多个判断节点组成的树
4.2 决策树分类原理【****】
    1.熵
        用于衡量一个对象的有序程度
        系统越有序，熵值越低；系统越混乱或者分散，熵值越高。
    2.信息熵
        1.从信息的完整性上进行的描述:
        当系统的有序状态一致时，数据越集中的地方熵值越小，数据越分散的地方熵值越大。
        2.从信息的有序性上进行的描述:
        当数据量一致时，系统越有序，熵值越低；系统越混乱或者分散，熵值越高。
    3.把信息转换成熵值
        -plogp


1 linear_model_demo
# coding:utf-8

"""
1.获取数据
2.数据基本处理
2.1 数据集划分
3.特征工程 --标准化
4.机器学习(线性回归)
5.模型评估
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error


def linear_model1():
    """
    正规方程
    :return: None
    """
    # 1.获取数据
    boston = load_boston()

    # 2.数据基本处理
    # 2.1 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习(线性回归)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    print("这个模型的偏置是:\n", estimator.intercept_)

    # 5.模型评估
    # 5.1 预测值和准确率
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)

    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)

    # 5.2 均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


def linear_model2():
    """
    梯度下降法
    :return: None
    """
    # 1.获取数据
    boston = load_boston()

    # 2.数据基本处理
    # 2.1 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习(线性回归)
    estimator = SGDRegressor(max_iter=1000, learning_rate="constant", eta0=0.001)

    estimator.fit(x_train, y_train)
    print("这个模型的偏置是:\n", estimator.intercept_)

    # 5.模型评估
    # 5.1 预测值和准确率
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)

    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)

    # 5.2 均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


def linear_model3():
    """
    岭回归
    :return: None
    """
    # 1.获取数据
    boston = load_boston()

    # 2.数据基本处理
    # 2.1 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习(线性回归)
    # estimator = Ridge()
    estimator = RidgeCV(alphas=(0.001, 0.1, 1, 10, 100))

    estimator.fit(x_train, y_train)
    print("这个模型的偏置是:\n", estimator.intercept_)

    # 5.模型评估
    # 5.1 预测值和准确率
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)

    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)

    # 5.2 均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


if __name__ == '__main__':
    linear_model1()
    linear_model2()
    linear_model3()


2 model_dump_load
# coding:utf-8

"""
1.获取数据
2.数据基本处理
2.1 数据集划分
3.特征工程 --标准化
4.机器学习(线性回归)
5.模型评估
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


def dump_load_demo():
    """
    模型保存和加载
    :return: None
    """
    # 1.获取数据
    boston = load_boston()

    # 2.数据基本处理
    # 2.1 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22, test_size=0.2)

    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    #
    # # 4.机器学习(线性回归)
    # # 4.1 模型训练
    # estimator = Ridge()
    #
    # estimator.fit(x_train, y_train)
    # print("这个模型的偏置是:\n", estimator.intercept_)
    #
    # # 4.2 模型保存
    # joblib.dump(estimator, "./data/test.pkl")

    # 4.3 模型加载
    estimator = joblib.load("./data/test.pkl")

    # 5.模型评估
    # 5.1 预测值和准确率
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)

    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)

    # 5.2 均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


if __name__ == '__main__':
    dump_load_demo()

3 logistic_regression_demo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# 1.获取数据
# 2.基本数据处理
# 2.1 缺失值处理
# 2.2 确定特征值,目标值
# 2.3 分割数据
# 3.特征工程(标准化)
# 4.机器学习(逻辑回归)
# 5.模型评估

# 1.获取数据
names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                  names=names)

data.head()

# 2.基本数据处理
# 2.1 缺失值处理
data = data.replace(to_replace="?", value=np.nan)
data = data.dropna()

data.describe()

data.head()

x = data.iloc[:, 1:-1]
x.head()

y = data["Class"]
y.head()

# 2.3 分割数据
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.2)

# 3.特征工程(标准化)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)

x_test = transfer.fit_transform(x_test)

# 4.机器学习(逻辑回归)
estimator = LogisticRegression()
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 基本评估
y_pre = estimator.predict(x_test)
print("预测值是：\n", y_pre)

score = estimator.score(x_test, y_test)
print("准确率是：\n", score)

# 5.2 其他评估
ret = classification_report(y_test, y_pre, labels=(2,4), target_names=("良性", "恶性"))
print(ret)

# 不平衡二分类问题评估方法
y_test = np.where(y_test>3, 1, 0)

roc_auc_score(y_true=y_test, y_score=y_pre)


day7 
4.2 决策树分类原理【*****】
    1.信息增益
        信息增益 = entroy(前) - entroy(后)
        注意：信息增益越大，我们优先选择这个属性进行计算
        信息增益优先选择属性总类别比较多的进行划分
    2.信息增益率
        维持了一个分离信息度量，通过这个分离信息度量当分母，进行限制
    3.基尼增益
        1.基尼值：
            从数据集D中随机抽取两个样本，其类别标记不一致的概率
            Gini（D）值越小，数据集D的纯度越高。
        2.基尼指数：
            选择使划分后基尼系数最小的属性作为最优化分属性
        3.基尼增益：
            选择基尼增益最大的点，进行优化划分
        4.基尼增益构造过程：
            1.开始将所有记录看作一个节点
            2.遍历每个变量的每一种分割方式，找到最好的分割点
            3.分割成两个节点N1和N2
            4.对N1和N2分别继续执行2-3步，直到每个节点足够“纯”为止。
        5.决策树的变量可以有两种，分别对应的划分方式：
            1.数字型
                通过对数据取两个数字之间的中间值，进行划分
            2.名称型
                通过对属性的类别进行划分
        6.如何评估分割点的好坏？
            主要看分割的是否纯
    4.三种算法对比：【****】
        ID3 算法
            采用信息增益作为评价标准
            只能对描述属性为离散型属性的数据集构造决策树
            缺点是倾向于选择取值较多的属性
        C4.5算法
            用信息增益率来选择属性
            可以处理连续数值型属性
            采用了一种后剪枝方法
            对于缺失值的处理
            缺点是：C4.5只适合于能够驻留于内存的数据集
        CART算法
            C4.5不一定是二叉树，但CART一定是二叉树
            是信息增益的简化版本
4.3 cart剪枝
    1.剪枝原因
        噪声、样本冲突，即错误的样本数据
        特征即属性不能完全作为分类标准
        巧合的规律性，数据量不够大。
    2.常用剪枝方法
        预剪枝
            在构建树的过程中，同时剪枝
                eg:
                限制节点最小样本数
                指定数据高度
                指定熵值的最小值
        后剪枝
            把一棵树，构建完成之后，再进行从下往上的剪枝

4.4 特征工程-特征提取【***】
    1.特征提取
        将任意数据（如文本或图像）转换为可用于机器学习的数字特征
    2.特征提取分类:
        字典特征提取(特征离散化)
        文本特征提取
        图像特征提取（深度学习将介绍）
    3.api
        sklearn.feature_extraction
    4.字典特征提取
        字典特征提取就是对类别型数据进行转换
        api:
            sklearn.feature_extraction.DictVectorizer(sparse=True,…)
            aparse矩阵
                1.节省内容
                2.提高读取效率
            属性：
                DictVectorizer.get_feature_names() 返回类别名称
        注意：
            对于特征当中存在类别信息的我们都会做one-hot编码处理
    5.文本特征提取（英文）
        api:
            sklearn.feature_extraction.text.CountVectorizer(stop_words=[])
                stop_words -- 停用词
                注意：没有sparse这个参数
                    单个字母，标点符号不做统计
    6.文本特征提取（中文）
        注意：
            1.在中文文本特征提取之前，需要对句子（文章）进行分词（jieba）
            2.里面依旧可以使用停用词，进行词语的限制
    7.tfidf
        1.主要思想：
            如果某个词或短语在一篇文章中出现的概率高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类
        2.tfidf
            tf -- 词频
            idf -- 逆向文档频率
        3.api
            sklearn.feature_extraction.text.TfidfVectorizer
        注意：
            分类机器学习算法进行文章分类中前期数据处理方式
4.5 决策树算法api【*】
    sklearn.tree.DecisionTreeClassifier(criterion=’gini’, max_depth=None,random_state=None)
        参数：
        criterion
            特征选择标准
        min_samples_split
            内部节点再划分所需最小样本数
        min_samples_leaf
            叶子节点最少样本数
        max_depth
            决策树最大深度
4.6 案例：泰坦尼克号乘客生存预测【***】
    1.流程分析
        1.获取数据
        2.数据基本处理
        2.1 确定特征值,目标值
        2.2 缺失值处理
        2.3 数据集划分
        3.特征工程(字典特征抽取)
        4.机器学习(决策树)
        5.模型评估
    2.可视化
        sklearn.tree.export_graphviz()
    3.小结
        优点：
            简单的理解和解释，树木可视化。
        缺点：
            决策树学习者可以创建不能很好地推广数据的过于复杂的树,容易发生过拟合。
        改进：
            减枝cart算法
            随机森林（集成学习的一种）

5. 集成学习
5.1 集成学习算法简介
    1.什么是集成学习
        超级个体和弱者联盟对比，后者更优
    2.复习：机器学习两个核心任务
        1.解决欠拟合问题
            弱弱组合变强
            boosting
        2.解决过拟合问题
            互相遏制变壮
            Bagging
5.2 Bagging【**】
    1.bagging集成过程
        1.采样
            从所有样本里面，采样一部分
        2.学习
            训练弱学习器
        3.集成
            使用平权投票
    2.随机森林介绍
        1.随机森林定义
            随机森林 = Bagging + 决策树
        2.流程：
            1.随机选取m条数据
            2.随机选取k个特征
            3.训练决策树
            4.重复1-3
            5.对上面的若决策树进行平权投票
        3.注意：
            1.随机选取样本，且是有放回的抽取
            2.选取特征的时候吗，选择m<<M
                M是所有的特征数
        4.api
            sklearn.ensemble.RandomForestClassifier()
    3.bagging的优点
        Bagging + 决策树/线性回归/逻辑回归/深度学习… = bagging集成学习方法
        1.均可在原有算法上提高约2%左右的泛化正确率
        2.简单, 方便, 通用

1 feature_extration
# coding:utf-8

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


def dict_demo():
    """
    字典特征提取
    :return:
    """
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 字典特征提取
    # 1.实例化
    transfer = DictVectorizer(sparse=False)

    # 2.调用fit_transform
    trans_data = transfer.fit_transform(data)

    print("特征名字是：\n", transfer.get_feature_names())

    print(trans_data)


def english_count_text_demo():
    """
    文本特征提取 -- 英文
    :return: NOne
    """
    data = ["life is is short,i like python",
            "life is too long,i dislike python"]

    # 1.实例化
    # transfer = CountVectorizer(sparse=False)  # 注意，没有sparse
    transfer = CountVectorizer(stop_words=["dislike"])

    # 2.调用fit_transform
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names())
    print(transfer_data.toarray())


def chinese_count_text_demo1():
    """
    文本特征提取 -- 中文
    :return: NOne
    """
    data = ["人生 苦短, 我 喜欢 Python",
            "生活 太长久, 我 不 喜欢 Python"]

    # 1.实例化
    transfer = CountVectorizer()

    # 2.调用fit_transform
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names())
    print(transfer_data.toarray())


def cut_word(sen):
    """
    中文分词
    :return: sen
    """
    # print(" ".join(list(jieba.cut(sen))))
    return " ".join(list(jieba.cut(sen)))


def chinese_count_text_demo2():
    """
    文本特征提取 -- 中文
    :return: NOne
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    list = []
    for temp in data:
        # print(temp)
        list.append(cut_word(temp))
    print(list)

    # 1.实例化
    transfer = CountVectorizer(stop_words=["一种", "还是"])

    # 2.调用fit_transform
    transfer_data = transfer.fit_transform(list)

    print(transfer.get_feature_names())
    print(transfer_data.toarray())


def tfidf_text_demo():
    """
    文本特征提取 -- 中文
    :return: NOne
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    list = []
    for temp in data:
        # print(temp)
        list.append(cut_word(temp))
    # print(list)

    # 1.实例化
    # transfer = CountVectorizer(stop_words=["一种", "还是"])
    transfer = TfidfVectorizer()

    # 2.调用fit_transform
    transfer_data = transfer.fit_transform(list)

    print(transfer.get_feature_names())
    print(transfer_data.toarray())


if __name__ == '__main__':
    # dict_demo()
    # english_count_text_demo()
    # chinese_count_text_demo1()
    # cut_word("我喜欢你中国")
    # chinese_count_text_demo2()
    tfidf_text_demo()

2 decisition_tree_demo
# 1.获取数据
# 2.数据基本处理
# 2.1 确定特征值,目标值
# 2.2 缺失值处理
# 2.3 数据集划分
# 3.特征工程(字典特征抽取)
# 4.机器学习(决策树)
# 5.模型评估

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# 1.获取数据
data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
data
data.describe()

# 2.数据基本处理
# 2.1 确定特征值,目标值
x = data[["pclass", "age", "sex"]]
x.head()
y = data["survived"]
y.head()
# 2.2 缺失值处理
x["age"].fillna(value=data["age"].mean(), inplace=True)
x.head()
# 2.3 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

# 3.特征工程(字典特征抽取)
x.head()
x_train = x_train.to_dict(orient="records")
x_test = x_test.to_dict(orient="records")
x_train

transfer = DictVectorizer()

x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
x_train

# 4.机器学习(决策树)
estimator = DecisionTreeClassifier(max_depth=5)
estimator.fit(x_train, y_train)

# 5.模型评估
y_pre = estimator.predict(x_test)
print(y_pre)

ret = estimator.score(x_test, y_test)
ret

# 决策树可视化
export_graphviz(estimator, out_file="./data/tree.dot", feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])


3 random_forest_demo
# 1.获取数据
# 2.数据基本处理
# 2.1 确定特征值,目标值
# 2.2 缺失值处理
# 2.3 数据集划分
# 3.特征工程(字典特征抽取)
# 4.机器学习(随机森林+cv)
# 5.模型评估

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer
# from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier

# 1.获取数据
data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
data
data.describe()

# 2.数据基本处理
# 2.1 确定特征值,目标值
x = data[["pclass", "age", "sex"]]
x.head()
y = data["survived"]
y.head()
# 2.2 缺失值处理
x["age"].fillna(value=data["age"].mean(), inplace=True)
x.head()
# 2.3 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

# 3.特征工程(字典特征抽取)
x.head()
x_train = x_train.to_dict(orient="records")
x_test = x_test.to_dict(orient="records")
x_train

transfer = DictVectorizer()

x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

x_train

# 4.机器学习（模型训练）
estimator = RandomForestClassifier()

param_grid = {"n_estimators": [120,200,300,500,800,1200], "max_depth": [5, 8, 15, 25, 30]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)

estimator.fit(x_train, y_train)
estimator.score(x_test, y_test)

estimator.best_estimator_


day8 
5.3 Boosting【**】
    1.boosting集成原理
        随着学习的积累从弱到强
    2.实现过程
        1.初始化训练数据权重，初始权重是相等的
        2.通过这个学习器，计算错误率
        3.计算这个学习期的投票权重
        4.对每个样本进行重新赋权
        5.重复前面1-4
        6.对构建后的最后的学习器进加权投票
    3.bagging集成与boosting集成的区别：
        数据方面：
            bagging:重新采样
            boosting:对数据进行权重调整
        投票方面：
            bagging:平权
            boosting:加权
        学习顺序方面：
            bagging:并行
            boosting:串行
        主要作用：
            bagging:过拟合
            boosting:欠拟合
    2 GBDT
        梯度提升决策树(GBDT Gradient Boosting Decision Tree)
        GBDT = 梯度下降 + Boosting + 决策树
    3.XGBoost
        XGBoost= 二阶泰勒展开+boosting+决策树+正则化

6.聚类算法
6.1 聚类算法简介
    1.聚类算法分类
        粗聚类
        细聚类
    2.定义
        一种典型的无监督学习算法，
        主要用于将相似的样本自动归到一个类别中
        计算样本和样本之间的相似性，一般使用欧式距离
6.2 聚类算法api初步使用
    1.api
        sklearn.cluster.KMeans(n_clusters=8)
        参数:
        n_clusters:开始的聚类中心数量
6.3 聚类算法实现流程【***】
    k-means其实包含两层内容：
        k -- 选几个中心店
        means -- 均值计算
    流程
        1、随机设置K个特征空间内的点作为初始的聚类中心
        2、对于其他每个点计算到K个中心的距离，未知的点选择最近的一个聚类中心点作为标记类别
        3、接着对着标记的聚类中心之后，重新计算出每个聚类的新中心点（平均值）
        4、如果计算得出的新中心点与原中心点一样（质心不再移动），那么结束，否则重新进行第二步过程
    kmeans小结
        kmeans由于要计算质心到每一个样本的距离，所以其收敛速度比较慢
6.4 模型评估【**】
    0.sse
        误差平方和
        值越小越好
    1. 肘部法
       下降率突然变缓时即认为是最佳的k值
    2. SC系数
       取值为[-1, 1]，其值越大越好
    3. CH系数
        分数s高则聚类效果越好
        CH需要达到的目的：
            用尽量少的类别聚类尽量多的样本，同时获得较好的聚类效果。
6.5 算法优化【***】
    1.k_means
        优点：
            简单，容易理解
        缺点：
            特别人容易陷入到局部最优解
    2.Canopy
        通过绘制同心圆，进行k值选择筛选
        需要确定同心圆的半径t1,t2
    3.K-means++
        距离平方进行求解
        保证下一个质心到当前质心，距离最远
    4.二分k-means
        通过误差平方和，设置阈值，然后进行划分
    5.k-medoids
        和kmeans选取中心点的方式不同
        通过从当前点选择中心点（质心）进行判断
    6.kernel kmeans【了解】
        映射到高维空间
    7.ISODATA【了解】
        动态聚类
        可以更改k值的大小
    8.Mini-batch K-Means【了解】
        大数据集分批聚类

6.6 特征降维【***】
    1.定义
        就是改变特征值，选择哪列保留，哪列删除
        目标是得到一组”不相关“的主变量
    2.降维的两种方式
        特征选择
        主成分分析（可以理解一种特征提取的方式）
    3.特征选择
        定义：提出数据中的冗余变量
        方法：
            Filter(过滤式)：主要探究特征本身特点、特征与特征和目标值之间关联
                方差选择法：低方差特征过滤
                相关系数
            Embedded (嵌入式)：算法自动选择特征（特征与目标值之间的关联）
                决策树:信息熵、信息增益
                正则化：L1、L2
                深度学习：卷积等
    4.低方差特征过滤
        把方差比较小的某一列进行剔除
        api:
            sklearn.feature_selection.VarianceThreshold(threshold = 0.0)
                删除所有低方差特征
                注意，参数threshold一定要进行值的指定
    5.相关系数
        主要实现方式：
            皮尔逊相关系数
            斯皮尔曼相关系数
        5.1 皮尔逊相关系数
            通过具体值的大小进行计算
            相对复杂
            api:
                from scipy.stats import pearsonr
                返回值，越接近|1|，相关性越强；越接近0，相关性越弱
        5.2 斯皮尔曼相关系数
            通过等级差进行计算
            比上一个简单
            api:
                from scipy.stats import spearmanr
                返回值，越接近|1|，相关性越强；越接近0，相关性越弱
    6.pca
        定义：
            高维数据转换为低维数据，然后产生了新的变量
        api:
            sklearn.decomposition.PCA(n_components=None)
                n_components
                    整数 -- 表示降低到几维
                    小数 -- 保留百分之多少的信息
6.7 案例：探究用户对物品类别的喜好【***】
    1.获取数据
    2.数据基本处理
    2.1 合并表格
    2.2 交叉表合并
    2.3 数据截取
    3.特征工程 — pca
    4.机器学习（k-means）
    5.模型评估

1 feature_selection_demo
# coding:utf-8

import pandas as pd
from sklearn.feature_selection import VarianceThreshold

def var_thr():
    """
    特征选择：低方差特征过滤
    :return:
    """
    data = pd.read_csv("./data/factor_returns.csv")
    print(data)

    transfer = VarianceThreshold(threshold=10)
    trans_data = transfer.fit_transform(data.iloc[:, 1:10])

    print("之前数据的形状：\n",data.iloc[:, 1:10].shape)
    print("之后数据的形状：\n",trans_data.shape)

    print(trans_data)
    pass


if __name__ == '__main__':
    var_thr()




2 hello_kmeans
import matplotlib.pyplot as plt
from sklearn import datasets

from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score

# 获取数据

X, y = datasets.make_blobs(n_samples=1000, n_features=2, 
                    centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                    cluster_std=[0.4, 0.1, 0.1, 0.1], random_state=1)

plt.scatter(X[:, 0], X[:, 1])
plt.show()


# 当n_clusters=2
# 模型训练
estimator = KMeans(n_clusters=2, random_state=2)
y_pre = estimator.fit_predict(X)

# 结果可视化
plt.scatter(X[:, 0], X[:, 1], c=y_pre)
plt.show()

# 模型评估
calinski_harabaz_score(X, y_pre)


# 当n_clusters=3
# 模型训练
estimator = KMeans(n_clusters=3, random_state=2)
y_pre = estimator.fit_predict(X)

# 结果可视化
plt.scatter(X[:, 0], X[:, 1], c=y_pre)
plt.show()

# 模型评估
calinski_harabaz_score(X, y_pre)


# 当n_clusters=4
# 模型训练
estimator = KMeans(n_clusters=4, random_state=2)
y_pre = estimator.fit_predict(X)

# 结果可视化
plt.scatter(X[:, 0], X[:, 1], c=y_pre)
plt.show()

# 模型评估
calinski_harabaz_score(X, y_pre)






3 相关系数
# coding:utf-8

from scipy.stats import pearsonr, spearmanr

# 皮尔逊演示
x1 = [12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9]
x2 = [21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]

ret = pearsonr(x1, x2)
print("这两列数据的皮尔逊相关系数为：\n", ret)


ret = spearmanr(x1, x2)
print("这两列数据的斯皮尔曼相关系数为：\n", ret)




4 pca_demo
# coding:utf-8

from sklearn.decomposition import PCA

data = [[2, 8, 4, 5],
        [6, 3, 0, 8],
        [5, 4, 9, 1]]

# 1.保留到多少维度
# transfer = PCA(n_components=2)
# trans_data = transfer.fit_transform(data)
# print(trans_data)

# 2.保留信息的百分比
transfer = PCA(n_components=0.95)
transfer_data = transfer.fit_transform(data)
print(transfer_data)



5 kmeans_demo
# 1.获取数据
# 2.数据基本处理
# 2.1 合并表格
# 2.2 交叉表合并
# 2.3 数据截取
# 3.特征工程 — pca
# 4.机器学习（k-means）
# 5.模型评估

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1.获取数据
order_product = pd.read_csv("./data/instacart/order_products__prior.csv")
products = pd.read_csv("./data/instacart/products.csv")
orders = pd.read_csv("./data/instacart/orders.csv")
aisles = pd.read_csv("./data/instacart/aisles.csv")

# 2.数据基本处理
# 2.1 合并表格
table1 = pd.merge(order_product, products, on=["product_id", "product_id"])

table2 = pd.merge(table1, orders, on=["order_id", "order_id"])

table = pd.merge(table2, aisles, on=["aisle_id", "aisle_id"])

table.shape

table.head()

# 2.2 交叉表合并
data = pd.crosstab(table["user_id"], table["aisle"])

data.head()

data.shape

# 2.3 数据截取
new_data = data[:1000]
new_data.shape

# 3.特征工程 — pca
transfer = PCA(n_components=0.9)
trans_data = transfer.fit_transform(new_data)
trans_data.shape
trans_data


# 4.机器学习（k-means）
estimator = KMeans(n_clusters=5)
y_pre = estimator.fit_predict(trans_data)


# 5.模型评估
silhouette_score(trans_data, y_pre)





*****可copy机器学习Python实践****
CH1 初学机器学习 
评估数据集 等价于 测试集
冲突矩阵 等价于 误差矩阵 混淆矩阵
1. scikit-learn 监督学习 中的分类与回归问题
安装包  https://pip.pypa.io/en/stable/getting-started/
py -m pip install sampleproject
py -m pip install --upgrade sampleproject
安装scipy py -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
conda create --name scipy numpy scipy matplotlib ipython jupyter pandas sympy nose
conda安装包
conda create --name <env_name> <package_names>
注意：
<env_name> 即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。
<package_names> 即安装在环境中的包名。名称两边不加尖括号“<>”。
① 如果要安装指定的版本号，则只需要在包名后面以 = 和版本号的形式执行。如： conda create --name python2 python=2.7 ，即创建一个名为“python2”的环境，环境中安装版本为2.7的python。
② 如果要在新创建的环境中创建多个包，则直接在 <package_names> 后以空格隔开，添加多个包名即可。如： conda create -n python3 python=3.5 numpy pandas ，即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。
当使用 conda install 无法进行安装时，可以使用pip进行安装。例如：see包。
→ 命令
pip install <package_name>
注意： <package_name> 为指定安装包的名称。包名两边不加尖括号“<>”。
如： pip install see 即安装see包。
→ 注意
pip只是包管理器，无法对环境进行管理。因此如果想在指定环境中使用pip进行安装包，则需要先切换到指定环境中，再使用pip命令安装包。
pip无法更新python，因为pip并不将python视为包。
pip可以安装一些conda无法安装的包 conda也可以安装一些pip无法安装的包。因此当使用一种命令无法安装包时，可以尝试用另一种命令。
conda remove --name <env_name> <package_name>
conda upgrade --all

import scipy
import numpy
import matplotlib
import pandas
print ('scipy:{}' .format(scipy.__version__))
print ('numpy:{}'.format(numpy. __version__))
print ( 'matplotlib:{}' .format(matplotlib. __version__))
print ( 'pandas:{}'.format(pandas.__version__))

CH3 第一个机器学习项目
#导入类库
from pandas import read csv
from pandas.plotting import scatter_matrix 
from matplotlib import pyplot 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GussianNB
from sklearn.svm import SVC 
#导入数据
filename = 'iris.data.csv'
names = ['separ-length', 'separ-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(filename, names=names)
#显示数据维度
通过查看数据的维度，可以对数据集有一个大概的了解，如数据集中有多少行数据、
数据有几个属性
print('数据维度: 行 %s, 列 %s' % dataset.shape)
执行结果
数据维度 150 ，列 5
#查看数据的前10行
print(dataset.head(10))
#分类分布情况
通过前面设定的数据特征名称来查看数据
print(dataset.groupby('class').size())
可视化
#箱线图
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, share=False)
pyplot.show()
#直方图
dataset.hist()
pyplot.show()
多变量图表
通过散点矩阵图查看每个属性的影响关系
#散点矩阵图
scatter_matrix(dataset)
pyplot.show()

评估算法
(1)分离出评估数据集
(2)采用 10 折交叉验证来评估算法模型
(3)生成 6 个不同的模型来预测新数据
(4)选择最优模型

分离出评估数据集
想知道算法模型对真实数据的准确度如何 这就是保留一部分数据来评估算法模型的主要原因
将按照 80% 训练数据集 20%的测试数据集来分离数据
#分离数据集
array = dataset.value 
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = \
    train_test_split(X, Y, test_size = validation_size, random_state=seed)
分离出了X_train 和 Y_train 用来训练算法创建模型 X_validation和Y_validation在后面会用来验证评估模型

评估模式
在这里将通过 10 折交叉验证来分离训练数据集并且评估算法模型的准确度。10折交叉验证是随机地将数据分成 10 份，9 份用来训练模型 1 份用来评估算法 后面我
会使用相同的数据对每一种算法进行训练和评估 从中选择最好模型

创建模型
六种算法
线性回归(LR)
线性判别分析(LDA)
K近邻(KNN)
分类与回归树(CART)
贝叶斯分类器(NB)
支持向量机(SVM)

#算法审查
models = {}
models['LR'] = LogisticRegression()
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
models['NB'] = GaussianNB()
models['SVM'] = SVC()
#评估算法
现在已经有了六种模型，并且评估了它们的精确度。接下来就需要比较这六个模型，
并选出准确度最高的算法。
results = []
for key in models:
    kfold = KFold(n_splits=10, random_state=seed)
    cv_results = cross_val_score(models[key], X_train, Y_train, cv=kfold, soring='accuracy')
    resluts.append(cv_results)
    print('%s: %f (%f)' %(key, cv_results.mean(), cv_results.std()))
#箱线图比较算法
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(lll)
pyplot.boxplot(results)
ax.set_xticklabels(models.keys())
pyplot.show()

评估的结果显示，支持向量机SVM 是准确度最高的算法 
使用全部训练集的数据生成支持向量机 SVM 的算法模型，并用预留的评估数据
集给出SVM算法模型的报告
#使用测试数据集评估算法
svm = SVC()
svm.fit(X=X_train, y=Y_train)
predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, prediction))
print(classification_report(Y_validation, prediction))
算法模型的准确度是0.93 。通过冲突矩阵看到只有两个数据预测错误。最后提供了包含准确度 precision 、召回率 recall 、 Fl值 Fl- core 等数据的报告。

********************
CH4 python和scipy速成

#多赋值运算
a, b, c = l, 'hello', True
print(a, b, c)
结果是 1 hello True
#空值 空对象
a = None 
b = a 
print(a) 
print(b)
结果是 None None

元组 元组不可变
列表 列表可变
字典
mydict = {'a': 6.18, 'b' : 'str', 'c': True}
print('A value: %.2f' % mydict['a'])
增加字典元素
mydict['a'] = 523
print('A value ：%d' % mydict['a'])
print('keys: %s' % mydict.keys())
print('values: %s' % mydict.value()) 
for key in mydict:
    print (mydict [key])
函数
#定义函数
def mysum(x, y):
    return x + y 
#测试函数
result = mysum(x = 1, y = 2) 传入实参
print(result)

with语句
上下文管理协议 Context Management Protocol ：包含方法__enter_()和__exit__() 支持该协议的对象要实现这两个方法。
上下文管理器 Context Manager 支持上下文管理协议的对象，这种对象实现了__enter__()和__exit__()方法
运行时上下文Runtime Context 由上下文管理器创建 通过上下文管理器的__enter__()和__exit__()方法实现
上下文表达式Context Expression with 语句中跟在关键 with 之后的表达式，
该表达式要返回一个上下文管理器对象
语句体（ with-body): with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的__enter__()方法 
使用 with 语句，简化了对异常的处理 
因此，当需要对异常进行处理时，如果对象遵循了上下文管理协议 Context Management Protocol ，建议使用 with 语句来实现

一、上下文管理协议
即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__和__exit__方法

__enter__()会在with语句出现（实例化对象）时执行
__exit__()会在with语句的代码块实行完毕才会执行

class Open:
   def __init__(self,name):
          self.name = name
  
   def __enter__(self):                 #在实例化打开文件时即触发，在with时触发
         print('执行__enter__')
         return self                    #return的self会赋值给f，相当于通过Open类实例化处对象f

   def __exit__(self,exc_type,exc_val,exc_tb):    #在with中的代码块执行完毕才会触发
         print('执行__exit__')
 

with Open('a.txt') as f:                #会触发enter  '执行__enter__'，相当于--》f=Open('a.txt').__enter__()
  print(f)                              #<__main__.Open object at 0x01477270>
  print(f.name)                         #'a.txt'
print('*'*10)                           #先---'执行__exit__'
                                        #后---'*********'   


Output:
---------------------------------------------
执行__enter__
<__main__.Open object at 0x000000000210B208>
a.txt
执行__exit__
**********
---------------------------------------------

二、__exit__
__exit__()中有三个参数分别代表异常类型，异常值和追溯信息，执行了__exit__则表示with语句执行完毕
1、若__exit__返回值不为True，则：
    a、若with语句中没有异常，则程序正常执行
    b、若with语句中出现异常，则程序会执行到with中出错的语句并执行__exit__，然后程序终止，‘吐出’异常

class Open:
    def __init__(self,name):
        self.name = name
  
    def __enter__(self):                        
        print('执行__enter__')
        return self                    
  
    def __exit__(self,exc_type,exc_val,exc_tb):    
        print('执行__exit__')
        print(exc_type)                #<class 'AttributeError'>
        print(exc_val)                #'Open' object has no attribute 'age'
        print(exc_tb)                #<traceback object at 0x0178F738>
 
with Open('a.txt') as f:
     print(f)
     print(f.age)       
     #因为f对象没有age属性，则出现异常，程序执行到该句时将异常传递给__exit__的三个参数，并结束程序执行，报错
     print(f.name)        #该行语句后面的语句都不会执行，包括with语句的以外的语句也不会执行
print('*'*10) 


Output:
---------------------------------------------------------
执行__enter__
    print(f.age)
AttributeError: 'Open' object has no attribute 'age'
<__main__.Open object at 0x000000000257E4A8>
执行__exit__
<class 'AttributeError'>
'Open' object has no attribute 'age'
<traceback object at 0x0000000002583288>
---------------------------------------------------------

2、若__exit__返回值为True，则：
 a、若with语句中没有异常，则程序正常执行
 b、若with语句中出现异常，则程序会执行到with中出错的语句并执行__exit__，‘吞掉’异常。然后with语句中剩下的语句不会执行，但是会继续执行with语句以外的语句

class Open:
    def __init__(self,name):
        self.name = name
  
    def __enter__(self):                        
        print('执行__enter__')
        return self                    
  
    def __exit__(self,exc_type,exc_val,exc_tb):    
        print('执行__exit__')
        print(exc_type)                #<class 'AttributeError'>
        print(exc_val)                #'Open' object has no attribute 'age'
        print(exc_tb)                #<traceback object at 0x0178F738>
        return True
with Open('a.txt') as f:
     print(f)
     print(f.age)        #因为f对象没有age属性，则出现异常，程序执行到该句时将异常传递给__exit__的三个参数，并结束程序执行，'吞掉异常'不会报错
     print(f.name)       #该行语句后面的with中的语句都不会执行，但是with语句的以外的语句会继续执行
print('*'*10)            #'*********'

三、作用及好处：
1.使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
2.在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处



*******NumPy
NumPy为SciPy 提供了基本的数据结构和运算，其中最主要的是 ndarrays 多维数组
它提供了高效的矢量运算功能

import numpy as np
#创建数组
myarray = np.array([1, 2, 3])
print(myarray)
print(myarray.shape)
#创建多维数组
myarray = np.array([1, 2, 3], [2, 3, 4], [3, 4, 5])
print(myarray)
print(myarray.shape)
执行结果
[1 2 3]
(3,) 
[ [1 2 3] 
[2 3 4] 
[3 4 5]] 
(3, 3)
通过下标访问数据
import numpy as np 
#创建多维数组
myarray = np.array([1, 2, 3], [2, 3, 4], [3, 4, 5])
print(myarray)
print(myarray.shape)
#访问数据
print('这是第一行: %s' % myarray[0])
print('这是最后一行: %s' % myarray[-1]) 
print('访问整列(3列)数据: %s' % myarray[:2])
print('访问指定行(2行)和列(3列)的数据: %s' % myarray[1, 2]) 
访问整列（列）数据：[3 4 5]
访问指定行（行）和列（列）的数据：4

算数运算/向量运算
使用 NumPy的 ndarray 数组可以直接进行算术运算，或者说向量运算。
NumPy主要用来处理大量数字应用
import numpy as np 
#创建多维数组
myarray1 = np.array([1, 2, 3], [2, 3, 4], [3, 4, 5])
myarray2 = np.array([11, 21, 31], [21, 31, 41], [31, 41, 51])
print('向量加法运算: ')
print(myarray1 + myarray2)
print('向量乘法运算: ')
print(myarray1 + myarray2)


*****Matplotlib
Matplotlib Python 中著名的 2D 绘图库，使用方法比较简单，按照下面的三步进行操作就能很简单地完成绘图。
(1)调用 plot()、 scatter()等方法，并为绘图填充数据。数据是 NumPy ndarray 类型的对象。
(2)设定数据标签，使用 xlabel()、 ylabel()方法
(3)展示绘图结果，使用 show()方法。
*绘制线条图
import matplotlib.pyplot as plt
import numpy as np 
#定义绘图的数据
myarray = np.array([1, 2, 3], [2, 3, 4], [3, 4, 5])
#初始化绘图
plt.xlabel('x axis')
plt.ylabel('y axis')
#绘图
plt.show()
*散点图
#定义绘图的数据
myarray1 = np.array( [ 1, 2, 3] ) 
myarray2 = np.array([11, 21, 31]) 
#初始化绘图
plt.scatter(myarray1, myarray2) 
#设定 轴和
plt.xlabel ('x axis') 
plt.ylabel ('y axis') 
#绘图
plt.show ()
Matplotlib 提供了很多种类的图表的绘制功能 
在http://matplotlib.org/gallery.html 提供了超过 100种示例

*******Pandas 
Pandas 提供了用于机器学习的复杂数据类型：矢量运算方法和数据分析方法 
Pandas也提供了多种数据结构
• Series: 一维数组，与 NumPy 中的一维 Array 类似。二者与python基本的数据结构 List 也很相近，其区别是：List 中的元素可以是不同的数据类型，而Array
和 Series 中则只允许存储相同的数据类型，这样可以更有效地使用内存，提高运算
效率
• Time-Series: 以时间为索引的Series
• DataFrame: 二维的表格型数据结构。很多功能与R语言中的data.frame类似。
可以将 DataFrame 理解为 Series 的容器。
• Panel: 三维数组，可以理解为 DataFrame 的容器

Series 
在建立Series时可以设定index 也可以像访问NumPy数组或者字典一样来访问Series元素
import numpy as np 
import pandas as pd 
myarray = np.array([1, 2, 3])
index = ['a', 'b', 'c']
myseries = pd.Series(myarray, index = index)
print(myseries)

print('Series中的第一个元素: ')
print(myseries[0])
print('Series中的c index 元素: ')
print(myseries['c'])
打印结果
a 1 
b 2 
c 3 
dtype: int64 

Series 中的第一个元素
1 
Series 中的 index ji;
3

DataFrame
DataFrame 是一个可以指定行和列标签的二维数组。数据可以通过指定列名来访问特
定列的数据
import numpy as np 
import pandas as pd
myarray = np.array([1, 2, 3], [2, 3, 4], [3, 4, 5])
rowindex = ['row1', 'row2', 'row3']
colname = ['col1', 'col2', 'col3']
mydataframe = pd.Dataframe(data = myarray, index = rowindex, columns = colname)
print(mydataframe)
print('访问col3的数据: ')
print(mydataframe['col2'])

pandas是一个强大的对数据进行切片的工具 http://pandas.pydata.org/pandas-docs/stable/

*****CH5 数据导入
通过标准 Python 库导入CSV文件。
通过 NumPy导入CSV文件。
通过 Pandas导入CSV文件。

文件头
csv 文件是用逗号（）分隔的文本文件。在数据导入之前，通常会审查 csv
文件中包含的内容。如果 csv 的文件里包括文件头的信息 可以很方便地使用文件头信息来设置读入数据字段的属性名称。如果文件里不含有文件头信息，需要自己手动设定读入文件的字段属性名称。数据导入时 ，设置字段属性名称 有助于提高数据处理程序的可读性。

Pima Indians 数据集
这是一个分类问题的数据集，主要记录了印第安人最近五年内是否患糖尿病的医疗数据
这些数据都是以数字的方式记录的，并且输出结果是0或1

*采用标准 Python 类库 导入数据
这个类库中的 reader() 函数用来读入 csv 文件 
csv 文件被读入后可以利用这些数据生成一个 NumPy 数组，用来训练算法模型
from csv import reader
import numpy as np 
#使用标准的python类库导入csv数据
filename = 'pima_data.csv'
with open(filename, 'rt') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x = list(readers)
    data = np.array(x).astype('float')
    print(data.shape)
执行结果
(768, 9)

*采用NUmPy导入数据
使用numpy的loadtxt()函数导入数据
使用这个函数处理的数据没有文件头，并且所有的数据结构是一样的，也就是说，数据类型是一样的
from numpy import loadtxt
#使用numpy导入csv数据
filename = 'pima_data.csv'
with open(filename, 'rt') as row_data:
    data = loadtxt(raw_data, delimiter=',')
    print(data.shape)
执行结果
(768, 9)

*采用pandas导入数据
通过 pandas 来导入 csv 文件要使用pandas.read_csv()函数 这个函数的返回值是 DataFrame,在机器学习的项目中经常利用pandas来做数据清洗与数据准备工作
from pandas import read_csv
#使用pandas导入csv数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.shape)

***** CH6 数据理解****

简单地查看数据。
审查数据的维度。
审查数据的类型和属性。
总结查看数据分类的分布情况。
通过描述性统计分析数据。
理解数据属性的相关性。
审查数据的分布状况。
from pandas import read_csv
#显示数据的前10行
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
peek = data.head(10)
print(peek)
通过 DataFrame的shape 属性，可以很方便地查看数据集中有多少行和多少列
from pandas import read_csv
#显示数据的行和列数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.shape)
通过 DataFrame的type属性来查看每一个字段的数据类型
from pandas import read_csv
#显示数据的行和列数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.dtypes)
执行结果
preg int64 
plas int64 
pres int64 
skin int64 
test int64 
mass float64 
pedi float64 
age int64
class int64 
dtype: object

描述性统计
通过DataFrame的describe()方法，展示：数据记录数、平均值、标准方差、最小值、下四分位数、中位数、上四分位数、最大值
from pandas import read_csv
from pandas import set_option
#描述性统计
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.shape)
set_option('display.width', 100)
#设置数据的精确度
set_option('precision', 4)
print(data.describe())

数据分组分布（适用于分类算法）
在分类算法中， 需要知道每个分类的数据大概有多少条记录，以及数据分布是否平
衡。如果数据分布的平衡性很差 要在数据加工阶段进行数据处理，来提高数据分布
的平衡性 利用 Pandas 的属性和方法，可以很方便地查看数据的分布情况
from pandas import read_csv
#数据分类分布统计
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.groupby('class'.size()))
执行结果
class 
0 500 
1 268 
dtype: int64

数据属性的相关性 数据的两个属性是否互相影响
非常通用的两个属性的相关性的方法是皮尔逊相关系数，皮尔逊相关系数是度
两个变量间相关程度的方法 它是一个介于 -1 和 1 之间的值，其中，1 表示变量完
全正相关 0 表示无关，-1 表示完全负相关。
在机器学习中，当数据的关联性比较高时，有些算法（如linear 、逻辑回归算法 ）的性能会降低，所以在开始训练算法前，查看一下算法的关联性是一个很好的方法。当数据特征的相关性比较高时，应该考虑对特征进行降维处理。
使用Dataframe的corr()方法来计算数据属性之间的 关联关系矩阵
from pandas import read_csv
from pandas import set_option
#显示数据的相关性
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
#设置数据的精确度
set_option('precision', 2)
print(data.corr(methor='pearson'))
得到一个每个属性相互影响的矩阵 

数据的分布分析
通过分析数据的高斯分布情况来确认数据的偏离情况
使用DataFrame的skew()方法来计算算所有数据属性的高斯分布偏离情况
from pandas import read_csv
#计算数据的高斯偏离
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = read_csv(filename, names=names)
print(data.skew())
skew()函数的结果显示了数据分布是左偏还是右偏。当数据接近0时，表示数据的偏差非常小

***** CH7 数据可视化 *****
直方图Histogram
from pandas import read_csv
import matplotlib.pyplot as plt
filename =  'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
data.hist()
pit.show()

密度图density
密度图是一种表现与数据值对应的边界或域对象的图形表示方法，用于呈现连
续变量。
from pandas import read_csv
import matplotlib.pyplot as plt
filename =  'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
pit.show()

箱线图box
from pandas import read_csv
import matplotlib.pyplot as plt
filename =  'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False)
pit.show()

相关矩阵图 热图
把所有属性两两影响的关系展示出来的图表就叫相关矩阵图。矩阵图法就是从多维问题的事件中找出成对的因素，排列成矩阵图，然后根据矩阵图来分析问题，确定关键点。它是一种通过多因素综合思考来探索问题的好方法
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)

correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin= -1, vmax = 1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklables(names)
ax.set_yticklabels(names)

pit.show()

散点矩阵图
可以快速发现多个变量间的主要相关性，这在进行多元线性回归时显得尤为重要。
from pandas import read_csv
import matplotlib.pyplot as plt
import pandas.plotting import scatter_matrix
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
scatter_matrix(data)
pit.show()

数据准备
特征选择是困难耗时的，也需要对需求的理解和专业知识的掌握 在机器
学习的应用开发中，最基础的是特征工程。Kaggers和天池比赛的冠军其实在比赛中并没有用到很高深的算法，大多数都是在特征工程这个环节做了出色的工作，然后使用一些常见的算沽，如逻辑回归，就能得到性能出色的模型，因此特征工程是建立高准确度机器学习算法的基础。

***** CH8 数据预处理
数据预处理大致分为三个步骤 数据准备、数据转换、数据输出
利用scikit-learn来转换数据
数据转换的方法
(1) 调整数据尺度Rescale Data
(2) 正态化数据Standardize Data
(3) 标准化数据Normalize Data
(4) 二值数据Binarize Data

格式化数据
导入数据
按照算法的输入和输出整理数据
格式化输入数据
总结显示数据的变化
scikit-learn 提供了两种标准的格式化数据的方法，每一种方法都有适用的算法
用这两种方法整理的数据，可以直接用来训练算法模型。
适合和多重变换Fit and Multiple Transform
适合和变换组合Combined Fit-and-Transform
推荐优先选择适合和多重变换 方法。首先调用fit()函数来准备数据转换的参数，然后调用 transform()函数做数据的预处理。适合和变换组合 Combined Fit-and-Transform 对绘图或汇总处理具有非常好的效果。

调整数据尺度
通过调整数据的尺度让所有的属性按照相同的尺度来度量数据
通常将数据的所有属性标准化，并将数据转换成0-1之间的值，这对于梯度下降等算法非常有用，对于回归算法、神经网络算法、K临近算法的准确度提高也有用
在统计学中，按照对事物描述的精确度，对所采用的尺度从低级到高级分成四个层次：定类尺度、定序尺度、定距尺度和定比尺度。
定类尺度是对事物类别属性的一种测度，按照事物的属性进行分组或分类 
定序尺度是对事物之间的等级或顺序的一种测度，可以比较优劣或排序。
定距尺度和定比尺度是对事物类别或次序之间间距的测量，
定距尺度的特点是其不仅能将事物区分为不同的类型并进行排序，而且可以准确地指出类别之间的差距 
而定比尺度则更进一步，它和定距尺度的差别在于它有一个固定的绝对“零”
scikit-learn 中，可以通过 MinMaxScaler 类来调整数据尺度。将不同计量单位的数据统一成相同的尺度，利于对事物的分类或分组。
实际上， MinMaxScaler 是将属性缩放一个指定范围，或者对数据进行标准化并将数据都聚集到0附近，方差为1。数据尺度的统一，通常能够提高与距离相关的算法的准确度（如K近邻算法）
数据进行缩放的例子
#调整数据尺度(0..)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values 
X = array[:, 0:8]
Y = array[:, 8]
transformer = MinMaxScaler(feature_range=(0, 1))
#数据转换
newX = transformer.fit_transform(X)
#设定数据的打印格式
set_printoptions(precision=3)
print(newX)

正态化数据Stamdardize Data
正态化数据是有效的处理符合高斯分布的数据的手段，输出结果以0为中位数，方差为1,并作为假定数据符合 高斯分布 的算法的输入。这些算法有线性回归、逻辑回归和线性判别分析等。
在这里可以通过 scikit-learn 提供的StandardScaler类来进行正态化数据处理。
#正态化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values 
X = array[:, 0:8]
Y = array[:, 8]
transformer = StandardScaler().fit(X)
#数据转换
newX = transformer.transform(X)
#设定数据的打印格式
set_printoptions(precision=3)
print(newX)

标准化数据 Normalize Data 
标准化数据处理是将每一行的数据的距离处理成 1（在线性代数中矢量距离为 1）的数据又叫作“归一元”处理，适合处理稀疏数据（具有很多为 0 数据），归一元处理的数据对使用权重输入的神经网络和使用距离的K近邻算法的准确度的提升有显著作用 
使用 scikit-learn 中的 Normalizer 类实现
#标准化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Normlizer
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
transformer = Normalizer().fit(X)
#数据转换
newX = transformer.transform(X)
#设定数据的打印格式
set_printoptions(precision=3)
print(newX)

二值数据 Binarize Data
二值数据是使用值将数据转化为二值，大于1阈值设置为1，小于阈值设置0 这个过程被叫作二分数据或阈值转换。在生成明确值或特征工程增加属性的时候使用。
使用scikit-learn 中的 Binarizer 类实现 
#二值数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
transformer = Binarizer(threshold=0.0).fit(X)
#数据转换
newX = transformer.transform(X)
#设定数据的打印格式
set_printoptions(precision=3)
print(newX)

******CH9 数据特征选择
选择数据的特征属性来训练预测（分类与回归）模型
数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已。因此，特征
过程的本质就是一项工程活动，目的是最大限度从原始数据中提取合适的特征以供算法和模型使用。特征处理是特征工程的核心部分，scikit-learn提供了较为完整的特征
处理方法，包括数据预处理、特征选择、降维等。
学习通过scikit-learn来自动选择用于建立机器学习模型的数据特征的方法。
(1)单变量特征选定。
(2)递归特征消除。
(3)主要成分分析。
(4)特征的重要性。

特征选择
特征选定是一个流程，能够选择有助于提高预测结果准确度的特征数据，或者有助于发现感兴趣的输出结果的特征数据
如果数据中包含无关的特征属性，会降低算法的准确度，对预测新数据造成干扰，尤其是线性相关算法（如线性回归算法和逻辑回归算法）。因此，在开始建立模型之前，执行特征选定有助于
降低数据的拟合度：较少的冗余数据，会使算法得出结论的机 更大
提高算法精度：较少的误导数据，能够提高算法的准确度
减少训练时间：越少的数据 ，训练模型所需要的时间越少

可以在scikit-learn的特征选定文档查看
http://scikit-learn.org/stable/modules/feature_selection.html

单变量特征选定
统计分析可以用来分析选择对结果影响最大的数据特征 
scikit-learn 中提供了SelectKBest类 ，可以使用一系列统计方法来选定数据特征，是对卡方检验的实现。经典
的卡方检验是检验定性自变量对定性因变量的相关性的方法 
假设自变量有N种取值，因变量有M种取值，考虑自变量等于i且因变量等于j的样本频数的 观测值 和 期望值 的差距，构建统计量。
卡方检验就是统计样本的实际观测值与理论推断值之间的偏离程度，偏离程度决定了卡方值的大小。卡方值越大，越不符合; 卡方值越小，偏差值越小，越符合。若两个值完全相等，卡方值就为0，,表明理论值完全符合。 
下面的例子是通过卡方检验 chi-squared 的方式来选择四个对结果影响最大的数据特征。
#通过卡方检验选定数据特征
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
#特征选择
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x)
print(features)
执行结束后，我们得到了卡方检验对每一个数据特征的评分，以及得分最高的四个
数据特征.通过设置 Select.KBest的score_func 参数，SelectKBest 不仅可以执行卡方检验来选择数据特征，还可以通过相关系数、互信息法等统计方法来选定数据特征。

递归特征消除 RFE 
递归特征消除使用一个基模型来进行多轮训练，每轮训练后消除若干权值系数的特征，再基于新的特征集进行下一轮训练。通过每一个基模型的精度，找到对最终的预测结果影响最大的数据特征. 
以逻辑回归算法为基模型，通过递归特征消除来选定对预测结果影响最大的三个数据特征
#通过递归消除来选定特征
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
#特征选择
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("特征个数: ")
print(fit.n_features_)
print("被选定的特征: ")
print(fit.support_)
print("特征排名: ")
print(fit.ranking_)
执行结果看书
执行后，我们可以看到 RFE 选定了preg mass pedi 三个数据特征，他们在特征support_中被标记为 True ，在 特征排名ranking_中被标记为1

主成分分析
PCA）是使用线性代数来转换压缩数据，通常被称作数据降维。常见的降维方法除了主要成分分析PCA ，还有线性判别分析（LDA ），它本身也是一个分类模型。 
PCA LDA 有很多的相似之处，其本质是将原始的样本映射到维度更低的样本空间中，但是 PCA LDA 的映射目标不一样： 
PCA 是为了让映射后的样本具有最大的发散性
 DA 是为了让映射后的样本有最好的分类性能 
所以说， PCA无监督的降维方法，而 LDA 种有监督的降维方法。

在聚类算法中，通常会利用 PCA对数据进行降维处理，以利于对数据的简化分析和可视化 (因为聚类是无监督)
#通过主成分分析选定数据特征
from pandas import read_csv
from sklearn.decomposition import PCA
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
#特征选择
pca = PCA(n_components=3)
fit = pca.fit(X)
print("解释方差: %s" % fit.explained_variance_ratio_)
print(fit.components_)

CH 特征重要性
袋装决策树算法 Bagged Decision Tress
随机森林算法
极端随机数算法 ExtraTreesClassifier
这三个算法都可以用来计算数据特征的重要性
这三个算法都是 集成算法中的袋装算法，在后面的集成算法章节会有详细的介绍
示例 使用ExtraTreesClassifier类进行特征重要性计算
#通过决策树计算特征的重要性
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
#特征选择
model = ExtraTreesClassifier()
fit = model.fit(X, Y)
print(fit.feature_importances_)
执行后，算法给出了每一个数据特征的得分

选择模型
建立模型之后就要去评估模型，确定模型是否有用

*******CH10 评估算法
要知道算法模型对未知的数据表现如何，最好的评估办法是利用已经明确知道结
的数据运行生成的算法模型进行验证 此外，还可以采用重新采样评估的方法，使用新
的数据来评估算法模型。

在评估机器学习算法的时候，为什么不将训练数据集直接作为评估数据集，最直接
的原因是过度拟合，不能有效地发现算法模型的不足。

拟合是指己知某函数的若干离散函数值{f1, f2, ..., fn}，通过调整该函数中若干待定系数，使该函数与已知点集的差别（最小二乘意义）最小 。

过度拟合是指机器学习算模型在训练集上的误差和测试集上的误差之间差异过大, 造成过度拟合的原因可能有多种, 最常见的就是模型容量过高，模型过于复杂，换句话说是模型假设所包含的参数数量过多.

避免过度拟合是分类器设计中的一个核心任务，通常采用增大数据量和评估数据集的方法对分类器进行评估。

评估就是估计算法在预测新数据的时候能达到什么程度，但这不是对算法准确度的
保证 当评估完算法模型之后，可以用整个数据集（训练数据集和评估数据集的合集）
重新训练算法，生成最终的算法模型 

C分离训练数据集和评估数据集
(1)分离训练数据集和评估数据集
(2)k折交叉验证分离
(3)弃一交叉验证分离。
(4)重复随机评估、训练数据集分离

(1)分离训练数据集和评估数据集
下面给出一个简单的按照67% : 33%的比例分离数据，来评估逻辑回归模型的例子
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, test_size= test_size, random_state=seed)
model = LogisticRegression()
model.fit(X.train, Y_traing)
result = model.score(X_test, Y_test)
print("算法评估结果: %.3f%%" % (result * 100))
为了让算法模型具有良好的可复用性，在指定了分离数据的大小的同时，还指定了数据随机的粒度（ seed=4 ），将数据随机进行分离 通过指定随机的粒度，可以确保每次执行程序得到相同的结果 ，这有助于比较两个不同的算法生成的模型的结果。为了保证算法比较是在相同的条件下执行的，必须保证训练数据集和评估数据集是相同的。

(2)k折交叉验证分离
交叉验证是用来验证分类器的性能的一种统计分析方法，有时也称作循环估计，在
统计学上是将数据样本切割成小子集的实用方法。
K折交叉验证是将原始数据分成K组（一般是均分），将每个子集数据分别做一次验证集，其余的K-1组子集数据作为训练集，这样会得到K个模型，再用这K个模型最终
的验证集的分类准确率的平均数，作为此K折交叉验证下分类器的性能指标
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果: %.3f%% (%.3f%%)" % (result.mean() * 100, results.std() * 100))

(3)弃一交叉验证分离
如果原始数据有 N 个样本，那么弃一交叉验证就是 N-1 个交叉验证 即每个样本单独作为验证集，其余的 N-1 个样本作为训练集，所以弃一交叉验证会得到 N 个模型，用
这N个模型最终的验证集的分类准确率的平均数作为此次弃一交叉验证分类器的性能指
标。 相较于K折交叉验证,弃一交叉验证
每一回合中几乎所有的样本皆用于训练模型，因此最接近原始样本的分布，评估所得的结果比较可靠。
实验过程中没有随机因素会影响实验数据，确保实验过程是可以被复制的

弃一交叉验证在实际运行上便有困难， 需要花费大量的时间来完成算法的运算与评估， 除非每次训练分类器得到模型的速度很快，或者可以用并行化计算减少计算所需的时间
from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
model = LogisticRegression()
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=loocv)
print("算法评估结果: %.3f%% (%.3f%%)" % (result.mean() * 100, results.std() * 100))


(4)重复随机评估、训练数据集分离
随机分离数据为训练数据集和评估数据 ，重复这个过程多次
from pandas import read_csv
from sklearn.model_selection import ShuffleSolit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=num_splits, test_size = test_size, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果: %.3f%% (%.3f%%)" % (result.mean() * 100, results.std() * 100))

K折交叉验证是用来评估机器学习算法的黄金准则。通常会取 K = 3、 5、10 来分离数据
分离训练数据集和评估数据集。因为执行效率比较高，通常会用于算法的执行效率比较低，或者具有大量数据的时候。
弃一交叉验证和重复随机分离评估数据集与训练数据集这两种方法，通常会用于平衡评估算法、模型训练的速度及数据集的大小。
还有一条黄金准则就是，当不知道如何选择分离数据集的方法时，请选择K折交叉
验证来分离数据集，当不知道如何设定K值时，请将K值设为 10

******CH11 算法评估矩阵
分类算法: 使用Pima Indians数据集
回归算法: 使用Boston House Price数据集


用来评估分类算法的评估矩阵
(1)分类准确度
(2)对数损失函数Logloss
(3)AUC图
(4)混淆矩阵
(5)分类报告Classification Report 

(1)分类准确度
分类准确度就是算法自动分类正确的样本数除以所有的样本数得出的结果。通常，
准确度越高，分类器越好 这是分类算法中最常见，也最易被误用的评估参数 准确度
确实是 个很好、很直观的评价指标，但是有时候准确度高并不代表算法就一定好.
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_splits = 10
seed = 7
kfold = KFold(n_splits=num_splits, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果: %.3f%% (%.3f%%)" % (result.mean() * 100, results.std() * 100))


(2)对数损失函数Logloss
逻辑回归的推导中，它假设样本服从伯努利分布（0~1分布） 然后求得满足该分布的似然函数，再取对数、求极值等。
而逻辑回归并没有求似然函数的极值，而是把极大化当作一种思想，进而推导出它的经验风险函数为：最小化负的似然函数 max F(y,f(x)) -> min -  F(y,f(x)) 
从损失函数的视角来看，它就成了对数（ Log ）损失函数了.
对数损失函数越小，模型就越好，而且使损失函数尽量是一个凸函数，便于收敛计算。
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_splits = 10
seed = 7
kfold = KFold(n_splits=num_splits, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果: %.3f%% (%.3f%%)" % (result.mean() * 100, results.std() * 100))


(3)AUC图
ROC和AUC 是评价分类器的指标。
Roc 受试者工作特征曲线Receiver Operating Characteristic Curve， 感受性曲线Sensitivity Curve 曲线上各点反映相同的感受性，它们都是对同一信号剌激的反应，只不过是在几种不同的判定标准下所得的结果而已。
ROC 是反映敏感性和特异性连续变量的综合指标，用构图法揭示敏感性和特异性的相互关系，通过将连续变量设定出多个不同的临界值计算出一系列敏感性和特异性，再以敏感性为纵坐标、（1-特异性）为横坐标绘制成曲线。
AUC是 ROC 曲线下的面积AUC 的值， 通常AUC 值介于 0.5 到 1.0 之间， AUC
的值越大，诊断准确性越高。在 ROC 曲线上，靠近坐标图左上方的点为敏感性和特异
均较高的临界值。
对一个二分类问题来说，会出现四种情况：
如果一个实例是正类并且也被预测成正类，即为真正类（true Positive）
如果实例是负类却被预测成正类，称之为假正类 (False Positive)。
相应地，如果实例是负类也被预测成负类，称之为真负类True Negative 
如果实例为正类却被预测成负类，则为假负类 False Negative

敏感性指标 sensitivity=TP/(TP+FN) 敏感性指标又称为真正类率TPR，计算的是分类器所识别出的正实例占所有正实例的比例
负正类率 FPR=FP/(FP+TN) 负正类率计算的是分类器错认为正类的负实例占所有负实例的比例
特异性指标 Specificity=TN/(FP+TN)=F1-FPR 特异性指标又称为真负类率TNR 

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_folds = 10
seed = 7
kfold = KFold(n_splits=num_splits, random_state=seed)
model = LogisticRegression()
scoring = 'roc_auc'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("AUC %.3f (%.3f)" % (result.mean(), results.std() ))

(4)混淆矩阵Confusion Matrix
混淆矩阵
主要用于比较分类结果和实际测得值，可以把分类结果的精度显示在一个混淆矩阵里面。
混淆矩阵是可视化工具 ，特别适用于监督学习 在无监督学习时一般叫作匹配矩阵.
混淆矩阵的每列代表预测类别，每列的总数表示预测为该类别的数据的数目, 每行代表数据的真实归属类别，每行的数据总数表示该类别的数据的数目,每列中的数值表示真实数据被预测为该类的数目。

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, test_size= test_size, random_state=seed)
model = LogisticRegression()
model.fit(X.train, Y_traing)
predicted =model.predict(X_test)
matrix = confussion_matrix(Y_test,predicted)
classes = ['0', '1']
dataframe = pd.DataFrame(data=matrix,
                        index=classes,
                        columns=classes)
print(dataframe)

(5)分类报告Classification Report 
Classification_report()方法能够给出精确率precision、召回率recall、F1值 F1-score和样本数目support

精确率precision P=TP/(TP+FP) 计算的是所有被检索到的项目中应该被检索到的项
目的比例
召回率recall R=TP/(TP+FN) 计算的是所有检索到的项目占所有应该检索到的项目的比例
F1值 是精确率和召回率的调和均值 2F1=P+R

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, test_size= test_size, random_state=seed)
model = LogisticRegression()
model.fit(X.train, Y_traing)
predicted =model.predict(X_test)
report = classification_report(Y_test, predicted)
print(dataframe)

用来评估回归算法的评估矩阵
(1)平均绝对误差
(2)均方绝对误差
(3)决定系数

(1)平均绝对误差MAE
平均绝对误差是所有单个观测值与算术平均值的偏 的绝对值的平均值。与平均误差相比，平均绝对误差由于离差被绝对值化，不会出现正负相抵消的情况，因而，平均绝对误差能更好地反映预测值误差的实际情况。
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
#导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
#将数据分为输入数据和输出结果
array = data.values 
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
#评价绝对误差(MAE)
scoring = 'neg_mean_absolute_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring = scoring)
print('MAE: %.3f (%.3f)' %(result.mean(), result.std())) 

(2)均方绝对误差MSE
均方误差是衡量平均误差的方法，可以评价数据的变化程度。均方根误差是均方算术平方根。均方误差的值越小，说明用该预测模型描述实验数据的准确度越高。
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
#导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
#将数据分为输入数据和输出结果
array = data.values 
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
#评价均方误差(MSE)
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring = scoring)
print('MSE: %.3f (%.3f)' %(result.mean(), result.std())) 

(3)决定系数R2
决定系数，反映因变量的全部变异能通过回归关系被自变量解释的比例 拟合优度越大，自变量对因变量的解释程度越高，自变量引起的变动占总变动的百分比越高，观察点在回归直线附近越密集.
例如R2为0.8 ，则表示回归关系可以解释因变量80%的变异，换句话说，如果我们能控制自变量不变，则因变量的变异程度会减少80%
R2是样本观测值的函数，是因随机抽样而变动的随机变量。R2的统计的可靠性也应进行检验。
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
#导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
#将数据分为输入数据和输出结果
array = data.values 
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
#评价决定系数
scoring = 'r2'
result = cross_val_score(model, X, Y, cv=kfold, scoring = scoring)
print('MSE: %.3f (%.3f)' %(result.mean(), result.std())) 


#回归算法评价指标 以线性回归为例，波士顿房价预测
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn import datasets
boston = datasets.load_boston()
kfold = KFold(n_splits=10, random_state=7)
model = LinearRegression()
#----------
# (1)评价绝对误差(MAE)
scoring = 'neg_mean_absolute_error'
result = cross_val_score(model, boston.data, boston.target, cv=kfold, scoring = scoring)
print('MAE: %.3f (%.3f)' %(result.mean(), result.std()))  
# (2)均方误差(MSE)
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, boston.data, boston.target, cv=kfold, scoring = scoring)
print('MSE: %.3f (%.3f)' %(result.mean(), result.std())) 
# (3)R的平方（决定系数）
#决定系数，反映因变量的全部变异能通过回归关系被自变量解释的比例
# r2=0.8,表示如果我们能控制自变量不变，则因变量的变异程度会减少80%
#拟合优度越大，解释程度越高，自变量引起的变动占总变动的百分比越高
# 是个统计量，需要进行检验
scoring = 'r2'
result = cross_val_score(model, boston.data, boston.target, cv=kfold, scoring = scoring)
print('R2: %.3f (%.3f)' %(result.mean(), result.std())) 




****** CH12 审查分类算法
import numpy as np
import pandas as pd

import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#os.chdir(r'D:\Spyder_Workspace')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 精度要求
pd.set_option('precision',3) 

#%% 导入数据
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('pima_data.csv', names = colnames)
# 分出特征与标签
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
from numpy import set_printoptions # 显示精度设置
set_printoptions(precision=3)

审查算法前没有办法判断哪个算法对数据集最有效、能够生成最优模型，必须通过
系列实验判断出哪些算法对问题最有效，然后再进一步来选择算法。这个过程被叫作
算法审查。

在选择算法时，应该换一种思路，不是针对数据应该采用哪种算法，
而是应该用数据来审查哪些算法。猜测哪些算法会取得好结果。（数据敏感性）

*分类算法
1 线性算法：逻辑回归算法。线性判别分析。岭回归算法（脊回归算法）。套索回归算法。弹性网络（Elastic Net）回归算法。
2 非线性算法：K近邻算法（KNN）。贝叶斯分类器。分类与回归树算法。支持向量机（SVM）。

线性算法:
(1)逻辑回归LR
(2)线性判别分析LDA

逻辑回归和线性判别分析都是假定输入的数据符合高斯分布。

(1)逻辑回归LR logistic
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# 逻辑回归
from sklearn.linear_model import LogisticRegression
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.76951469583

回归是一种极易理解的模型，相当于 y=f(x)
逻辑回归是分类算法 通常是利用已知的自变量来预测一个离散因变量的值，预测的是一个概率值 处理二分类

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# 逻辑回归
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%, std= %.3f%%'\
      %(result.mean()*100, result.std()*100))# 0.76951469583


(2)线性判别分析LDA 也叫作Fisher 线性判别 FLD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LinearDiscriminantAnalysis()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.773462064252

LDA是模式识别的经典算法。
线性判别的基本思想是将高维的模式样本投影到最佳鉴别矢量空间，以达到抽取分类信息和压缩特征空间维数的效果，投影后保证模式样本在新的子空间有最大的类间距离和最小的类内距离 ，即模式在该空间中有最佳的可分离性。因此， 它是一种有效的特征抽取方法。
使用这种方法能够使投影后模式样本的类间散布矩阵最大，并且类内散布矩阵最小。就是说，它能够保证投影后模式样本在新的间中有最小的类内距离和最大的类间距离，即模式在该空间中有最佳的可分离性。
线性判别分析与主成分分析一样，被广泛应用在数据降维中。

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))

非线性算法：
(1)K近邻KNN
(2)贝叶斯分类器NB
(3)分类与回归树cart
(4)支持向量机svm

(1)K近邻
from sklearn.neighbors import KNeighborsClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = KNeighborsClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.726

K近邻算法（KNN）可以用于分类 也可以用于回归
该方法的思路是：如果一个样本在特征空间中的k个最相似（特征空间中最邻近）的样本中的大多数属于某一个类别，则该样本也属于这个类别。
在KNN 中，通过计算对象间距离来作为各个对象之间的非相似性指标，避免了对象之间的匹配问题，距离一般使用欧氏距离或曼哈顿距离; 同时，KNN 通过依据k个对象中占优的类别进行决策，而不是通过单一的对象类别决策，这就是 KNN 算法的优势。

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))

(2)贝叶斯分类器
from sklearn.naive_bayes import GaussianNB

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = GaussianNB()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.7557

贝叶斯分类器
在贝叶斯分类器中，对输入数据同样做了符合高斯分布的假设。
贝叶斯分类器的分类原理：
通过某对象的先验概率，利用贝叶斯公式计算出其在所有类别上的后验概率，即该对象属于某一类的概率，选择具有最大后验概率的类作为该对象所属的类。
也就是说，贝叶斯分类器是最小错误率意义上的优化。
对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，哪个最大就认为此待分类项属于哪个类别。
贝叶斯分类器的特点：
贝叶斯分类器是一种基于统计的分类器，它根据给定样本属于某一个具体类的概率来对其进行分类。
贝叶斯分类器的理论基础是贝叶斯理论。
贝叶斯分类器的一种简单形式是朴素贝叶斯分类器，与随机森林、神经网络等分类器都具有可比的性能。
贝叶斯分类器是一种增量型的分类器。

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))

(3)分类与回归树
from sklearn.tree import DecisionTreeClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = DecisionTreeClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.701

分类与回归树(CART)
CART也属于一种决策树，树的构建基于基尼指数。
CART 假设决策树是二叉树，内部结点特征的取值为 是”和“否”。左分支是取值为“是”
的分支，右分支是取值为“否”的分支。
这样的决策树等价于递归二分每个特征，将输入空间（特征空间）划分为有限个单元，并在这些单元上确定预测的概率分布，
也就是在输入给定的条件下输出的条件概率分布。

CART 算法由以下两步组成：
1 树的生成：基于训练数据集生成决策树，生成的决策树要尽量大
2 树的剪枝：用验证数据集对己生成的树进行剪枝，并选择最优子树，这时以损失
函数最小作为剪枝的标准。

决策树的生成就是通过递归构建二叉决策树的过程，对回归树用平方误差最小化准则，或对分类树用基尼指数最小化准则，进行特征选择，生成二叉树。

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))

(4)支持向量机SVM
from sklearn.svm import SVC

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = SVC()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.65

支持向量机（SVM）
它在解决小样本、非线性及高维模式识别中表现出许多特有的优势，并能够推广应用到函数拟合等其他机器学习问题中。
在机器学习中，支持向量机（SVM）是与相关的学习算法有关的监督学习模型，可以分析数据、识别模式，用于分类和回归分析。
给定一组训练样本，每条记录标记所属类别，使用支持向量机算法进行训练，并建立一个模型，对新数据实例进行分类，使其成为非概率二元线性分类。
一个 SVM 模型的例子是，如在空间中的不同点的映射，使得所属不同类别的实例是由一个差距明显且尽可能宽的划分表示。新的实例则映射到相同的空间中，并基于它们落在相同间隙上预测其属于同一个类别。

现在 SVM也被扩展到处理多分类问题。
可以通过scikit-learn中的SVC类来构建一个SVM模型

from sklearn.svm import SVC
model = SVC()
kfold = KFold(n_splits= 10, random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))


****** CH13 审查回归算法
审查算法前并不知道哪个算法对问题最有效，必须设计一定的实验进行验证，以找到对问题最有效的算法。

*七种回归算法
四种线性算法：线性回归算法、岭回归算法/脊回归算法。套索回归算法。弹性网络/Elastic Net回归算法。
三种非线性算法：近邻算法 CKNN、分类与回归树算法。支持向量机 SVM。

线性算法
(1)线性回归算法
(2)岭回归算法/脊回归算法
(3)套索回归算法/lasso
(4)弹性网络/Elastic Net回归算法。

首先进行导入包和数据
from sklearn import datasets
boston = datasets.load_boston()
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
X = boston.data
y = boston.target

(1)线性回归算法LR Linear
矩阵形式表达式 y = w'x + e ' e表示误差服从均值为0的正态分布
一元线性回归分析：只包括一个自变量和一个因变量 且二者的关系可以用一条直线近似表示。
多元线性回归：两个或两个以上的自变量和因变量 且因变量和自变量之间是线性关系

from sklearn.linear_model import LinearRegression
model = LinearRegression()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('Linear Regression: %.3f' % result.mean())

(2)岭回归算法/脊回归算法ridge
一种专门用于共线性数据分析的有偏估计回归，实际上是一种改良的最小二乘估计法。通过放弃最小二乘法的无偏性，以损失部分信息、降低精度为代价，获得回归系数更符合实际、更可靠的回归方法，对病态数据的拟合要强于最小二乘法。

from sklearn.linear_model import Ridge
model = Ridge()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('Ridge Regression: %.3f' % result.mean())

(3)套索回归算法/lasso
套索回归与岭回归类似，套索回归也会惩罚回归系数，在Lasso中会惩罚回归系数的绝对值大小（在Ridge岭回归中惩罚函数是平方） 这导致惩罚（或等于约束估计的绝对值之和）值使得一些参数估计结果等于0。使用惩罚值越大，进一步估计会使缩小值越趋近零。
这将导致我们要从给定的n个变量中选择变量。如果预测的一组变量高度相似，lasso会选择其中的一个变量，并将其他的变量收缩为零。
此外，它能够减少变化程度并提高线性回归模型的精度。

from sklearn.linear_model import Lasso 
model = Lasso()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('Lasso Regression: %.3f' % result.mean())

(4)弹性网络/Elastic Net回归算法
弹性网络回归算法是Lasso回归算法和Ridge回归算法的混合体，在模型训练时，弹性网络回归算法综合使用L1和L2两种正则化方法。
当有多个相关的特征时，弹性网络回归算法是很有用的，Lasso会随机挑选算法中的一个，而弹性网络则会选两个。
与Lasso和Ridge岭回归相比，弹性网络的优点是：它允许弹性网络回归继承循环状态下Ridge的一些稳定性。另外，在高度相关变量的情况下，它会产生群体效应; 选择变量的数目没有限制; 可以承受双重收缩。

from sklearn.linear_model import ElasticNet
model = ElasticNet()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('ElasticNet Regression: %.3f' % result.mean())


非线性算法 
(1)近邻算法 CKNN
(2)分类与回归树算法
(3)支持向量机 SVM 

(1)近邻算法 CKNN 可以用于分类 也可以用于回归
K近邻算法（按照距离来预测结果）, 默认的距离参数为闵式距离，可以指定曼哈顿距离作为距离的计算方式。
该方法的思路是：如果一个样本在特征空间中的k个最相似（特征空间中最邻近）的样本中的大多数属于某一个类别，则该样本也属于这个类别。
在KNN 中，通过计算对象间距离来作为各个对象之间的非相似性指标，避免了对象之间的匹配问题，距离一般使用欧氏距离或曼哈顿距离; 同时，KNN 通过依据k个对象中占优的类别进行决策，而不是通过单一的对象类别决策，这就是 KNN 算法的优势。

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('KNeighbors Regression: %.3f' % result.mean())

(2)分类与回归树算法 可以用于分类 也可以用于回归

CART也属于一种决策树，树的构建基于基尼指数。
CART 假设决策树是二叉树，内部结点特征的取值为 是”和“否”。左分支是取值为“是”
的分支，右分支是取值为“否”的分支。
这样的决策树等价于递归二分每个特征，将输入空间（特征空间）划分为有限个单元，并在这些单元上确定预测的概率分布，
也就是在输入给定的条件下输出的条件概率分布。

CART 算法由以下两步组成：
1 树的生成：基于训练数据集生成决策树，生成的决策树要尽量大
2 树的剪枝：用验证数据集对己生成的树进行剪枝，并选择最优子树，这时以损失
函数最小作为剪枝的标准。

决策树的生成就是通过递归构建二叉决策树的过程，对回归树用平方误差最小化准则，或对分类树用基尼指数最小化准则，进行特征选择，生成二叉树。

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('CART Regression: %.3f' % result.mean())

(3)支持向量机 SVM 可以用于分类 也可以用于回归
它在解决小样本、非线性及高维模式识别中表现出许多特有的优势，并能够推广应用到函数拟合等其他机器学习问题中。
在机器学习中，支持向量机（SVM）是与相关的学习算法有关的监督学习模型，可以分析数据、识别模式，用于分类和回归分析。
给定一组训练样本，每条记录标记所属类别，使用支持向量机算法进行训练，并建立一个模型，对新数据实例进行分类，使其成为非概率二元线性分类。
一个 SVM 模型的例子是，如在空间中的不同点的映射，使得所属不同类别的实例是由一个差距明显且尽可能宽的划分表示。新的实例则映射到相同的空间中，并基于它们落在相同间隙上预测其属于同一个类别。

现在 SVM也被扩展到处理多分类问题。
可以通过scikit-learn中的SVC类来构建一个SVM模型

from sklearn.svm import SVR
model = SVR()
scoring = 'neg_mean_squared_error'
kfold = KFold(n_splits = 10, random_state = 7)
result = cross_val_score(model, X, y, cv= kfold, scoring = scoring)
print('SVM Regression: %.3f' % result.mean())

*********
在scikit-learn中，算法评估矩阵的计算 经常使用cross_val_score函数，通过指定的scoring参数来选择使用的不同评估矩阵


****** CH14 算法比较
当参与一个机器学习的项目时，会经常因为如何选择一种合适的算法模型而苦恼。每种模型都有各自适合处理的数据特征，通过交叉验证等抽样验证方式可以得到每种模型的准确度，并选择合适的算法。通过这种评估方式，可以找到一种或两种最适合问题
的算法。
当得到一个新的数据集时，应该通过不同的维度来审查数据，以便于找到数据的特征，这种方法也适用于选择算法模型。同样需要从不同的维度，用不同的方法来观察机器学习算法的准确度，并从中选择一种或两种对问题最有效的算法。
一种比较好的方法是通过可视化的方式来展示平均准确度、方差等属性，以便于更方便地选择算法。
接下来就介绍如何通过 scikit-learn 实现对算法的比较。

最合适的算法比较方法是，使用相同的数据、相同的方法来评估不同的算法，以得到一个准确的结果。

**原书的代码 评估分类算法
逻辑回归LR 
线性判别分析LDA
K近邻KNN
分类与回归树CART
贝叶斯分类器
支持向量机SVM

数据是一个二分类的数据集,结果只有两个分类,用来训练算法模型的数据是八种全部由数字构成的属性特征值，采用 10 折交叉验证来分离数据，并采用相同的随机数分配方式来确保所有的算法都使用相同的数据。

比较不同的算法，并选择最佳的机器学习算法
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
models = {}
models['LR'] = LogisticRegression()
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
models['SVM'] = SVC()
models['NB'] = GaussianNB()
results = []
for name in models:
    result = cross_val_score(models[name], X, Y, cv=kfold)
    results.append(result)
    msg = '%s: %.3f (%.3f)' % (name, result.mean(), result.std())
    print(msg)、
'''
LR: 0.768 (0.052)
LDA: 0.773 (0.052)
KNN: 0.727 (0.062)
CART: 0.693 (0.065)
SVM: 0.760 (0.053)
NB: 0.755 (0.043)
'''

# 图表显示
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(models.keys())
pyplot.show()

** 评估回归算法 各种算法比较性能
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)

model = LinearRegression()
# model = Ridge()
# model = Lasso()
# model = ElasticNet()
# model = KNeighborsRegressor()
# model = DecisionTreeRegressor()
# model = SVR()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Linear Regression: %.3f' % result.mean())

线性回归算法：-34.705
岭回归算法：-34.078
套索回归算法：-34.464
弹性网络（Elastic Net）回归算法：-31.164
K近邻算法（KNN）：-107.287
分类与回归树算法：-37.104
支持向量机（SVM）：-91.048

**评估分类算法
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 精度要求
pd.set_option('precision',3) 

#%% 导入数据
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('pima_data.csv', names = colnames)
# 分出特征与标签
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
from numpy import set_printoptions # 显示精度设置
set_printoptions(precision=3)

#%% 第十四章 算法比较（一种模式/一种框架）
#一种可以比较不同算法的模式（模板）可视化
from sklearn.model_selection import KFold # K折
from sklearn.model_selection import cross_val_score # 交叉验证

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

models = {}
models['LR'] = LogisticRegression()
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
models['NB'] = GaussianNB()
models['SVM'] = SVC()

# 评估算法
results = []
for key in models: # eee
    kfold = KFold(n_splits=10, random_state= 7)
    cv_results = cross_val_score(models[key], X, y,
            cv= kfold, scoring= 'accuracy') # ndarray
    results.append(cv_results)
    print('{}: {} ({})'.format(key, cv_results.mean(), cv_results.std()))

# 箱线图比较算法(可视化比较)
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)#
ax.set_xticklabels(models.keys())
plt.show()



****** CH15 自动流程
在机器学习方面有一些可以采用的标准化流程，这些标准化流程是从共同的问题中
提炼出来的，例如评估框架中的数据缺失等。在 ciki -leam 提供了自动化运行流程的工具--Pipeline。
Pipeline能够将从数据转换到评估模型的整个机器学习流程进行自动化处理。

在机器学习的实践中有一个很常见的错误，就是训练数据集与评估数据集之间的数据泄露，这会影响到评估的准确度 要想避免这个问题，需要有一个合适的方式把数据
分离成训练数据集和评估数据集，这个过程被包含在数据的准备过程中 
数据准备过程是很好的理解数据和算法关系的过程，举例来说，当对训练数据集做标准化和正态化理来训练算法时，就应该理解并接受这同样要受评估数据集的影响

Pipeline 能够处理训练数据集与评估数据集之间的数据泄露问题，通常会在数据处理过程中对分离出的所有数据子集做同样的数据处理，如正态化处理。

通过Pipeline来处理这个过程，共分为以下两个步骤：
（1）正态化数据。
（2）训练一个线性判别分析模型。
采用10折交叉验证来分离数据集
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import  Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
steps = []
# 创建Pipeline
steps.append(('Standardize', StandardScaler()))
steps.append(('lda', LinearDiscriminantAnalysis()))
model = Pipeline(steps)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())

Pipeline的各个步骤，通过列表参数传递给Pipeline实例，并通过Pipeline进行流程化处理过程。

*特征选择和生成模型的Pipeline
特征选择也是一个容易受到数据泄露影响的过程。和数据准备一样，特征选择时也必须确保数据的稳固性，Pipeline也提供了一个工具(FeatureUnion) 来保证数据特征选择时数据的稳固性。下面是一个在数据选择过程中保持数据稳固性的例子。这个过程包括以下四个步骤：
（1）通过主要成分分析进行特征选择。
（2）通过统计选择进行特征选择。
（3）特征集合。
（4）生成一个逻辑回归模型。
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import  Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
# 生成 feature union
features = []
features.append(('pca', PCA()))
features.append(('select_best', SelectKBest(k=6)))
# 生成 Pipeline
steps = []
steps.append(('feature_union', FeatureUnion(features)))
steps.append(('logistic', LogisticRegression()))
model = Pipeline(steps)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())



****** CH16 集成算法
将多种机器学习算法组合在一起，从而提高算法精确度的方法，被称之为集成学习。
(1)装袋算法Bagging：先将训练集分离成多个子集，然后通过各个子集训练多个模型
(2)提升算法Boosting：训练多个模型并组成一个序列，序列中的每一个模型都会修正前一个模型的错误
(3)投票算法Voting：训练多个模型，并采用样本统计来提高模型的准确度
三种流行的集成算法的方法
boosting(提升)算法 串性 序列化方法 
 bagging(袋装)算法 并行 并行化方法
  voting(投票)算法 
bagging：先将训练集分离成多个子集，然后通过各个子集训练多个模型。
boosting：训练多个模型并组成一个序列，序列中的每一个模型都会修正前一个模型的错误。
voting：训练多个模型，并采用样本统计来提高模型的准确度。



(1)装袋算法Bagging
装袋算法是一种提高分类准确率的算法，通过给定组合投票的方式获得最优解。
哪一个获得的票数最多，就是最优解 

装袋算法在数据具有很大的方差时非常有效

三种袋装模型
(1)袋装决策树
(2)随机森林
(3)极端决策树

(1)装袋决策树（Bagged Decision Trees）
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
cart = DecisionTreeClassifier()
num_tree = 100
model = BaggingClassifier(base_estimator=cart, n_estimators=num_tree, random_state=seed)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.77

(2)随机森林（Random Forest）RF
随机森林是用随机的方式建立一个森林，森林由很多的决策树组成，且每一棵决策树之间是没有关联的。得到森林之后，当有一个新的输入样本进入的时候，就让森林中的每一棵决策树分别进行判断，看看这个样本应该属于哪一类，再看看哪一类被选择最多，就预测这个样本为哪一类。
在建立每一棵决策树的过程中，有两点需要注意：采样与完全分裂。
首先是两个随机采样的过程，随机森林对输入的数据要进行 行、列的采样。
对于行采样采用有放回的方式，也就是在采样得到的样本集合中可能有重复的样本。
假设输入样本为N个，那么采样的样本也为N个。这样在训练的时候，每一棵树的输入样本都不是全部的样本，就相对不容易出现过拟合。然后进行列采样，从M个 feature 中选出m个(m <<M) , 之后再对采样之后的数据使用完全分裂的方式建立决策树，这样决策树的某一个叶节点要么是无法继续分裂的，要么所有样本都指向同一个分类。

一般很多的决策树都有一个重要的步骤一一剪枝，但是随机森林不这么做。

因为两个随机采样过程已经保证了随机性 所以随机森林通常不剪枝也不容易出现过拟合。

可以这样比喻随机森林算法 每一棵决策树就是一个精通某一个领域的专家，这样在随机森林中就有了很多个精通不同领域的专家，对于一个新的问题（新的输入数据），可以从不同的角度去看待它，最终由各个专家技票得到结果。

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
#导入数据
filename = 'pima_data.csv'
names = ['preg',  'plas', 'skin', 'test', 'mass', 'pedi', 'age','class']  
data = read_csv(filename, names=names)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
num_tree = 100
max_features = 3
model = RandomForestClassifier(n_estimators=num_tree, random_state=seed, max_features=max_features)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 

# （2）随机森林（Random Forest）
# 顾名思义，用随机的方式建立一个森林，由很多决策树组成，树之间没有关联。
# 新样本输入，每棵树判断，哪类多就哪类（涉及结合策略）
#--------
# 在建立每一棵决策树的过程中，有两点需要注意：(采样)与(完全分裂)。
# 首先是(两个随机采样的过程)，RF对输入的数据要进行 行、列的采样。
#--------
# 对于(行采样)采样有放回的方式，得到可能重复的样本集合。
# 假设输入样本有N个，那么采样的样本也为N个。
# 这样在训练时，每棵树的输入样本都不是全部的样本，相对减轻过拟合。------
# 然后进行(列采样)，从M个feature中选出m个（m<<M)。？？？？
# 之后再对采样之后的数据使用(完全分裂的方式)建立决策树,
# 这样决策树的叶子要么(无法再分)，要么所有样本指向同一个类(无需再分)-----
# 这里不用剪枝，因为之前的两个随机采样过程保证了随机性，不剪枝也不会过拟合。
#---------
# 有个比喻：
# 每一棵决策树就是一个精通某一领域的专家，于是对于一个新问题，
# 就可以从不同的角度去看待它，最终由各个专家投票得到结果。
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier #
kfold = KFold(n_splits= 10, random_state= 7)
model = RandomForestClassifier(n_estimators= 100, 
                               random_state= 7,
                               max_features= 3)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()))






(3)极端随机树（Extra Trees）ET
极端随机树与随机森林RF十分相似，都是由许多决策树构成。但它与随机森林有两个主要的区别：
随机森林应用的是Bagging模型，而极端随机树是使用所有的训练样本得到每棵决策树，也就是每棵决策树应用的是相同的全部训练样本。
随机森林是在一个随机子集内得到最优分叉特征属性，而极端随机树是完全随机地选择分叉特征属性，从而实现对决策树进行分叉的。
from sklearn.ensemble import ExtraTreesClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
num_tree = 100
max_features = 7
model = ExtraTreesClassifier(n_estimators=num_tree, random_state=seed, max_features=max_features)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean()) # 0.7629

# （3）极端随机树（Extra Trees） (随机性在于划分属性完全随机选取)
# 与RF十分相似，都是有很多树构成，两个主要区别：
# 1.RF应用的是bagging模型，而ET是使用（所有的训练样本）得到每棵树
# 2.RF是在一个（随机子集）内得到最优分叉特征属性，ET是(完全随机地选择分叉属性)
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
kfold = KFold(n_splits= 10, random_state= 7)
model = ExtraTreesClassifier(n_estimators= 100,
                             random_state= 7,
                             max_features= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()))


(2)提升算法Boosting
提升算法是一种用来提高弱分类算法准确度的方法，这种方法先构造一个预测函数系列，然后以一定的方式将它们组合成一个预测函数。提升算法也是一种提高任意给定
法准确度的方法，它是一种集成算沽，主要通过对样本集的操作获得样本子集，然后用弱分类算法在样本子集上训练生成一系列的基分类器。
它可以用来提高其他弱分类算法的识别率，也就是将其他的弱分类算法作为基分类算法放于提升框架中 ，通过提升框架对训练样本集的操作，得到不同的训练样本子集，再用该样本子集去训练、生成基分类器。每得到一个样本集就用该基分类算法在该样本集上产生一个基分类器，这样在给定训练轮数n后，就可产生n个基分类器，然后提升算法将这n个基分类器进行加权融合，产生最后的结果分类器。
在这n个基分类器中，每个分类器的识别率不一定很高，但它们联合后的结果有很高的识别率，这样便提高了弱分类算法的识别率。


提升算法是一种用来提高弱分类算法准确度的方法，该方法先构造一个预测函数系列
然后以一定的方式将它们组合成一个预测函数。（加强融合）

(1)AdaBoost

(2)随机梯度提升


*** AdaBoost 迭代算法 
针对同一个训练集训练不同的分类器(弱分类器)，然后把这些弱分类器集合起来，构成一个更强的最终分类器(强分类器)。
其算法本身是通过（改变数据分布）来实现的，（调整每个样本的权重）
Adaboost分类器可以排除一些不必要的训练数据特征，并放在关键的训练数据上

from sklearn.ensemble import AdaBoostClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
num_tree = 30
model = AdaBoostClassifier(n_estimators=num_tree, random_state=seed)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())


#（1）Adaboost (基学习器默认为None ？)
# 针对同一个训练集训练不同的分类器，然后把分类器集合起来。
# 其算法本身是通过（改变数据分布）来实现的，（调整每个样本的权重）
# Adaboost分类器可以排除一些不必要的训练数据特征，并放在关键的训练数据上
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
kfold = KFold(n_splits= 10, random_state= 7)
model = AdaBoostClassifier(n_estimators= 30,
                           random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()))



***随机梯度提升（Stochastic Gradient Boosting）
GBM
要找到某个函数的最大值，最好的办法就是沿着该函数的梯度方向探寻。
梯度算子总是指向函数值增长最快的方向。
由于梯度提升算法在每次更新数据集时都需要遍历整个数据集，计算复杂度较高，于是有了一个改进算法--随机梯度提升算法，该算法一次只用一个样本点来更新回归系数，极大地改善了算法的计算复杂度。

from sklearn.ensemble import GradientBoostingClassifier

kfold = KFold(n_splits=10, random_state=0)
model = GradientBoostingClassifier(n_estimators=100, random_state=0)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())

#（2）随机梯度提升(Stochastic Gradient Boosting, ? SGB)
# 随机梯度提升法(GBM)基于的思想是：要找到某个函数的最大值，最好的办法就是
# 沿着该函数的梯度方向探寻。（梯度方向，函数值增长最快）
# 由于梯度提升算法在每次更新数据集时都需要遍历整个数据集，计算复杂度高，
# 而SGB一次只用一个样本点来更新回归系数，极大地改善了算法的计算复杂度。
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
kfold = KFold(n_splits= 10, random_state= 7)
model = GradientBoostingClassifier(n_estimators= 100,
                                   random_state= 7)
result = cross_val_score(model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()))
# 梯度提升和梯度下降其实是一回事？ 损失函数

(3)投票算法Voting
集成学习voting Classifier在sklearn中的实现（投票机制）

# 投票算法是一个非常简单的多个机器学习算法的集成算法。
# 投票算法是通过创建两个或多个算法模型，利用投票算法将这些算法包装起来。
# 在实际的应用中，可以对每个子模型的预测结果增加权重，以提高准确度。
# 但是，sklearn中不提供加权算法。。。
 
# 在sklearn中实现投票算法。
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier #
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
kfold = KFold(n_splits= 10, random_state= 7)
models = []
models.append(('logistic', LogisticRegression()))
models.append(('cart', DecisionTreeClassifier()))
models.append(('svm', SVC()))
ensemble_model = VotingClassifier(estimators = models)
result = cross_val_score(ensemble_model, X, y, cv= kfold)
print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()))

Voting即投票机制，分为软投票和硬投票两种，其原理采用少数服从多数的思想。
1）使用方式
voting = ‘hard’：表示最终决策方式为 Hard Voting Classifier
voting = ‘soft’：表示最终决策方式为 Soft Voting Classifier
2）思想
Hard Voting Classifier：根据少数服从多数来定最终结果
Soft Voting Classifier：将所有模型预测样本为某一类别的概率的平均值作为标准，概率最高的对应的类型为最终的预测结果

*****硬投票法：
模型 1：A - 99%、B - 1%，表示模型 1 认为该样本是 A 类型的概率为 99%，为 B 类型的概率为 1%
from sklearn.ensemble import VotingClassifier
clf1 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=3, min_child_weight=2, subsample=0.7,
                     colsample_bytree=0.6, objective='binary:logistic')
clf2 = RandomForestClassifier(n_estimators=50, max_depth=1, min_samples_split=4,
                              min_samples_leaf=63,oob_score=True)
clf3 = SVC(C=0.1)
# 硬投票
eclf = VotingClassifier(estimators=[('xgb', clf1), ('rf', clf2), ('svc', clf3)], voting='hard')
for clf, label in zip([clf1, clf2, clf3, eclf], ['XGBBoosting', 'Random Forest', 'SVM', 'Ensemble']):
    scores = cross_val_score(clf, x, y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))


'''
硬投票：对多个模型直接进行投票，不区分模型结果的相对重要度，最终投票数最多的类为最终被预测的类。
'''
iris = datasets.load_iris()

x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

clf1 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=3, min_child_weight=2, subsample=0.7,
                     colsample_bytree=0.6, objective='binary:logistic')
clf2 = RandomForestClassifier(n_estimators=50, max_depth=1, min_samples_split=4,
                              min_samples_leaf=63,oob_score=True)
clf3 = SVC(C=0.1)

# 硬投票
eclf = VotingClassifier(estimators=[('xgb', clf1), ('rf', clf2), ('svc', clf3)], voting='hard')
for clf, label in zip([clf1, clf2, clf3, eclf], ['XGBBoosting', 'Random Forest', 'SVM', 'Ensemble']):
    scores = cross_val_score(clf, x, y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))


*****软投票：
将所有模型预测样本为某一类别的概率的平均值作为标准
clf1 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=3, min_child_weight=2, subsample=0.8,
                     colsample_bytree=0.8, objective='binary:logistic')
clf2 = RandomForestClassifier(n_estimators=50, max_depth=1, min_samples_split=4,
                              min_samples_leaf=63,oob_score=True)
clf3 = SVC(C=0.1, probability=True)

# 软投票
eclf = VotingClassifier(estimators=[('xgb', clf1), ('rf', clf2), ('svc', clf3)], voting='soft', weights=[2, 1, 1])
clf1.fit(x_train, y_train)

for clf, label in zip([clf1, clf2, clf3, eclf], ['XGBBoosting', 'Random Forest', 'SVM', 'Ensemble']):
    scores = cross_val_score(clf, x, y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))


'''
软投票：和硬投票原理相同，增加了设置权重的功能，可以为不同模型设置不同权重，进而区别模型不同的重要度。
'''
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

clf1 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=3, min_child_weight=2, subsample=0.8,
                     colsample_bytree=0.8, objective='binary:logistic')
clf2 = RandomForestClassifier(n_estimators=50, max_depth=1, min_samples_split=4,
                              min_samples_leaf=63,oob_score=True)
clf3 = SVC(C=0.1, probability=True)

# 软投票
eclf = VotingClassifier(estimators=[('xgb', clf1), ('rf', clf2), ('svc', clf3)], voting='soft', weights=[2, 1, 1])#设置权重
clf1.fit(x_train, y_train)

for clf, label in zip([clf1, clf2, clf3, eclf], ['XGBBoosting', 'Random Forest', 'SVM', 'Ensemble']):
    scores = cross_val_score(clf, x, y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))



模型融合
平均：
简单平均法 加权平均法
投票：
简单投票法 加权投票法
综合：
排序融合 log融合
stacking:
构建多层模型，并利用预测结果再拟合预测。
blending：
选取部分数据预测训练得到预测结果作为新特征，带入剩下的数据中预测。Blending只有一层，而Stacking有多层
stacking 将若干基学习器获得的预测结果，将预测结果作为新的训练集来训练一个学习器。如下图 假设有五个基学习器，将数据带入五基学习器中得到预测结果，再带入模型六中进行训练预测。但是由于直接由五个基学习器获得结果直接带入模型六中，容易导致过拟合。所以在使用五个及模型进行预测的时候，可以考虑使用K折验证，防止过拟合。
blending 与stacking不同，blending是将预测的值作为新的特征和原特征合并，构成新的特征值，用于预测。为了防止过拟合，将数据分为两部分d1、d2，使用d1的数据作为训练集，d2数据作为测试集。预测得到的数据作为新特征使用d2的数据作为训练集结合新特征，预测测试集结果。

Blending与stacking的不同
stacking
stacking中由于两层使用的数据不同，所以可以避免信息泄露的问题。
在组队竞赛的过程中，不需要给队友分享自己的随机种子。
Blending
blending比stacking简单，不需要构建多层模型。
由于blending对将数据划分为两个部分，在最后预测时有部分数据信息将被忽略。
同时在使用第二层数据时可能会因为第二层数据较少产生过拟合现象。

简单加权平均，结果直接融合求多个预测结果的平均值。pre1-pren分别是n组模型预测出来的结果，将其进行加权融
pre = (pre1 + pre2 + pre3 +...+pren )/n
加权平均法一般根据之前预测模型的准确率，进行加权融合，将准确性高的模型赋予更高的权重。
pre = 0.3pre1 + 0.3pre2 + 0.4pre3 

简单投票
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
clf1 = LogisticRegression(random_state=1)
clf2 = RandomForestClassifier(random_state=1)
clf3 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=4, min_child_weight=2, subsample=0.7,objective='binary:logistic')
 
vclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('xgb', clf3)])
vclf = vclf .fit(x_train,y_train)
print(vclf .predict(x_test))

加权投票
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
clf1 = LogisticRegression(random_state=1)
clf2 = RandomForestClassifier(random_state=1)
clf3 = XGBClassifier(learning_rate=0.1, n_estimators=150, max_depth=4, min_child_weight=2, subsample=0.7,objective='binary:logistic')
 
vclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('xgb', clf3)])
vclf = vclf .fit(x_train,y_train)
print(vclf .predict(x_test))


***stacking融合 https://zhuanlan.zhihu.com/p/258852400
使用之前的训练的lgb和xgb模型作为基分类器，逻辑回归作为目标分类器做stacking
import warnings
warnings.filterwarnings('ignore')
import itertools
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB 
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import StackingClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from mlxtend.plotting import plot_learning_curves
from mlxtend.plotting import plot_decision_regions


# 以python自带的鸢尾花数据集为例
iris = datasets.load_iris()
X, y = iris.data[:, 1:3], iris.target


clf1 = KNeighborsClassifier(n_neighbors=1)
clf2 = RandomForestClassifier(random_state=1)
clf3 = GaussianNB()
lr = LogisticRegression()
sclf = StackingClassifier(classifiers=[clf1, clf2, clf3], 
                          meta_classifier=lr)


label = ['KNN', 'Random Forest', 'Naive Bayes', 'Stacking Classifier']
clf_list = [clf1, clf2, clf3, sclf]
    
fig = plt.figure(figsize=(10,8))
gs = gridspec.GridSpec(2, 2)
grid = itertools.product([0,1],repeat=2)


clf_cv_mean = []
clf_cv_std = []
for clf, label, grd in zip(clf_list, label, grid):
        
    scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
    print("Accuracy: %.2f (+/- %.2f) [%s]" %(scores.mean(), scores.std(), label))
    clf_cv_mean.append(scores.mean())
    clf_cv_std.append(scores.std())
        
    clf.fit(X, y)
    ax = plt.subplot(gs[grd[0], grd[1]])
    fig = plot_decision_regions(X=X, y=y, clf=clf)
    plt.title(label)


plt.show()

***blending融合
# 以python自带的鸢尾花数据集为例
data_0 = iris.data
data = data_0[:100,:]


target_0 = iris.target
target = target_0[:100]
 
#模型融合中基学习器
clfs = [LogisticRegression(),
        RandomForestClassifier(),
        ExtraTreesClassifier(),
        GradientBoostingClassifier()]
 
#切分一部分数据作为测试集
X, X_predict, y, y_predict = train_test_split(data, target, test_size=0.3, random_state=914)


#切分训练数据集为d1,d2两部分
X_d1, X_d2, y_d1, y_d2 = train_test_split(X, y, test_size=0.5, random_state=914)
dataset_d1 = np.zeros((X_d2.shape[0], len(clfs)))
dataset_d2 = np.zeros((X_predict.shape[0], len(clfs)))
 
for j, clf in enumerate(clfs):
    #依次训练各个单模型
    clf.fit(X_d1, y_d1)
    y_submission = clf.predict_proba(X_d2)[:, 1]
    dataset_d1[:, j] = y_submission
    #对于测试集，直接用这k个模型的预测值作为新的特征。
    dataset_d2[:, j] = clf.predict_proba(X_predict)[:, 1]
    print("val auc Score: %f" % roc_auc_score(y_predict, dataset_d2[:, j]))


#融合使用的模型
clf = GradientBoostingClassifier()
clf.fit(dataset_d1, y_d2)
y_submission = clf.predict_proba(dataset_d2)[:, 1]
print("Val auc Score of Blending: %f" % (roc_auc_score(y_predict, y_submission)))


****************** CH17 算法调参 ********************
机器学习的模型都是参数化的，可以通过 调参来提高模型的准确度。

如何找到最佳的参数组合，可以把它当作一个查询问题来处理，到何时停止？
（应该遵循偏差和方差协调原则）调整算法参数是采用机器学习解决问题的（最后一个步骤），有时也被称为（超参数优化）。

参数可分两种：
一种是影响模型在训练集上的（准确度）或（防止过拟合能力）的参数
另一种是不影响这两者的参数。
模型在样本总体上的准确度由其在训练集上的准确度及其防止过拟合的能力共同决定。

在调参时主要针对第一种参数进行调整，最终达到的效果是
模型在训练集上的准确度和防止过拟合能力最优

两种自动寻找最优化参数的算法：
（1）网格搜索优化参数 （网格寻优）
（2）随机搜索优化参数

（1）网格搜索优化参数 （网格寻优）
通过（遍历）已定义参数的列表，来评估算法的参数，从而找到最优参数。
网格搜索优化参数适用于（三四个或更少）的超参数，参数较多时要改用随机搜索。
当超参数的数量增加时，网格搜索的计算复杂度会呈现（指数型增长）。

由用户列出一个较小的超参数值域，这些超参数值域的笛卡尔集（排列组合）为一组组超参数。网格搜索算法使用每组超参数训练模型，并挑选验证集误差最小的超参数组合。
在sklearn中使用GridSearchCV来实现对参数的跟踪、调整与评估，从而找到最优参数。
#GridSearchCV使用（字典对象）来指定需要调参的参数，
#可以同时对一个或多个进行调参。
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
算法实例化
model = Ridge()
设置要遍历的参数(以算法的参数名为key，参数值为列表，可设置多个key-value)
param_grid = {'alpha': [1, 0.1, 0.01, 0.001, 0]}
通过网格搜索查询最优参数
grid = GridSearchCV(estimator= model, param_grid= param_grid)
grid.fit(X,y)
搜索结果
print('最高得分：%.3f' %grid.best_score_)
print('最优参数：%.3f' %grid.best_estimator_.alpha)
#为什么叫网格？因为只是各参数列表的笛卡尔积？
param_grid是一个字典对象，以算法的参数名为 key ，需要遍历的参数值列表为 value, 在验证算法最优参数的网格搜索算法中, 可以设定多个 key: value 对，同时查询多个参数的最优参数值

（2）随机搜索优化参数
随机搜索通过（固定次数的迭代），采用随机采样分布的方式搜索合适的参数。
随机搜索为每个参数定义了一个分布函数，并在该空间中采样。
与网格搜索优化参数相比，随机搜索优化参数提供了一种更高效的解决方法（特别是在参数数量多的情况下），随机搜索优化参数为每个参数定义了一个分布函数，并在该空间中采样.

下面的例子通过RandomizedSearchCV对Ridge岭回归算法的参数进行100次迭代，并选出最优的参数。

Scipy中的uniform是一个均匀随机采样函数，默认生成0与1之间的随机采样数值。

from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
# 算法实例化
model = Ridge()
# 设置要遍历的参数
param_grid = {'alpha': uniform}
# 通过随机搜索查询最优参数
grid = RandomizedSearchCV(estimator= model,
                          param_distributions= param_grid,
                          n_iter= 100,
                          random_state= 7)
grid.fit(X,y)
# 搜索结果
print('最高得分：%.3f' %grid.best_score_)
print('最优参数：%.3f' %grid.best_estimator_.alpha)




********** CH18 序列化 加载模型。
在实际的项目中，需要将生成的模型序列化，并将其发布到生产环境。
 当新数据出现时，需要反序列化已保存的模型，然后用其预测新的数据。
 （1）模型序列化和重用的重要性
 （2）如何通过pickle来序列化和反序列化机器学习模型。
 （3）如何通过joblib来序列化和反序列化机器学习模型。
当模型训练需要花费大量的时间时，模型序列化就尤为重要。

(1)通过pickle 序列化和反序列化机器学习的模型
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
# 训练模型
model = LogisticRegression()
model.fit(X_train, Y_traing)

# 保存模型
model_file = 'finalized_model.sav'
with open(model_file, 'wb') as model_f:
    dump(model, model_f)

# 加载模型
with open(model_file, 'rb') as model_f:
    loaded_model = load(model_f)
    result = loaded_model.score(X_test, Y_test)
    print("算法评估结果：%.3f%%" % (result * 100))

pickle是标准的python序列化的方法，可以通过它序列化模型，并将其保存到文件中。
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= 0.33, random_state= 4)
#训练模型
model = LogisticRegression()
model.fit(X_train, y_train)

#保存模型
model_file = 'finalized_model.sav'
with open(model_file, 'wb') as model_f:
    dump(model, model_f) # 模型序列化

#加载模型
with open(model_file, 'rb') as model_f:
    loaded_model = load(model_f) 
    # 模型反序列化
    result = loaded_model.score(X_test, y_test)
    print('算法评估结果：%.3f%%' %(result*100))



(2)通过joblib序列化和反序列化机器学习的模型
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load

# 训练模型
model = LogisticRegression()
model.fit(X_train, Y_traing)

# 保存模型
model_file = 'finalized_model_joblib.sav'
with open(model_file, 'wb') as model_f:
    dump(model, model_f)

# 加载模型
with open(model_file, 'rb') as model_f:
    loaded_model = load(model_f)
    result = loaded_model.score(X_test, Y_test)
    print("算法评估结果：%.3f%%" % (result * 100))

joblib是scipy生态环境的一部分，提供了通用的工具来序列化和反序列化python的对象 。   
通过joblib序列化对象时会采用Numpy的格式保存数据，这对某些保存数据到模型中的算法非常有效，如k近邻。

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load
model = LogisticRegression()
model.fit(X_train, y_train)

#保存模型
model_file = 'finalized_model_joblib.sav'
with open(model_file, 'wb') as model_f:
    dump(model, model_f) # 模型序列化

#加载模型
with open(model_file, 'rb') as model_f:
    loaded_model = load(model_f) 
    # 模型反序列化
    result = loaded_model.score(X_test, y_test)
    print('算法评估结果：%.3f%%' %(result*100))

在生成机器学习模型时，需要考虑以下几个问题
• Python 的版本： 要记录下 Python 的版本， 大部分情况下，在序列化模型和反
列化模型时，需要使用相同的 Python 版本。
·类库版本：同样需要记录所有的主要类库的版本，因为在序列化模型和反序列化模型时需要使用相同版本的类库，不仅需要 SciPy scikit-learn 版本一致，其他的类库版本也需要一致。
·手动序列化：有时需要手动序列化算法参数，这样可以直接在 scikit-learn 中或其
他的平台重现这个模型。我们通常会花费大量的时间在选择算法和参数调整上，将这个过程手动记录下来比仅序列化模型更有价值。

*********** CH19 预测模型项目模板
端到端地预测（分类与回归）模型的项目结构。
如何将前面学到的内容引入到项目中。
如何通过这个项目模板来得到一个高准确度的模板。

机器学习是针对数据进行自动挖掘，找出数据的内在规律，并应用这个规律来预测
新数据。

import numpy as np
import pandas as pd

import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#os.chdir(r'D:\Spyder_Workspace')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 精度要求
pd.set_option('precision',3) 
np.set_printoptions(precision=3)

一个很好的实践机器学习项目的方法，是使用从UCI机器学习仓库获取的数据集开启一个机器学习项目。

机器学习项目的python模板
通常是六个步骤：
1.定义问题
a）导入类库
b）导入数据集

2.理解数据
a）描述性统计
b）数据可视化

3.数据准备
a）数据清洗
b）特征选择
c）数据转换

4.评估算法
a）分离数据集
b）定义模型评估标准
c）算法审查
d）算法比较

5.优化模型
a）算法调参
b）集成算法

6.结果部署
a）预测评估数据集
b）利用整个数据集生成模型
c）序列化模型

使用模板的小技巧
（1）快速执行一遍：首先要快速地在项目中将模板中的每一个步骤执行一遍，这样会加
强对项目每一部分的理解并给如何改进带来灵感.
（2）循环：整个流程不是线性的，需要多次重复步骤3和4
（3）尝试每一个步骤，即使你认为不适用，也不要跳过，而是减少该步骤所做的贡献。

定向准确度：机器学习项目的目标是得到一个准确度足够高的模型。每一个步骤都要为实现这个目标做出贡献 要确保每次改变都会给结果带来正向的影响，或者对其他的步骤带来正向的影响。在整个项目的每个步骤中，准确度只能向变好的方向移动。
按需适用：可以按照项目的需要来修改步骤，尤其是对模板中的各个步骤非常熟悉之后。需要把握的原则是，每一次改进都以提高算法模型的准确度为前提。



步骤 1 定义问题
要是导入在机器学习项目中所需要的类库和数据集等，以便完成机器学习的项目，包括导入 Python 类库、类和方法，以及导入数据。同时这也是所有的配置参数的配置模块。当数据集过大时，可以在这里对数据集进行瘦身处理，理想状态是可以在 1 分钟甚至是 30 秒内完成模型的建立或可视化数据集。

步骤 2 理解数据
这是加强对数据理解的步骤，包括通过描述性统计来分析数据和通过可视化来观察数据 在这一步需要花费时间多问几个问题，设定假设条件并调查分析一下 ，这对模型的建立会有很大的帮助

步骤 3 数据准备
数据准备主要是预处理数据，以便让数据可以更好地展示问题，以及熟悉输入与输出结果的关系 包括
·通过删除重复数据、标记错误数值，甚至标记错误的输入数据来清洗数据。
.特征选择，包括移除多余的特征属性和增加新的特征属性。
·数据转化，对数据尺度进行调整，或者调整数据的分布，以便更好地展示问题。
要不断地重复这个步骤和下一个步骤，直到找到足够准确的算法生成模型。

步骤 4 评估算法
估算法主要是为了寻找最佳的算法子集，包括
·分离出评估数据集，以便于验证模型
·定义模型评估标准，用来评估算法模型。
.抽样审查线性算法和非线性算法。
·比较算法的准确度
在面对一个机器学习的问题的时候，需要花费大量的时间在评估算法和准备数据上
直到找到 3-5 种准确度足够的算法为止。

步骤 5 优化模型
当得到一个准确度足够的算法列表后,要从中找出最合适的算法，通常有两种方法可以提高算法的准确度。
.对每一种算法进行调参，得到最佳结果。
.使用集合算法来提高算法模型的准确度。

步骤 6 结果部署
一旦认为模型的准确度足够高 就可以将这个模型 序列化，以便有新数据时使用该模型来预测数据。
.通过验证数据集来验证被优化过的模型。
.通过整个数据集来生成模型。
.将模型序列化，以便于预测新数据。
做到这一步的时候，就可以将模型展示并发布给相关人员 当有新数据产生时，可以采用这个模型来预测新数据。


**********CH20 回归项目实例
本章主要内容：
如何端到端地完成一个回归问题的模型
如何通过（数据转换、调参、集成算法）提高模型的准确度

Boston House Price数据集 回归数据集

导入在项目中需要的类库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #可视化工具
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor 
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
导入数据集
import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#os.chdir(r'D:\Spyder_Workspace')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
pd.set_option('display.width',120)
# 精度要求
pd.set_option('precision',3) 
np.set_printoptions(precision=3)

from sklearn import datasets
boston = datasets.load_boston()
dataset = pd.DataFrame(boston.data, columns= boston.feature_names)

2.理解数据
print('数据维度：行 %s, 列 %s' %dataset.shape)
#print(dataset.dtypes) # 包含在下info()里面了
print(dataset.info()) #缺失值情况，数据类型
print(dataset.head()) #可以看到：不同单位

# a）描述性统计
print(dataset.describe()) # 对max、min的理解
print(dataset.corr(method='pearson'))# 大的相关系数 person相关 查看关联关系
print(dataset.skew()) # 偏离程度

# b）数据可视化
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
plt.show() # 直方图 有指数分布、双峰分布

dataset.plot(kind='density', subplots=True, layout=(4,4),sharex=False,fontsize=1)
plt.show() # 密度图 更容易的看出双峰 

dataset.plot(kind='box', subplots=True, layout=(4,4), sharex=False,sharey=False, fontsize=1)
plt.show() # 偏离程度

scatter_matrix(dataset)
plt.show() #散点矩阵图 

sns.heatmap(dataset.corr(), annot=True, cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix 相关矩阵图
fig=plt.gcf()
fig.set_size_inches(12,10)
plt.show()# 强相关的，建议后续处理中移除这些特征。。。

'''通过数据的相关性和分布等发现，数据集中数据结构比较复杂
需要考虑对数据进行转换，以提高准确度
1.通过特征选择来减少大部分相关性高的特征。
2.通过标准化数据来降低不同数据度量单位带来的影响。
3.通过正态化数据来降低不同的数据分布结构，以提高准确度
可进一步查看数据的可能性分级（离散化），他可以提高决策树准确度
'''

3.数据准备
a）数据清洗
b）特征选择
c）数据转换

4.评估算法（评估框架来选择合适的算法）
分析完数据不能立刻选择出哪个算法对需要解决的问题最有效 我们认为，由于部分数据的线性分布，线性回归算法和弹性网络回归算法对解决问题可能比较有效。另外，由于数据的离散化，通过决策树算法或支持向量机法也许可以生出高准确度的模型。
到这里，依然不清楚哪个算法会生成准确度最高的模型，因此 要设计一个评估框架来选择合适的算法。
采用 10 折交叉验证来分离数据，通过均方误差来比较算法的准确度 
均方误差越趋近于 0 算法准确度越高 

# a）分离数据集
X = dataset.values
y = boston.target
#y = pd.DataFrame(boston.target,columns=['MEDV'])
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= 0.2, random_state = 7)
# b）定义模型评估标准
scoring = 'neg_mean_squared_error'
# c）算法审查(评估算法——baseline)
对原始数据不做任何处理，对算法进行一个评估，形成一个算法的评估基准，这个基准值是对后续算法改善优劣比较的基准值
选择三个线性算法和三个非线性算法来进行比较
线性算法：线性回归LR、套索回归LASSO 弹性网络回归EN
非线性算法：分类与回归树（CART）、支持向量机 SVM K 近邻算法（KNN
# ======== 原始数据
models = {}
models['LR'] = LinearRegression()
models['LASSO'] = Lasso()
models['EN'] = ElasticNet()
models['KNN'] = KNeighborsRegressor()
models['CART'] = DecisionTreeRegressor()
models['SVM'] = SVR()
#评估算法
对所有的算法使用默认参数，并比较算法的准确度，此处比较的是均方误差的均值和标准方差
results = []
for key in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(models[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
从执行结果来看，线性回归具有最优的 MSE，接下来是分类与回归树算法
# d）算法比较
查看所有的10折交叉分离验证的结果
# 箱线图
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()
从图中可以看到，线性算法的分布比较类似，并且K近邻算法的结果分布非常紧凑

'''
不同的数据度量单位，也许是KNN和SVM算法表现不佳的主要原因
'''

评估算法--正态化数据
在这里对训练数据集进行数据转换处理，将所有的数据特征值转化成“0”为中位值、标准差为"1"的数据。
对数据正态化时，为了防止数据泄露，采用 Pipeline 来正态化数据和对模型进行评估。为了与前面的结果进行比较，此处采用相同的评估框架来评估算法模型。

'''
下面将对数据进行正态化处理，再次比较算法的结果
'''
# ==========正态化数据
# 为了防止数据泄露，采用Pipeline来正态化数据和对模型进行评估。
#steps = [] #--------
#steps.append(('Scaler', StandardScaler()))
#steps.append(('LR', LinearRegression()))
#pipelines['ScalerLR'] = Pipeline(steps) # model: Scaler+LR
pipelines = {} # models
pipelines['ScalerLR'] = Pipeline([('Scaler',StandardScaler()), ('LR',LinearRegression())])
pipelines['ScalerLASSO'] = Pipeline([('Scaler',StandardScaler()), ('LASSO',Lasso())])
pipelines['ScalerEN'] = Pipeline([('Scaler',StandardScaler()), ('EN',ElasticNet())])
pipelines['ScalerKNN'] = Pipeline([('Scaler',StandardScaler()), ('KNN',KNeighborsRegressor())])
pipelines['ScalerCART'] = Pipeline([('Scaler',StandardScaler()), ('CART',DecisionTreeRegressor())])
pipelines['ScalerSVM'] = Pipeline([('Scaler',StandardScaler()), ('SVM',SVR())])
results = []
for key in pipelines:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(pipelines[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
    #print('%s: %f (%f)' % (key, cv_result.mean(), cv_result.std()))
    执行后发现K近邻算法具有最优的 MSE

#评估算法--箱线图   
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(pipelines.keys())
plt.show()
'''可以看到KNN具有最优的MSE和最紧凑的数据分布'''

5.优化模型
# a）算法调参
目前来看K近邻算法对做过数据转换的数据集有很好的结果，但是是否可以进一步对结果做一些优化呢？K近邻算法的默认参数近邻个数（n_neighbors）是 5，下面通过网格搜索算法来优化参数。
# 调参改善算法--KNN
# 网格搜索KNN的K。
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_neighbors': range(1,23,2)}
model = KNeighborsRegressor()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid = param_grid,
                    scoring = scoring, cv = kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)

print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
cv_results = zip(grid_result.cv_results_['mean_test_score'],
                 grid_result.cv_results_['std_test_score'],
                 grid_result.cv_results_['params'])
for mean, std, param in cv_results:
    print('{} ({}) with {}'.format(mean, std, param))
最优结果--K近邻算法的默认参数近邻个数（n_neighbors）是 3


除调参之外，提高模型准确度的方法是使用集成算法。
下面会对表现比较好的线性回归、 K近邻、分类与回归树算法进行集成，来看看算法能否提高。
袋装算法：随机森林RF 极端随机数ET
提升算法：AdaBoost(AB) 随机梯度上升GBM
依然采用和前面同样的评估框架和正态化之后的数据来分析相关的算法
# b）集成算法
ensembles = {} # models
ensembles['ScalerAB'] = Pipeline([('Scaler',StandardScaler()), ('AB',AdaBoostRegressor())])
ensembles['ScalerAB-KNN'] = Pipeline([('Scaler',StandardScaler()), ('ABKNN',AdaBoostRegressor(
        base_estimator= KNeighborsRegressor(n_neighbors=3)))])
ensembles['ScalerAB-LR'] = Pipeline([('Scaler',StandardScaler()), ('ABLR',AdaBoostRegressor(
        base_estimator= LinearRegression()))])
ensembles['ScalerRFR'] = Pipeline([('Scaler',StandardScaler()), ('RFR',RandomForestRegressor())])
ensembles['ScalerETR'] = Pipeline([('Scaler',StandardScaler()), ('ETR',ExtraTreesRegressor())])
ensembles['ScalerGBR'] = Pipeline([('Scaler',StandardScaler()), ('GBR',GradientBoostingRegressor())])
results = []
for key in ensembles:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(ensembles[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
与前面的线性算法和非线性算法相比，这次的准确度都有了较大的提高。

通过箱线图看一下集成算法在 10 折交叉验证中均方误差 的分布状况。
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(ensembles.keys())
plt.show()
    
20.9 集成算法调参！！！
集成算法都有一个参数n_estimators，这是一个很好的可以用来调整的参数。
#下面对随机梯度上升（GBM）和极端随机树（ET）算法进行调参，来确定最终的模型。
（1） 集成算法GBM调参(每次的结果并不一样，为什么？)   
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_estimators':[10,50,100,200,300,400,500,600,700,800,900]}
model = GradientBoostingRegressor()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid= param_grid,
                    scoring= scoring, cv= kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
（2） 集成算法ET调参(每次的结果并不一样)   
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_estimators':[5]+np.linspace(10,100,10).astype(int).tolist()}
model = ExtraTreesRegressor()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid= param_grid,
                    scoring= scoring, cv= kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
对于随机梯度上升GBM 算法来说，最优的 n_estimators 500 ，对于极端随机树 ET 算法来说，最优的 n_estimators 执行结果，极端随机树 ET 算法略优于随机梯度上升（ GBM ）算法，因此采用极端随机树（ET 算法来训练最终的模型。

也许需要执行多次这个过程才能找到最优参数 
这里有一个技巧，当最优参数是 param_grid 的边界值时，有必要调整 param_grid 行下一次调参。

20.10 确定最终模型
# 训练模型 使用ET算法
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
gbr = ExtraTreesRegressor(n_estimators=80)
gbr.fit(X=rescaledX, y= y_train)
# 评估算法模型的准确度
rescaledX_test = scaler.transform(X_test)
predictions = gbr.predict(rescaledX_test)
print(mean_squared_error(y_test, predictions))

6.结果部署
a）预测评估数据集
b）利用整个数据集生成模型
c）序列化模型

使用模板的小技巧
#（1）快速执行一遍：
#（2）整个流程不是线性的，需要多次重复步骤3和4
#（3）尝试每一个步骤，即使你认为不适用，也不要跳过，而是减少该步骤所做的贡献。



*********CH21 二分类实例
本章主要内容：
如何端到端地完成一个分类问题的模型
如何通过（数据转换、调参、集成算法）提高模型的准确度

项目介绍
#在这个项目中将采用声呐、矿山和岩石数据集
#http://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+%28Sonar%2C+Mines+vs.+Rocks%29
#通过声呐返回的信息判断物质是金属还是岩石。
#数据集共208条数据，每条数据记录了60种不同的声呐探测的数据和一个分类结果
#若结果是岩石则标记为R，否则为金属标记为M
机器学习项目的python模板
# 通常是六个步骤：
# 1.定义问题
# a）导入类库
# b）导入数据集
导入类库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #可视化工具
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier

import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#os.chdir(r'D:\Spyder_Workspace')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
pd.set_option('display.width',120)
# 精度要求
pd.set_option('precision',3) 
np.set_printoptions(precision=3)
 
导入数据
dataset = pd.read_csv('sonar.all-data.csv', header=None)

2.理解数据
print('数据维度：行 %s, 列 %s' %dataset.shape)
#print(dataset.dtypes) # 包含在下info()里面了
print(dataset.info()) #缺失值情况，数据类型
print(dataset.head()) #可以看到：不同单位
# a）描述性统计
print(dataset.groupby(60).size()) # 数据分类的分布情况
print(dataset.describe()) # 对max、min的理解
#print(dataset.corr(method='pearson'))# 大的相关系数
print(dataset.skew()) # 偏离程度
# b）数据可视化
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
plt.show() # 大部分数据呈现高斯分布或指数分布
dataset.plot(kind='density', subplots=True, layout=(8,8),sharex=False,fontsize=1)
plt.show() # 更容易的看出双峰，指数分布的密度函数
'''
该数据集大部分数据呈现一定程度的偏态分布，也许通过Box-Cox转换可以提高模型的准确度
Box-Cox转换是统计中常用的一种数据变化方式，用于连续响应变量不满足正态分布的情况
Box-Cox转换后，可以在一定程度上减少不可观测的误差，也可以预测变量的相关性，
将数据转换成正态分布
'''
dataset.plot(kind='box', subplots=True, layout=(8,8), sharex=False,sharey=False, fontsize=1)
plt.show() # 偏离程度

scatter_matrix(dataset)
plt.show()

sns.heatmap(dataset.corr(), annot=True, cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(12,10)
plt.show()# 强相关的，建议后续处理中移除这些特征。。。
'''通过数据的相关性和分布等发现，数据集中数据结构比较复杂
需要考虑对数据进行转换，以提高准确度
1.通过特征选择来减少大部分相关性高的特征。
2.通过标准化数据来降低不同数据度量单位带来的影响。
3.通过正态化数据来降低不同的数据分布结构，以提高准确度
可进一步查看数据的可能性分级（离散化），他可以提高决策树准确度
'''

3.数据准备
# a）数据清洗
# b）特征选择
# c）数据转换

4.评估算法（评估框架来选择合适的算法）
# a）分离数据集
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
test_size = 0.2 #分离数据集 20%的数据作为评估数据集 80%的数据作为训练数据集
seed = 7
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= test_size, random_state = seed)
# b）定义模型评估标准
#scoring = 'neg_mean_squared_error'
scoring = 'accuracy'

# c）算法审查(评估算法——baseline)
#分析完数据后，并不能决定哪个算法对这个问题最有效。
#直观的感觉是，也行基于距离计算的算法会有不错的表现。

# ======== 原始数据
models = {}
models['LR'] = LogisticRegression()
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
models['NB'] = GaussianNB()
models['SVM'] = SVC()
results = []
for key in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(models[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))

# d）算法比较
# 箱线图
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()
'''
可以看到KNN的结果分布比较紧凑，说明算法对数据的处理比较准确
但SVM算法表现不佳，这出乎我们的意料。
也许是因为数据分布的多样性导致SVM算法不够准确。


下面将对数据进行正态化处理，再次比较算法的结果
'''
# ==========正态化数据
# 为了防止数据泄露，采用Pipeline来正态化数据和对模型进行评估。
#steps = [] #--------
#steps.append(('Scaler', StandardScaler()))
#steps.append(('LR', LinearRegression()))
#pipelines['ScalerLR'] = Pipeline(steps) # model: Scaler+LR
pipelines = {} # models
pipelines['ScalerLR'] = Pipeline([('Scaler',StandardScaler()), ('LR',LogisticRegression())])
pipelines['ScalerLDA'] = Pipeline([('Scaler',StandardScaler()), ('LDA',LinearDiscriminantAnalysis())])
pipelines['ScalerKNN'] = Pipeline([('Scaler',StandardScaler()), ('KNN',KNeighborsClassifier())])
pipelines['ScalerCART'] = Pipeline([('Scaler',StandardScaler()), ('CART',DecisionTreeClassifier())])
pipelines['ScalerNB'] = Pipeline([('Scaler',StandardScaler()), ('NB',GaussianNB())])
pipelines['ScalerSVM'] = Pipeline([('Scaler',StandardScaler()), ('SVM',SVC())])
results = []
for key in pipelines:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(pipelines[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(pipelines.keys())
plt.show()
'''可以看到KNN和SVM的数据分布最紧凑'''

5.优化模型
# a）算法调参
#======== KNN算法调参
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_neighbors': range(1,23,2)}
model = KNeighborsClassifier()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid = param_grid,
                    scoring = scoring, cv = kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)

print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
cv_results = zip(grid_result.cv_results_['mean_test_score'],
                 grid_result.cv_results_['std_test_score'],
                 grid_result.cv_results_['params'])
for mean, std, param in cv_results:
    print('{} ({}) with {}'.format(mean, std, param))
#=========SVM算法调参
支持向量机有两个重要的参数 C（惩罚系数）和 kernel（径向基函数），默认的C参数是 1.0 ，默认的 kernel 参数是 rbf 
下面将对这两个参数进行调参
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {}
param_grid['C'] = np.arange(0.1,2.0,0.2)
#param_grid['kernel'] = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
param_grid['kernel'] = ['linear', 'poly', 'rbf', 'sigmoid']
model = SVC()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid = param_grid,
                    scoring = scoring, cv = kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)

print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
cv_results = zip(grid_result.cv_results_['mean_test_score'],
                 grid_result.cv_results_['std_test_score'],
                 grid_result.cv_results_['params'])
for mean, std, param in cv_results:
    print('{} ({}) with {}'.format(mean, std, param))
'''
最好的SVM的参数是C=1.5,kernel=RBF。准确度达到0.8675，高于KNN
'''
    
# b）集成算法
ensembles = {} # models
ensembles['ScalerAB'] = Pipeline([('Scaler',StandardScaler()), ('AB',AdaBoostClassifier())])
ensembles['ScalerGBM'] = Pipeline([('Scaler',StandardScaler()), ('GBM',GradientBoostingClassifier())])
ensembles['ScalerRF'] = Pipeline([('Scaler',StandardScaler()), ('RFR',RandomForestClassifier())])
ensembles['ScalerET'] = Pipeline([('Scaler',StandardScaler()), ('ETR',ExtraTreesClassifier())])
results = []
for key in ensembles:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(ensembles[key], X_train,y_train,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(ensembles.keys())
plt.show()
我们可以看到，随机梯度上升（ GBM ）也许值得进行进一步的分析，因为它具有良
的准确度，并且数据比较紧凑 接下来对其进行调参 

20.9 集成算法调参！！！
#集成算法都有一个参数n_estimators，这是一个很好的可以用来调整的参数。
#下面对随机梯度上升（GBM）和极端随机树（ET）算法进行调参，来确定最终的模型。
#（1） 集成算法GBM调参(每次的结果并不一样)   
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_estimators':[10,50,100,200,300,400,500,600,700,800,900]}
model = GradientBoostingClassifier()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid= param_grid,
                    scoring= scoring, cv= kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
#（2） 集成算法ET调参(每次的结果并不一样)   
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = {'n_estimators':[5]+np.linspace(10,100,10).astype(int).tolist()}
model = ExtraTreesClassifier()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid= param_grid,
                    scoring= scoring, cv= kfold)
grid_result = grid.fit(X=rescaledX, y=y_train)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))


通过前面对算法评估发现，支持向量机SVM 具有最佳的准确度，所以将会采用SVM，通过训练集数据生成算法模型，并通过预留的评估数据集来评估模型。
在算法评估过程中发现， SVM 对正态化的数据具有较高的准确度。所以对训练集做正态化处理，对评估数据集也做相同的处理。

20.10 确定最终模型
# 训练模型，模型最终化 采用SVM
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
model = SVC(C=1.5, kernel='rbf')
model.fit(X=rescaledX, y= y_train)
# 评估算法模型
rescaledX_test = scaler.transform(X_test)
predictions = model.predict(rescaledX_test)
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
执行结果准确度大概达到86%左右 

6.结果部署
# a）预测评估数据集
# b）利用整个数据集生成模型
# c）序列化模型

使用模板的小技巧
#（1）快速执行一遍：
#（2）整个流程不是线性的，需要多次重复步骤3和4
#（3）尝试每一个步骤，即使你认为不适用，也不要跳过，而是减少该步骤所做的贡献。



********CH22 文本分类实例
本章主要内容：
如何端到端地完成一个文本分类问题的模型
如何通过文本特征提取生成数据特征
如何通过（调参、集成算法）提高模型的准确度
项目介绍
#在这个项目中将采用20Newgroups的数据（http://qwone.com/~jason/20Newgroups/）
#这个是网上非常流行的对文本进行分类和聚类的数据集。
#数据集分两部分，训练数据和评估数据。
#网上还提供了3个数据集，这里采用20news-bydata这个数据集进行项目研究。
#这个数据集是按照日期进行排序的，并去掉了部分重复数据和header，共包含18846个文档
机器学习项目的python模板
# 通常是六个步骤：
# 1.定义问题
# a）导入类库
# b）导入数据集

导入类库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB# 这次不是GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction.text import CountVectorizer #文本特征提取：
from sklearn.feature_extraction.text import TfidfVectorizer

import os
os.chdir(r'E:\大学\大学课程\专业课程\机器学习\机器学习python实践')
#os.getcwd()
#os.chdir(r'D:\Spyder_Workspace')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
pd.set_option('display.width',120)
# 精度要求
pd.set_option('precision',3) 
np.set_printoptions(precision=3)

导入数据
#这里使用scikit-learn的loadfile导入文档数据，
#文档是按照不同的分类分目录来保存的，文件目录名称即所属类别。
categories = ['alt.atheism',
              'rec.sport.hockey',
              'comp.graphics',
              'sci.crypt',
              'comp.os.ms-windows.misc',
              'sci.electronics',
              'comp.sys.ibm.pc.hardware',
              'sci.med',
              'comp.sys.mac.hardware',
              'sci.space',
              'comp.windows.x',
              'soc.religion.christian',
              'misc.forsale',
              'talk.politics.guns',
              'rec.autos' 
              'talk.politics.mideast',
              'rec.motorcycles',
              'talk.politics.misc',
              'rec.sport.baseball',
              'talk.religion.misc']

#导入训练数据和评估数据
from sklearn.datasets import load_files
train_path = '20news-bydate-train'
test_path = '20news-bydate-test'
dataset_train = load_files(container_path= train_path, categories= categories)
dataset_test = load_files(container_path= test_path, categories= categories)

22.3 文本特征提取
# =============================================================================
# 文本数据属于非结构化的数据，一般要转换成结构化的数据才能进行ML文本分类。
# 常见的做法是将文本转换成“文档-词项矩阵”，
# 矩阵的元素可以用词频或TF-IDF值等。TF-IDF实际上是TF*IDF。
# TF-IDF值是一种用于信息检索与数据挖掘的常用加权技术。
# TF的意思是词频（Term Frequency），IDF是逆向文件频率（Inverse Document Frequency）。
# 
# TF(t)= 该词语在当前文档出现的次数 / 当前文档中词语的总数
# IDF(t)= log_e（文档总数 / 出现该词语的文档总数）
#
# TF-IDF的主要思想是：如果某一个词或短语在一篇文章中出现的频率高，
# 并且在其他文章中很少出现，则认为此词或短语具有很好的类别区分能力，适合用来分类。
# 
# IDF的主要思想是：如果包含词条t的文档数n越小，IDF越大，类别区分能力好。
# 如果某一类文档C中包含词条t的文档数为m，而其他类包含词条t的总数为k，
# 显然n=m+k，当m大的时候，n也大，按照IDF公式得到的IDF值小，说明t的区分能力不强。
# 
# 但实际上，如果一个词条在一个类的文档中频繁出现，
# 则说明该词条能够很好地代表这个类的文本特征，这样的词条应该被赋予较高的权重，
# 并作为该类文本的特征词，以区别于其他类文档。
# 
# 这就是IDF的不足之处，在一份给定的文件里，
# TF指的是某一个给定的词语在该文件中出现的频率，
# 这是对词数（Term Count)的归一化，以防止它偏向长的文件。
# 
# IDF是一个词语普遍重要性的度量，
# 某一个特定词语的IDF，可以由总文件数目除以包含该词语的文件的数目，再取对数。
# =============================================================================

#scikit-learn中提供了词频和TF-IDF来进行文本特征提取的实现，
#分别是CountVectorizer和TfidfTransformer.
# 计算词频
count_vect = CountVectorizer(stop_words= 'english', decode_error= 'ignore')
X_train_counts = count_vect.fit_transform(dataset_train.data)
print(X_train_counts.shape)
# 计算TF-IDF
tf_transformer = TfidfVectorizer(stop_words= 'english', decode_error= 'ignore')
X_train_counts_tf = tf_transformer.fit_transform(dataset_train.data)
print(X_train_counts_tf.shape)
'''
这里通过两种方法进行了文本特征的提取，并且查看了数据维度，得到的维度非常大。
在后续的项目中，将使用TF-IDF进行分类模型的训练。
因为，TF=IDF的数据维度巨大，并且自用提取的特征数据，进一步对数据进行分析的意义不大，
因此只简单地查看数据维度的信息。（没必要进行过多的数据理解？）
'''

2.理解数据
# a）描述性统计
# b）数据可视化

3.数据准备
# a）数据清洗
# b）特征选择
# c）数据转换

4.评估算法（评估框架来选择合适的算法）
# a）分离数据集

# b）定义模型评估标准
#scoring = 'neg_mean_squared_error'
scoring = 'accuracy'

# c）算法审查(评估算法——baseline)
#分析完数据后，并不能决定哪个算法对这个问题最有效。

# ======== 
models = {}
models['LR'] = LogisticRegression()
#models['SVM'] = SVC()
models['CART'] = DecisionTreeClassifier()
models['MNB'] = MultinomialNB()
models['KNN'] = KNeighborsClassifier()
results = []
for key in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_result = cross_val_score(models[key], 
                   X_train_counts_tf, dataset_train.target,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
# d）算法比较
# 箱线图
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()
'''
结果显示：逻辑回归具有最好的准确度，朴素贝叶斯分类器MNB和KNN值得进一步研究。

从图可得：MNB的数据离散程度比较好，逻辑回归的偏度较大
'''

5.优化模型
# a）算法调参
#======== 逻辑回归算法调参
#在逻辑回归中的超参数是C。C是目标的约束函数，C值越小则正则化强度越大。
对C进行调参，每次给C设定一定数量的值，如果临界值是最优参数，重复这个步骤，
直到找到最优值
param_grid = {}
param_grid['C'] = [0.1, 5, 13, 15]
model = LogisticRegression()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid = param_grid,
                    scoring = scoring, cv = kfold)
grid_result = grid.fit(X=X_train_counts_tf , y=dataset_train.target)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
可以看到C的最优参数是 13 ( 13 是通过多次调 param_grid 参数得到的）

#=========朴素贝叶斯分类器 NB算法调参
#NB有一个alpha参数，该参数是一个平滑参数，默认值为1.0。
通过对逻辑回归调参，准确度提升到大概 0.92 ，提升比较大。 
朴素贝叶斯分类器有一个 alpha 参数，该参数是一个平滑参数，默认值为 1.0。可以对alpha 参数进行调参 以提升算法的准确度

param_grid = {}
param_grid['alpha'] = [0.001, 0.01, 0.1, 1.5]
model = MultinomialNB()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid = param_grid,
                    scoring = scoring, cv = kfold)
grid_result = grid.fit(X=X_train_counts_tf , y=dataset_train.target)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
'''
C=13，alpha=0.01 同样，通过多次调整 param_grid 得到朴素贝叶斯分类器的 lpha 参数的最优值0.01
'''
    
b）集成算法
随机森林 RF 
AdaBoost AB

ensembles = {} # models
ensembles['AB'] = AdaBoostClassifier()
ensembles['RF'] = RandomForestClassifier()
results = []
for key in ensembles:
    kfold = KFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(models[key], 
                   X_train_counts_tf, dataset_train.target,
                                cv=kfold, scoring= scoring)
    results.append(cv_result)
    print('{}: {} {}'.format(key, cv_result.mean(), cv_result.std()))
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(ensembles.keys())
plt.show()
'''
从执行结果看到RF的分布比较均匀，对数据的适用性比较高，更值得进一步优化。

'''    
20.9 集成算法调参！！！
#集成算法都有一个参数n_estimators，这是一个很好的可以用来调整的参数。
param_grid = {'n_estimators':[10,100,150,200]}
model = RandomForestClassifier()
kfold = KFold(n_splits=10, random_state=7)
grid = GridSearchCV(estimator= model, param_grid= param_grid,
                    scoring= scoring, cv= kfold)
grid_result = grid.fit(X=X_train_counts_tf , y=dataset_train.target)
print('最优: {} 使用{}'.format(grid_result.best_score_,
                              grid_result.best_params_))
'''150'''

20.10 确定最终模型
通过对算法的比较和调参发现，逻辑回归算法具有最高的准确度，因此使用逻辑回归算法生成算法模型 接下来会利用评估数据集对生成的模型进行验证，以确认模型的准确度。
需要注意的是，为了保持数据特征的一致性，对新数据进行文本特征提取时应进行特征扩充，下面使用之前生成的 tf_transformer 的 transform 方法来处理评估数据集。

model = LogisticRegression(C=13)
model.fit(X=X_train_counts_tf , y=dataset_train.target)
X_test_counts_tf = tf_transformer.transform(dataset_test.data)
predictions = model.predict(X_test_counts_tf)
print(accuracy_score(dataset_test.target, predictions))
print(classification_report(dataset_test.target, predictions))

总结：
这类问题可以应用在垃圾邮件自动分类、新闻分类等方面。
在文本分类中，很重要的一点是文本特征提取，可以进一步优化，以提高准确度。
对中文文本分类，需要先进行分词，然后利用sklearn.dataset.base.Bunch
将分词后的文件加载到scikit-learn中。

草稿
#from sklearn.svm import SVC
#model = SVC(gamma=1)
#kfold = KFold(n_splits= 10, random_state= 7)
#result = cross_val_score(model, X_train_counts_tf, dataset_train.target, cv= kfold, scoring=scoring)
#print('算法评估结果(准确度acc)：mean= %.3f%%' %(result.mean()*100))
#算法评估结果(准确度acc)：mean= 90.774%


***************************************************************
TensorFlow 是使用数据流图进行分布式数值计算的更复杂的库。它通过在潜在的数千个 多 GPU 服务器上分布式计算，可以高效地训练和运行非常大的神经网络。TensorFlow 是被 Google 创造的，支持其大型机器学习应用程序。
https://github.com/ageron/handson-ml 在线实现 Jupyter notebooks 上的代码示例。
Jupyter ，第 2 章将指导你完成安装和基本操作：它是你工具箱中的一个 很好的工具。

机器学习 基于scikit-learn
典型的机器学习项目中的主要步骤。 
通过拟合数据来学习模型。 
优化成本函数（cost function）。
处理，清洗和准备数据。 
选择和设计特征。 
使用交叉验证选择一个模型并调整超参数。 
机器学习的主要挑战，特别是欠拟合和过拟合（偏差和方差权衡）。 
对训练数据进行降维以对抗 the curse of dimensionality（维度诅咒） 
最常见的学习算法：线性和多项式回归，Logistic 回归，k-最近邻，支持向量机，决策树，随机森林，集成方法。

神经网络和深度学习 基于TensorFlow
使用 TensorFlow 构建和训练神经网络。 
最重要的神经网络架构：前馈神经网络，卷积网络，递归网络，长期短期记忆网络 （LSTM）、自动编码器。 
训练深度神经网络的技巧。
对于大数据集缩放神经网络。 
强化学习。

Andrew Ng 在 Coursera 上的 ML 课程和 Geoffrey Hinton 关于神经网络和深度学习的课程都是非常棒的

有许多关于机器学习的比较有趣的网站，当然还包括 scikit-learn 出色的 用户指南。你可能会喜欢上 Dataquest ，它提供了一个非常好的交互式教程，还有 ML 博客，比如那些在 Quora 上列出来的博客。最后，Deep Learning 网站 有一个很好的资源列表来学习更多。
http://sklearn.apachecn.org/cn/0.19.0/user_guide.html
https://www.dataquest.io/
http://deeplearning.net/

补充材料（代码示例，练习题等）可以从 https://github.com/ageron/handson-ml 下载。


机器学习有多种类型，可以根据如下规则进行分类： 
是否在人类监督下进行训练（监督，非监督，半监督和强化学习） 
是否可以动态渐进学习（在线学习 vs 批量学习） 
它们是否只是通过简单地比较新的数据点和已知的数据点，或者在训练数据中进行模式 识别，以建立一个预测模型，就像科学家所做的那样（基于实例学习 vs 基于模型学习）

监督学习
在监督学习中，用来训练算法的训练数据包含了答案，称为标签
监督学习算法：
K近邻算法 
线性回归 
逻辑回归 
支持向量机（SVM） 
决策树和随机森林 
神经网络

一个典型的监督学习任务是分类。垃圾邮件过滤器就是一个很好的例子：用许多带有归类 （垃圾邮件或普通邮件）的邮件样本进行训练，过滤器必须还能对新邮件进行分类。 
另一个典型任务是预测目标数值，例如给出一些特征（里程数、车龄、品牌等等）称作预测 值，来预测一辆汽车的价格。这类任务称作回归（图 1-6）。要训练这个系统，你需要给出大量汽车样本，包括它们的预测值和标签（即，它们的价格）。
在机器学习中，一个属性就是一个数据类型（例如，“里程数”），取决于具体问题 
一个特征会有多个含义，但通常是属性加上它的值（例如，“里程数 =15000 ”）


非监督学习
在非监督学习中，你可能猜到了，训练数据是没有加标签的
(1)聚类
K 均值 
层次聚类分析（Hierarchical Cluster Analysis，HCA） 
期望最大值
(2)可视化和降维
主成分分析（Principal Component Analysis，PCA） 
核主成分分析 
局部线性嵌入（Locally-Linear Embedding，LLE）
t-分布邻域嵌入算法（t-distributed Stochastic Neighbor Embedding，t-SNE）
(3)关联性规则学习
Apriori 算法 
Eclat 算法
例如，假设你有一份关于你的博客访客的大量数据。你想运行一个聚类算法，检测相似访客 的分组（图 1-8）。你不会告诉算法某个访客属于哪一类：它会自己找出关系，无需帮助。
降维的目的是简化数据、但是不能失去大部分信息。做法之一是 合并若干相关的特征。例如，汽车的里程数与车龄高度相关，降维算法就会将它们合并成一 个，表示汽车的磨损。这叫做特征提取。

在用训练集训练机器学习算法（比如监督学习算法）时，最好对训练集进行降维。这样可以运行的更快，占用的硬盘和内存空间更少，有些情况下性能也更好。

另一个重要的非监督任务是异常检测（anomaly detection） —— 例如，检测异常的信用卡转 账以防欺诈，检测制造缺陷，或者在训练之前自动从训练数据集去除异常值。异常检测的系 统使用正常值训练的，当它碰到一个新实例，它可以判断这个新实例是像正常值还是异常值。

另一个常见的非监督任务是关联规则学习，它的目标是挖掘大量数据以发现属性间有 趣的关系。例如，假设你拥有一个超市。在销售日志上运行关联规则，可能发现买了烧烤酱 和薯片的人也会买牛排。因此，你可以将这些商品放在一起。


半监督学习
一些算法可以处理部分带标签的训练数据，通常是大量不带标签数据加上小部分带标签数 据。这称作半监督学习。

一些图片存储服务，比如 Google Photos，是半监督学习的好例子。一旦你上传了所有家庭相 片，它就能自动识别相同的人 A 出现了相片 1、5、11 中，另一个人 B 出现在了相片 2、5、 7 中。这是算法的非监督部分（聚类）。现在系统需要的就是你告诉这两个人是谁。只要给每 个人一个标签，算法就可以命名每张照片中的每个人，特别适合搜索照片。

多数半监督学习算法是非监督和监督算法的结合。
例如，深度信念网络（deep belief networks）是基于被称为互相叠加的受限玻尔兹曼机（restricted Boltzmann machines， RBM）的非监督组件。
玻尔兹曼机RBM 是先用非监督方法进行训练，再用监督学习方法进行整个系统微 调。

强化学习
强化学习非常不同。学习系统在这里被称为智能体（agent），可以对环境进行观察，选择和 执行动作，获得奖励（负奖励是惩罚）。然后它必须自己学习哪个是最佳方法 （称为策略，policy），以得到长久的最大奖励。
policy策略决定了智能体在给定情况下应该采取的行动。
DeepMind 的 AlphaGo 也是强化学习 的例子：它在 2016 年三月击败了世界围棋冠军李世石（译者注：2017 年五月，AlphaGo 又 击败了世界排名第一的柯洁）。它是通过分析数百万盘棋局学习制胜策略，然后自己和自己 下棋。要注意，在比赛中机器学习是关闭的，AlphaGo 只是使用它学会的策略。

批量学习
在批量学习中，系统不能进行持续学习：必须用所有可用数据进行训练。这通常会占用大量 时间和计算资源，所以一般是线下做的。首先是进行训练，然后部署在生产环境且停止学 习，它只是使用已经学到的策略。这称为离线学习。
如果你想让一个批量学习系统明白新数据（例如垃圾邮件的新类型），就需要从头训练一个 系统的新版本，使用全部数据集（不仅有新数据也有老数据），然后停掉老系统，换上新系 统。

在线学习
在在线学习中，是用数据实例持续地进行训练，可以一次一个或一次几个实例（称为小批 量）。每个学习步骤都很快且廉价，所以系统可以动态地学习到达的新数据。
在线学习很适合系统接收连续流的数据（比如，股票价格），且需要自动对改变作出调整。
这整个过程通常是离线完成的（即，不在部署的系统上），所以在线学习这个名字会让人疑惑。可以把它想成持续学习。

基于实例学习
系统先用记忆学习案例，然后使用 相似度测量 推广到新的例子
一个（简单的）相似度测量方法是统计两封邮件包 含的相同单词的数量。如果一封邮件含有许多垃圾邮件中的词，就会被标记为垃圾邮件。

基于模型学习
另一种从样本集进行归纳的方法是建立这些样本的模型，然后使用这个模型进行预测。这称 作基于模型学习。
示例
你想知道钱是否能让人快乐，你从 OECD 网站下载了 Better Life Index 指数数据，还 从 IMF 下载了人均 GDP 数据。
用一些国家的数据画图
确实能看到趋势！尽管数据有噪声（即，部分随机），看起来生活满意度是随着人均 GDP 的 增长线性提高的。所以，你决定生活满意度建模为人均 GDP 的线性函数。
这一步称作模型选择：你选一个生活满意度的线性模型，只有一个属性，人均 GDP
life_satisfaction = θ0 + θ1 * GDP_per_capita
这个模型有两个参数 θ0 和 θ1 。通过调整这两个参数，你可以使你的模型表示任何线性函数.
在使用模型之前，你需要确定 θ0 和 θ1 。
如何能知道哪个值可以使模型的性能最佳呢？
要回 答这个问题，你需要指定性能的量度。
可以定义一个实用函数（或拟合函数）用来测量模型是否够好，或者可以定义一个 代价函数 来测量模型有多差。
对于线性回归问题，人们一般是用 代价函数 测量线性模型的预测值和训练样本的距离差，目标是使距离差最小。
接下来就是线性回归算法。
用训练样本训练算法，算法找到使线性模型最拟合数据的参数。这称作模型训练。在我们的例子中，算法得到的参数值是 θ0=4.85 和 θ1=4.91*10-5 。
现在模型已经最紧密地拟合到训练数据了。
最后，可以准备运行模型进行预测了。查询塞浦路斯的人均 GDP，为 22587 美 元，然后应用模型得到生活满意度，后者的值在 4.85 + 22,587 * 4.91 * 10-5 = 5.96 左右
使用scikit-learn训练并运行这个线性模型 
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np import pandas as pd 
import sklearn 
# 加载数据 
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',') gdp_per_capita = pd.read_csv("gdp_per_capita.csv",thousands=',',delimiter='\t', 
encoding='latin1', na_values="n/a") 
# 准备数据 
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita) X = np.c_[country_stats["GDP per capita"]] 
y = np.c_[country_stats["Life satisfaction"]] 
# 可视化数据 
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction') 
plt.show() 
# 选择线性模型 
lin_reg_model = sklearn.linear_model.LinearRegression() 
# 训练模型 
lin_reg_model.fit(X, y) 
# 对塞浦路斯进行预测 
X_new = [[22587]] 
# 塞浦路斯的人均GDP 
print(lin_reg_model.predict(X_new)) # outputs [[ 5.96242338]]
注解：如果你之前接触过基于实例学习算法，你会发现斯洛文尼亚的人均 GDP（20732 美元）和塞浦路斯差距很小，OECD 数据上斯洛文尼亚的生活满意度是 5.7，就可以预 测塞浦路斯的生活满意度也是 5.7。如果放大一下范围，看一下接下来两个临近的国家， 你会发现葡萄牙和西班牙的生活满意度分别是 5.1 和 6.5。对这三个值进行平均得到 5.77，就和基于模型的预测值很接近。
这个简单的算法叫做k近邻回归（这个例子 中， k=3 ）。 
在前面的代码中 替换 线性回归模型 为 K 近邻模型 ，只需将
clf = sklearn.linear_model.LinearRegression()
替换为
clf = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
如果一切顺利，你的模型就可以作出好的预测。如果不能，你可能需要使用更多的属性（就 业率、健康、空气污染等等），获取更多更好的训练数据，或选择一个更好的模型（比如， 多项式回归模型）。

总结一下： 
研究数据 
选择模型 
用训练数据进行训练（即，学习算法搜寻模型参数值，使代价函数最小） 
最后，使用模型对新案例进行预测（这称作推断），但愿这个模型推广效果不差
#可以定义一个 拟合函数 用来测量模型是否够好
# 或者可以定义一个 代价函数 来测量模型有多差

机器学习的主要挑战
(1)训练数据量不足：需要大量数据，才能让多数机器学习算法正常工作
(2)没有代表性的训练数据：使用具有代表性的训练集对于推广到新案例是非常重要的。但是做起来比说起来要难：如果 样本太小，就会有样本噪声（即，会有一定概率包含没有代表性的数据），但是即使是非常 大的样本也可能没有代表性，如果取样方法错误的话。这叫做样本偏差。
(3)低质量数据: 如果训练集中的错误、异常值和噪声（错误测量引入的）太多，系统检测出潜在规 律的难度就会变大，性能就会降低。花费时间对训练数据进行清理是十分重要的。
如果一些实例是明显的异常值，最好删掉它们或尝试手工修改错误。
如果一些实例缺少特征（比如，你的 5% 的顾客没有说明年龄），你必须决定是否忽略 这个属性、忽略这些实例、填入缺失值（比如，年龄中位数），或者训练一个含有这个 特征的模型和一个不含有这个特征的模型，等等。
(4)不相关的特征
(5)过拟合训练数据
(6)欠拟合训练数据






