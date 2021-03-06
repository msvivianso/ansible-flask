from flask.ext.wtf import Form
from wtforms import TextField, FormField, FieldList, SubmitField, Field, BooleanField
from wtforms.validators import Required, ValidationError, Optional
from wtforms.widgets import TableWidget, HTMLString, Input
from wtforms_alchemy import model_form_factory, ModelFieldList
from app.models import Server, Variable

ModelForm = model_form_factory(Form)


class VariableForm(ModelForm):
    class Meta:
        model = Variable


class ServerForm(ModelForm):
    class Meta:
        model = Server

    variables = ModelFieldList(FormField(VariableForm, widget=TableWidget(with_table_tag=False)), min_entries=1)
    create_server = SubmitField('Create Server')
    add_variable = SubmitField('Add Variable')
    delete_variable = SubmitField('Remove Variable')
