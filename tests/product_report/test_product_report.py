from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "12345001",
        "notebook",
        "dell",
        "01/01/2023",
        "01/01/2030",
        "123456789",
        "instrucoes de armazenamento",
    )

    assert str(product) == (
        "The product 12345001 - notebook "
        "with serial number 123456789 "
        "manufactured on 01/01/2023 "
        "by the company dell "
        "valid until 01/01/2030 "
        "must be stored according to the following instructions: "
        "instrucoes de armazenamento."
    )
