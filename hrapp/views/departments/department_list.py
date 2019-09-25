import sqlite3
from django.shortcuts import render
from ..connection import Connection
from hrapp.models import Department
from hrapp.models import Employee

def department_list(request):
    """Show all departments include budget and department size"""
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # TODO: Add to query: e.department,
            db_cursor.execute("""
            select
                d.id,
                d.department,
                d.budget,
                e.department_id
            from hrapp_department d
            join hrapp_employee e on  e.department_id = d.id;
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.department = row['department']
                department.budget = row['budget']
                # e.department_id = row['department_id']

                all_departments.append(department)

    template = 'departments/departments_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)