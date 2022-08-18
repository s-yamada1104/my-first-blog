# addCsv.py

from django.db import connection
import logging
import csv
from datetime import datetime as dt
from collections import defaultdict
from .models import Sell
logger = logging.getLogger('development')

# DBへの追加用SQL
sell_sql_insert = ("insert into blog_sell (store_id, payment_id, payment_method, offering_method, time, product_id, product_name, price, tax, price_including_tax, member_id_id) "
              "select * from (select %s as store_id, %s as payment_id, %s as payment_method, %s as offering_method, %s as time, %s as product_id, %s as product_name, %s as price, %s as tax, %s as price_including_tax,"
              "%s as member_id_id) as tmp")
              # "where not exists (select * from blog_sell where payment_id = %s and product_id = %s)")
member_sql_insert = ("insert into blog_member (member_id, name, email, points) "
              "select * from (select %s as member_id, %s as name, %s as email, %s as points) as tmp")
              # "where not exists (select * from blog_sell where payment_id = %s and product_id = %s)")


def regist_sell_data(cursor, file_path):
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
                logger.debug('add_data = ' + str(add_data))
                if add_data[-1] == "":
                  add_data[-1] = "Non_member"
                if Sell.objects.filter(payment_id = add_data[1]).filter(product_id = add_data[5]):
                  continue
                print(add_data)
                cursor.execute(sell_sql_insert,add_data)
            logger.info("=== > End DB登録 ==")


# csvファイルのデータをDBに追加する。
def insert_sell_csv_data(file_path):
    logger.info('== csvデータ登録処理開始 ==')

    with connection.cursor() as cursor:
        regist_sell_data(cursor, file_path)

    logger.info('== csvデータ登録処理終了 ==')




def regist_member_data(cursor, file_path):
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
                logger.debug('add_data = ' + str(add_data))
                if Sell.objects.filter(payment_id = add_data[0]):
                  continue
                print(add_data)
                cursor.execute(member_sql_insert,add_data)
            logger.info("=== > End DB登録 ==")


def insert_member_csv_data(file_path):
    logger.info('== csvデータ登録処理開始 ==')

    with connection.cursor() as cursor:
        regist_member_data(cursor, file_path)

    logger.info('== csvデータ登録処理終了 ==')


