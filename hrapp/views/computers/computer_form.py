import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee
from ..connection import Connection

def create_employee(cursor,row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row['id']
    employee.first_name = _row['first_name']
    employee.last_name = _row['last_name']

    return employee


def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
                e.id,
                e.first_name,
                e.last_name,
            from hrapp_employee e
        """)

        return db_cursor.fetchall()

def computer_form(request):
    if request.method == 'GET':
        employees = get_employees()
        template = 'books/form.html'
        context = {
            'all_employees': employees
        }

        return render(request, template, context)