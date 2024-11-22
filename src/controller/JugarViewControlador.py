import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.JugarView import JugarView
from .CanchaViewControlador import CanchaController


class JugarController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = JugarView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__cancha = CanchaController(pygame.display.set_mode((ANCHO, ALTO)))
        self.__formacion_actual = FORMACION_PREDETERMINADA
        self.__comienza_partida = False

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):  # Boton del Dado
                    self.__comienza_partida = True
                elif botones[1].checkForInput(mouse_pos):  # Boton Comenzar Partia
                    if self.__comienza_partida:
                        self.__cancha.main_loop()
                elif botones[2].checkForInput(mouse_pos):  # Boton Back
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                elif botones[3].checkForInput(mouse_pos) or botones[4].checkForInput(
                    mouse_pos
                ):  # flechas para cambiar formacion
                    if self.__formacion_actual == "4-4-2":
                        self.__formacion_actual = "4-3-3"
                    else:
                        self.__formacion_actual = "4-4-2"
                    self._view.texto_formacion(self.__formacion_actual)
        clock.tick(FPS)
        pygame.display.update()

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._view.mostrar()  # Mostrar el menú
            self._view.dibujar_formaciones(
                self._view._pantalla, FORMACIONES, self.__formacion_actual
            )
            self._view.texto_formacion(self.__formacion_actual)
            eventos = pygame.event.get()  # Manejar eventos
            self.manejar_eventos(eventos, mouse_pos)
            clock.tick(60)
            pygame.display.update()
