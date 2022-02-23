import sqlite3

def main():
    historyPath = input("Enter the path to your history file: ")
    file = sqlite3.connect(historyPath)
    cursor = file.cursor()
    keywords = input("Enter keywords to delete, space seperated:").split()
    rows = []
    for row in cursor.execute("SELECT * FROM urls"):
        rows.append(row)
    for row in rows:
        for keyword in keywords:
            if keyword in row[1]:
                cursor.execute("DELETE FROM urls WHERE id = ?", (row[0],))
                print("deleted", row[2])
            elif keyword in row[2]:
                cursor.execute("DELETE FROM urls WHERE id = ?", (row[0],))
                print("deleted", row[2])
    file.commit()
    print("Done!")

main()