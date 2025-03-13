from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import logging

logger = logging.getLogger(__name__)

class ActionCheckFever(Action):
    def name(self) -> Text:
        return "action_check_fever"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve body temperature entity or slot
        temperature = next(tracker.get_latest_entity_values("body_temperature"), None) or tracker.get_slot("body_temperature")

        if temperature:
            try:
                # Convert to float for better accuracy
                temp_value = float(temperature)

                # Store the value in a slot
                return_value = [SlotSet("body_temperature", temp_value)]

                if temp_value >= 100.4:
                    dispatcher.utter_message(text="You have a fever. Take paracetamol 500mg and rest for one hour. If symptoms persist, visit the hospital.")
                elif temp_value >= 95:  # Normal range
                    dispatcher.utter_message(text="Your temperature is normal. It might be due to climate changes or minor fluctuations.")
                else:
                    dispatcher.utter_message(text="Your temperature seems too low. Please check if the reading is correct or consult a doctor.")

            except ValueError:
                dispatcher.utter_message(text="Please provide a valid numeric temperature reading.")
                return_value = []

        else:
            dispatcher.utter_message(text="Can you please provide your body temperature?")
            return_value = []

        return return_value

class ActionShowHospital(Action):
    def name(self) -> Text:
        return "action_show_hospital"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here is the nearest hospital location: [Hospital Location]. You can book an appointment if needed.")
        return []
