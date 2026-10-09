"""Eco Data SP application entry point."""
from database.database import initialize_database


def main() -> None:
    initialize_database()
    print("Eco Data SP")
    print("Database initialized successfully.")
    print("MVP interface: next development step.")


if __name__ == "__main__":
    main()
