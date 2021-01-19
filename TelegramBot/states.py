"""
    initial state:
        Display the welcome message at the start ===change state===> LOADING

    loading state:
        Load the img ===change state===> PREDICT ===ELSE===> return to the initial state and display the error message.

    predict state:
        run the two models to give some predictions ===change state===> RESULTS

    results state:
        print the results ===change state===> INITIAL

    GENERAL:
        Display the error message for unknown command
        Display the help message when requested
"""

from utils import *
from PIL import Image
from io import BytesIO
from imagePreprocessing import preprocessing


def initial(bot, chat_id):
    bot.send_message(chat_id, WELCOME_MESSAGE)

    return STATES["LOADING"]


def loading(bot, chat_id, file_id):
    bot.send_message(chat_id, "Please Wait......")

    img_name = bot.get_file_path(file_id)
    img = bot.load_image(img_name)
    img = Image.open(BytesIO(img))

    return STATES["PREDICT"], img


def predict(img, model):
    # Process the image for training
    pre_image = preprocessing(img)

    # Generate sklearn prediction
    output = model.predict(pre_image)
    pred = "With Mask" if output == 0 else "Without Mask"

    return STATES["RESULTS"], pred


def results(bot, chat_id, result):
    message = f"The Model Prediction is = {result}"
    print(message)
    bot.send_message(chat_id, message)

    return STATES["LOADING"]


def help(bot, chat_id, help):
    bot.send_message(chat_id, HELP_MESSAGES[help])


def error(bot, chat_id, error):
    bot.send_message(chat_id, ERROR_MESSAGES[error])
