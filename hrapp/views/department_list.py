import sqlite3
from django.shortcuts import render
from ..connection import Connection
from hrapp.models import Department

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
                e.department_id,
                d.budget,
                d.employee
            from hrapp_department d
            join department d.id on e.department_id
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                department.id = row['id']
                department.budget = row['budget']
                employee.department = row['department']

                all_departments.append(department)

    template = 'departments/departments_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)