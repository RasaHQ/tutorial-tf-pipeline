from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load('models/current/nlu_model')

print(interpreter.parse("Yes, sounds good. Can you also tell me how to get to the venue?"))


