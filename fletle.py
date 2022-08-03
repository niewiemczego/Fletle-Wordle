
import random

import flet
from flet import (Column, Container, ElevatedButton, Page, Row, Text,
                  TextField, UserControl, alignment, colors, icons, padding)


class Board(UserControl):
    def build(self) -> None:
        """
        It creates a 5x5 grid of blue-grey squares
        :return: A Column - our board with 5 Rows, each with 5 Containers.
        """
        board = Column()
        for _ in range(5):
            row = Row()
            for _ in range(5):
                row.controls.append(
                    Container(
                        width=75,
                        height=75,
                        bgcolor=colors.BLUE_GREY_200,
                        alignment=alignment.center
                    )
                )
            board.controls.append(row)
        return board

class Fletle:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.words = ["Johny", "Smith", "Jolie"]
        self.setup_page()
        self.game()

    def setup_page(self) -> None:
        """
        > The function sets the page title, theme mode, vertical and horizontal alignment, and padding
        """
        self.page.title = "Fletle"
        self.page.theme_mode = "dark"
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"
        self.page.padding = 15
        self.page.update()

    def get_word_chars(self) -> dict[str, int]:
        """
        Counts each char in daily_word and returns a dictionary with the char as key and the count as value.
        """
        chars = {}
        for char in self.daily_word:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        return chars

    def has_lifes(self) -> bool:
        return self.tries < 5

    def is_char_left(self, chars: dict, char: str) -> bool:
        """
        It checks if there is char left in the dictionary.
        """
        return chars.get(char, 0) > 0

    def check_word(self, e) -> None:
        """
        The function checks if the current word is the same as the daily word, if it is, the user wins,
        if not, the user loses.
        """
        current_word = e.control.value.lower()
        if len(self.daily_word) != len(current_word):
            return
        current_row: Row = self.board.controls[0].controls[self.tries]  # row contains 5 blue_grey containers
        word_chars = self.get_word_chars()
        for idx, char in enumerate(current_word):  # iterate over the chars in the current word
            if self.daily_word.find(char) == idx:  # check if the char is in the right position
                if not self.is_char_left(word_chars, char):  # checks if the char is left in the dictionary
                    current_row.controls[idx].bgcolor = colors.RED_200
                else:
                    current_row.controls[idx].bgcolor = colors.GREEN_200
                    word_chars[char] -= 1
            elif self.daily_word.find(char) == -1:  # .find(char) returns -1 if the char is not in the word
                current_row.controls[idx].bgcolor = colors.RED_200
            elif self.daily_word.find(char) != idx:
                if not self.is_char_left(word_chars, char):
                    current_row.controls[idx].bgcolor = colors.RED_200
                else:
                    current_row.controls[idx].bgcolor = colors.YELLOW_200
                    word_chars[char] -= 1
            # update the containter with the char
            current_row.controls[idx].content = Text(
                value=char.upper(), 
                size=25, 
                weight="bold"
            )
            current_row.update()
        self.tries += 1
        if self.daily_word == current_word:
            self.game_msg.content.value = f"You win in {self.tries} tries!"
            self.game_msg.update()
            self.txt_field.value = ""
            self.txt_field.disabled = True
            self.txt_field.update()
        elif not self.has_lifes():
            self.game_msg.content.value = f"The word was {self.daily_word}."
            self.game_msg.update()
            self.txt_field.value = ""
            self.txt_field.disabled = True
            self.txt_field.update()

    def reset_game(self, e) -> None:
        self.page.clean()
        self.page.update()
        return self.game()

    def game(self) -> None:
        self.tries = 0
        self.daily_word = random.choice(self.words).lower()
        self.board = Board()
        self.txt_field = TextField(
            label="Guess the word...", 
            icon=icons.SEARCH, 
            text_align="center", 
            on_submit=self.check_word
        )
        self.game_msg = Container(
            content=Text(
                size=20, 
                weight="bold"
            ),
            alignment=alignment.center,
            padding=padding.symmetric(
                vertical=25, 
                horizontal=5
            )
        )
        self.reset_btn = Container(
            content=ElevatedButton(
                text="Reset Game", 
                color="white", 
                bgcolor=colors.BLUE_GREY_200, 
                on_click=self.reset_game
            ),
            alignment=alignment.center,
            padding=padding.symmetric(
                vertical=25, 
                horizontal=5
            )
        )
        self.page.add(
            Row(
                controls=[
                    self.board, 
                    Column(
                        controls=[
                            self.game_msg,
                            self.txt_field,
                            self.reset_btn 
                        ],
                        horizontal_alignment="center"
                    )
                ],
            )
        )

if __name__ == "__main__":
    flet.app(name="Fletle", target=Fletle)
