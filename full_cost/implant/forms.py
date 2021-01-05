from django.forms import IntegerField, DateInput, TimeInput, Textarea, NumberInput, Select, CharField, ModelChoiceField, TextInput
from .models import Record
from lab.models import Project, User, Extraction
from lab.forms import RecordForm as LRecordForm
from lab.forms import ExtractionForm as LExtractionForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Submit, Row, Column, Div, Reset, Layout, Button
from crispy_forms.bootstrap import FormActions

class RecordForm(LRecordForm):

    class Meta(LRecordForm.Meta):
        model = Record
        fields = ['date_from',
                  'date_to',
                  'time_from',
                  'sample_id',
                  'duration',
                  'user',
                  'wu',
                  'group', 'project', 'experiment', 'remark']

        labels = {'wu': 'WU:', 'date_from': 'starting at:', 'time_from': 'at:', 'duration': 'Duration in s:',
                  'date_to': 'to:', 'experiment': 'Experiment:', 'sample_id': 'Sample  ID:'
                  }

        help_texts = {'date_from': 'The starting date of your run',
                      'date_to': 'The end date of your run',
                      'duration': 'Enter the run duration in seconds',
                      'wu': 'Number of hours for the run calculated from the seconds and rounded to the tenth',
                      'sample_id': 'Unique identifier of your sample',
                      'experiment': 'Pick an experiment'
                      }

        widgets = {
            'date_from': DateInput(attrs={'type':'date', 'class': 'datepicker dfrom time'}),
            'date_to': DateInput(attrs={'type': 'date', 'class': 'datepicker dto time'}),
            'time_from': TimeInput(attrs={'type': 'time', 'class': 'timepicker tfrom time'}),
            'duration': NumberInput(attrs={'min':0, 'step':1, 'class': 'seconds'}),
            'remark': Textarea(attrs={'placeholder': 'Enter some detail here about your experiment',
                                       'rows': '1', 'cols' :'50'}),
            'experiment': Select(attrs={'class': 'experiment', }),
            'group': Select(attrs={'class': 'group', }),
            'project': Select(attrs={'class': 'project', }),
            'user': Select(attrs = {'placeholder': 'Surname Name', 'class': 'user'}),
            'wu': NumberInput(attrs = {'required': False, 'class': 'uo', 'value': 0, 'min': 0, 'step':0.5,'style': 'width:10ch'}),
        }
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.help_text_inline = False
        self.helper.form_class = 'form-horizontal formclass'
        self.helper.form_id = 'form_id'
        self.helper.form_tag = True
        self.helper.layout = Layout(
                Div(
                    Row(
                        Column('date_from', css_class='form-group col-md-6'),
                        Column('time_from', css_class='form-group col-md-6'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('duration', css_class='form-group col-md-6 gi-col durationcol'),
                        Column('date_to', css_class='form-group col-md-6 dtocol'),
                        css_class='form-row'
                    ),
                    Row(Column('sample_id', css_class='form-group col-md-6 gi-col'),
                        Column('wu', css_class='form-group col-md-6 uocol'),
                        css_class='form-row'
                    ),
                    Row(Column('experiment', css_class='form-group col-md-6 gi-col exp'),
                        css_class='form-row gi-row',
                        ),
                    Row(Column('project', css_class='form-group col-md-8'),
                        css_class='form-row',
                    ),
                    Row(
                        Column('user', css_class='form-group col-md-4'),
                        Column('user_text_name', css_class='form-group col-md-3 usercol'),
                        Column('user_text_surname', css_class='form-group col-md-3 usercol'),
                        Column('group', css_class='form-group col-md-2'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('remark', css_class='form-group mr-5'),
                        Column(FormActions(
                                        Button('okbutton', 'Submit', css_class='btn-primary okclass'), #form will be triggered using a popup jquery, see static/js/osp_records.js
                                        Reset('name', 'Reset', css_class='btn-secondary')
                                            ),css_class='form-group align-items-center')
                        ),
            )
        )

        super().__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                if 'class' in self.fields[field].widget.attrs:
                    self.fields[field].widget.attrs['class'] += ' has-popover'
                self.fields[field].widget.attrs.update(
                    {'data - toggle': 'popover',
                     'data-content': help_text, 'data-placement': 'right',
                     'data-container': 'body'})


