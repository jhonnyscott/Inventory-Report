from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        12345001,
        'notebook',
        'dell',
        '01/01/2023',
        '01/01/2030',
        123456789,
        'instrucoes de armazenamento'
    )

    assert product.id == 12345001
    assert product.product_name == 'notebook'
    assert product.company_name == 'dell'
    assert product.manufacturing_date == '01/01/2023'
    assert product.expiration_date == '01/01/2030'
    assert product.serial_number == 123456789
    assert product.storage_instructions == 'instrucoes de armazenamento'
