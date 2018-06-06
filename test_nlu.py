from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load('models/current/nlu_model')

print(interpreter.parse("Sounds good. Can you tell me how I could get to the venue?"))


