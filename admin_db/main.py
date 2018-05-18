from db_api import handler as db

def main() -> None:
    while True:
        print("!> NEW QUESTION ")
        qu1 = input("title: ")
        qu2 = input("desc: ")
        qu3 = input("score: ")
        ans = input("answers: ").split()
        db.Question(qu1, qu2, qu3, ans)


if __name__ == "__main__":
    main()