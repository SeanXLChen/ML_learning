'''
Author: Runjie Lyu

This file contains a generate_menu function.
'''

from streamlit_antd_components import MenuItem


def generate_menu(menu_options):
    """
    Generates a list of MenuItem objects based on the given menu_options.

    Parameters:
        menu_options (list): A list of menu options (strings).

    Returns:
        list: A list of MenuItem objects.
    """
    menu_items = list(map(lambda option: MenuItem(option), menu_options))

    return menu_items