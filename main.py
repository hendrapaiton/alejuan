import flet as ft
import time

def main(page: ft.Page):
    page.title = "Alergi Kemajuan | Chatbot"
    page.theme_mode = ft.ThemeMode.LIGHT

    chat_history = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    history_list = ft.ListView(
        expand=True,
        spacing=5,
        controls=[
            ft.Text("Obrolan 1", color=ft.Colors.BLACK87),
            ft.Text("Obrolan 2", color=ft.Colors.BLACK87),
            ft.Text("Obrolan 3", color=ft.Colors.BLACK87),
        ]
    )

    sidebar = ft.Container(
        content=ft.Column([
            ft.Text("Riwayat Obrolan", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
            ft.Divider(height=1, color=ft.Colors.BLACK26),
            history_list
        ]),
        width=200,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border=ft.Border.only(right=ft.border.BorderSide(1, ft.Colors.OUTLINE)),
    )

    def send_message_click(e):
        user_input_text = user_input.value
        if not user_input_text:
            return

        user_input.value = ""
        
        chat_history.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(user_input_text, color=ft.Colors.WHITE, selectable=True),
                        bgcolor=ft.Colors.BLUE_GREY_500,
                        padding=12,
                        border_radius=15,
                        margin=ft.Margin.only(left=60)
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
            )
        )
        page.update()

        time.sleep(0.5)

        bot_response_text = f"Anda berkata: '{user_input_text}'"
        
        chat_history.controls.append(
            ft.Row(
                [
                    ft.CircleAvatar(
                        content=ft.Icon(ft.Icons.SMART_TOY_OUTLINED),
                        bgcolor=ft.Colors.BLUE_100
                    ),
                    ft.Container(
                        content=ft.Text(bot_response_text, color=ft.Colors.BLACK, selectable=True),
                        bgcolor=ft.Colors.GREY_200,
                        padding=12,
                        border_radius=15,
                        margin=ft.Margin.only(right=60)
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            )
        )
        page.update()

    user_input = ft.TextField(
        hint_text="Ketik pesan Anda...",
        expand=True,
        on_submit=send_message_click,
        border_radius=20,
        border_color=ft.Colors.BLUE_GREY_300,
        autofocus=True,
    )

    send_button = ft.IconButton(
        icon=ft.Icons.SEND_ROUNDED,
        tooltip="Kirim Pesan",
        on_click=send_message_click,
        icon_color=ft.Colors.BLUE_GREY_500,
    )

    page.add(
        ft.Row(
            controls=[
                sidebar,
                ft.Column(
                    controls=[
                        ft.Container(
                            content=chat_history,
                            border=ft.Border.all(1, ft.Colors.OUTLINE),
                            border_radius=5,
                            padding=10,
                            expand=True,
                        ),
                        ft.Row(
                            controls=[user_input, send_button],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

ft.run(main)
