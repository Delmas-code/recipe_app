Start_Screen = '''

<Starter>
    img: ""
    Image:
        # source:"C:/Users/DELMAS/Desktop/Invore/Demo Project/Recipia/Images/logo2.png"
        source: root.img
        pos_hint: {'center_x':0.45 ,'center_y':0.5}
    MDLabel:
        text: "From"
        pos_hint: {'center_x':0.5 ,'center_y':0.25}
        halign: "center"
        # font_name: "fonts/Poppins-Regular"
        font_size: "15sp"
    MDLabel:
        text: "INVORE"
        pos_hint: {'center_x':0.5 ,'center_y':0.2}
        halign: "center"
        # font_name: "fonts/Poppins-SemiBold"
        font_size: "20sp"

MDScreen:
    name: 'StartScreen'
    md_bg_color: app.theme_cls.primary_color
    bg_img: ''
    Starter:
        img: root.bg_img
'''