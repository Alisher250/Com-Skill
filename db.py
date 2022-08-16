import psycopg2
import datetime

now = datetime.datetime.now()

class BotDB:

    def __init__(self, DB_URI):
        """Инициализация"""
        self.conn = psycopg2.connect(DB_URI, sslmode="require")
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """user exists"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def update_user(self, user_id, user_fullname, username):
        """update пользователя в БД"""
        self.cursor.execute("UPDATE users SET user_id = ?, user_fullname = ?, username = ? WHERE user_id = ?", (user_id, user_fullname, username, user_id,))
        return self.conn.commit()

    def add_user(self, user_id, user_fullname,username):
        """Добавляем пользователя в БД"""
        self.cursor.execute("INSERT INTO users(user_id,join_date,user_fullname,username) VALUES (?,?,?,?)", (user_id, now, user_fullname, username))
        return self.conn.commit()

    def add_user_know_skill(self, know_skill, user_id):
        """Добавляем знающий навык пользователя в БД"""
        self.cursor.execute("UPDATE users SET know_skill = ? WHERE user_id = ?", (know_skill, user_id))
        return self.conn.commit()

    def add_user_wknow_skill(self, wknow_skill, user_id):
        """Добавляем навык которому пользователь хочет научится в БД"""
        self.cursor.execute("UPDATE users SET wknow_skill = ? WHERE user_id = ?", (wknow_skill, user_id))
        return self.conn.commit()


    def get_skills_user(self, user_id):
        """Ищем навыки пользователя"""
        result = list(self.cursor.execute("SELECT know_skill, wknow_skill FROM users WHERE user_id = ?", (user_id,)))
        return result

    def get_know_skill_user(self, user_id):
        """Ищем know навыки пользователя"""
        result = list(self.cursor.execute("SELECT know_skill FROM users WHERE user_id = ?", (user_id,)))
        return result

    def get_wknow_skill_user(self, user_id):
        """Ищем wknow навыки пользователя"""
        result = list(self.cursor.execute("SELECT wknow_skill FROM users WHERE user_id = ?", (user_id,)))
        return result


    def get_need_user(self, wknow_skill, know_skill):
        """Ищем пользователя, который знает навык нужный пользователю и который хочет научится навыку который знает пользователь"""
        return list(self.cursor.execute("SELECT user_fullname, username FROM users WHERE know_skill = ? AND wknow_skill = ?", (wknow_skill, know_skill)))

    def get_count_need_user(self,wknow_skill,know_skill):
        """Считаем количество нужных пользователей"""
        count = (len(self.cursor.execute("SELECT user_fullname, username FROM users WHERE know_skill = ? AND wknow_skill = ?", (wknow_skill, know_skill)).fetchall()))
        return count

    def get_count_school_skills(self):
        """Считаем количество школьных предметов"""
        count = (len(self.cursor.execute("SELECT * FROM school_skills").fetchall()))
        return count

    def get_title_school_skills(self):
        """Находим все названия школьных предметов и превращаем их в список"""
        titles = list(self.cursor.execute("SELECT title FROM school_skills"))
        return titles

    def get_count_profi_skills(self):
        """Считаем количество профи предметов"""
        count = (len(self.cursor.execute("SELECT * FROM profi_skills").fetchall()))
        return count

    def get_title_profi_skills(self):
        """Находим все названия профи предметов и превращаем их в список"""
        titles = list(self.cursor.execute("SELECT title FROM profi_skills"))
        return titles

    def get_user_id(self, user_id):
        """Get user id"""
        self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        return self.conn.commit()

    def close(self):
        """Закрытие БД"""
        self.conn.close()

"""    def update_null_know_skill_user(self, user_id):

        self.cursor.execute("UPDATE users SET know_skill = NULL WHERE user_id = ?", (user_id,))
        return self.conn.commit()

    def update_null_wknow_skill_user(self, user_id):

        self.cursor.execute("UPDATE users SET wknow_skill = NULL WHERE user_id = ?", (user_id,))
        return self.conn.commit()
        
    def update_null_know_skill_user(self, user_id):
        result = list(self.cursor.execute("UPDATE users SET know_skill = NULL WHERE user_id = ?", (user_id,)))
        return result

    def update_null_wknow_skill_user(self, user_id):
        result = list(self.cursor.execute("UPDATE users SET wknow_skill = NULL WHERE user_id = ?", (user_id,)))
        return result        
        
        
"""
