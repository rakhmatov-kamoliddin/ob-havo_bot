from utils.db_api.sqlite import Database


def test():
    
    db = Database(path_to_db='data/main.db')
    try:
        db.create_table_users()
    except:
        pass
    db.add_user(112, "Bob", "email", 'ru')
    db.add_user(2352, "olim", "olim@gmail.com", 'uz')
    db.add_user(3236, 'Fred', 'en')
    db.add_user(4246, 'Messi', 'ar')
    db.add_user(5236, "John", "john@mail.com")

    users = db.select_all_users()
    print(f"Barcha fodyalanuvchilar: {users}")

    user = db.select_user(Name="Messi")
    print(f"Bitta foydalanuvchini ko'rish: {user}")



test()