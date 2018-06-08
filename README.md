# How to handle multiple intents per input using Rasa NLU Tensorflow pipeline

In release 0.12, Rasa introduced a new Tensorflow-based pipeline for NLU models. This repository contains the code for a tutorial on how to use this pipeline to handle multiple intents per input. You can find a detailed walkthrough through the code here. The result of this tutorial is a chatbot which can recommend the meetups to attend in Berlin. The example conversation is:

```text
User: Hello
Bot: Hey, how can I help you?
User: I am new to Berlin and I would like to join some meetups. Any suggestions?
Bot: Rasa Bots Berlin meetup is definitely worth checking out! They are having an event today at Behrenstraße 42. Would you like to join?
User: Sure! Can you also tell me how can I get to the venue?
Bot: Great, I have just booked a spot for you. The venue is close to the Berlin Friedrichstraße station, you can get there by catching U-Bahn U6.
User: Thanks a lot. Talk to you later.
Bot: You are very welcome. Goodbye!
```

In order to keep the main focus on the usage of the new pipeline and to ensure that the tutorial is fully reproducible, we didn't use any custom actions or APIs here. Instead, we would like to encourage you to take this code, build things on top of it and keep us posted on how it goes!

If you want to test the agent on your local machine, you can clone the repository and run the following command in the project directory:

```
python -m rasa_core.run -d models/current/dialogue -u models/current/nlu_model
```


## Versions of the software used in this tutorial:

* Python 3.6  
* Rasa NLU 0.12.3  
* Rasa Core 0.9.3  



## Useful resources:
* [Rasa NLU installation](https://nlu.rasa.com/installation.html) - guidelines on how to install Rasa NLU.
* [Rasa Core installation](https://core.rasa.com/installation.html) - guidelines on how to install Rasa Core.
* [Supervised Word Vectors from Scratch in Rasa NLU](https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8) - Rasa blogpost on the new Tensorflow pipeline.
* [Docs: Preprocessing Pipeline](https://nlu.rasa.com/pipeline.html) - Official Rasa documentation on preprocessing pipelines.
* [Rasa NLU Gitter](https://gitter.im/RasaHQ/rasa_nlu) and [Rasa Core Gitter](https://gitter.im/RasaHQ/rasa_core) - Places where Rasa community hangs out.

