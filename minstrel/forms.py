
import pickle

from mingus.core import keys
from mingus.containers.instrument import MidiInstrument
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Div, Fieldset, HTML, Submit,
                                 MultiWidgetField)
from crispy_forms.bootstrap import FormActions

from popgen.composition import DEFAULT_PARAMETERS


class ProgressionWidget(forms.widgets.MultiWidget):
    def __init__(self, count, attrs=None):
        self.count = count
        widgets = [forms.NumberInput()] * count
        super(ProgressionWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return pickle.loads(value)
        else:
            return [0.0] * self.count


class ProgressionField(forms.fields.MultiValueField):

    def __init__(self, count, *args, **kwargs):
        self.widget = ProgressionWidget(count, attrs={'step': 0.01})
        self.count = count
        list_fields = [
            forms.FloatField(min_value=0., max_value=999.)
        ] * count
        if kwargs.get('initial'):
            kwargs['initial'] = pickle.dumps(kwargs.get('initial'))

        super(ProgressionField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        return pickle.dumps(values)


class DynamicField(forms.fields.MultiValueField):

    def __init__(self, count, *args, **kwargs):
        self.widget = ProgressionWidget(count)
        self.count = count
        list_fields = [
            forms.IntegerField(min_value=0, max_value=999)
        ] * count
        if kwargs.get('initial'):
            kwargs['initial'] = pickle.dumps(kwargs.get('initial'))

        super(DynamicField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        return pickle.dumps(values)


def ProgressionTitle(*titles):
    tag_titles = [HTML("""
        <div class='col-sm-2 progression-title' style="width: %s%%;">
        <label>%s</label>
    </div>""" % (100. / len(titles), title)) for title in titles]
    return Div(
        Div(
            css_class='col-sm-2 progression-label',
        ),
        Div(
            *tag_titles,
            **dict(css_class='row col-sm-10')
        ),
        css_class='row progression-fields',
    )


def DynamicFields(title, field, count):
    return Div(
        MultiWidgetField(
            field,
            attrs=(
                {
                    'class': "col-sm-2",
                    'style': "width: %s%%; " % (100. / count)
                }
            )
        ),
        # css_class='row col-sm-10'
        # css_class='row progression-fields',
    )


def ProgressionFields(title, field, count):
    return Div(
        Div(
            HTML("<label clas='text-right'>%s</label>" % title),
            css_class='col-sm-2 progression-label',
        ),
        Div(
            MultiWidgetField(
                field,
                attrs=(
                    {
                        'class': "col-sm-2",
                        'style': "width: %s%%;" % (100. / count)
                    }
                )
            ),
            css_class='row col-sm-10'
        ),
        css_class='row progression-fields',
    )

# TODO fix bemol
keys = [(key, key) for key in (keys.major_keys + keys.minor_keys)
        if not key.endswith('b')]
instruments = zip(MidiInstrument.names, MidiInstrument.names)


class MinstrelForm(forms.Form):
    # Tempo Field
    tempo_lower = forms.IntegerField(
        min_value=1, max_value=999,
        initial=DEFAULT_PARAMETERS['tempo']['lower']
    )
    tempo_upper = forms.IntegerField(
        min_value=1, max_value=999,
        initial=DEFAULT_PARAMETERS['tempo']['upper']
    )
    tempo_fixed = forms.IntegerField(
        min_value=1, max_value=999,
        required=False
    )

    key = forms.ChoiceField(choices=keys, initial=DEFAULT_PARAMETERS['key'])
    harmony_markov_chain_I = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][0]
    )
    harmony_markov_chain_II = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][1]
    )
    harmony_markov_chain_III = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][2]
    )
    harmony_markov_chain_IV = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][3]
    )
    harmony_markov_chain_V = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][4]
    )
    harmony_markov_chain_VI = ProgressionField(
        6,
        initial=DEFAULT_PARAMETERS['harmony']['markov_chain'][5]
    )

    melody_power = forms.FloatField(
        initial=DEFAULT_PARAMETERS['melody']['power']
    )
    melody_preferred_center = forms.IntegerField(
        min_value=1, max_value=9,
        initial=DEFAULT_PARAMETERS['melody']['preferred_range']['center']
    )
    melody_preferred_lower = forms.IntegerField(
        min_value=1, max_value=100,
        initial=DEFAULT_PARAMETERS['melody']['preferred_range']['lower_offset']
    )
    melody_preferred_upper = forms.IntegerField(
        min_value=1, max_value=100,
        initial=DEFAULT_PARAMETERS['melody']['preferred_range']['upper_offset']
    )
    melody_maximum_lower = forms.IntegerField(
        min_value=1, max_value=100,
        initial=DEFAULT_PARAMETERS['melody']['maximum_range']['lower_offset']
    )
    melody_maximum_upper = forms.IntegerField(
        min_value=1, max_value=100,
        initial=DEFAULT_PARAMETERS['melody']['maximum_range']['upper_offset']
    )
    melody_inner_drop_off = forms.FloatField(
        initial=DEFAULT_PARAMETERS['melody']['inner_drop_off']
    )
    melody_outer_drop_off = forms.FloatField(
        initial=DEFAULT_PARAMETERS['melody']['outer_drop_off']
    )

    melody_harmonic_compilance_I = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][0]
    )
    melody_harmonic_compilance_II = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][1]
    )
    melody_harmonic_compilance_III = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][2]
    )
    melody_harmonic_compilance_IV = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][3]
    )
    melody_harmonic_compilance_V = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][4]
    )
    melody_harmonic_compilance_VI = ProgressionField(
        7,
        initial=DEFAULT_PARAMETERS['melody']['harmonic_compilance'][5]
    )

    melody_dynamics = DynamicField(
        16,
        initial=DEFAULT_PARAMETERS['melody']['dynamics']
    )

    instruments_melody = forms.ChoiceField(
        choices=instruments,
        initial=DEFAULT_PARAMETERS['instruments']['melody']
    )
    instruments_chord = forms.ChoiceField(
        choices=instruments,
        initial=DEFAULT_PARAMETERS['instruments']['chord']
    )
    instruments_bass = forms.ChoiceField(
        choices=instruments,
        initial=DEFAULT_PARAMETERS['instruments']['bass']
    )

    def __init__(self, *args, **kwargs):
        super(MinstrelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Melody Tables',
                DynamicFields('Dynamic', 'melody_dynamics', 16),
                ProgressionTitle('I', 'II', 'III', 'IV', 'V', 'VI', 'VII'),
                ProgressionFields('I', 'melody_harmonic_compilance_I', 7),
                ProgressionFields('II', 'melody_harmonic_compilance_II', 7),
                ProgressionFields('III', 'melody_harmonic_compilance_III', 7),
                ProgressionFields('IV', 'melody_harmonic_compilance_IV', 7),
                ProgressionFields('V', 'melody_harmonic_compilance_V', 7),
                ProgressionFields('VI', 'melody_harmonic_compilance_VI', 7),
                css_class='col-sm-6',
            ),
            Fieldset(
                'Harmony',
                'key',
                ProgressionTitle('I', 'II', 'III', 'IV', 'V', 'VI'),
                ProgressionFields('I', 'harmony_markov_chain_I', 6),
                ProgressionFields('II', 'harmony_markov_chain_II', 6),
                ProgressionFields('III', 'harmony_markov_chain_III', 6),
                ProgressionFields('IV', 'harmony_markov_chain_IV', 6),
                ProgressionFields('V', 'harmony_markov_chain_V', 6),
                ProgressionFields('VI', 'harmony_markov_chain_VI', 6),
                css_class='col-sm-6',
            ),
            Fieldset(
                'Tempo',
                'tempo_fixed',
                'tempo_lower',
                'tempo_upper',
                css_class='col-sm-6',
            ),
            Fieldset(
                'Instruments',
                'instruments_melody',
                'instruments_chord',
                'instruments_bass',
                css_class='col-sm-6',
            ),
            Fieldset(
                'Melody Params',
                Div(
                    'melody_power',
                    'melody_preferred_center',
                    'melody_preferred_lower',
                    'melody_preferred_upper',
                    css_class='col-sm-6',
                ),
                Div(
                    'melody_maximum_lower',
                    'melody_maximum_upper',
                    'melody_inner_drop_off',
                    'melody_outer_drop_off',
                    css_class='col-sm-6',
                ),
                css_class='col-sm-12 whole',
            ),
            FormActions(
                Submit('play', "Play", css_class="btn btn-success"),
                Submit('random', 'Random', css_class="btn btn-info"),
                Submit('happy', 'Happy', css_class="btn btn-success"),
                Submit('angry', 'Angry', css_class="btn btn-danger"),
                Submit('sad', 'Sad', css_class="btn btn-primary"),
                Submit('tender', 'Tender', css_class="btn btn-warning"),
                css_class='col-sm-12',
            ),
        )
