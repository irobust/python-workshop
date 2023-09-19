import psycopg

def get_connection():
    connection = psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "mysecret"
    )
    return connection

def new_investment(coin_id, currency, amount):
    sql = f"""INSERT INTO investments(coin_id, currency, amount) 
             VALUES('{coin_id}', '{currency}', {amount})
          """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()

    print(f"Added investment for {coin_id} in {currency}")

def show_investments():
    connection = get_connection()
    cursor = connection.cursor()

    sql = 'SELECT * FROM investments'

    cursor.execute(sql)
    investments = cursor.fetchall()

    cursor.close()
    connection.close()

    for investment in investments:
        print(investment)

def main():
    new_investment('bitcoin', 'thb', 1000)
    show_investments()

if __name__=='__main__': main()