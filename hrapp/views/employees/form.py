import sqlite3
from django.shortcuts import render
from hrapp.models import Employee
from hrapp.models import Department
from ..connection import Connection
from django.urls import reverse
from django.shortcuts import redirect


def employee_form(request):
    if request.method == 'GET':
        departments = get_department()
        template = 'employees/form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

    

def get_department():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department,
            d.budget
        from hrapp_department d
        """)

        return db_cursor.fetchall()


