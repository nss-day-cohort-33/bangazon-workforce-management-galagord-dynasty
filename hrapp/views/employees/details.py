import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Employee, Department
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                d.department,
                e.department_id
            from hrapp_employee e
            join hrapp_department d on e.department_id = d.id
            where e.id = ?
            """, (employee_id,))

        
        dataset = db_cursor.fetchone()

    

        
        

        return dataset



def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/details.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)