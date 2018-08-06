# How to handle multiple intents per input using Rasa NLU TensorFlow pipeline

In release 0.12, Rasa introduced a new TensorFlow-based pipeline for NLU models. This repository contains the code for a tutorial on how to use this pipeline to handle multiple intents per input. You can find a step-by-step tutorial on how to use this code [here](https://blog.rasa.com/how-to-handle-multiple-intents-per-input-using-rasa-nlu-tensorflow-pipeline/). The result of this tutorial is a chatbot which can recommend the meetups to attend in Berlin. The example conversation is:

```text
User: Hello
Bot: Hey, how can I help you?
User: I am new to Berlin and I would like to join some meetups. Any suggestions?
Bot: Rasa Bots Berlin meetup is definitely worth checking out! They are having an event today at Behrenstraße 42. Would you like to join?
User: Sure! Can you also tell me how can I get to the venue?
Bot: Great, just made an RSVP for you. 
Bot: The venue is close to the Berlin Friedrichstraße station, so the best option is to catch a U-Bahn U6.
User: Thanks a lot. Talk to you later.
Bot: Glad I could help!
Bot: Talk to you later! 
```

In order to keep the main focus on the usage of the new pipeline and to ensure that the tutorial is fully reproducible, we didn't use any custom actions or APIs here. Instead, we would like to encourage you to take this code, build things on top of it and keep us posted on how it goes!


## Versions of the software used in this tutorial:

* Python 3.6  
* Rasa NLU 0.12.3  
* Rasa Core 0.9.6  

## How to use this repository:
1. Clone or download the repository and install Rasa NLU and Rasa Core:
```
pip install -r requirements.txt
```
2. Follow a step-by-step tutorial [here](https://blog.rasa.com/how-to-handle-multiple-intents-per-input-using-rasa-nlu-tensorflow-pipeline/).
3. At any time you can load the chatbot and test it on your local machine:
```
python -m rasa_core.run -d models/current/dialogue -u models/current/nlu_model
```


## Useful resources:
* [Rasa NLU installation](https://nlu.rasa.com/installation.html) - guidelines on how to install Rasa NLU.
* [Rasa Core installation](https://core.rasa.com/installation.html) - guidelines on how to install Rasa Core.
* [Supervised Word Vectors from Scratch in Rasa NLU](https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8) - Rasa blog post on the new TensorFlow pipeline.
* [Docs: Processing Pipeline](https://nlu.rasa.com/pipeline.html) - Official Rasa documentation on processing pipelines.
* [Rasa Community Forum](https://forum.rasa.com) - A place where the Rasa community meets.

