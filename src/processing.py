def sort_by_date(my_list: list, reverse=True) -> list:
    '''Функция сортирует список словарей по дате'''
    :param my_list: Список словарей для сортировки.
    :param reverse: Определяет порядок сортировки, по умолчанию — убывающий.
    :return: Отсортированный список.
    """
    sorted_list = sorted(my_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list