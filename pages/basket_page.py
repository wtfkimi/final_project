from .base_page import BasePage
from final_project.locators import MainPageLocators
from final_project.locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        # Гость открывает главную страницу
        # Переходит в корзину по кнопке в шапке сайта
        # Ожидает, что есть текст 'корзина пуста'
        self.click(*MainPageLocators.BASKET)
        busket_message = self.get_text(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert self.some_in_something('empty', busket_message), 'Element not in something'


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        # Гость открывает страницу товара
        # Переходит в корзину по кнопке в шапке сайта
        # Ожидает, что в корзине нет товаров
        # Ожидает, что есть текст 'корзина пуста'
        self.click(*MainPageLocators.BASKET)
        busket_message = self.get_text(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert self.some_in_something('empty', busket_message)