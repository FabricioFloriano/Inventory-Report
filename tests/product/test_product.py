from inventory_report.product import Product


def test_create_product() -> None:
    products = Product(
        "1",
        "NoProduct",
        "NoName",
        "01/11/2023",
        "30/11/2024",
        "12345",
        "NoInstructions",
    )

    assert products.id == "1"
    assert products.company_name == "NoName"
    assert products.product_name == "NoProduct"
    assert products.manufacturing_date == "01/11/2023"
    assert products.expiration_date == "30/11/2024"
    assert products.serial_number == "12345"
    assert products.storage_instructions == "NoInstructions"
