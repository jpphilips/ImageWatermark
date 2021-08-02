import PySimpleGUI as sg


class Gui:

    FONTS = ['Abadi MT Condensed Light', 'Albertus Extra Bold', 'Albertus Medium', 'Antique Olive', 'Arial', 'Arial Black', 'Arial MT', 'Arial Narrow', 'Bazooka', 'Book Antiqua', 'Bookman Old Style', 'Boulder', 'Calisto MT', 'Calligrapher', 'Century Gothic', 'Century Schoolbook', 'Cezanne', 'CG Omega', 'CG Times', 'Charlesworth', 'Chaucer', 'Clarendon Condensed', 'Comic Sans MS', 'Copperplate Gothic Bold', 'Copperplate Gothic Light', 'Cornerstone', 'Coronet', 'Courier', 'Courier New', 'Cuckoo', 'Dauphin', 'Denmark', 'Fransiscan', 'Garamond', 'Geneva', 'Haettenschweiler', 'Heather', 'Helvetica', 'Herald', 'Impact', 'Jester', 'Letter Gothic', 'Lithograph', 'Lithograph Light', 'Long Island', 'Lucida Console', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Unicode', 'Marigold', 'Market', 'Matisse ITC', 'MS LineDraw', 'News GothicMT', 'OCR A Extended', 'Old Century', 'Pegasus', 'Pickwick', 'Poster', 'Pythagoras', 'Sceptre', 'Sherwood', 'Signboard', 'Socket', 'Steamer', 'Storybook', 'Subway', 'Tahoma', 'Technical', 'Teletype', 'Tempus Sans ITC', 'Times', 'Times New Roman', 'Times New Roman PS', 'Trebuchet MS', 'Tristan', 'Tubular', 'Unicorn', 'Univers', 'Univers Condensed', 'Vagabond', 'Verdana', 'Westminster	Allegro',
             'Amazone BT', 'AmerType Md BT', 'Arrus BT', 'Aurora Cn BT', 'AvantGarde Bk BT', 'AvantGarde Md BT', 'BankGothic Md BT', 'Benguiat Bk BT', 'BernhardFashion BT', 'BernhardMod BT', 'BinnerD', 'Bremen Bd BT', 'CaslonOpnface BT', 'Charter Bd BT', 'Charter BT', 'ChelthmITC Bk BT', 'CloisterBlack BT', 'CopperplGoth Bd BT', 'English 111 Vivace BT', 'EngraversGothic BT', 'Exotc350 Bd BT', 'Freefrm721 Blk BT', 'FrnkGothITC Bk BT', 'Futura Bk BT', 'Futura Lt BT', 'Futura Md BT', 'Futura ZBlk BT', 'FuturaBlack BT', 'Galliard BT', 'Geometr231 BT', 'Geometr231 Hv BT', 'Geometr231 Lt BT', 'GeoSlab 703 Lt BT', 'GeoSlab 703 XBd BT', 'GoudyHandtooled BT', 'GoudyOLSt BT', 'Humanst521 BT', 'Humanst 521 Cn BT', 'Humanst521 Lt BT', 'Incised901 Bd BT', 'Incised901 BT', 'Incised901 Lt BT', 'Informal011 BT', 'Kabel Bk BT', 'Kabel Ult BT', 'Kaufmann Bd BT', 'Kaufmann BT', 'Korinna BT', 'Lydian BT', 'Monotype Corsiva', 'NewsGoth BT', 'Onyx BT', 'OzHandicraft BT', 'PosterBodoni BT', 'PTBarnum BT', 'Ribbon131 Bd BT', 'Serifa BT', 'Serifa Th BT', 'ShelleyVolante BT', 'Souvenir Lt BT', 'Staccato222 BT', 'Swis721 BlkEx BT', 'Swiss911 XCm BT', 'TypoUpright BT', 'ZapfEllipt BT', 'ZapfHumnst BT', 'ZapfHumnst Dm BT', 'Zurich BlkEx BT', 'Zurich Ex BT', ]

    sg.theme('DarkGray9')

    @staticmethod
    def get_text_watermark_popup():
        text_col = [[sg.Col([
                            [sg.Text('Text')],
                            [sg.Text('Font Type')],
                            [sg.Text('Font Size')],
                            ], element_justification='left'),
                    sg.Col([
                        [sg.Input(key='-INPUT-TEXT-')],
                        [sg.Combo(values=([i.lower() for i in Gui.FONTS]),
                                  default_value=Gui.FONTS[37], readonly=True, k='-FONT-TYPE-')],
                        [sg.Combo(values=([i for i in range(1, 100)]),
                                  default_value=12, readonly=True, k='-FONT-SIZE-')]
                    ], element_justification='left'
        )
        ],
            [sg.Col([[sg.Submit(), sg.Cancel()]], justification='right')]
        ]

        return sg.Window('Enter Watermark Text', [
            [sg.Col(text_col)]], modal=True, no_titlebar=True, grab_anywhere=True).read(close=True)

    @staticmethod
    def main_window():
        layout = [
            [
                sg.Col([
                    [sg.Text('Select Watermark')],
                    [sg.Col([
                        [  # sg.Button('Text', k='-TEXT-'),
                            sg.Button('Image', k='-W_IMAGE-')]
                    ], justification='center')
                    ]
                ]),
                sg.VerticalSeparator(pad=None),
                sg.Col([
                    [sg.Text('Select Process Type')],
                    [sg.Col([
                        [sg.Button('Image', k='-IMAGE-'),
                         sg.Button('Folder', k='-IMAGE_FOLDER-')]
                    ], justification='center')
                    ]
                ])
            ],
            [sg.Text('Transparency:'),
             sg.Spin([i/10 for i in range(1, 11)],
                     initial_value=0.3, k='-OPACITY-'),
             sg.Col([
                 [sg.Button('Watermark!', k='-WATERMARK-')]
             ], justification='center')
             ]
        ]

        return sg.Window('Image Watermarking Desktop App', layout,
                         no_titlebar=False, grab_anywhere=True)

    @staticmethod
    def get_file():
        return sg.popup_get_file(
            'Select image', no_titlebar=True, grab_anywhere=True, file_types=(('ALL Files', '.png'), ('ALL Files', '.jpg'), ('ALL Files', '.jpeg'),))

    @staticmethod
    def get_working_folder_path():
        return sg.popup_get_folder(
            'Select folder containing images', no_titlebar=True, grab_anywhere=True)

    @staticmethod
    def watermarkdone():
        return sg.PopupOK('Done', no_titlebar=True)

    @staticmethod
    def close_window():
        return sg.WINDOW_CLOSED
