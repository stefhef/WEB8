from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader_id = IntegerField('ID лидера работы', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объём работы', validators=[DataRequired()])
    collaborations = StringField('Соработчики', validators=[DataRequired()])
    is_finished = BooleanField("Работа завершена?")
    submit = SubmitField('Отправить')
