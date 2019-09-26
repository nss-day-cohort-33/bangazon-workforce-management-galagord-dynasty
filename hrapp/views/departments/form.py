import sqlite3
from django.shortcuts import render
from ..connection import Connection
from hrapp.models import Department
from hrapp.models import Employee


def get_department_info():
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

def department_form(request):
    if request.method == 'GET':
        departments = get_department_info()
        template = 'departments/form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)