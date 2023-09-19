import sqlite3
import requests
import click
import datetime

CREATE_INVESTMENT_SQL = """
CREATE TABLE IF NOT EXISTS investments(
    coin_id TEXT,
    currency TEXT,
    amount INT,
    current_price TEXT,
    sell INT,
    date TIMESTAMP
);
"""

def get_coin_price(coin_id, currency):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    return coin_price

@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="thb")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def new_investment(coin_id, currency, amount, sell):
    print("new investment")
    current_price = get_coin_price(coin_id, currency)
    sql = "INSERT INTO investments VALUES(?, ?, ?, ?, ?, ?)"
    values = (coin_id, currency, amount, str(current_price), sell, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="thb")
def show_investment(coin_id, currency):
    sql = """SELECT * FROM investments
             WHERE coin_id=? AND currency=? AND sell=?
    """
    buy_results = cursor.execute(sql, (coin_id, currency, False)).fetchall()
    sell_results = cursor.execute(sql, (coin_id, currency, True)).fetchall()

    print("Print buy results")
    for result in buy_results:
        print(f'Buy {coin_id} {result[2]} {currency} at {result[3]} {currency}')
    print("-----------------")

    print("Print sell results")
    for result in sell_results:
        print(f'Sell {coin_id} {result[2]} {currency} at {result[3]} {currency}')
    print("-----------------")

    buy_amount = sum([row[2] for row in buy_results])
    sell_amount = sum([row[2] for row in sell_results])

    print(f'Total is {buy_amount - sell_amount}')

@click.group()
def cli():
    pass

cli.add_command(show_investment)
cli.add_command(new_investment)

if __name__ == '__main__':
    database = sqlite3.connect('portfolio.db')
    cursor = database.cursor()
    cursor.execute(CREATE_INVESTMENT_SQL)
    cli()