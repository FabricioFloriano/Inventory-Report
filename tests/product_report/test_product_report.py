from inventory_report.product import Product


def test_product_report(capsys) -> None:
    mock_product = {
        "id": "1",
        "product_name": "boardgame",
        "company_name": "hasbro",
        "manufacturing_date": "2021-08-01",
        "expiration_date": "2022-08-01",
        "serial_number": "123456",
        "storage_instructions": "keep in dry place",
    }
    instance = Product(**mock_product)

    expected_output = (
        "The product 1 - boardgame with serial number 123456 "
        "manufactured on 2021-08-01 by the company hasbro valid"
        " until 2022-08-01 must be stored according to the following "
        "instructions: keep in dry place.\n"
    )
    print(instance.__str__())
    captured = capsys.readouterr()
    assert captured.out == expected_output
