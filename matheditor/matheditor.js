var $buttons = document.getElementById('buttons');

    const editor = new MathJaxEditor({
        el: '#editor',
        debug: false,
        newLine: false
        });
    editor.focus()

    const buttons = {
        '\\sqrt{a}': function (editor) { editor.insertCommand('sqrt', 1) },
        '\\frac{a}{b}': function (editor) { editor.insertCommand('frac', 2) },
        'a^n': function (editor) { editor.insertCommand('^', 1) },
        };

    Object.keys(buttons).forEach(function (label) {
        var $button = document.createElement('button');
        var fn = buttons[label];

        $button.innerHTML = '\\(' + label + '\\)';
        $button.addEventListener('click', function () {
            fn(editor);
        });

        $buttons.appendChild($button);
    });

