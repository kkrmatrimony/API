from connection import get_connection,close_connection
def getProfileId():
    connection = get_connection()
    cursor = connection.cursor()
    query = """select concat(seq_type, LPAD(last_seq_no+1,5,'0')) as pid, last_seq_no+1 as last_seq_no from vts_seq_generator"""
    cursor.execute(query);
    records = cursor.fetchall()
    close_connection(connection)
    return records

def updateSeqNumber(seqNo, seqType):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """update vts_seq_generator SET last_seq_no = %s where seq_type = %s"""
        input_data = (seqNo, seqType)
        cursor.execute(query,input_data);
        connection.commit()        
        close_connection(connection)
    except:
        print("Failed to update record to database: {}".format())
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    