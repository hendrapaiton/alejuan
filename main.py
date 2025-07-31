from dataclasses import dataclass

import flet as ft


@dataclass
class AppState:
    count: int

    def increment(self):
        self.count += 1


def main(page: ft.Page):
    page.title = "Alergi Kemajuan | ALEJUAN"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 360
    page.window.height = 720
    page.window.resizable = False

    state = AppState(count=0)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=state.increment
    )
    page.add(
        ft.ControlBuilder(
            state,
            lambda state: ft.SafeArea(
                ft.Container(
                    ft.Text(value=f"{state.count}", size=50),
                    alignment=ft.Alignment.CENTER,
                ),
                expand=True,
            ),
            expand=True,
        )
    )


ft.run(main)
