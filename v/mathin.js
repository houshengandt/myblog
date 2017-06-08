var Signs = {
    frac: "frac",
    sqrt: "sqrt",
    power: "power"
}

let editorId = 0;

function Editor (elem) {
    this.id = editorId++;
    this.$ContainerElem = $(elem);

}

Editor.prototype = {
    constructor: Editor,

    // 初始化 DOM
    _initDom: function () {
        const ContainerElem = this.$ContainerElem;
        
        let $Elem, $inputElem, $actionElem;
        $Elem = $('<span></sapn>');

        $inputElem = $('<input type="text" />').css("height", "30px").css("width", "60px");

        $actionElem = $('<select type="button" class="action" id="action' + editorId + '"><option>插入算符</option></select>').css("height", "30px");

        $Elem.append($inputElem).append($actionElem);

        ContainerElem.append($Elem);


        this.$actionElem = $actionElem;
        this.$Elem = $Elem;

    },

    _initAction: function () {
        var actionId = "action" + editorId;

        for(var i in Signs){
            var newOption = $('<option value="' + Signs[i] + '">' + Signs[i] + '</option>');
            this.$actionElem.append(newOption);

        }

        // $("#" + actionId).prettyDropdown({
        //     classic: true,
        //     height: 30
        // });
        
    },

    getValue: function () {
        return(this.$Elem.find("input").val());
    },

    getResult: function () {
        return(this.getValue());
    },

    create: function () {
        this._initDom();
        this._initAction();
    }
}






var signExp = {
    "frac": "\\( \\frac{\\FormInput{m0}}{\\FormInput{m1}} \\)",
    "sqrt": "\\( \\sqrt{\\FormInput{m0}} \\)",
    "power": "\\( \\FormInput{m0}^\\FormInput{m1} \\)"
}


function mathIn (Elem,ExpressionType) {
    this.Elem = Elem;
    this.$Elem = $(Elem);
    if(signExp[ExpressionType]){
        this.expression = signExp[ExpressionType];
    }
    this.create();
}


mathIn.prototype = {
    constructor: mathIn,

    _initDom: function () {
        this.$Elem.html("<span>" + this.expression + "</span><button>重置</button>");
    },

    create: function () {
        this._initDom();
    },

    getDom: function () {
        return(this.$Elem);
    },

    getValue: function () {
        var v = {};
        this.$Elem.find("span>input").each(function(i){
            v["m" + i] = $(this).val();

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


function Minput (Elem, isComplex, ExpressionType) {
    this.Elem = Elem;
    this.$Elem = $(Elem);
    
    if(isComplex == null){
        this.isComplex = false;
    }else{
        this.isComplex = isComplex;
        this.ExpressionType = ExpressionType;
    }
    this.create();
}


Minput.prototype = {
    constructor: Minput,

    _initInput: function () {
        if(this.isComplex){
            this.E = new mathIn(this.Elem,this.ExpressionType);
        }else{
            this.E = new Editor(this.Elem);
            this.E.create();
        }
    },

    _changeToPlainInput: function () {
        if(this.isComplex){
            this.isComplex = false;
            this.ExpressionType = null;

            this._initInput();
        }
    },

    _changeToComplexInput: function (ExpressionType) {
        if(this.isComplex){

        } else {
            this.isComplex = true;
            this.ExpressionType = ExpressionType;
            this.$Elem.empty();
            var newMath = new mathIn(this.Elem,this.ExpressionType);
            this._initInput();
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
    },

    _action: function () {
        var t = this;
        var action_id = 'action' + this.E.id;
        
        if(this.isComplex){
            t.$Elem.on('click', 'button', function() {
                console.log(2);
                this.isComplex = false;
                this.ExpressionType = null;
                window.location.reload();
            })

        } else {
            $("select").on('change',function () {
                t._changeToComplexInput($(this).val());
                t._action();
            })
        }
    },


    create: function () {
        this._initInput();
        this._action();
    }
}
