import pytest


@pytest.mark.database
def test_database_connection(create_database):
    create_database.test_connection()


@pytest.mark.database
def test_check_all_users(create_database):
    result = create_database.get_all_users()
    print(result)


@pytest.mark.database
def test_check_user_sergii(create_database):
    user_data = create_database.get_user_address_by_name('Sergii')

    assert user_data[0][0] == 'Maydan Nezalezhnosti 1'
    assert user_data[0][1] == 'Kyiv'
    assert user_data[0][2] == '3127'
    assert user_data[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(create_database):
    create_database.update_product_qnt_by_id(1, 25)
    product_qnt = create_database.select_product_qnt_by_id(1)

    assert product_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(create_database):
    create_database.insert_product(4, "печиво", "солодке", 30)
    product_qnt = create_database.select_product_qnt_by_id(4)

    assert product_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(create_database):
    create_database.insert_product(99, "тестові", "дані", 999)
    create_database.delete_product_by_id(99)
    product_qnt = create_database.select_product_qnt_by_id(99)

    assert len(product_qnt) == 0


@pytest.mark.database
def test_get_detailed_orders(create_database):
    join_result = create_database.get_detailed_orders()

    assert len(join_result) == 1
    assert join_result[0][0] == 1
    assert join_result[0][1] == "Sergii"
    assert join_result[0][2] == "солодка вода"
    assert join_result[0][3] == "з цукром"
