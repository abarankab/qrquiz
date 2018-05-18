import sqlite3 as sql

path = "../db_api/db/quiz.db"
db = sql.connect(path)


class User:
    def __init__(self, tel_id, score=0):
        self.tel_id = tel_id
        self.score = score

        #adding user to db
        c = db.cursor()
        c.execute("INSERT INTO users (telegram_id, score) VALUES (?, ?)", (tel_id, score))
        db.commit()
        c.close()

    def change_score(self, score) -> None:
        c = db.cursor()
        c.execute("UPDATE users SET score=? WHERE telegram_id=?", (score, self.tel_id))
        self.score = score
        db.commit()
        c.close()

    def _get_id_from_DB(self) -> int:
        c = db.cursor()
        c.execute("SELECT * FROM users")
        for user in c.fetchall():
            if user[1] == self.tel_id:
                return user[0]
        return -1

    def set_unavailable_task(self, task_id) -> None:
        c = db.cursor()
        c.execute("INSERT INTO unavailable (for_id, quest_id) VALUES (?,?)",
                  (self._get_id_from_DB(), task_id))



class Question:
    def __init__(self, title, desc, score, answers: list):
        self.title = title
        self.desc = desc
        self.score = score
        self.answers: list = answers

        c = db.cursor()
        c.execute("INSERT INTO questions (title, description, score) VALUES (?,?,?)",
                  (title, desc, score))

        questions = c.execute("SELECT * FROM questions").fetchall()

        for ans in self.answers:
            c.execute("INSERT INTO answers (for_id, answer) VALUES (?,?)",
                      (len(questions), ans))

        db.commit()
        c.close()