# Fletle-Wordle

Fletle is written in python using Flet framework and it's basically a copy of [Wordle game](https://wordlegame.org/).
The rules are very simple: You need to guess the hidden word (5 letters) in 5 tries. To get started, just type any word on the text filed. If the letter is guessed correctly and is in the correct place, it will be highlighted in green, if the letter is in the word, but in the wrong place - in yellow, and if the letter is not in the word, it will remain red

## Screenshots

<img width="789" alt="Screenshot 2022-08-03 at 21 11 32" src="https://user-images.githubusercontent.com/50675404/182696878-a3ae8000-0e1f-42a9-89fc-683045103d48.png">

<img width="787" alt="Screenshot 2022-08-03 at 21 09 43" src="https://user-images.githubusercontent.com/50675404/182696814-64c10b09-83ca-4f31-9262-37d02a1c335f.png">

<img width="793" alt="Screenshot 2022-08-03 at 21 11 16" src="https://user-images.githubusercontent.com/50675404/182696939-ebdc6977-af6c-4013-87a9-cbd79bc39691.png">

## Run Locally

Clone the project

```bash
  git clone https://github.com/niewiemczego/Fletle-Wordle
```

Install requirement packages

```bash
  pip install -r requirements.txt
```

Run the code

```bash
  python fletle.py
```

## Adding more words

```python
line 33: add to list as many words as u want.
Keep in mind that words should be 5 characters long
```
