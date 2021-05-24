from db_methods import Db

test_obj = {"ident": 300, "miles": 31, "kms": 50, "loc": "",
            "opening": "01/01/2021, 01:28 AM", "close": "01/01/2021, 03:30 AM", "notes": None}


def test_db_methods():
    db = Db()
    db.insert_row(test_obj)
    list_of_dicts = list(db.find_content())
    db.drop_all({"ident": 300})
