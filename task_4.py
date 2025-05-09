new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенос task_005 в список выполненных задач (в одно действие)
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# Удаление task_007 из списка новых задач
new_tasks.remove('task_007')

# Вывод последней задачи из new_tasks
print(f'Последняя задача в списке (приоритет повышен): {new_tasks[-1]}')

# Вывод финального состояния списков
print('\nОбновлённый список новых задач:', new_tasks)
print('Обновлённый список выполненных задач:', completed_tasks)