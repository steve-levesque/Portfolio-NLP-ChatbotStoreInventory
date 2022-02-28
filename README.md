<!-- Repo's Banner -->
![Portfolio-NLP-ChatbotStoreInventory](https://user-images.githubusercontent.com/42849270/155863780-d74b38db-afd6-4731-be15-b4f285d4446a.png)



<!-- Shield Badges -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- Description of the Project -->
## About


### Introduction
The Chatbot Store Inventory is a simple NLP project to demonstrate interaction with a user by the mean of natural language. It can be for simple discussion, general information or to query the inventory count of a specific article from a database.

### Model
The model explaination will be detailed in a Kaggle Notebook to make it possible to run fast and efficiently.

Kaggle Notebook link : TODO

But, in a very simple matter, the chatbot is based on two models to assist in a logic accuracy.

First, the model 1 is a neural network with tensorflow that has been feeded augmented data by the mean of stemming and vectorization (lancaster + bag of words respectively).

After, the model 2 is a HuggingFace distilbert transformer, which is very simple to add in a project and use (without training) with the intent to query more specificaly the inventory with question-answering type of formula (instead of a similarity type of check like model 1).

The tradeoffs of why the 2 models works fine in alternance is discussed in the notebook.

![image](https://user-images.githubusercontent.com/42849270/156004629-e2614582-588c-44b6-9823-4109e6e597a1.png)



<!-- Repo's Content Tree -->
## Directories and Files
<details open>
  <summary><b>Project's Tree</b></summary>
    
  ``` bash
    |- data                   # Intents data, pickle file, sql database, etc.
    |- docs                   # Useful documents.
    |- models                 # All models for the chatbot.
    |- utils                  # Contains all utilities for the website and chatbot. (i.e. stemming, vectorization, dataset, text_processing, etc.)
    |- .gitignore             #
    |- LICENSE                #
    |- README.md              # This file
    |- app.py                 # Website logic and entry-points. (CRUD and chatbot chatting)
    |- main_train.py          # Logic to train the model. (stemming, vectorization and tensorflow NN)
    |- requirements.txt       # Contains all necessary modules.
  ```
</details>


<!-- Getting Started -->
## Installation
For this project to work, some programs needs to be installed with the required Python libraries:
- Python 3.x (i.e. and all modules in requirements.txt)
- A web browser.

``` bash
pip install -r requirements.txt
```


## How to Execute

- Executing the venv (virtual environment), in windows with the commands in the /docs folder, or automatically with PyCharm.

- Running the main_train.py file, which is not necessay with all included data, but is recommended to see if everything works.

- Running the flask application with the IDE or "flask run" to start using the CRUD and chatbot.

![image](https://user-images.githubusercontent.com/42849270/156001703-b1457d88-6fd1-4bd1-8790-5f3a691c3bdf.png)



<!-- Contribution -->
## Contribution

Contributions are always welcome, thank you for you time. Here are the steps to do so.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/MyContribution`)
3. Commit your Changes (`git commit -m 'Add MyContribution'`)
4. Push to the Branch (`git push origin feature/MyContribution`)
5. Open a Pull Request



<!-- License -->
## License

See the `LICENSE` file at the root of the project directory for more information.



<!-- Acknowlegements and Sources -->
## Acknowlegements and Sources

Sources :

- https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077

- https://www.tensorflow.org/guide/migrate

- https://huggingface.co/distilbert-base-uncased-distilled-squad

- https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-fr



<!-- md links & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/steve-levesque/Portfolio-NLP-ChatbotStoreInventory.svg?style=for-the-badge
[contributors-url]: https://github.com/steve-levesque/Portfolio-NLP-ChatbotStoreInventory/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/steve-levesque/Portfolio-NLP-ChatbotStoreInventory.svg?style=for-the-badge
[forks-url]: https://github.com/steve-levesque/Portfolio-NLP-ChatbotStoreInventory/network/members
[stars-shield]: https://img.shields.io/github/stars/steve-levesque/Portfolio-NLP-ChatbotStoreInventory.svg?style=for-the-badge
[stars-url]: https://github.com/steve-levesque/Portfolio-NLP-ChatbotStoreInventory/stargazers
[issues-shield]: https://img.shields.io/github/issues/steve-levesque/Portfolio-NLP-ChatbotStoreInventory.svg?style=for-the-badge
[issues-url]: https://github.com/steve-levesque/Portfolio-NLP-ChatbotStoreInventory/issues
[license-shield]: https://img.shields.io/github/license/steve-levesque/Portfolio-NLP-ChatbotStoreInventory.svg?style=for-the-badge
[license-url]: https://github.com/steve-levesque/Portfolio-NLP-ChatbotStoreInventory/blob/main/LICENSE
