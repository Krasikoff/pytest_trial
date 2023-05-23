# test_engine.py
import pytest
from time import sleep
from engine_class import Engine


def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running


def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    assert isinstance(engine, Engine)

@pytest.mark.sloww  # Отмечаем маркером тест.
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    sleep(3)  # Трёхсекундная пауза.
