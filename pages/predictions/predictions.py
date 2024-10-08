from taipy.gui import Markdown, notify
import datetime as dt


selected_data_node = None
selected_scenario = None
selected_date = None
results = {"Date": [dt.datetime(2020,10,1)], "Deaths": [0], "ARIMA": [0], "Linear Regression": [0]}


def get_result(scenario):
    if scenario is None or isinstance(scenario, str) or not scenario.result.is_ready_for_reading:
        return results
    return scenario.result.read()


def on_submission_change(state, submitable, details):
    if details['submission_status'] == 'COMPLETED':
        state.results = get_result(state.selected_scenario)
        notify(state, "success", "Predictions ready!")
        print("Predictions ready!")
    elif details['submission_status'] == 'FAILED':
        notify(state, "error", "Submission failed!")
        print("Submission failed!")


def on_change_params(state):
    if state.selected_date.year < 2020 or state.selected_date.year > 2021:
        notify(state, "error", "Invalid date! Must be between 2020 and 2021")
        state.selected_date = dt.datetime(2020,10,1)
        return
    
    state.selected_scenario.date.write(state.selected_date.replace(tzinfo=None))
    state.selected_scenario.country.write(state.selected_country)
    notify(state, "success", "Scenario parameters changed!")

    state['Country'].on_change_country(state)


def on_change(state, var_name, var_value):
    if var_name == 'selected_scenario' and var_value:
        state.selected_date = state.selected_scenario.date.read()
        state.selected_country = state.selected_scenario.country.read()
        state.results = get_result(state.selected_scenario)


predictions_md = Markdown("pages/predictions/predictions.md")