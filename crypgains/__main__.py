from crypgains.prices import update_price_histories, update_price_current
from crypgains.portfolio.portfolio import calculate_total

if __name__ == '__main__':
    update_price_histories.run()
    update_price_current.run()
    calculate_total('crypgains/resources/portfolio.yaml')