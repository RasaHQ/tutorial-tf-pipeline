# How to handle multiple intents per input using Rasa NLU Tensorflow pipeline

In release 0.12, Rasa introduced a new Tensorflow-based pipeline for NLU models. This repository contains the code for a tutorial on how to use this pipeline to handle multiple intents per input. You can find a detailed walkthrough through the code here. The result of this tutorial is a very simple chatbot which can recommend the meetups to attend in Berlin. The example conversation is:

```text
U: Hello
B: Hello! How can I help you?
U: I have just moved to Berlin. Can you recommend any great meetups to attend here?
B: Rasa Bots Berlin meetup is definitely worth checking out! Would you like to join and attend the nearest meetup on 15th of July?
U: Yes, sure! Can you also tell me what is the best way to get to the venue?
B: Great, I have just booked a spot for you and  I will send you a reminder the day before. The venue is next to the Alexanderplatz so you can take a U-Bahn U2.
U: Thank you very much! Talk to you later.
B: You are very welcome. Goodbye!
```

In order to keep the main focus on the usage of the new pipeline and to ensure that the tutorial is fully reproducible, we didn't use any custom actions or APIs here. Instead, we would like to encourage you to take this code, build things on top of it and keep us posted on how it goes!


## Versions of the software used in this tutorial:

* Python 3.6  
* Rasa NLU 0.12.3  
* Rasa Core 0.9.3  



## Useful resources:
* [Rasa NLU installation](https://nlu.rasa.com/installation.html) - guidelines on how to install Rasa NLU.
* [Rasa Core installation](https://core.rasa.com/installation.html) - guidelines on how to install Rasa Core.
* [Supervised Word Vectors from Scratch in Rasa NLU](https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8) - Rasa blogpost on the new Tensorflow pipeline.
* [Docs: Preprocessing Pipeline](https://nlu.rasa.com/pipeline.html) - Official Rasa documentation on preprocessing pipelines.
* [RasaNLU Gitter](https://gitter.im/RasaHQ/rasa_nlu) and [RasaCore Gitter](https://gitter.im/RasaHQ/rasa_core) - Places where Rasa community hangs out.

