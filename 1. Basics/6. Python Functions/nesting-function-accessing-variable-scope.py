def display_message(message):
    """Hello"""

    def message_sender():
        """Nested Function"""
        print(message)

    message_sender()


display_message("Be strong!")
