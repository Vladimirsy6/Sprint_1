import pprint

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


# Функция для удаления дублей из списка
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


# Функция для формирования словаря с уникальными тикетами
def categorize_tickets(types, tickets):
    seen = set()
    result = {}

    for level in sorted(types.keys()):
        unique_tickets = []
        for ticket in tickets.get(level, []):
            if ticket not in seen:
                unique_tickets.append(ticket)
                seen.add(ticket)
        result[types[level]] = remove_duplicates(unique_tickets)

    return result


# Получение и вывод итогового словаря
tickets_by_type = categorize_tickets(types, tickets)

# Выводим результат с отступами
pprint.pprint(tickets_by_type, indent=4)