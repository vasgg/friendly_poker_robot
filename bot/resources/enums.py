from enum import Enum

from aiogram.filters.state import State, StatesGroup


class States(StatesGroup):
    MISSING_PLAYSERS = State()
    ENTER_REMAINING_BALANCE = State()
    ADD_ADMIN = State()
    DELETE_ADMIN = State()


class GameStatus(Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    ABORTED = "aborted"


class SlideType(Enum):
    TEXT = "text"
    IMAGE = "image"
    SMALL_STICKER = "small_sticker"
    BIG_STICKER = "big_sticker"
    PIN_DICT = "pin_dict"
    QUIZ_OPTIONS = "quiz_options"
    QUIZ_INPUT_WORD = "quiz_input_word"
    QUIZ_INPUT_PHRASE = "quiz_input_phrase"
    FINAL_SLIDE = "final_slide"


class LessonLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class KeyboardType(Enum):
    FURTHER = "further"
    QUIZ = "quiz"


class UserLessonProgress(Enum):
    NO_PROGRESS = "no_progress"
    IN_PROGRESS = "in_progress"


class SessionStartsFrom(Enum):
    BEGIN = "begin"
    EXAM = "exam"
