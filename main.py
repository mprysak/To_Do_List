def adding_task(list, task):
  list.append(task)
  print('Your task is add')

def removeing_task(list, task):
  list.remove(task)
  print('Your task is remove')

def complete_task(list, task):
  list.remove(task)
  print('Your task is complete and romove from the list')

tasks = []

print('Welcome in the "to do list"\n It is a simple project working on list')

while True:
  try:
    action = int(input('What action do you want to do?\n 1. add task\n 2. remove task\n 3. complete task    '))
  except ValueError:
    print('ERROR - Select actions bettwen 1 and 2')
  except KeyboardInterrupt:
    print("ERROR! - You can't quit!")
  
  if action == 1:
    action1 = input('What task you want to add?: ')
    adding_task(tasks, action1)
  elif action == 2:
    action2 = input('What task you want to remove?: ')
    removeing_task(tasks, action2)
  elif action == 3:
    action3 = input('What task you completed?: ')
    complete_task(tasks, action3)
  
  # dorób coś takiego że jeżeli użytkownik wybierze usunięcie taska a lista jest pusta to jest error

  print(f'This is your to do list {tasks}')

  repeat = input('Do you want to add, remove or complete task?:')

  if repeat == 'yes' or 'Yes' or 'Yeah' or 'yeah':
    continue
  elif repeat == 'no' or 'No' or 'Nah' or 'nah':
    break
  else:
    print('Error!\n program is end')
    break

print(f'This is your to do list {tasks}\n Have a nice day')