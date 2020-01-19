import pytest

#Тестируем метод keys у dict
#Получаем на вход dict
def test_keys_dict(fixture_dict):
	keys_dict = fixture_dict.keys()
	assert len(keys_dict) != 0

#Тестируем метод get у dict 
#Используем параметризацию
#Получаем на вход dict
def test_get_dict(fixture_dict, fixture_with_params):
	m_dict = fixture_dict.get(fixture_with_params)
	assert m_dict == None

