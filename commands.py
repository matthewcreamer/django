#   python3 manage.py makemigrations
#   python3 manage.py migrate

#   run server
#   python3 manage.py runserver


#   delete db
#   find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#   find . -path "*/migrations/*.pyc"  -delete
#   delete db.sqlite3



# name = models.CharField(max_length=255)
# val = models.FloatField()
# val2 = models.DecimalField(max_digits=10, decimal_places=2)



#   TO-DO
#   - create user model
#   


#   FEATURES
#   - VPS purchase generate account for DBO
#   - owner must create a server, only one can be made
#   - owner import csv
#   - owner create user accounts for team
#   - owner set user permissions for each table and for GET, PUT, POST, DELETE, EXPORT
#   - copy icon folder and name it as "DBO-[id_owner]"