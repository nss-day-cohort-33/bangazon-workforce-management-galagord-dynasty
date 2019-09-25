import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Computer
from ..connection import Connection


def get_computer(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.manufacturer,
            c.model,
            c.purchase_date,
            c.decommission_date,
            e.first_name,
            e.last_name
        from hrapp_employeecomputer ec
        join hrapp_computer c on c.id = ec.computer_id
        join hrapp_employee e on e.id = ec.employee_id;
        WHERE c.id = ?
        """, (computer_id,))

        computer = []
        dataset = db_cursor.fetchone()

        for row in dataset:
            computer = Computer()
            computer.id = row['id']
            computer.manufacturer = row['manufacturer']
            computer.model = row['model']
            computer.purchase_date = row['purchase_date']
            computer.decommission_date = row['decommission_date']
            computer.first_name = row['first_name']
            computer.last_name = row['last_name']

            computer.append(computer)

    template = 'computers/computer_detail.html'
    context = {
        'computer': computer
    }

    return render(request, template, context)


def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)

        template = 'computers/detail.html'
        context = {
            'computer': computer
        }

        return render(request, template, context)