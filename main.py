import logging
from connect_db import connect

def insert_db():
    try:
        logging.basicConfig(
            filename="app.log",
            encoding="utf-8",
            filemode="a",
            format="{asctime} : {name} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )
        conn = connect.connect_db()
        cursor = conn.cursor()
        gc_td1 = '''
            SET NOCOUNT ON
            {CALL [192.168.100.53\sql2014].MinhAn_App.dbo.GETDL_TBMT_Zulip}
        '''
        sql_query = f"""
            insert into notify_zullip(to_person, group_yn, status, datetime0, gc_td1)
            select 64, 0, 0, getdate(), {gc_td1} 
        """
        cursor.execute(sql_query)
        conn.commit()
        logging.info(f'Inserted successfully!')
    except Exception as e:
        logging.error(f'{e}')

if __name__ == "__main__":
    insert_db()