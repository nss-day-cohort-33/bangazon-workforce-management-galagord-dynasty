import sqlite3
from datetime import datetime
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from hrapp.models import TrainingProgram
from ..connection import Connection


def training_programs_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                tp.id,
                tp.title,
                tp.description,
                tp.start_date,
				tp.end_date,
				tp.capacity
            from hrapp_trainingprogram tp
            """)

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.id = row['id']
                training_program.title = row['title']
                training_program.description = row['description']
                # training_program.start_date = row['start_date']
                training_program.start_date = datetime.strptime(row['start_date'], '%Y-%m-%d')
                training_program.end_date = row['end_date']
                training_program.capacity = row['capacity']

                today = datetime.today()

                # if (training_program.start_date > today):
                all_programs.append(training_program)

        template = 'training_programs/training_programs_list.html'
        context = {
            'programs': all_programs,
            'time': today
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
                title, description, start_date,
                end_date, capacity
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['description'],
                form_data['start_date'], form_data['end_date'],
                form_data["capacity"]))

        return redirect(reverse('hrapp:training_programs'))