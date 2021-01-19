TOKEN = ""

# STATES
STATES = {"INITIAL": "initial",
          "LOADING": "loading",
          "PREDICT": "predict",
          "RESULTS": "result",
          "HELP": "help",
          "ERROR": "error",
          "NO_IMAGE": "no_image"}

# MESSAGES
WELCOME_MESSAGE = "This is a face mask detection bot.\n" \
                  "\nIt can predict if a person is wearing a mask or not." \
                  "\n" \
                  "\nEnter your image to start predicting!"

# Help Messages
HELP_MESSAGES = {"initial": "HELP: Enter '/start' to initiate the bot.",
                 "loading": "HELP: Load an image to predict."}

# Error Messages
ERROR_MESSAGES = {"error": "ERROR: Unknown command, enter 'help' for more information.",
                  "no_image": "ERROR: Load your image."}

# Model Path
BEST_MODEL_PATH = "./models/best_model.pt"
