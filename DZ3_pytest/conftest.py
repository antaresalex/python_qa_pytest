import pytest

#Создаем список для тестирования
#Получаем список длинной 5
@pytest.fixture
def fixture_someone_list():
	return [1, 4, 3, 2, 5]

@pytest.fixture(params=[1, 4, 2, 6])
def fixture_with_params(request):
    return request.param

#Создаем set для тестирования
#Получаем set длинной 5
@pytest.fixture
def fixture_set():
	return {0, 1, 4, 64, 9, 16, 25}