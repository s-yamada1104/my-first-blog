# addCsv.py

from django.db import connection
import logging
import csv
from datetime import datetime as dt
from collections import defaultdict
from .models import Sell
logger = logging.getLogger('development')

# DBへの追加用SQL
sql_insert = ("insert into blog_sell (store_id, payment_id, payment_method, offering_method, time, product_id, product_name, price, tax, price_including_tax, user_id, quantity) "
              "select * from (select %s as store_id, %s as payment_id, %s as payment_method, %s as offering_method, %s as time, %s as product_id, %s as product_name, %s as price, %s as tax, %s as price_including_tax,"
              "%s as user_id, %s as quantity) as tmp")
              # "where not exists (select * from blog_sell where payment_id = %s and product_id = %s)")


def regist_data(cursor, file_path):
    # ファイル読み込み（CSV形式）
    try:
        file = open(file_path, newline='')
    except IOError:
        logger.warning('対象ファイルが存在しません：' + file_path)
        logger.warning('DB登録は行いません:' + file_path)
    else:
        logger.info('=== > Start DB登録 ==')
        with file:
            reader = csv.reader(file)
            header = next(reader)  # ヘッダーをスキップ
            d = defaultdict(int)
            for row in reader:
                str_time = [dt.now().strftime('%Y-%m-%d %H:%M:%S')]
                add_data = []
                add_data.extend(row)  # csvから読み取った情報
                d[tuple(add_data)] += 1
                logger.debug('add_data = ' + str(add_data))
                # add_data.append(row[1])
                # add_data.append(row[5])
                print(add_data)
                # cursor.execute(sql_insert,add_data)

                # レコード追加
            for k,v in d.items():
                k = list(k) + [str(v)]
                print(k)
                if Sell.objects.filter(payment_id = k[1]).filter(product_id = k[5]):
                  continue
                cursor.execute(sql_insert,k)

            logger.info("=== > End DB登録 ==")


# csvファイルのデータをDBに追加する。
def insert_csv_data(file_path):
    logger.info('== csvデータ登録処理開始 ==')

    with connection.cursor() as cursor:
        regist_data(cursor, file_path)

    logger.info('== csvデータ登録処理終了 ==')