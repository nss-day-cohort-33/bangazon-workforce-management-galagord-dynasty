import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Computer, Employee
from ..connection import Connection

def create_computer(cursor, row):
    _row = sqlite3.Row(cursor, row)

    computer = Computer()
    computer.id = _row['id']
    computer.manufacturer = _row['manufacturer']
    computer.model = _row['model']
    computer.purchase_date = _row['purchase_date']
    computer.decommission_date = _row['decommission_date']

    # employee = Employee()
    # employee.id = _row['id']
    # employee.first_name = _row['first_name']
    # employee.last_name = _row['last_name']

    # computer.employee = employee

    return computer


def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_computer
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.manufacturer,
            c.model,
            c.purchase_date,
            c.decommission_date
        from hrapp_computer c
        WHERE c.id = ?
        """, (computer_id,))

    return db_cursor.fetchone()


def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)

        template = 'computers/computer_detail.html'
        context = {
            'computer': computer
        }

        return render(request, template, context)