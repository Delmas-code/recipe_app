DynamicRec_Screen = '''

<ImageBlock>
    orientation: 'vertical'
    image: ""
    recipeName: ""
    duration: ""
    category: ""
    Image:
        source: root.image
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: 200
        # height: self.parent.width/ self.image_ratio
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'top':1}
    MDFloatLayout:
        # md_bg_color: (0, 0, 0, 0.1)
        radius: [0, 0, 15, 15]
        size_hint_y: .30
        # pos_hint: {"center_y":.7}
        MDBoxLayout:
            # pY: 42
            pos_hint: {'y':1}
            MDLabel:
                text: root.recipeName
                # font_name: "fonts/Poppins-SemiBold"
                font_size: "20sp"
                theme_text_color: "Primary"

        
        MDBoxLayout:
            pY: .91
            pos_hint: {'center_y':.1}
            MDIconButton:
                icon:'clock-outline'
                size_hint_x:None
                width:root.width*.2
                pos_hint: {'center_y':.91}
            
            MDLabel:
                text: root.duration
                pos_hint: {'center_y':self.parent.pY}
                # font_name: "fonts/Poppins-Light"
            MDIconButton:
                icon:'group'
                size_hint_x:None
                width:root.width*.2
                pos_hint: {'center_y':.91}
            
            MDLabel:
                text: root.category
                pos_hint: {'center_y':self.parent.pY}
                # font_name: "fonts/Poppins-Light"

    # Widget:


<StepsItem>
    orinetation: 'horizontal'
    size_hint_y: None
    stepNum: ""
    step: ""
    
    MDBoxLayout:
        size_hint: .38, .34
        pos_hint: {"top": .8} 
        canvas.before:
            Color:
                rgb: (1, 170/255, 23/255, 1)  
            RoundedRectangle:
                size: self.size 
                pos: self.pos
                radius: [22, 22, 22, 22]
        MDLabel:
            text: "Step"+ root.stepNum
            halign: "center"
            # font_name: "fonts/Poppins-Medium"
            # color: 0, 0, 0, 0


    MDLabel:
        text: root.step    
        text_size: root.width, None
        size: self.size
        # color: 0, 0, 0, 0


MDScreen:
    name: 'DynamicRec'
    topblock: topblock
    container: container
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            id:topblock
            orientation: 'vertical'

 
        MDFloatLayout:
            # pos_hint: {"x": .2}
            ScrollView:
                pos_hint: {"center_y": .45}
                MDList:
                    id: container
                    # font_name: "fonts/Poppins-Regular"
 




    MDBoxLayout:
        size_hint_y:None
        height:dp(60)
        adaptive_width:True
        padding:dp(12)
        spacing:dp(10)
        pos_hint:{'center_x':.5}
        md_bg_color:.9,0.9,0.9,.5
        radius:[50,50,0,0]
        MDIconButton:
            icon:'food'
            size_hint_x:None
            width:root.width*.2
            on_press: app.put_recipe_to_screen()
        MDIconButton:
            icon:'magnify'
            size_hint_x:None
            width:root.width*.2
            on_press: app.searchpopup()
        MDFloatingActionButton:
            icon: "home"
            color: app.theme_cls.primary_color
            size_hint_x:None
            width:root.width*.2
            on_press: app.homeScreen()
        MDIconButton:
            icon:'moon-waning-crescent'
            size_hint_x:None
            width:root.width*.2
            on_press: app.mode(self)
        MDIconButton:
            icon:'group'
            size_hint_x:None
            width:root.width*.2
            on_press: app.put_category_to_screen()


'''