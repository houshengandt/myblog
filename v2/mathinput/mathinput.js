var signExp = {
    "frac": "\\( \\frac{\\FormInput{m0}}{\\FormInput{m1}} \\)",
    "sqrt": "\\( \\sqrt{\\FormInput{m0}} \\)",
    "power": "\\( \\FormInput{m0}^\\FormInput{m1} \\)"
}

var buttonImage = {
    "frac": "./mathinput/image/20.png",
    "fracOn": "./mathinput/image/21.png",
    "sqrt": "./mathinput/image/10.png",
    "sqrtOn": "./mathinput/image/11.png",
    "power": "./mathinput/image/30.png",
    "powerOn": "./mathinput/image/31.png",
}


function mathIn (Elem,ExpressionType) {
    this.Elem = Elem;
    this.$Elem = $(Elem);
    this.ExpressionType = ExpressionType
    if(signExp[ExpressionType]){
        this.expression = signExp[ExpressionType];
    }
    this.create();
}


mathIn.prototype = {
    constructor: mathIn,

    _initDom: function () {
        this.$Elem.html(this.expression);
    },

    create: function () {
        this._initDom();
    },

    getDom: function () {
        return(this.$Elem);
    },

    getValue: function () {
        var v = {};
        v['type'] = this.ExpressionType
        this.$Elem.find("span>input").each(function(i){
            v["m" + i] = $(this).val().replace(/\s+/g, "").toLowerCase();

        })
        return(v);
    },

    getResult: function () {
        var exp = this.expression;
        var r = this.getValue();
        for(var i in r){
            console.log(i);
            console.log(r[i]);
            exp = exp.replace("\\FormInput{" + i + "}", r[i]);
        }
        console.log(exp);
        return exp;
    }
}


function MathInput (Elem) {
    this.$Elem = $(Elem)
    this.create()
}

MathInput.prototype = {
    _initDom: function () {
        var self = this
        self.layerElem = $("<div class='layer' style='display:none;'></div>")
        this.$Elem.after(self.layerElem)
    },
    _initLayer: function () {
        var self = this
        self.inputArea = $("<div class='input-area'></div>")
        self.layerElem.append(self.inputArea)
        self.submitButton = $("<button class='submit-button'>Enter</button>")
        self.layerElem.append(self.submitButton)
        self.sqrtButton = $("<img class='sign-img' expression-type='sqrt' status='0' src='" + buttonImage['sqrt'] + "'>")
        self.layerElem.append(self.sqrtButton)
        self.fracButton = $("<img class='sign-img' expression-type='frac' status='0' src='" + buttonImage['frac'] + "'>")
        self.layerElem.append(self.fracButton)
        self.powerButton = $("<img class='sign-img' expression-type='power' status='0' src='" + buttonImage['power'] + "'>")
        self.layerElem.append(self.powerButton)
        $(self.layerElem).click(function(event){
            event.stopPropagation()
        })
    },
    _setDefaultButton: function () {
        var self = this
        self.sqrtButton.attr('src', buttonImage['sqrt']).attr('status', '0')
        self.fracButton.attr('src', buttonImage['frac']).attr('status', '0')
        self.powerButton.attr('src', buttonImage['power']).attr('status', '0')
    },
    _initExpression: function () {
        this.M = new mathIn(this.inputArea, this.expressionType)
        this.M.create()
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    },
    getExpressionType: function () {
        var self = this
        $('.sign-img').on('click', function(event) {
            event.stopPropagation()
            self.expressionType = $(this).attr('expression-type')
            self.changeStatus($(this))
            self._initExpression()
        })
    },
    changeStatus: function ($button) {
        var self = this
        var et = $button.attr('expression-type')
        if($button.attr('status')==1){
            $button.attr('status', '0').attr('src', buttonImage[et])
        } else {
            self._setDefaultButton()
            $button.attr('status', '1').attr('src', buttonImage[et + 'On'])
            if(self.oriInput){
                self.$Elem.replaceWith(self.oriInput)
                MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
            }
        }
    },
    create: function () {
        this._initDom()
        this._initLayer()
        this.getExpressionType()
    }
}


function Control (Elem) {
    this.$parent = $(Elem).parent()
    this.$$parent = this.$parent.parent()
    this.$Elem = $(Elem)
    // this.$Elem.css('position', 'relative')
    this.MathInput = new MathInput(this.$parent)
    this.create()
}

Control.prototype = {
    _toggle: function (Elem) {
        var self = this
        self._getElemPos(Elem)
        self.$$parent.css('position','relative')
        self.MathInput.layerElem.css('position', 'absolute').css('top', self.layer_y).css('left', self.layer_x).css('z-index', '999')
        // if(self.$Elem.is("input")){
        //     self.$Elem.focus(function(event){
        //         self.MathInput.layerElem.show()
        //         // $('body').click(function(event){
        //         //     console.log(event)
        //         //     console.log(event.target)
        //         //     // if(event.target=='body'){
        //         //     //     self.MathInput.layerElem.hide()
        //         //     // }
        //         //     self.MathInput.layerElem.hide()
        //         // })
        //     })

            
        // }
        if(Elem.is("input")){
            self.$parent.click(function(event){
                self.MathInput.layerElem.show()
                event.stopPropagation()
            })

            $('body').click(function(event){
                    // if(event.target=='body'){
                    //     self.MathInput.layerElem.hide()
                    // }
                    self.MathInput.layerElem.hide()
                })
            Elem.focusout(function(){
                // self.MathInput.layerElem.hide()
               
            })
        }
    },
    _getElemPos: function (Elem) {
        var self = this
        var x = Elem.position().left
        var y = Elem.position().top
        var control_x = Elem.outerWidth()
        var control_y = Elem.outerHeight()
        self.layer_x = control_x/2 - 105 + 'px'
        self.layer_y = control_y + 'px'
        console.log(x)
        console.log(y)
        console.log(self.layer_x)
        console.log(self.layer_y)
    },
    enter: function () {
        var self = this
        $('.submit-button').click(function () {
            event.stopPropagation()
            self.showResult()
        })
    },
    showResult: function () {
        var self = this
        self.oriInput = self.$Elem
        self.$parent.html(self.MathInput.M.getResult())
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        self.MathInput.layerElem.hide()
        // self.$parent.click(function(){
        //     self.$parent.html(self.oriInput)
        // })
        self.$parent.one('click', function(){
            self.$parent.html(self.oriInput)
            self._toggle(self.oriInput)
        })
    },
    check: function (answer){
        var self = this
        var input = self.MathInput.M.getValue()
        if(input['type']==answer['type']&&input['m0']==answer['m0']&&input['m1']==answer['m1']){
            return true
        } else {
            return false
        }
    },
    create: function () {
        this._toggle(this.$Elem)
        this.enter()
    }
}