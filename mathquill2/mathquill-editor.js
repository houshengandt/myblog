MQ = MathQuill.getInterface(2)
const buttons = {
    '\\frac{a}{b}': '\\frac',
    'a^n': '^',
    '\\sqrt{a}': '\\sqrt',
    };
let editorId = 0;

function mathEditor (elem) {
    this.id = editorId++;
    this.$ContainerElem = $(elem);
    this.create()
}

mathEditor.prototype = {
    constructor: mathEditor,


    // 初始化 DOM
    _initDom: function () {
        var self = this
        var $ContainerElem = this.$ContainerElem
        $ContainerElem.css('position','relative')
        let $Editor, $buttons

        $Editor = $('<span class="editor"></sapn>').css('position', 'relative').css('top', 25)
        this.$Editor = $Editor
        this._getEditorPos()
        $buttons = $('<div class="buttons" button_id="' + self.id + '" style="display:none;"></div>')
                    .css('position', 'absolute').css('top', self.layer_y).css('left', 0).css('z-index', '999')
                    .on('click', function(event){
                        event.stopPropagation()
                    })

        $ContainerElem.append($Editor)
        $ContainerElem.append($Editor).append($buttons);

        
        this.$buttons = $buttons

    },

    _toggle: function() {
        var self = this
        self.$Editor.on('click', function(event){
            event.stopPropagation()
            self.$buttons.show()
            $('.buttons').each(function(){
                if($(this).attr('button_id')!=self.id) $(this).hide()
            })
        })
        $('body').on('click', function(event){
            self.$buttons.hide()
        })
    },

    _getEditorPos: function () {
        var self = this
        var $editor = self.$Editor
        var x = $editor.position().left
        var y = $editor.position().top
        var control_x = $editor.outerWidth()
        var control_y = $editor.css('min-height')
        self.layer_x = control_x + 'px'
        self.layer_y = control_y
    },

    _initEditor: function () {
        var self = this
        var editor = MQ.MathField(this.$Editor[0], {
            autoSubscriptNumerals: true,
            handlers: {
                edit: function() {
                    
                },
                enter: function() {

                }
            }
        })
        function restrictInput(exp) {
            var latex = editor.latex()
            if(exp=='^'){
                exp = '\\^'
            } else {
                exp = exp.replace('\\',"\\\\")
            }
            var reg = new RegExp(exp, "g")
            return latex.match(reg)?latex.match(reg).length:0
        }
        Object.keys(buttons).forEach(function (lable) {
            var $button = $('<button></button>')

            $button.text(lable);
            $button.on('click', function () {
                if(restrictInput(buttons[lable])<3){
                    editor.cmd(buttons[lable])
                    editor.focus()
                }else {
                   
                }
                
            });
            MQ.StaticMath($button[0]);
            self.$buttons.append($button);
            
        });
        this.editor = editor;
    },
    
    getResult: function() {
        var result = this.editor.latex();
        return result;
    },

    create: function () {
        this._initDom();
        this._initEditor();
        this._toggle()
        
    }
}






