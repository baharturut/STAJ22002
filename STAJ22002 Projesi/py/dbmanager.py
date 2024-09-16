from membership_detail import membership_detail as md
from nlp_result import nlp_result 
from user_detail import user_detail as ud

class DbManager:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def register(self, user_details: ud):
        sql_1 = "INSERT INTO user_detail(user_name, user_surname) VALUES (%s, %s)"
        value = (user_details.user_name, user_details.user_surname)
        self.cursor.execute(sql_1, value)
        self.connection.commit()
        return self.cursor.lastrowid  

    def add_membership(self, membership_details):
        sql_2 = "INSERT INTO membership_detail(membership_e_mail, membership_password, user_id) VALUES (%s, %s, %s)"
        value2 = (membership_details.membership_e_mail, membership_details.membership_password, membership_details.user_id)
        self.cursor.execute(sql_2, value2)
        self.connection.commit()
    

    def login(self, membership_details: md):
        sql = "SELECT membership_id FROM membership_detail WHERE membership_e_mail = %s AND membership_password = %s"
        value = (membership_details.membership_e_mail, membership_details.membership_password)
        self.cursor.execute(sql, value)
        result = self.cursor.fetchone()
        return result  
    

    def get_nlp_results(self, user_id):
        sql = "SELECT nlp_text, nlp_result_text, membership_id FROM nlp_result WHERE membership_id = %s"
        value = (user_id,)
        self.cursor.execute(sql, value)
        results = self.cursor.fetchall()
        return [nlp_result(nlp_text=row[0], nlp_result_text=row[1], membership_id=row[2]) for row in results]
    

    def insertNLPResultToDatabase(self, text, result, membership_id):

        sql = "INSERT INTO nlp_result (nlp_text, nlp_result_text, membership_id) VALUES (%s,%s,%s)"
        value = (text, result, membership_id)
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")

   
    def get_user_details(self, membership_id):
        try:
            sql = """
            SELECT ud.user_name, ud.user_surname, md.membership_e_mail, md.membership_password
            FROM user_detail ud
            JOIN membership_detail md ON ud.user_id = md.user_id
            WHERE md.membership_id = %s
            """
            self.cursor.execute(sql, (membership_id,))
            result = self.cursor.fetchone()
            if result:
                user_details = {
                    "user_name": result[0],
                    "user_surname": result[1],
                    "membership_e_mail": result[2],
                    "membership_password": result[3]
                }
                return user_details
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_user_nlp_result_counts(self, user_id):
        sql="SELECT nlp_result_text, COUNT(*) as count FROM nlp_result WHERE membership_id = %s GROUP BY nlp_result_text"
        value=(user_id,)
        self.cursor.execute(sql,value)
        results = self.cursor.fetchall()
        return {row[0]: row[1] for row in results}
    
    def update_nlp_result_text(self, nlp_text, new_text):
        try:
            query = "UPDATE nlp_result SET nlp_result_text = %s WHERE nlp_text = %s"
            self.cursor.execute(query, (new_text, nlp_text))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")


