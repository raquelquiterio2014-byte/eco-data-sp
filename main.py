from database.database import init_database
from ui.app import App

if __name__ == "__main__":
    init_database()
    App().mainloop()
