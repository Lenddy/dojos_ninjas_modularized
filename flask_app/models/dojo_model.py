from flask_app.models import ninja_model
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "select * from dojos;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        all_dojos = []
        for row in result:
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod 
    def add_dojo(cls,data):
        query = "insert into dojos(name) values (%(name)s);"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)


    @classmethod
    def get_one_ninja(cls,data):
# you need to join the 2 tables
        query = "select * from dojos left join ninjas on ninjas.dojo_id = dojos.id where dojos.id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
#you need to see if the leangth if greater than 0 and if it is 
        if len(result) > 0:
            dojo = cls(result[0])
# you need to loop  the variable result 
            for row in result:
#we need to make a dictionary with the info that we have on the class
                ninja_data= {
# the **row means that all the info that we have that is similar will stay the same so you dont have to write it 
                    **row, 
                    "id": row["ninjas.id"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"]
                }
# this is  the vame as in line 35
                ninja = ninja_model.Ninja(ninja_data)
                dojo.ninjas.append(ninja)
            return dojo
        return False