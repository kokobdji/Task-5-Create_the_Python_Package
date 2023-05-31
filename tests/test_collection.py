import pytest
from unique_characters_kokobdji.collection_framework import (
    counter_unique_characters, list_input)


@pytest.mark.parametrize('string, expected_result',
                         [('qwerty', 6), ('qqwweerr', 0), ('123456789', 9)])
def test_counter_positive(string, expected_result):
    assert counter_unique_characters(string) == expected_result


@pytest.mark.parametrize('case', [['Москалі, то хворі люди лізуть воювати, '
                                   'А Ми будемо на них із Говерли срати.'],
                                  {123}, ('cash', 'грошi')])
def test_counter_error(case):
    with pytest.raises(Exception) as ExceptionInfo:
        counter_unique_characters(case)
    assert 'Only for str' == str(ExceptionInfo.value)


@pytest.mark.parametrize('string, expected_result',
                         [(['abdc123123'], [4]), (['Як умру, то поховайте '
                                                   'Мене на могилі, '
                                                   'Серед степу широкого, '
                                                   'На Вкраїні милій'], [11]),
                          (['Вчителi брехали, помилятися не страшно'], [9])])
def test_list_input(string, expected_result):
    assert list_input(string) == expected_result


@pytest.mark.parametrize('case', ['Москалі, то хворі люди лізуть воювати, '
                                  'А Ми будемо на них із Говерли срати.',
                                  123, {'cash': 'грошi'}])
def test_list_input_error(case):
    with pytest.raises(Exception) as ExceptionInfo:
        list_input(case)
    assert 'Only for list, tuple, set' == str(ExceptionInfo.value)
