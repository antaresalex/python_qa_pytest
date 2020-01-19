import pytest

#Создаем список для тестирования
#Получаем список длинной 5
@pytest.fixture
def fixture_someone_list():
	return [1, 4, 3, 2, 5]

#Тестируем метод remove у list
#Получаем на вход список длинной 5
def test_remove_element(fixture_someone_list):
	fixture_someone_list.remove(1)
	assert len(fixture_someone_list) == 4

#Тестируем метод append у list
#Получаем на вход список длинной 5
def test_append_element(fixture_someone_list):
	fixture_someone_list.append(7)
	assert len(fixture_someone_list) == 6

#Тестируем метод clear у list
#Получаем на вход список длинной 5
def test_clear_element(fixture_someone_list):
	fixture_someone_list.clear()
	assert len(fixture_someone_list) == 0

#Тестируем метод count у list
#Получаем на вход список длинной 5
def test_count_element(fixture_someone_list):
	count_number = fixture_someone_list.count(2)
	assert count_number == 1
	fixture_someone_list.append(2)
	count_number = fixture_someone_list.count(2)
	assert count_number == 2

#Тестируем метод sort у list
#Получаем на вход список длинной 5
def test_sort_element(fixture_someone_list):
	fixture_someone_list.sort()
	min_number = min(fixture_someone_list)
	max_number = max(fixture_someone_list)
	assert fixture_someone_list.index(min_number) == 0
	assert fixture_someone_list.index(max_number) == 4


