# How to handle multiple intents per input using Rasa NLU Tensorflow pipeline

Back in April, Rasa released a new Tensorflow-based pipeline for NLU models. This repository contains the code for our tutorial on how to use this pipeline to handle multiple intents per input. You can find a detail walkthrough thourhg the code here. The result of this tutorial is a very simple chatbot which can recommend the meetups to attend in Berlin. The example conversation is:

> U: Hello<br/>
> B: Hello! How can I help you?<br/>
> U: I have just moved to Berlin. Can you recommend any great meetups to attend here?<br/>
> B: Rasa Bots Berlin meetup is definitely worth checking out! Would you like to join and attend the nearest meetup on 15th of July?<br/>
> U: Yes, sure! Can you also tell me what is the best way to get to the venue?<br/>
> B: Great, I have just booked a spot for you and  I will send you a reminder the day before. The venue is next to the Alexanderplatz so you can take a U-Bahn U2.<br/>
> U: Thank you very much! Talk to you later.<br/>
> B: You are very welcome. Goodbye!<br/>


In oder to keep the main focus on the usage of the new pipeline and to ensure that the tutorial is fully reproducible, we didn't use any custom actions or APIs here. Instead, we would like to encourage you to take this code, build things on top of it and keep us posted on how it goes!

Useful resources:
* [Supervised Word Vectors from Scratch in Rasa NLU](https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8) - Rasa blogpost on the new Tensorflow pipeline
* [Docs: Preprocessing Pipeline](https://nlu.rasa.com/pipeline.html) - Official Rasa documentation on preprocessing pipelines.
* [RasaNLU Gitter](https://gitter.im/RasaHQ/rasa_nlu) and [RasaCore Gitter](https://gitter.im/RasaHQ/rasa_core) - Places where Rasa community hangs out.

