import qiita
import slack


def run():
    views = qiita.views()
    slack.notify(views)

if __name__ == "__main__":
    run()