card_style = {
                'width': '800px',
                'min-height': '300px',
                'padding-top': '25px',
                'padding-right': '25px',
                'padding-left': '25px',
            }

card_icon = {
                "color": "green",
                "textAlign": "right",
                "fontSize": 30,
                "margin": 'auto'
            }

card_group_css = {
                    'display': 'flex',
                    '-ms-flex-flow': 'row wrap',
                    'flex-flow': 'row wrap',
                    'flex-direction': 'row',
                    'flex-wrap': 'wrap',
                    'box-sizing': 'border-box'
                }

card_right = {
                "maxWidth": 15, 
                "height": 100, 
                "margin-left": "-10px", 
                'minWidth':15,
                'border-left': '0',
                'border-left-width': '0px',
                'border-left-style': 'initial',
                'border-left-color': 'initial',
                'border-top-left-radius': '0',
                'border-bottom-left-radius': '0'
            }       

style_button = {
                    'width': '100%',
                    'background-color': 'transparent',
                    'color':'black',
                    'border': 'none',
                    'text-align':'center'
                }

card_icon_menu = {
                    "color": "#66a593",
                    "textAlign": "center",
                    "fontSize": 30,
                    "margin": 'auto',
                    'align-items':'center',
                }


mascaras_js = '''
// Adicionando máscara de CPF
document.getElementById('cpf').addEventListener('input', function () {
  this.value = this.value.replace(/\D/g, '').replace(/(\d{3})(\d)/, '$1.$2').replace(/(\d{3})(\d)/, '$1.$2').replace(/(\d{3})(\d{1,2})/, '$1-$2');
});

// Adicionando máscara de CNPJ
document.getElementById('cnpj').addEventListener('input', function () {
  this.value = this.value.replace(/\D/g, '').replace(/(\d{2})(\d)/, '$1.$2').replace(/(\d{3})(\d)/, '$1.$2').replace(/(\d{3})(\d)/, '$1/$2').replace(/(\d{4})(\d{1,2})/, '$1-$2');
});
'''