from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load('models/current/nlu_model')

print(interpreter.parse("Yes please! Can you tell me how do I get to the venue?"))


