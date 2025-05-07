new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенос task_005 в список выполненных задач
completed_task = new_tasks.pop(new_tasks.index('task_005'))
completed_tasks.append(completed_task)
print(f'Задача {completed_task} перенесена в список выполненных.')

# Удаление task_007 из списка новых задач
new_tasks.remove('task_007')
print('Задача task_007 удалена из списка новых задач (ожидается доработка требований).')

# Вывод последней задачи из new_tasks
print(f'Последняя задача в списке (приоритет повышен): {new_tasks[-1]}')

# Вывод финального состояния списков
print('\nОбновлённый список новых задач:', new_tasks)
print('Обновлённый список выполненных задач:', completed_tasks)